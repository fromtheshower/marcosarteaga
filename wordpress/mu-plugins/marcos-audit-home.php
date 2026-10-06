<?php
/**
 * Plugin Name: Marcos Arteaga Audit Pages
 * Description: Shows the standalone audit homepage and privacy pages in WordPress.
 */

defined('ABSPATH') || exit;

add_filter('template_include', static function (string $template): string {
    if (is_front_page()) {
        $auditTemplate = __DIR__ . '/marcos-audit-home/template.php';
    } elseif (is_page('privacy')) {
        $auditTemplate = __DIR__ . '/marcos-audit-home/privacy-template.php';
    } else {
        return $template;
    }
    if (!is_readable($auditTemplate)) {
        error_log('Marcos audit page template is missing.');
        return $template;
    }

    return $auditTemplate;
}, 99);

// Serve exact localized routes without creating WordPress pages or flushing rewrite rules.
add_action('template_redirect', static function (): void {
    $path = parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH);
    if (!is_string($path)) return;

    $routes = [
        '/fr/' => 'fr-template.php',
        '/fr/privacy/' => 'fr-privacy-template.php',
    ];
    if (isset($routes[$path])) {
        $localizedTemplate = __DIR__ . '/marcos-audit-home/' . $routes[$path];
        if (!is_readable($localizedTemplate)) {
            error_log('Marcos localized audit page template is missing.');
            return;
        }
        status_header(200);
        header('Content-Type: text/html; charset=UTF-8');
        require $localizedTemplate;
        exit;
    }
    if (isset($routes[$path . '/'])) {
        wp_safe_redirect(home_url($path . '/'), 301);
        exit;
    }
}, 0);
