<?php
/**
 * Plugin Name: Marcos Arteaga Audit Pages
 * Description: Shows the standalone audit homepage and privacy page in WordPress.
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
