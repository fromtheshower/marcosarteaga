# marcosarteaga.com sales page

One-page sales page for the paid-media audit, with a separate privacy page. English for Canada and the US is at `/` and `/privacy/`; Québec French is at `/fr/` and `/fr/privacy/`. A small WordPress must-use plugin serves the four pages, preserving the existing `/blog/` and WordPress editor. `submit.php` handles email on the existing Plesk/PHP host.

## Private GitHub to Plesk

Use the same controlled workflow as FromTheShower: a private GitHub repository, then **pull and deploy manually in Plesk**. Do not point Plesk at this source branch with `/httpdocs` as its deployment path. The source root includes a preview `index.html`, documentation, and tooling, and the WordPress plugin needs to land under `wp-content/mu-plugins/`.

The private repository is `https://github.com/fromtheshower/marcosarteaga.git`. `main` holds the editable source; `plesk` holds only the 21 public files for deployment. Run `python3 tools/build-plesk-release.py` after source edits to create `build/plesk-release/`, then update the `plesk` branch from that generated tree. In Plesk, connect the private repository, select **`plesk`**, set the deployment path to the existing WordPress `/httpdocs`, and choose **Manual deployment**. Inspect the target for file-name conflicts and back up WordPress before the first deploy. Plesk's Git deployment copies matching paths into the target; it must not replace WordPress core or the existing blog. The generated tree intentionally contains no root `index.html`, static localized HTML, example mail config, or secret.

This machine has an ignored local clone of the `plesk` branch at `build/plesk-worktree/`. To refresh it after rebuilding the release tree, sync the generated files into that clone without touching its `.git` directory, inspect the diff, commit, and push `plesk`. On another machine, clone the same private repository with `--branch plesk` into a separate directory first. Pulling `main` into Plesk would publish the preview and development files, so always check the selected branch before deploying.

Keep the Google Workspace app password in `private/marcosarteaga-mail.php` beside `/httpdocs`, outside Git and the public web root. After deploying, create the WordPress page with slug `privacy`, check both rendered pages and the blog, then perform a real form-to-inbox test. Building the release tree does not itself connect Plesk or deploy the site.

## Email form integration

The form posts to `submit.php`. The handler authenticates to **Google Workspace SMTP** as **marcos@fromtheshower.com** over STARTTLS and sends each enquiry to that same address, with the visitor as Reply-To. PHPMailer v7.1.1 is bundled in `lib/phpmailer/`; no Composer install is needed on Plesk.

1. Deploy `styles.css`, `script.js`, `config.js`, `submit.php`, `assets/`, and `lib/` to the WordPress public web root (usually `httpdocs`). **Do not deploy `index.html` to that root**; it is the local preview and could bypass WordPress routing. Use PHP 7.4+ with OpenSSL enabled. Plesk must allow outbound connections to `smtp.gmail.com:587`.
2. Create a `private` directory **beside** the public web root, not inside it. Copy `mail-config.example.php` to `private/marcosarteaga-mail.php` and replace its placeholder with an app password for the **marcos@fromtheshower.com Google Workspace account**. Restrict the file so only the site/PHP user can read it. The handler reads this sibling path through `dirname(__DIR__)`; no password is stored in the public site or this repository. [Google's app-password guide](https://support.google.com/accounts/answer/185833?hl=en) explains the 2-Step Verification requirement and why the option may be unavailable for a Workspace account.
3. Submit real test enquiries in both spend branches after deployment. Verify that each appears in the mailbox, Reply-To points to the visitor, and the visitor receives the correct personalized auto-reply. An SMTP acceptance response does not guarantee inbox placement.

The public `fromtheshower.com` SPF record currently includes Google, and `google._domainkey.fromtheshower.com` currently publishes a key. Confirm Google Workspace is actively signing with DKIM and check SPF/DKIM results in the headers of the real test message. If DNS changes are needed, edit records at the authoritative DNS provider; the registrar and web host can be separate.

The page sends a JSON `POST` with `name`, `email`, `website`, `country` (`CA` or `US`), `monthlyAdSpend`, `platforms` (an array of selected values), `locale`, and `concern`. The platform values are `google`, `meta`, `tiktok`, `snapchat`, and `other`. When `other` is selected, it also sends `otherPlatform`; this is an enquiry about fit, not a promise of audit coverage. The handler validates inputs, discards honeypot submissions, limits requests per IP, sends the enquiry to Marcos with the requested language, and sends a personalized auto-reply in English or French for either spend branch. The country selection makes the spend ranges CAD for Canada and USD for the US; the owner email states the chosen currency. A non-2xx result displays a localized error.

The form promises a personal reply within 2 business days and shows a dedicated thank-you state only after the handler returns a successful response. Failed or unconfigured submissions keep the form visible and show an error. This reply-time promise needs to be met operationally after launch.

The supplied email address is the form destination and sender. It also appears on the privacy page as the public privacy contact, as requested in the policy draft.

## Search and WordPress blog launch

Each sales page has a localized title and meta description, one H1, a self canonical URL, social preview metadata, and factual `WebSite`/`Person`/`Service` JSON-LD. Each privacy page has its own title, description, and canonical URL. The four pages carry reciprocal `hreflang` links (`en`, `fr-CA`, and `x-default` to English) and visible language navigation. Main copy is present in HTML without JavaScript. The footer links to its matching privacy page, `/blog/` (marked English on translated pages), LinkedIn, and FromTheShower; Instagram is intentionally absent.

**Keep the existing WordPress install for `/blog/` and future posts.** The current `/blog/` is a WordPress page (ID 258), separate from the four current posts Marcos plans to remove manually. The live site already has a Yoast sitemap at `https://marcosarteaga.com/sitemap_index.xml` and a virtual `robots.txt` that points to it. Do not deploy a competing static `robots.txt` or one-page `sitemap.xml`; Yoast should remain the sitemap source for both the homepage and future blog posts.

To prepare the WordPress templates after editing English HTML, run `python3 tools/build-wordpress-template.py`. French copy lives in `tools/i18n_fr.py`; the build fails if a new visible English string lacks a translation. The build generates two localized HTML previews and four PHP templates. Install `wordpress/mu-plugins/marcos-audit-home.php` at `wp-content/mu-plugins/marcos-audit-home.php`, and install the four generated PHP files from `wordpress/mu-plugins/marcos-audit-home/` in that matching server directory. WordPress loads the top-level PHP file automatically. The generated templates output standalone HTML directly, so their metadata comes from these files rather than WordPress theme or Yoast head hooks. The WordPress editor remains for blog posts, not for these four pages.

The plugin serves the two French URLs directly; no translated WordPress pages or rewrite-rule flush is required. `/fr` and `/fr/privacy` redirect to the slash version. These custom routes are linked from the pages but are not WordPress Page objects, so do not assume Yoast includes them in its sitemap. Inspect the live Yoast sitemap and submit the two French URLs individually in Search Console if they are absent.

Create and publish an otherwise empty WordPress Page with the slug `privacy`. The must-use plugin serves `privacy-template.php` when WordPress recognizes that page. Its URL should be `https://marcosarteaga.com/privacy/`; WordPress and Yoast can then include it in the page sitemap. Do not deploy `privacy/index.html` into the public web root as a second copy.

Before going live:

1. Back up WordPress and deploy the homepage plugin and root assets as above. Keep WordPress's existing front-page setting so `is_front_page()` selects the generated template. Check Plesk's document-root index behavior; a leftover public `index.html` must not override WordPress `index.php`.
2. Verify all four page URLs return HTTP 200, the language links and matching privacy links work, `https://marcosarteaga.com/blog/` still returns a working blog index, and HTTP/`www` redirect to HTTPS non-`www`. Check that `/index.html` is not a second indexable copy. Test each language's form and both spend branches with real inboxes; the local build cannot verify SMTP delivery or WordPress routing.
3. After deleting the old posts and any unwanted template/commerce pages in WordPress, inspect the Yoast sitemap. It should contain only pages and posts intended for search. Removed articles without a close replacement should return 404 or 410, not redirect to the unrelated sales page. Update the blog's current outdated title (`Blog - Marcos Arteaga - Father & Full Stack Marketer`) and “Archives” heading in WordPress/Yoast.
4. Confirm the live `robots.txt` still points to the Yoast sitemap, WordPress's “Discourage search engines” setting is off, and the sales pages, privacy pages, and blog do not carry `noindex`. Verify the domain in Google Search Console, submit `sitemap_index.xml`, and inspect the live English, French, and blog URLs. Then run IndieSEO against the deployed site; a local file preview cannot prove crawlability, redirects, or indexing.

These are launch checks, not claims that Google has indexed the new page. A sitemap and structured data help discovery and understanding but do not guarantee search appearance.

## Privacy launch checks

The policy draft's 12-month non-client enquiry retention is a commitment Marcos must carry out in the Google Workspace mailbox; the site does not delete emails automatically. Before publishing, set up a repeatable deletion process and verify any legal retention exception. Check the live WordPress install, plugins, and Plesk settings for cookies, analytics, host-log and spam-record retention, and data location; update the policy if they differ from the local code. The form's anti-spam file stores a hashed IP key and timestamps outside the web root. The policy discloses Google Workspace and Plesk as service providers and the possibility of processing outside Québec.

## Source and boundaries

Page copy follows `website-brief.md`, with scope and deliverables checked against `offer-pack-v1.md` in `/Users/marcos/marcosarteaga.com/`. Marcos subsequently expanded platform coverage to TikTok Ads and Snapchat Ads alongside Google Ads and Meta Ads. The audit fee and payment terms are intentionally absent from public copy. Monthly ad-spend ranges are qualification data, not audit pricing.

The portrait and selected logos were copied from the current live site for reuse. The Groupe Dynamite logo is the GDI mark from [Groupe Dynamite's official site](https://groupedynamite.com/). The additional two small mark-only logo files are held in `assets/` but not shown because their identity is unclear at the size supplied.
