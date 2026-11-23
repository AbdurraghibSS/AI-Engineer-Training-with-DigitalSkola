"""
Pipeline

Dua path ke cloud PostgreSQL:
  Path A — ETL:  scrape → clean di pandas → load CLEAN
  Path B — ELT:  read CSV → load RAW → transform di SQL

Cara menjalankan:
    python pipeline.py --attrition-csv employee_attrition.csv
"""

import argparse
import logging

import pandas as pd

from db import engine, init_db, save_articles, count_articles, ARTICLES_TABLE, ATTRITION_TABLE_NAME, SCHEMA
from scraper import scrape_all
from cleaner import clean_articles

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
)
log = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Path A: ETL — scrape, clean in pandas, THEN load
# ------------------------------------------------------------------
def run_etl_scraping(rss: bool, book_pages: int, quote_pages: int) -> None:
    print("\n" + "=" * 60)
    print("  PATH A: ETL — Scrape → Clean → Load")
    print("=" * 60)

    # Extract
    print("\n[Extract] Scraping data dari web...")
    raw = scrape_all(rss=rss, book_pages=book_pages, quote_pages=quote_pages)
    print(f"  → Scraped: {len(raw)} raw records")

    # Transform (BEFORE load — this is what makes it ETL)
    print("\n[Transform] Cleaning data dengan Pandas...")
    df = clean_articles(raw)
    print(f"  → Cleaned: {len(df)} records")
    print(f"  → Sources: {df['source'].value_counts().to_dict()}")

    # Load (cleaned data)
    print(f"\n[Load] Menyimpan ke tabel {ARTICLES_TABLE}...")
    inserted = save_articles(df)
    total = count_articles()
    print(f"  → Inserted: {inserted} baru (duplikat di-skip)")
    print(f"  → Total di database: {total}")


# ------------------------------------------------------------------
# Path B: ELT — load RAW, transform AFTER in SQL
# ------------------------------------------------------------------
def run_elt_attrition(csv_path: str) -> None:
    print("\n" + "=" * 60)
    print("  PATH B: ELT — Load Raw → Transform in SQL")
    print("=" * 60)

    print(f"\n[Extract + Load] Reading {csv_path}...")
    df = pd.read_csv(csv_path)
    print(f"  → {len(df)} rows, {len(df.columns)} columns")
    print(f"  → Columns: {list(df.columns[:8])}...")
    print(f"  → Nulls: {df.isnull().sum().sum()} total")
    print(f"  → Loading RAW, TANPA cleaning...")

    df.to_sql(ATTRITION_TABLE_NAME, engine, if_exists="replace", index=False, schema=SCHEMA)

    print(f"  → Loaded table: {SCHEMA}.{ATTRITION_TABLE_NAME} (data mentah)")

    # Transform (AFTER load — this is what makes it ELT) terjadi saat query:
    # lihat fungsi get_attrition_* di db.py yang dipanggil endpoint /attrition/*.


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mini Project 2 — ETL & ELT pipeline")
    parser.add_argument(
        "--attrition-csv", required=True,
        help="Path to IBM HR Attrition CSV (download from Kaggle)",
    )
    parser.add_argument(
        "--book-pages", type=int, default=10,
        help="Book catalogue pages to scrape (default: 10)",
    )
    parser.add_argument(
        "--quote-pages", type=int, default=10,
        help="Quote pages to scrape (default: 10)",
    )
    parser.add_argument(
        "--no-rss", action="store_true",
        help="Skip RSS feeds (faster demo if internet is slow)",
    )
    parser.add_argument(
        "--skip-scraping", action="store_true",
        help="Skip all scraping, only run the CSV/ELT path",
    )
    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("  MINI PROJECT 2 — News & HR Analytics Pipeline")
    print("=" * 60)

    # Step 0: Connect + create tables
    print("\nStep 0: Inisialisasi Database...")
    init_db()

    # Step 1: ETL path (scrape → clean → load)
    if not args.skip_scraping:
        run_etl_scraping(
            rss=not args.no_rss,
            book_pages=args.book_pages,
            quote_pages=args.quote_pages,
        )

    # Step 2: ELT path (load raw → transform in SQL)
    run_elt_attrition(csv_path=args.attrition_csv)

    print("\n" + "=" * 60)
    print("  PIPELINE SELESAI")
    print("=" * 60 + "\n")
