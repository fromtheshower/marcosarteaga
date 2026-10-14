<?php
declare(strict_types=1);

if (!defined('ABSPATH')) { http_response_code(404); exit; }

$path = parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH) ?: '';
$isFrench = $path === '/fr' || strncmp($path, '/fr/', 4) === 0;
$home = $isFrench ? '/fr/' : '/';
$privacy = $isFrench ? '/fr/privacy/' : '/privacy/';
$copy = $isFrench ? [
    'title' => 'Page introuvable | Marcos Arteaga',
    'skip' => 'Aller au contenu',
    'home_label' => 'Marcos Arteaga, accueil',
    'request' => 'Demander un audit',
    'kicker' => 'Erreur 404',
    'heading' => 'Cette page est introuvable.',
    'message' => 'Le lien est peut-être ancien. Vous pouvez retourner à la page de l’audit ou m’envoyer une demande.',
    'back' => 'Voir l’audit',
    'privacy' => 'Confidentialité',
] : [
    'title' => 'Page not found | Marcos Arteaga',
    'skip' => 'Skip to content',
    'home_label' => 'Marcos Arteaga, homepage',
    'request' => 'Request an audit',
    'kicker' => '404 / Page not found',
    'heading' => 'That page isn’t here.',
    'message' => 'The link may be old. Head back to the audit page, or send me an enquiry.',
    'back' => 'See the audit',
    'privacy' => 'Privacy',
];
status_header(404);
header('X-Robots-Tag: noindex, follow', true);
function audit_error_text(string $value): string {
    return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}
?>
<!doctype html>
<html lang="<?= $isFrench ? 'fr-CA' : 'en' ?>">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#fafaf8" />
    <meta name="robots" content="noindex,follow" />
    <title><?= audit_error_text($copy['title']) ?></title>
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />
    <link rel="stylesheet" href="/styles.css" />
  </head>
  <body>
    <a class="skip-link" href="#main"><?= audit_error_text($copy['skip']) ?></a>
    <header class="site-header wrap">
      <a class="wordmark" href="<?= $home ?>" aria-label="<?= audit_error_text($copy['home_label']) ?>">Marcos Arteaga<span class="wordmark-dot">.</span></a>
      <a class="header-link" href="<?= $home ?>#booking"><?= audit_error_text($copy['request']) ?> <svg class="arrow-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 12.5 12 4M5.5 4H12v6.5" /></svg></a>
    </header>
    <main class="privacy-main error-main wrap" id="main">
      <div class="privacy-intro">
        <p class="section-kicker"><?= audit_error_text($copy['kicker']) ?></p>
        <div>
          <h1><?= audit_error_text($copy['heading']) ?></h1>
          <p class="privacy-lede"><?= audit_error_text($copy['message']) ?></p>
          <a class="button button-primary" href="<?= $home ?>"><?= audit_error_text($copy['back']) ?> <svg class="arrow-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 12.5 12 4M5.5 4H12v6.5" /></svg></a>
        </div>
      </div>
    </main>
    <footer class="site-footer wrap"><a class="wordmark" href="<?= $home ?>">Marcos Arteaga<span class="wordmark-dot">.</span></a><div class="footer-links"><a href="<?= $privacy ?>"><?= audit_error_text($copy['privacy']) ?></a><a href="https://www.linkedin.com/in/marcosarteaga/" target="_blank" rel="noopener noreferrer">LinkedIn <svg class="arrow-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 12.5 12 4M5.5 4H12v6.5" /></svg></a><a href="https://fromtheshower.com/" target="_blank" rel="noopener noreferrer">FromTheShower <svg class="arrow-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 12.5 12 4M5.5 4H12v6.5" /></svg></a></div><small>© Marcos Arteaga</small></footer>
  </body>
</html>
