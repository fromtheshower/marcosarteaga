<?php
declare(strict_types=1);

// Keep the recipient and sender on the server. The Google app password belongs
// in a private config file outside the web root, never in public JavaScript.
const ENQUIRY_RECIPIENT = 'marcos@fromtheshower.com';

require_once __DIR__ . '/lib/phpmailer/src/Exception.php';
require_once __DIR__ . '/lib/phpmailer/src/PHPMailer.php';
require_once __DIR__ . '/lib/phpmailer/src/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception as MailException;

function respond(int $status, string $message): void
{
    http_response_code($status);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    header('X-Robots-Tag: noindex, nofollow');
    echo json_encode(['message' => $message], JSON_THROW_ON_ERROR);
    exit;
}

function field(array $input, string $key, int $maxLength): string
{
    $value = $input[$key] ?? null;
    if (!is_string($value) || trim($value) === '' || strlen($value) > $maxLength || preg_match('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', $value)) {
        respond(422, 'Please check the form fields and try again.');
    }
    return trim($value);
}

function sendMail(string $to, string $subject, string $body, string $password, ?string $replyTo = null): bool
{
    $mail = new PHPMailer(true);
    try {
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com';
        $mail->Port = 587;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->SMTPAuth = true;
        $mail->Username = ENQUIRY_RECIPIENT;
        $mail->Password = $password;
        $mail->Timeout = 10;
        $mail->CharSet = 'UTF-8';
        $mail->setFrom(ENQUIRY_RECIPIENT, 'Marcos Arteaga');
        $mail->addAddress($to);
        if ($replyTo !== null) $mail->addReplyTo($replyTo);
        $mail->Subject = $subject;
        $mail->Body = $body;
        $mail->isHTML(false);
        return $mail->send();
    } catch (MailException $error) {
        error_log('Enquiry form SMTP delivery failed.');
        return false;
    }
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, 'Method not allowed.');
}

$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
$host = explode(':', $_SERVER['HTTP_HOST'] ?? '')[0];
if ($origin !== '' && parse_url($origin, PHP_URL_HOST) !== $host) {
    respond(403, 'Request origin is not allowed.');
}

if (strpos(strtolower($_SERVER['CONTENT_TYPE'] ?? ''), 'application/json') !== 0) {
    respond(415, 'Expected JSON.');
}
if ((int) ($_SERVER['CONTENT_LENGTH'] ?? 0) > 12000) {
    respond(413, 'Enquiry is too long.');
}
$raw = file_get_contents('php://input', false, null, 0, 12001);
if ($raw === false || strlen($raw) > 12000) {
    respond(413, 'Enquiry is too long.');
}
$decoded = json_decode($raw);
if (!is_object($decoded)) {
    respond(400, 'Invalid form data.');
}
$input = (array) $decoded;
if (!empty($input['companyFax'])) {
    respond(204, ''); // Quietly discard automated submissions.
}

$name = field($input, 'name', 120);
$email = field($input, 'email', 254);
$website = field($input, 'website', 500);
$concern = field($input, 'concern', 3000);
$spend = field($input, 'monthlyAdSpend', 16);
if (!filter_var($email, FILTER_VALIDATE_EMAIL) || !filter_var($website, FILTER_VALIDATE_URL)
    || !in_array(parse_url($website, PHP_URL_SCHEME), ['http', 'https'], true)
    || !in_array($spend, ['under-5k', '5k-15k', '15k-50k', '50k-plus'], true)) {
    respond(422, 'Please check the form fields and try again.');
}

$platforms = $input['platforms'] ?? null;
$allowedPlatforms = ['google', 'meta', 'tiktok', 'snapchat', 'other'];
if (!is_array($platforms) || $platforms === [] || count($platforms) > count($allowedPlatforms)) {
    respond(422, 'Please choose at least one valid platform.');
}
foreach ($platforms as $platform) {
    if (!is_string($platform) || !in_array($platform, $allowedPlatforms, true)) {
        respond(422, 'Please choose at least one valid platform.');
    }
}
if (count($platforms) !== count(array_unique($platforms))) {
    respond(422, 'Please choose at least one valid platform.');
}
$otherPlatform = in_array('other', $platforms, true) ? field($input, 'otherPlatform', 160) : '';

$privatePath = dirname(__DIR__) . '/private/marcosarteaga-mail.php';
$privateConfig = [];
if (is_file($privatePath)) {
    try {
        $privateConfig = require $privatePath;
    } catch (Throwable $error) {
        error_log('Enquiry form private mail config could not be loaded.');
        respond(503, 'The form is temporarily unavailable. Please try again later.');
    }
}
$password = is_array($privateConfig) ? ($privateConfig['app_password'] ?? '') : '';
if (!is_string($password) || $password === '' || $password === 'PASTE_GOOGLE_APP_PASSWORD_HERE'
    || !extension_loaded('openssl')) {
    error_log('Enquiry form Google SMTP is not configured.');
    respond(503, 'The form is temporarily unavailable. Please try again later.');
}

// A shared temp-file lock limits repeated mail from one source IP. The file is
// outside the web root and contains timestamps only, not submitted details.
$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$rateFile = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR
    . 'marcosarteaga-enquiry-' . hash('sha256', $ip);
$handle = @fopen($rateFile, 'c+');
if ($handle === false || !@flock($handle, LOCK_EX)) {
    if ($handle !== false) fclose($handle);
    error_log('Enquiry form rate limiter is unavailable.');
    respond(503, 'The form is temporarily unavailable. Please try again later.');
}
$now = time();
$history = stream_get_contents($handle);
$attempts = array_values(array_filter(array_map('intval', explode("\n", $history ?: '')), static fn (int $at): bool => $at > $now - 3600));
if (count($attempts) >= 5) {
    flock($handle, LOCK_UN);
    fclose($handle);
    respond(429, 'Too many enquiries. Please try again later.');
}
$attempts[] = $now;
rewind($handle);
ftruncate($handle, 0);
fwrite($handle, implode("\n", $attempts));
fflush($handle);
flock($handle, LOCK_UN);
fclose($handle);

$spendLabels = [
    'under-5k' => 'Under $5,000/month',
    '5k-15k' => '$5,000–$15,000/month',
    '15k-50k' => '$15,000–$50,000/month',
    '50k-plus' => '$50,000+/month',
];
$platformLabels = [
    'google' => 'Google Ads', 'meta' => 'Meta Ads', 'tiktok' => 'TikTok Ads',
    'snapchat' => 'Snapchat Ads', 'other' => 'Other',
];
$selected = array_map(static fn (string $platform): string => $platformLabels[$platform], $platforms);
if ($otherPlatform !== '') $selected[] = 'Other platform: ' . $otherPlatform;
$body = implode("\n", [
    'New paid-media audit enquiry', '',
    'Name: ' . $name,
    'Email: ' . $email,
    'Website: ' . $website,
    'Monthly ad spend: ' . $spendLabels[$spend],
    'Platforms: ' . implode(', ', $selected), '',
    'Concern:', $concern, '',
    'Reply to the sender at ' . $email,
]);
if (!sendMail(ENQUIRY_RECIPIENT, 'New audit enquiry from website', $body, $password, $email)) {
    respond(502, 'Your enquiry could not be sent. Please try again later.');
}

if ($spend === 'under-5k') {
    $reply = "Thanks for your enquiry. This audit is designed for accounts spending at least $5,000 a month on ads, so it may not be the right fit yet. If the range you selected doesn't reflect your situation, reply and tell me more.\n\nMarcos";
    if (!sendMail($email, 'About your audit enquiry', $reply, $password)) {
        error_log('Enquiry form under-threshold auto-reply failed.');
    }
}

respond(200, 'Enquiry accepted for delivery.');
