from typing import Optional, List, Dict, Tuple
from datetime import date, timedelta
import math
from sqlalchemy import create_engine, text
from pydantic_settings import BaseSettings, SettingsConfigDict
import pandas as pd
import logging

log = logging.getLogger(__name__)

class DBSettings(BaseSettings):
    database_url: str
    student_name: str

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=False, extra="ignore"
    )

settings = DBSettings()
engine = create_engine(settings.database_url)

SCHEMA = "ai_engineer3"
ARTICLES_TABLE = f'"{SCHEMA}".articles_{settings.student_name}'
ATTRITION_TABLE_NAME = f"raw_attrition_{settings.student_name}"
ATTRITION_TABLE = f'"{SCHEMA}".{ATTRITION_TABLE_NAME}'

def init_db():
    """Create tables and indexes if they don't exist."""
    ddl = f"""
    CREATE TABLE IF NOT EXISTS {ARTICLES_TABLE} (
        id           SERIAL PRIMARY KEY,
        title        TEXT NOT NULL,
        url          TEXT UNIQUE NOT NULL,
        source       TEXT NOT NULL,
        content      TEXT,
        published_at TIMESTAMP,
        scraped_at   TIMESTAMP DEFAULT NOW()
    );
    CREATE INDEX IF NOT EXISTS idx_articles_source
        ON {ARTICLES_TABLE}(source);
    CREATE INDEX IF NOT EXISTS idx_articles_published
        ON {ARTICLES_TABLE}(published_at DESC);
    """
    with engine.begin() as conn:
        conn.execute(text(ddl))
    log.info("Database ready. Table: %s", ARTICLES_TABLE)

def save_articles(df: pd.DataFrame) -> int:
    """Insert articles with ON CONFLICT — safe to re-run."""
    if df.empty:
        log.warning("DataFrame kosong, tidak ada yang di-insert.")
        return 0

    inserted = 0
    with engine.begin() as conn:
        for _, row in df.iterrows():
            result = conn.execute(
                text(f"""
                    INSERT INTO {ARTICLES_TABLE}
                        (title, url, source, content, published_at)
                    VALUES
                        (:title, :url, :source, :content, :published_at)
                    ON CONFLICT (url) DO NOTHING
                """),
                {
                    "title": row["title"],
                    "url": row["url"],
                    "source": row["source"],
                    "content": row["content"],
                    "published_at": row["published_at"]
                    if pd.notna(row["published_at"])
                    else None,
                },
            )
            inserted += result.rowcount

    log.info("Insert selesai: %d baru dari %d record.", inserted, len(df))
    return inserted


def count_articles() -> int:
    """Count total articles in DB."""
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {ARTICLES_TABLE}"))
        return result.scalar()

def count_articles_by_source() -> Dict[str, int]:
    """
    Hitung jumlah artikel per source.
    Return contoh: {"bbc": 50, "nytimes": 30, "books.toscrape": 200}
    """
    with engine.connect() as conn:
        rows = conn.execute(
            text(f"""
                SELECT
                    source,
                    COUNT(*) as count
                FROM {ARTICLES_TABLE}
                GROUP BY source
                ORDER BY count DESC
                """)
            ).mappings().all()
        return {row["source"]: row["count"] for row in rows}

def get_articles(
    source: Optional[str] = None,
    title: Optional[str] = None,
    limit: int = 20,
) -> List[Dict]:
    """
    Cari articles dengan optional filter source dan title.

    Contoh pemanggilan:
      get_articles(source="bbc", limit=5)           → artikel BBC saja
      get_articles(title="python", limit=10)         → judul mengandung "python"
      get_articles(source="bbc", title="AI", limit=5) → BBC + judul ada "AI"
    """
    query = f"SELECT * FROM {ARTICLES_TABLE} WHERE 1=1"
    params = {"limit": limit}

    if source:
        query += " AND source = :source"
        params["source"] = source

    if title:
        query += " AND title ILIKE :title"
        params["title"] = f"%{title}%"

    query += " ORDER BY published_at DESC NULLS LAST LIMIT :limit"

    with engine.connect() as conn:
        rows = conn.execute(text(query), params).mappings().all()
    return [dict(r) for r in rows]


def get_article_by_id(article_id: int) -> Optional[Dict]:
    """Get single article by ID. Return None jika tidak ditemukan."""
    with engine.connect() as conn:
        row = conn.execute(
            text(f"SELECT * FROM {ARTICLES_TABLE} WHERE id = :id"),
            {"id": article_id},
        ).mappings().first()
    return dict(row) if row else None


def get_attrition_summary() -> Dict:
    """
    Overall stats: total karyawan, jumlah & rate attrition.
    Return contoh: {"total_employees": 1470, "attrition_yes": 237, ...}
    """
    with engine.connect() as conn:
        row = conn.execute(
            text(f"""
                SELECT
                    COUNT(*) AS total_employees,
                    COUNT(*) FILTER (WHERE "Attrition" = 'Yes') AS attrition_yes
                FROM {ATTRITION_TABLE}
            """)
        ).mappings().first()
    if row:
        total_employees = row["total_employees"]
        attrition_yes = row["attrition_yes"]
        attrition_rate = (attrition_yes / total_employees) if total_employees > 0 else 0
        return {
            "total_employees": total_employees,
            "attrition_yes": attrition_yes,
            "attrition_rate": attrition_rate,
            "attrition_no": total_employees - attrition_yes,
        }
    else:
        return {
            "total_employees": 0,
            "attrition_yes": 0,
            "attrition_rate": 0,
            "attrition_no": 0,
        }


def get_attrition_by_department() -> List[Dict]:
    """
    Attrition rate + avg income per department.
    Ini gabungan query 1 & 2 dari transform_attrition.sql Session 9.
    """
    with engine.connect() as conn:
        rows = conn.execute(
            text(f"""
                SELECT
                    "Department",
                    COUNT(*) AS total,
                    COUNT(*) FILTER (WHERE "Attrition" = 'Yes') AS attrition_count,
                    round(count(*) FILTER (WHERE "Attrition" = 'Yes')::numeric / COUNT(*)::numeric, 4) AS attrition_rate,
                    round(AVG("MonthlyIncome")::numeric, 2) AS avg_income
                FROM {ATTRITION_TABLE}
                GROUP BY "Department"
                ORDER BY attrition_rate DESC
            """)
        ).mappings().all()

    return [dict(row) for row in rows]


def get_attrition_by_tenure() -> List[Dict]:
    """
    Attrition by tenure bucket.
    Ini query 3 dari transform_attrition.sql Session 9.
    """
    with engine.connect() as conn:
        rows = conn.execute(
            text(f"""
                SELECT
                    CASE
                        WHEN "YearsAtCompany" < 1 THEN '<1 year'
                        WHEN "YearsAtCompany" BETWEEN 1 AND 3 THEN '1-3 years'
                        WHEN "YearsAtCompany" BETWEEN 4 AND 6 THEN '4-6 years'
                        WHEN "YearsAtCompany" BETWEEN 7 AND 10 THEN '7-10 years'
                        ELSE '>10 years'
                    END AS tenure_bucket,
                    COUNT(*) AS total,
                    COUNT(*) FILTER (WHERE "Attrition" = 'Yes') AS attrition_count,
                    round(count(*) FILTER (WHERE "Attrition" = 'Yes')::numeric / COUNT(*)::numeric, 4) AS attrition_rate
                FROM {ATTRITION_TABLE}
                GROUP BY tenure_bucket
                ORDER BY tenure_bucket
            """)
        ).mappings().all()
    return [dict(row) for row in rows]

def get_attrition_by_overtime() -> List[Dict]:
    """
    Attrition by overtime status.
    Ini query 4 dari transform_attrition.sql Session 9.
    """
    with engine.connect() as conn:
        rows = conn.execute(
            text(f"""
                SELECT
                    "OverTime",
                    COUNT(*) AS total,
                    COUNT(*) FILTER (WHERE "Attrition" = 'Yes') AS attrition_count,
                    round(count(*) FILTER (WHERE "Attrition" = 'Yes')::numeric / COUNT(*)::numeric, 4) AS attrition_rate
                FROM {ATTRITION_TABLE}
                GROUP BY "OverTime"
                ORDER BY "OverTime"
            """)
        ).mappings().all()
    return [dict(row) for row in rows]


def get_top_earners_by_department(limit_per_dept: int = 5) -> List[Dict]:
    """
    Top earners per department menggunakan RANK() window function.
    Ini query 5 dari transform_attrition.sql Session 9.
    """
    with engine.connect() as conn:
        rows = conn.execute(
            text(f"""
                SELECT *
                FROM (
                    SELECT
                        "Department",
                        "EmployeeNumber",
                        "JobRole",
                        "MonthlyIncome",
                        "Attrition",
                        RANK() OVER (PARTITION BY "Department" ORDER BY "MonthlyIncome" DESC) AS income_rank
                    FROM {ATTRITION_TABLE}
                ) sub
                WHERE income_rank <= :limit_per_dept
                ORDER BY "Department", income_rank
            """),
            {"limit_per_dept": limit_per_dept}
        ).mappings().all()
    return [dict(row) for row in rows]


# ==================================================================
# MINI PROJECT 2
# ==================================================================

# ---------- Task 1: Article Search dengan Pagination ----------
def _build_article_filters(
    source: Optional[str],
    title: Optional[str],
    date_from: Optional[date],
    date_to: Optional[date],
) -> Tuple[str, Dict]:
    """
    Bangun klausa WHERE + params yang dipakai bersama oleh query COUNT
    dan query SELECT, supaya total_items selalu konsisten dengan data.
    """
    where = " WHERE 1=1"
    params: Dict = {}

    if source:
        where += " AND source = :source"
        params["source"] = source
    if title:
        where += " AND title ILIKE :title"
        params["title"] = f"%{title}%"
    if date_from:
        where += " AND published_at >= :date_from"
        params["date_from"] = date_from
    if date_to:
        # published_at bertipe TIMESTAMP, jadi "<= 2026-11-16" hanya mencakup
        # tepat jam 00:00. Pakai "< hari berikutnya" agar seluruh hari ikut.
        where += " AND published_at < :date_to_next"
        params["date_to_next"] = date_to + timedelta(days=1)

    return where, params


def search_articles(
    source: Optional[str] = None,
    title: Optional[str] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    page: int = 1,
    per_page: int = 10,
) -> Dict:
    """
    Cari artikel dengan filter + pagination (OFFSET/LIMIT).
    OFFSET = (page - 1) * per_page
    """
    where, params = _build_article_filters(source, title, date_from, date_to)

    with engine.connect() as conn:
        total_items = conn.execute(
            text(f"SELECT COUNT(*) FROM {ARTICLES_TABLE}{where}"), params
        ).scalar()

        rows = conn.execute(
            text(f"""
                SELECT * FROM {ARTICLES_TABLE}{where}
                ORDER BY published_at DESC NULLS LAST, id
                LIMIT :limit OFFSET :offset
            """),
            {**params, "limit": per_page, "offset": (page - 1) * per_page},
        ).mappings().all()

    return {
        "data": [dict(r) for r in rows],
        "page": page,
        "per_page": per_page,
        "total_items": total_items,
        "total_pages": math.ceil(total_items / per_page),
    }


# ---------- Task 3: Department Detail ----------
def get_department_detail(dept_name: str, top_n: int = 3) -> Optional[Dict]:
    """
    Statistik lengkap satu department + top earners.
    Pencocokan nama department case-insensitive ("sales" == "Sales").
    Return None jika department tidak ditemukan (endpoint → 404).
    """
    with engine.connect() as conn:
        stats = conn.execute(
            text(f"""
                SELECT
                    "Department" AS department,
                    COUNT(*) AS total_employees,
                    COUNT(*) FILTER (WHERE "Attrition" = 'Yes') AS attrition_count,
                    round(COUNT(*) FILTER (WHERE "Attrition" = 'Yes')::numeric
                          / COUNT(*)::numeric, 4) AS attrition_rate,
                    round(AVG("MonthlyIncome")::numeric, 2) AS avg_income,
                    MIN("MonthlyIncome") AS min_income,
                    MAX("MonthlyIncome") AS max_income
                FROM {ATTRITION_TABLE}
                WHERE LOWER("Department") = LOWER(:dept)
                GROUP BY "Department"
            """),
            {"dept": dept_name},
        ).mappings().first()

        if stats is None:
            return None

        top_earners = conn.execute(
            text(f"""
                SELECT "EmployeeNumber", "JobRole", "MonthlyIncome"
                FROM (
                    SELECT
                        "EmployeeNumber",
                        "JobRole",
                        "MonthlyIncome",
                        RANK() OVER (ORDER BY "MonthlyIncome" DESC) AS income_rank
                    FROM {ATTRITION_TABLE}
                    WHERE "Department" = :dept
                ) ranked
                ORDER BY income_rank, "EmployeeNumber"
                LIMIT :top_n
            """),
            {"dept": stats["department"], "top_n": top_n},
        ).mappings().all()

    return {**dict(stats), "top_earners": [dict(r) for r in top_earners]}


# ---------- Task 4: Attrition Risk Profile ----------
def get_attrition_risk_profile(limit: int = 20) -> Dict:
    """
    Karyawan high-risk attrition:
      - OverTime = 'Yes'
      - YearsAtCompany < 3
      - MonthlyIncome di bawah rata-rata department-nya
    Pakai CTE dept_avg untuk menghitung rata-rata per department.
    """
    cte = f"""
        WITH dept_avg AS (
            SELECT "Department", AVG("MonthlyIncome") AS avg_income
            FROM {ATTRITION_TABLE}
            GROUP BY "Department"
        ),
        high_risk AS (
            SELECT
                e."EmployeeNumber",
                e."Department",
                e."JobRole",
                e."MonthlyIncome",
                round(d.avg_income::numeric, 2) AS dept_avg_income,
                e."YearsAtCompany",
                e."OverTime",
                e."Attrition"
            FROM {ATTRITION_TABLE} e
            JOIN dept_avg d ON e."Department" = d."Department"
            WHERE e."OverTime" = 'Yes'
              AND e."YearsAtCompany" < 3
              AND e."MonthlyIncome" < d.avg_income
        )
    """
    with engine.connect() as conn:
        total = conn.execute(text(cte + "SELECT COUNT(*) FROM high_risk")).scalar()
        rows = conn.execute(
            text(cte + """
                SELECT * FROM high_risk
                ORDER BY "MonthlyIncome", "EmployeeNumber"
                LIMIT :limit
            """),
            {"limit": limit},
        ).mappings().all()

    return {
        "total_high_risk": total,
        "returned": len(rows),
        "data": [dict(r) for r in rows],
    }
