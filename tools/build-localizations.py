#!/usr/bin/env python3
"""Build the reviewed Québec French pages from the English page structure.

Every visible text node must have a translation or be an explicitly unchanged
brand, platform, symbol, or email address. New English copy fails the build
until the localized copy is supplied.
"""

from html import escape, unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re

from i18n_fr import ATTRS as FR_ATTRS, TEXT as FR_TEXT, SCHEMA as FR_SCHEMA


ROOT = Path(__file__).resolve().parents[1]
UNCHANGED = {
    ".", "*", "EN", "FR", "Marcos Arteaga", "marcos@fromtheshower.com",
    "Google Ads", "Meta Ads", "TikTok Ads", "Snapchat Ads", "Hippoc", "Future",
    "Mobile Nations", "MindGeek", "Fhios", "Groupe Dynamite", "LinkedIn",
    "FromTheShower", "© Marcos Arteaga",
}


class Localizer(HTMLParser):
    def __init__(self, text_map: dict[str, str], attr_map: dict[str, str]):
        super().__init__(convert_charrefs=False)
        self.text_map = text_map
        self.attr_map = attr_map
        self.parts: list[str] = []
        self.in_script = False
        self.missing: set[str] = set()

    def _start(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        raw = self.get_starttag_text()
        def replace_attr(match: re.Match[str]) -> str:
            key, quote, value = match.group(1), match.group(2), match.group(3)
            original = unescape(value)
            translated_value = self.attr_map.get(original, self.text_map.get(original))
            if translated_value is None:
                return match.group(0)
            translated = escape(translated_value, quote=True)
            return f'{key}={quote}{translated}{quote}'
        raw = re.sub(r'\b(content|alt|placeholder|aria-label)=("|\')(.*?)\2', replace_attr, raw)
        self.parts.append(raw)
        if tag == "script":
            self.in_script = True

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._start(tag, attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._start(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        self.parts.append(f"</{tag}>")
        if tag == "script":
            self.in_script = False

    def handle_data(self, data: str) -> None:
        value = data.strip()
        if self.in_script or not value:
            self.parts.append(data)
        elif value in self.text_map:
            self.parts.append(data.replace(value, escape(self.text_map[value], quote=False), 1))
        else:
            self.parts.append(data)
            if value not in UNCHANGED:
                self.missing.add(value)

    def handle_entityref(self, name: str) -> None:
        self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.parts.append(f"&#{name};")

    def handle_comment(self, data: str) -> None:
        self.parts.append(f"<!--{data}-->")

    def handle_decl(self, decl: str) -> None:
        self.parts.append(f"<!{decl}>")


def translate(source: Path, text_map: dict, attr_map: dict, schema: dict) -> str:
    is_privacy = source.parent.name == "privacy"
    parser = Localizer(text_map, attr_map)
    parser.feed(source.read_text(encoding="utf-8"))
    if parser.missing:
        raise SystemExit(f"Untranslated text in {source}: {sorted(parser.missing)}")
    html = "".join(parser.parts)
    html = html.replace('<html lang="en">', '<html lang="fr-CA">', 1)
    base = "https://marcosarteaga.com/fr/"
    canonical = base + ("privacy/" if is_privacy else "")
    html = re.sub(r'(<link rel="canonical" href=")[^"]+', lambda m: m.group(1) + canonical, html, count=1)
    html = re.sub(r'(<meta property="og:url" content=")[^"]+', lambda m: m.group(1) + canonical, html, count=1)

    links = ("/privacy/", "/fr/privacy/") if is_privacy else ("/", "/fr/")
    labels = ("EN", "FR")
    langs = ("en", "fr-CA")
    nav = '<nav class="language-nav" aria-label="' + attr_map['Language'] + '">'
    for link, label, lang in zip(links, labels, langs):
        current = ' aria-current="page"' if label == "FR" else ''
        nav += f'<a href="{link}" lang="{lang}"{current}>{label}</a>'
    nav += '</nav>'
    html = re.sub(r'<nav class="language-nav"[^>]*>.*?</nav>', lambda _: nav, html, count=1)

    if is_privacy:
        html = html.replace('href="../assets/', 'href="../../assets/')
        html = html.replace('href="../styles.css"', 'href="../../styles.css"')
    else:
        html = html.replace('href="assets/', 'href="../assets/')
        html = html.replace('src="assets/', 'src="../assets/')
        html = html.replace('href="styles.css"', 'href="../styles.css"')
        html = html.replace('src="config.js"', 'src="../config.js"')
        html = html.replace('src="script.js"', 'src="../script.js"')
        html = html.replace('name="locale" value="en"', 'name="locale" value="fr"')
        def translate_schema(match: re.Match[str]) -> str:
            graph = json.loads(match.group(1))
            graph['@graph'][0]['@id'] = base + '#website'
            graph['@graph'][0]['url'] = base
            graph['@graph'][0]['inLanguage'] = 'fr-CA'
            graph['@graph'][2]['@id'] = base + '#audit'
            graph['@graph'][2]['name'] = schema['name']
            graph['@graph'][2]['serviceType'] = schema['serviceType']
            graph['@graph'][2]['description'] = schema['description']
            graph['@graph'][2]['url'] = base + '#offer'
            return '<script type="application/ld+json">\n' + json.dumps(graph, ensure_ascii=False, indent=6) + '\n    </script>'
        html, replaced = re.subn(r'<script type="application/ld\+json">(.*?)</script>', translate_schema, html, count=1, flags=re.S)
        if replaced != 1:
            raise SystemExit('Expected one structured-data script')
    return html


for relative in ("index.html", "privacy/index.html"):
    source = ROOT / relative
    target = ROOT / "fr" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(translate(source, FR_TEXT, FR_ATTRS, FR_SCHEMA), encoding="utf-8")
    print(f"Updated {target.relative_to(ROOT)} from {source.relative_to(ROOT)}")
