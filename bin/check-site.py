#!/usr/bin/env python3
"""Reject unapproved HTML routes and broken local links in a built site."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and name in {"href", "src"}:
                self.urls.append(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default="_site")
    parser.add_argument("--baseurl", default="/al-folio")
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    baseurl = args.baseurl.rstrip("/")
    manifest = Path(__file__).resolve().parent.parent / "test/site-routes.json"
    routes = json.loads(manifest.read_text())
    expected = {route.lstrip("/") + ("index.html" if route.endswith("/") else "") for route in routes}
    actual = {str(path.relative_to(root)) for path in root.rglob("*.html")}
    errors = []
    for item in sorted(actual - expected):
        errors.append(f"Unapproved HTML output: {item}")
    for item in sorted(expected - actual):
        errors.append(f"Missing page: {item}")
    for name in ("docs", "test", "bin", "node_modules", "vendor", "README.md", "DESIGN.md", "AGENTS.md", "package.json"):
        if (root / name).exists():
            errors.append(f"Source-only material leaked into the site: {name}")
    for item in sorted(actual):
        links = Links()
        links.feed((root / item).read_text())
        for url in links.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            path = unquote(parts.path)
            if path.startswith("/"):
                if baseurl and not (path == baseurl or path.startswith(baseurl + "/")):
                    errors.append(f"{item}: link is missing baseurl: {url}")
                    continue
                target = root / path[len(baseurl):].lstrip("/")
            else:
                target = (root / item).parent / path
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"{item}: link escapes the site: {url}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{item}: missing local target: {url}")
    if errors:
        raise SystemExit("Site check failed:\n" + "\n".join(sorted(set(errors))))
    print(f"Site check passed: {len(actual)} approved HTML pages; local links and assets resolve.")


if __name__ == "__main__":
    main()
