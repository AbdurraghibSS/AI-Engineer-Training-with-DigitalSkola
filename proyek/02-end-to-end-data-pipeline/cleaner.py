"""
Cleaner

Cleans scraped data (RSS + books + quotes) BEFORE loading to DB.
This is the "Transform" step of the ETL path.

"""

import logging
from typing import List, Dict

import pandas as pd

log = logging.getLogger(__name__)


def clean_articles(raw_records: List[Dict]) -> pd.DataFrame:
    """Clean scraped data. Returns DataFrame ready for DB insert."""
    if not raw_records:
        return pd.DataFrame(columns=["title", "url", "source", "content", "published_at"])

    df = pd.DataFrame(raw_records)
    initial = len(df)
    log.info("Mulai cleaning: %d record", initial)

    df = df.drop_duplicates(subset=["url"])
    log.info("Setelah drop duplikat URL: %d record (-%d)", len(df), initial - len(df))

    before = len(df)
    df = df.dropna(subset=["title", "url"])
    if len(df) < before:
        log.info("Drop baris tanpa title/url: -%d", before - len(df))

    df["title"] = df["title"].astype(str).str.strip()
    df["url"] = df["url"].astype(str).str.strip()
    df["source"] = df["source"].astype(str).str.strip().str.lower()
    df["content"] = df["content"].fillna("").astype(str).str.strip()

    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce", utc=True)
    df["published_at"] = df["published_at"].dt.tz_localize(None)

    before2 = len(df)
    df = df[df["content"].str.len() >= 20]
    if len(df) < before2:
        log.info("Drop konten pendek (<20 char): -%d", before2 - len(df))

    # Hanya kolom yang masuk DB
    df = df[["title", "url", "source", "content", "published_at"]]
    df = df.reset_index(drop=True)

    log.info("Cleaning selesai: %d -> %d record", initial, len(df))
    return df
