"""Build with Jekyll before running these checks against the published files."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


class SiteHTML(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links = []
        self.resources = []
        self.ids = set()
        self.author_name = ""
        self.text = ""
        self.buttons = []
        self._in_author_name = False
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("img", "script") and attrs.get("src"):
            self.resources.append(attrs["src"])
        if tag == "link" and attrs.get("href") and attrs.get("rel") != "canonical":
            self.resources.append(attrs["href"])
        if tag == "h3" and "author__name" in attrs.get("class", "").split():
            self._in_author_name = True
        if tag == "button":
            self.buttons.append(attrs)

    def handle_endtag(self, tag):
        if tag == "h3":
            self._in_author_name = False

    def handle_data(self, data):
        self.text += data
        if self._in_author_name:
            self.author_name += data


class SiteTests(unittest.TestCase):
    def parse(self, path):
        self.assertTrue(path.is_file(), f"Build the site first; missing {path}")
        return SiteHTML(path.read_text(encoding="utf-8"))

    def assert_local_targets(self, page, urls):
        for url in urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            target = SITE / unquote(parts.path).lstrip("/") if parts.path.startswith("/") else page.parent / unquote(parts.path)
            if not parts.path:
                target = page
            elif parts.path.endswith("/") or target.is_dir():
                target = target / "index.html"
            with self.subTest(page=page.relative_to(SITE), url=url):
                self.assertTrue(target.is_file(), f"Broken local URL: {url}")
                if parts.fragment and target == SITE / "index.html":
                    self.assertIn(unquote(parts.fragment), self.parse(target).ids)

    def test_homepage_identity(self):
        home = self.parse(SITE / "index.html")
        self.assertEqual(home.author_name.strip(), "Xiaoyun Dong")
        self.assertTrue(any("user=YK8VvrAAAAAJ" in url for url in home.links))
        self.assertIn("mailto:luciana_dong@163.com", home.links)
        for button in home.buttons:
            self.assertTrue(button.get("aria-label"), "Menu buttons need an accessible name")

    def test_local_resources_and_anchors(self):
        page = SITE / "index.html"
        home = self.parse(page)
        self.assertTrue({"about", "news", "featured", "publications", "research"} <= home.ids)
        self.assert_local_targets(page, home.resources + home.links)
        source = page.read_text(encoding="utf-8")
        self.assertNotIn("{%", source)
        self.assertNotIn("{{", source)

    def test_legacy_page_export(self):
        page = SITE / "research/f1tenth/index.html"
        old = self.parse(page)
        self.assertEqual(page.read_bytes(), (ROOT / "research/f1tenth/index.html").read_bytes())
        self.assert_local_targets(page, old.resources)


if __name__ == "__main__":
    unittest.main()
