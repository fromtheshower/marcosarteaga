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
$locale = $input['locale'] ?? 'en';
if (!filter_var($email, FILTER_VALIDATE_EMAIL) || !filter_var($website, FILTER_VALIDATE_URL)
    || !in_array(parse_url($website, PHP_URL_SCHEME), ['http', 'https'], true)
    || !in_array($spend, ['under-5k', '5k-15k', '15k-50k', '50k-plus'], true)
    || !is_string($locale) || !in_array($locale, ['en', 'fr', 'es'], true)) {
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
if ($locale === 'es') {
    $spendLabels = [
        'under-5k' => 'Menos de 5.000 €/mes',
        '5k-15k' => '5.000–15.000 €/mes',
        '15k-50k' => '15.000–50.000 €/mes',
        '50k-plus' => '50.000 € o más/mes',
    ];
}
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
    'Language: ' . ['en' => 'English', 'fr' => 'French (Québec)', 'es' => 'Spanish (Spain)'][$locale],
    'Website: ' . $website,
    'Monthly ad spend: ' . $spendLabels[$spend],
    'Platforms: ' . implode(', ', $selected), '',
    'Concern:', $concern, '',
    'Reply to the sender at ' . $email,
]);
if (!sendMail(ENQUIRY_RECIPIENT, 'New audit enquiry from website', $body, $password, $email)) {
    respond(502, 'Your enquiry could not be sent. Please try again later.');
}

$autoReplies = [
    'en' => [
        'subject' => 'Thanks for your audit enquiry',
        'greeting' => 'Hi ' . $name . ',',
        'closing' => 'Best,',
        'under' => [
            'Thanks for your enquiry.',
            '',
            "This audit is designed for accounts spending at least $5,000 a month on ads. That's where the economics work and where there's enough waste to find to make the audit worthwhile.",
            '',
            "If you're not there yet but plan to be, reply and tell me where you're headed. I'll tell you honestly whether it's worth waiting or if there's something useful I can point you to now.",
        ],
        'qualified' => [
            "Thanks for your enquiry. I've got it.",
            '',
            "I'll personally review your website, the platforms you're running on, and what's bothering you about the account. I'll reply within 2 business days about fit and next steps.",
        ],
    ],
    'fr' => [
        'subject' => 'Merci pour votre demande d’audit',
        'greeting' => 'Bonjour ' . $name . ',',
        'closing' => 'Au plaisir,',
        'under' => [
            'Merci pour votre demande.',
            '',
            'Cet audit s’adresse aux comptes qui dépensent au moins 5 000 $ par mois en publicité. C’est à partir de là que l’analyse a le plus de chances d’être utile.',
            '',
            'Si vous n’y êtes pas encore, mais que vous comptez y arriver, répondez-moi et dites-moi où vous vous dirigez. Je vous dirai franchement s’il vaut mieux attendre ou si je peux déjà vous orienter vers quelque chose d’utile.',
        ],
        'qualified' => [
            'Merci pour votre demande. Je l’ai bien reçue.',
            '',
            'Je vais examiner personnellement votre site, les plateformes que vous utilisez et ce qui vous préoccupe dans vos comptes. Je vous répondrai dans les 2 jours ouvrables pour confirmer si l’audit vous convient et vous expliquer la suite.',
        ],
    ],
    'es' => [
        'subject' => 'Gracias por tu consulta sobre la auditoría',
        'greeting' => 'Hola ' . $name . ',',
        'closing' => 'Un saludo,',
        'under' => [
            'Gracias por tu consulta.',
            '',
            'Esta auditoría está pensada para cuentas que invierten al menos 5.000 € al mes en publicidad. A partir de ese nivel, el análisis tiene más posibilidades de resultar útil.',
            '',
            'Si aún no has llegado a esa cifra, pero esperas hacerlo, respóndeme y cuéntame adónde quieres llegar. Te diré con sinceridad si conviene esperar o si puedo orientarte hacia algo útil ahora.',
        ],
        'qualified' => [
            'Gracias por tu consulta. La he recibido.',
            '',
            'Revisaré personalmente tu web, las plataformas en las que te anuncias y lo que te preocupa de la cuenta. Te responderé en un plazo de 2 días laborables para hablar de si la auditoría encaja y de los siguientes pasos.',
        ],
    ],
];
$copy = $autoReplies[$locale];
$branch = $spend === 'under-5k' ? 'under' : 'qualified';
$reply = implode("\n", array_merge([$copy['greeting'], ''], $copy[$branch], ['', $copy['closing'], 'Marcos']));
if (!sendMail($email, $copy['subject'], $reply, $password)) {
    error_log('Enquiry form auto-reply failed.');
}

respond(200, 'Enquiry accepted for delivery.');
