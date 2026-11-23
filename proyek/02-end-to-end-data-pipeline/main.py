from fastapi import FastAPI, HTTPException, Header, Query, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import date, datetime, timedelta, timezone
import hmac
import secrets
import logging

import jwt as pyjwt
from pydantic_settings import BaseSettings, SettingsConfigDict

from db import (
    count_articles,
    count_articles_by_source,
    get_articles,
    get_article_by_id,
    get_attrition_summary,
    get_attrition_by_department,
    get_attrition_by_overtime,
    get_attrition_by_tenure,
    get_top_earners_by_department,
    # Mini Project 2
    search_articles,
    get_department_detail,
    get_attrition_risk_profile,
)

log = logging.getLogger(__name__)

class Settings(BaseSettings):
    database_url: str
    student_name: str
    internal_api_key: str
    jwt_secret: str
    jwt_expiry_minutes: int = 30
    client_id: str
    client_secret: str

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=False, extra="ignore"
    )

settings = Settings()

app = FastAPI(
    title="News & HR Analytics API",
    description=(
        "Mini Project 2 — Dua data pipeline, satu API.\n\n"
        "**Path A (ETL):** Scraped articles (RSS, books, quotes) "
        "cleaned di Pandas, loaded ke PostgreSQL.\n\n"
        "**Path B (ELT):** IBM HR Attrition CSV di-load mentah, "
        "di-transform dengan SQL saat query."
    ),
    version="1.0",
)
security_scheme = HTTPBearer(auto_error=False)

class Article(BaseModel):
    """Model untuk satu artikel dari tabel articles."""
    id: int
    title: str
    url: str
    source: str
    content: Optional[str] = None
    published_at: Optional[datetime] = None
    scraped_at: Optional[datetime] = None


class ArticleStats(BaseModel):
    total_articles: int
    by_source: Dict[str, int]


class TokenRequest(BaseModel):
    """Request body untuk POST /token."""
    client_id: str
    client_secret: str


class TokenResponse(BaseModel):
    """Response dari POST /token."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class AttritionSummary(BaseModel):
    total_employees: int
    attrition_yes: int
    attrition_no: int
    attrition_rate: float


class DepartmentAttrition(BaseModel):
    """Attrition per department."""
    Department: str
    total: int
    attrition_count: int
    attrition_rate: float
    avg_income: float


class OvertimeAttrition(BaseModel):
    """Attrition per overtime status."""
    OverTime: str
    total: int
    attrition_count: int
    attrition_rate: float


class TenureAttrition(BaseModel):
    """Attrition per tenure bucket."""
    tenure_bucket: str
    total: int
    attrition_count: int
    attrition_rate: float


class TopEarner(BaseModel):
    """Top earner dalam satu department."""
    EmployeeNumber: int
    Department: str
    JobRole: str
    MonthlyIncome: int
    Attrition: str
    income_rank: int


# ------------------------------------------------------------------
# Mini Project 2 — Response models
# ------------------------------------------------------------------
class ArticleSearchResponse(BaseModel):
    """Task 1: hasil search + metadata pagination."""
    data: List[Article]
    page: int
    per_page: int
    total_items: int
    total_pages: int


class DepartmentTopEarner(BaseModel):
    EmployeeNumber: int
    JobRole: str
    MonthlyIncome: int


class DepartmentDetail(BaseModel):
    """Task 3: statistik lengkap satu department."""
    department: str
    total_employees: int
    attrition_count: int
    attrition_rate: float
    avg_income: float
    min_income: int
    max_income: int
    top_earners: List[DepartmentTopEarner]


class RiskEmployee(BaseModel):
    EmployeeNumber: int
    Department: str
    JobRole: str
    MonthlyIncome: int
    dept_avg_income: float
    YearsAtCompany: int
    OverTime: str
    Attrition: str


class RiskProfileResponse(BaseModel):
    """Task 4: karyawan dengan indikator risiko attrition tinggi."""
    criteria: Dict[str, str]
    total_high_risk: int
    returned: int
    data: List[RiskEmployee]


# ==================================================================
# Authentication Helpers
#
# API ini support 2 metode autentikasi:
#   1. API Key — kirim header X-API-Key
#   2. JWT Bearer — POST /token dulu, lalu kirim header Authorization
#
# Keduanya bisa dipakai di endpoint yang sama.
# ==================================================================

def create_access_token(client_id: str) -> str:
    """Buat JWT token dengan expiry."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": client_id,
        "iat": now,
        "exp": now + timedelta(minutes=settings.jwt_expiry_minutes),
        "jti": secrets.token_hex(16),
    }
    return pyjwt.encode(payload, settings.jwt_secret, algorithm="HS256")


def verify_jwt_token(token: str) -> dict:
    """Decode dan validasi JWT token. Raise HTTPException jika invalid."""
    try:
        return pyjwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except pyjwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token sudah expired")
    except pyjwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token tidak valid")


def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Cek API key dari header X-API-Key."""
    if x_api_key is None:
        return None
    if hmac.compare_digest(x_api_key, settings.internal_api_key):
        return {"auth_method": "api_key"}
    raise HTTPException(status_code=401, detail="API Key tidak valid")


def get_current_client(
    api_key_result=Depends(verify_api_key),
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
):
    """
    Dependency utama — terima API Key ATAU Bearer token.
    FastAPI akan inject hasil verify_api_key dan credentials otomatis.
    """
    if api_key_result is not None:
        return api_key_result
    if credentials is not None:
        payload = verify_jwt_token(credentials.credentials)
        return {"auth_method": "bearer", "client_id": payload["sub"]}
    raise HTTPException(status_code=401, detail="Authentication Required. Gunakan API Key atau JWT")

# ==================================================================
# PUBLIC ENDPOINTS — tanpa auth
# ==================================================================
@app.get("/", tags=["Public"])
def read_root():
    return {
        "message": "News & HR Analytics API — Mini Project 2",
        "student": settings.student_name,
        "paths": {
            "etl_articles": "/articles",
            "elt_attrition": "/attrition",
            "docs": "/docs",
        },
    }

@app.get("/health", tags=["Public"])
def health_check():
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}

# ==================================================================
# AUTH ENDPOINT
# ==================================================================
@app.post("/token", response_model=TokenResponse, tags=["Auth"])
def login_for_token(req: TokenRequest):
    """Exchange client_id + client_secret untuk JWT access token."""
    if not hmac.compare_digest(req.client_id, settings.client_id) or not hmac.compare_digest(req.client_secret, settings.client_secret):
        raise HTTPException(status_code=401, detail="Invalid client credentials")
    token = create_access_token(req.client_id)
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        expires_in=settings.jwt_expiry_minutes * 60,
    )

# ==================================================================
# ETL PATH: Article Endpoints
# ==================================================================
@app.get("/articles", response_model=List[Article], tags=["Articles (ETL)"])
def list_articles(
    source: Optional[str] = Query(None, description="Filter by source (e.g. bbc, nytimes)"),
    title: Optional[str] = Query(None, description="Search title (case-insensitive)"),
    limit: int = Query(20, le=100, ge=1, description="Max results (1-100)"),
    auth=Depends(get_current_client),
):
    """List articles dengan optional filter source dan title."""
    return get_articles(source=source, title=title, limit=limit)


# Mini Project 2 — Task 2: Article Stats per Source
@app.get("/articles/stats", response_model=ArticleStats, tags=["Articles (ETL)"])
def article_stats(auth=Depends(get_current_client)):
    """Get article stats: total count and count by source."""
    return ArticleStats(
        total_articles=count_articles(),
        by_source=count_articles_by_source(),
    )


# Mini Project 2 — Task 1: Article Search dengan Pagination
# PENTING: harus didefinisikan SEBELUM /articles/{article_id},
# kalau tidak "search" akan dianggap sebagai article_id → 422.
@app.get("/articles/search", response_model=ArticleSearchResponse, tags=["Articles (ETL)"])
def article_search(
    source: Optional[str] = Query(None, description="Filter by source (e.g. bbc, nytimes)"),
    title: Optional[str] = Query(None, description="Case-insensitive partial match pada judul"),
    date_from: Optional[date] = Query(None, description="YYYY-MM-DD, published_at >= date_from"),
    date_to: Optional[date] = Query(None, description="YYYY-MM-DD, published_at <= date_to (inklusif sehari penuh)"),
    page: int = Query(1, ge=1, description="Nomor halaman (mulai dari 1)"),
    per_page: int = Query(10, ge=1, le=50, description="Artikel per halaman (max 50)"),
    auth=Depends(get_current_client),
):
    """Search artikel dengan filter source/title/tanggal + pagination OFFSET/LIMIT."""
    if date_from and date_to and date_from > date_to:
        raise HTTPException(status_code=400, detail="date_from tidak boleh setelah date_to")
    return search_articles(
        source=source,
        title=title,
        date_from=date_from,
        date_to=date_to,
        page=page,
        per_page=per_page,
    )


@app.get("/articles/{article_id}", response_model=Article, tags=["Articles (ETL)"])
def get_single_article(
    article_id: int,
    auth=Depends(get_current_client),
):
    """Get single article by database ID."""
    article = get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


# ==================================================================
# ELT PATH: Attrition Endpoints
#
# Data attrition di-load MENTAH dari CSV oleh pipeline.py.
# Transform terjadi SAAT query — inilah "T" di ELT.
# ==================================================================
@app.get("/attrition/summary", response_model=AttritionSummary, tags=["Attrition (ELT)"])
def attrition_summary(auth=Depends(get_current_client)):
    """Overall attrition stats."""
    return get_attrition_summary()

@app.get("/attrition/by-department", response_model=List[DepartmentAttrition], tags=["Attrition (ELT)"])
def attrition_by_department(auth=Depends(get_current_client)):
    """Attrition by department."""
    return get_attrition_by_department()

@app.get(
    "/attrition/by-overtime",
    response_model=List[OvertimeAttrition],
    tags=["Attrition (ELT)"],
)
def attrition_by_overtime(auth=Depends(get_current_client)):
    """Attrition by overtime status (SQL cross-tab)."""
    return get_attrition_by_overtime()

@app.get(
    "/attrition/by-tenure",
    response_model=List[TenureAttrition],
    tags=["Attrition (ELT)"],
)
def attrition_by_tenure(auth=Depends(get_current_client)):
    """Attrition by tenure bucket (SQL CASE WHEN)."""
    return get_attrition_by_tenure()

@app.get(
    "/attrition/top-earners",
    response_model=List[TopEarner],
    tags=["Attrition (ELT)"],
)
def top_earners(
    limit_per_dept: int = Query(5, le=20, ge=1, description="Top N per department"),
    auth=Depends(get_current_client),
):
    """Top earners per department (SQL RANK window function)."""
    return get_top_earners_by_department(limit_per_dept=limit_per_dept)


# Mini Project 2 — Task 3: Department Detail
@app.get(
    "/attrition/department/{dept_name}",
    response_model=DepartmentDetail,
    tags=["Attrition (ELT)"],
)
def attrition_department_detail(
    dept_name: str,
    auth=Depends(get_current_client),
):
    """
    Statistik lengkap satu department + 3 top earners (RANK window function).
    Nama department case-insensitive. Untuk "Research & Development",
    encode '&' jadi %26 di URL.
    """
    detail = get_department_detail(dept_name)
    if detail is None:
        raise HTTPException(status_code=404, detail=f"Department '{dept_name}' tidak ditemukan")
    return detail


# Mini Project 2 — Task 4: Attrition Risk Profile
@app.get(
    "/attrition/risk-profile",
    response_model=RiskProfileResponse,
    tags=["Attrition (ELT)"],
)
def attrition_risk_profile(
    limit: int = Query(20, ge=1, le=100, description="Max karyawan yang dikembalikan (1-100)"),
    auth=Depends(get_current_client),
):
    """Karyawan high-risk: OverTime=Yes, YearsAtCompany<3, income < rata-rata department (CTE)."""
    result = get_attrition_risk_profile(limit=limit)
    return {
        "criteria": {
            "OverTime": "Yes",
            "YearsAtCompany": "< 3",
            "MonthlyIncome": "< rata-rata department",
        },
        **result,
    }
