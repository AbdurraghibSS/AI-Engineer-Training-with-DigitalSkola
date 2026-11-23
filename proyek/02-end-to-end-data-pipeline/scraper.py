"""
Scraper

Tiga sumber data:
  1. RSS Feeds (berita dari NYT, BBC, CNN, dll)
  2. books.toscrape.com
  3. quotes.toscrape.com

"""

import time
import logging
from typing import Optional, List, Dict
from datetime import datetime, timezone
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

HEADERS = {"User-Agent": "DigitalSkola-Learner/1.0"}
REQUEST_TIMEOUT = 15
DELAY_BETWEEN_REQUESTS = 1.0


def _get(url: str) -> BeautifulSoup:
    time.sleep(DELAY_BETWEEN_REQUESTS)
    resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


# ==================================================================
# 1. RSS NEWS FEEDS
# ==================================================================
RSS_FEEDS = [
    {"url": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",      "source": "nytimes"},
    {"url": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml", "source": "nytimes"},
    {"url": "https://feeds.bbci.co.uk/news/world/rss.xml",                "source": "bbc"},
    {"url": "https://feeds.bbci.co.uk/news/technology/rss.xml",           "source": "bbc"},
    {"url": "http://rss.cnn.com/rss/edition_world.rss",                   "source": "cnn"},
    {"url": "http://rss.cnn.com/rss/edition_technology.rss",              "source": "cnn"},
    {"url": "https://www.aljazeera.com/xml/rss/all.xml",                  "source": "aljazeera"},
    {"url": "https://feeds.skynews.com/feeds/rss/world.xml",              "source": "skynews"},
    {"url": "https://techcrunch.com/feed/",                               "source": "techcrunch"},
]


def _parse_rss_xml(xml_text: str, source_name: str) -> List[Dict]:
    """
    Parse RSS XML text and extract articles.

    RSS XML structure:
        <item>
            <title>Judul artikel</title>
            <link>https://example.com/article</link>
            <description>Isi singkat artikel</description>
            <pubDate>Mon, 01 Jan 2024 12:00:00 +0000</pubDate>
        </item>
    """
    soup = BeautifulSoup(xml_text, "xml")

    items = soup.find_all("item")
    results = []

    for item in items:
        title_tag = item.find("title")
        link_tag = item.find("link")
        desc_tag = item.find("description")
        pubdate_tag = item.find("pubDate")

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        url = link_tag.get_text(strip=True)

        # Clean HTML dari description
        content = ""
        if desc_tag:
            raw_desc = desc_tag.get_text(strip=True)
            content = BeautifulSoup(raw_desc, "html.parser").get_text(strip=True)

        # Parse published date
        published_at = None
        if pubdate_tag:
            raw_date = pubdate_tag.get_text(strip=True)
            for fmt in [
                "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S %Z",
                "%Y-%m-%dT%H:%M:%S%z",
            ]:
                try:
                    published_at = datetime.strptime(raw_date, fmt)
                    break
                except ValueError:
                    continue

        results.append({
            "title": title[:200],
            "url": url,
            "source": source_name,
            "content": content if content else title,
            "published_at": published_at,
        })

    return results


def scrape_rss(feeds: Optional[List[Dict]] = None) -> List[Dict]:
    if feeds is None:
        feeds = RSS_FEEDS

    all_articles = []
    for feed in feeds:
        url = feed["url"]
        source = feed["source"]
        log.info("[rss] Scraping %s: %s", source, url)

        try:
            time.sleep(DELAY_BETWEEN_REQUESTS)
            resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            articles = _parse_rss_xml(resp.text, source)
            all_articles.extend(articles)
            log.info("[rss] %s: %d artikel (total: %d)", source, len(articles), len(all_articles))
        except Exception as e:
            log.warning("[rss] %s gagal: %s", source, e)
            continue

    return all_articles


# ==================================================================
# 2. BOOKS.TOSCRAPE.COM
# ==================================================================
BOOKS_BASE = "https://books.toscrape.com/"
STAR_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_books(max_pages: int = 10) -> List[Dict]:
    results = []

    for page_num in range(1, max_pages + 1):
        url = f"{BOOKS_BASE}catalogue/page-{page_num}.html"
        log.info("[books] Scraping halaman %d: %s", page_num, url)

        try:
            soup = _get(url)
        except requests.HTTPError as e:
            log.warning("[books] Halaman %d gagal (%s), berhenti.", page_num, e)
            break

        pods = soup.select("article.product_pod")
        if not pods:
            break

        for pod in pods:
            h3 = pod.select_one("h3 a")
            title = h3["title"]
            relative_url = h3["href"]
            book_url = urljoin(url, relative_url)

            price = pod.select_one("p.price_color").get_text(strip=True)

            avail = pod.select_one("p.instock.availability")
            availability = avail.get_text(strip=True) if avail else "Unknown"

            star_tag = pod.select_one("p.star-rating")
            star_classes = [c for c in star_tag.get("class", []) if c != "star-rating"]
            rating = STAR_MAP.get(star_classes[0], 0) if star_classes else 0

            results.append({
                "title": title,
                "url": book_url,
                "source": "books.toscrape",
                "content": f"{title}. Price: {price}. Rating: {rating}/5 stars. {availability}.",
                "published_at": None,
            })

        log.info("[books] Halaman %d: %d buku (total: %d)", page_num, len(pods), len(results))

    return results


# ==================================================================
# 3. QUOTES.TOSCRAPE.COM
# ==================================================================
QUOTES_BASE = "https://quotes.toscrape.com/"


def scrape_quotes(max_pages: int = 10) -> List[Dict]:
    results = []

    for page_num in range(1, max_pages + 1):
        url = f"{QUOTES_BASE}page/{page_num}/"
        log.info("[quotes] Scraping halaman %d: %s", page_num, url)

        try:
            soup = _get(url)
        except requests.HTTPError as e:
            log.warning("[quotes] Halaman %d gagal (%s), berhenti.", page_num, e)
            break

        quotes = soup.select("div.quote")
        if not quotes:
            break

        for q in quotes:
            text = q.select_one("span.text").get_text(strip=True)
            author = q.select_one("small.author").get_text(strip=True)
            tags = [t.get_text(strip=True) for t in q.select("div.tags a.tag")]
            tag_str = ", ".join(tags) if tags else "none"

            results.append({
                "title": text[:100],
                "url": f"{QUOTES_BASE}#quote-{len(results) + 1}-{author.replace(' ', '-')}",
                "source": "quotes.toscrape",
                "content": f"{text} -- {author}. Tags: {tag_str}.",
                "published_at": datetime.now(timezone.utc),
            })

        log.info("[quotes] Halaman %d: %d kutipan (total: %d)", page_num, len(quotes), len(results))

    return results


# ==================================================================
# SCRAPE ALL
# ==================================================================
def scrape_all(
    rss: bool = True,
    book_pages: int = 10,
    quote_pages: int = 10,
) -> List[Dict]:
    all_records = []

    log.info("=" * 60)
    log.info("MULAI SCRAPING")
    log.info("=" * 60)

    if rss:
        rss_articles = scrape_rss()
        all_records.extend(rss_articles)
        log.info("Total RSS: %d", len(rss_articles))

    books = scrape_books(max_pages=book_pages)
    all_records.extend(books)
    log.info("Total buku: %d", len(books))

    quotes = scrape_quotes(max_pages=quote_pages)
    all_records.extend(quotes)
    log.info("Total kutipan: %d", len(quotes))

    log.info("=" * 60)
    log.info("SELESAI. Total record: %d", len(all_records))
    log.info("=" * 60)

    return all_records


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s")
    records = scrape_all(book_pages=2, quote_pages=2)
    print(f"\nTotal: {len(records)} records")
    for r in records[:5]:
        print(f"  [{r['source']}] {r['title'][:60]}")
