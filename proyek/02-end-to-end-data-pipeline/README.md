<div align="center">

<sub><a href="../../">🏠 Beranda · <i>Home</i></a> &nbsp;·&nbsp; <a href="../">🗂️ Proyek · <i>Projects</i></a></sub>

# 🔁 Project 2 — End-to-End Data Pipeline

<img src="https://img.shields.io/badge/Project-2%20%2F%204-8A2BE2?style=for-the-badge" alt="Project"/> <img src="https://img.shields.io/badge/Sesi-11-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Data%20Pipeline-FF6F00?style=flat-square" alt="Data Pipeline"/> <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/> <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT"/>

</div>

---

<div align="justify">

## 📌 Ringkasan · *Overview*

**News & HR Analytics API**: dua <i>pipeline</i> data yang bermuara ke satu API. *Path* A (ETL) mengambil artikel dari RSS, books.toscrape, dan quotes.toscrape, membersihkannya di Pandas, lalu menyimpannya ke PostgreSQL. *Path* B (ELT) memuat CSV IBM HR Attrition apa adanya, lalu transformasinya dikerjakan dengan SQL saat *query*. Mini Project 2 menambahkan empat *endpoint* analitik di atas fondasi Sesi 9–11.<br>
***News & HR Analytics API**: two data pipelines feeding one API. Path A (ETL) scrapes articles from RSS, books.toscrape and quotes.toscrape, cleans them in Pandas, then stores them in PostgreSQL. Path B (ELT) loads the IBM HR Attrition CSV raw and transforms it with SQL at query time. Mini Project 2 adds four analytics endpoints on top of the Session 9–11 groundwork.*

📚 Materi sesi · *Session notes*: [Sesi 11](../../sesi-11-project-2-end-to-end-data-pipeline/)

## ✨ Fitur · *Features*

| Task | Endpoint | Teknik SQL · *SQL technique* |
|:-:|---|---|
| 1 | `GET /articles/search` | Filter dinamis + `LIMIT`/`OFFSET`, `COUNT(*)` terpisah untuk `total_items`<br>*Dynamic filters + `LIMIT`/`OFFSET`, a separate `COUNT(*)` for `total_items`* |
| 2 | `GET /articles/stats` | `GROUP BY source` |
| 3 | `GET /attrition/department/{dept_name}` | Agregat `COUNT FILTER`/`AVG`/`MIN`/`MAX` + `RANK() OVER (ORDER BY "MonthlyIncome" DESC)` |
| 4 | `GET /attrition/risk-profile` | CTE `dept_avg` + `JOIN` |

- **Search & pagination**: filter `source`, `title` (ILIKE, *case-insensitive*), `date_from`, `date_to` (format `YYYY-MM-DD`), `page`, `per_page` (maks 50). Respons memuat `data`, `page`, `per_page`, `total_items`, `total_pages`.<br>
  ***Search & pagination**: filters on `source`, `title` (case-insensitive ILIKE), `date_from`, `date_to` (`YYYY-MM-DD`), `page`, `per_page` (max 50). The response carries `data`, `page`, `per_page`, `total_items`, `total_pages`.*
- **Department detail**: total karyawan, jumlah & *rate* attrition, rata-rata/min/maks gaji, dan 3 *top earners*. Nama department tidak peka huruf besar-kecil; department yang tidak ada → `404`.<br>
  ***Department detail**: headcount, attrition count & rate, average/min/max income, and the top 3 earners. Department names are case-insensitive; an unknown department returns `404`.*
- **Risk profile**: karyawan dengan `OverTime = Yes`, `YearsAtCompany < 3`, dan gaji di bawah rata-rata department-nya, diurutkan dari gaji terendah. Parameter `limit` (default 20, maks 100).<br>
  ***Risk profile**: employees with `OverTime = Yes`, `YearsAtCompany < 3` and income below their department average, lowest income first. `limit` parameter (default 20, max 100).*
- **Dua metode auth**: header `X-API-Key` atau JWT *Bearer* dari `POST /token`. Semua *endpoint* data wajib terautentikasi.<br>
  ***Two auth methods**: an `X-API-Key` header or a JWT Bearer token from `POST /token`. Every data endpoint requires authentication.*
- **Validasi input**: tanggal tidak valid, `per_page > 50`, atau `limit > 100` → `422`; `date_from` setelah `date_to` → `400`.<br>
  ***Input validation**: an invalid date, `per_page > 50` or `limit > 100` returns `422`; `date_from` after `date_to` returns `400`.*

## 📦 Berkas · *Files*

| Berkas · *File* | Isi · *Contents* |
|---|---|
| [main.py](main.py) | Aplikasi FastAPI: model Pydantic, auth (API Key + JWT), semua *endpoint*.<br>*FastAPI app: Pydantic models, auth (API key + JWT), every endpoint.* |
| [db.py](db.py) | Koneksi SQLAlchemy dan semua *query* SQL, termasuk `search_articles`, `get_department_detail`, `get_attrition_risk_profile`.<br>*SQLAlchemy connection and every SQL query, including the three new functions.* |
| [pipeline.py](pipeline.py) · [scraper.py](scraper.py) · [cleaner.py](cleaner.py) | *Pipeline* ETL/ELT dari Sesi 9 untuk mengisi database.<br>*The Session 9 ETL/ELT pipeline that fills the database.* |
| [.env.example](.env.example) | Contoh variabel lingkungan (salin jadi `.env`).<br>*Sample environment variables (copy to `.env`).* |
| `employee_attrition.csv` | Dataset dari tutor (tidak diunggah).<br>*Tutor-provided dataset (not uploaded).* |

## 🧰 Tech Stack

Python 3 · FastAPI · Uvicorn · Pydantic · SQLAlchemy · PostgreSQL · PyJWT · Pandas · BeautifulSoup

## ▶️ Cara Menjalankan · *How to Run*

```bash
cd proyek/02-end-to-end-data-pipeline
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # isi kredensial · fill in credentials

# (sekali saja) isi database · (once) fill the database
python pipeline.py --attrition-csv employee_attrition.csv

uvicorn main:app --reload       # buka · open http://localhost:8000/docs
```

Contoh panggilan · *Sample calls*:

```bash
curl -H "X-API-Key: $INTERNAL_API_KEY" "localhost:8000/articles/search?source=bbc&date_from=2026-11-01"
curl -H "X-API-Key: $INTERNAL_API_KEY" "localhost:8000/attrition/department/Sales"
curl -H "X-API-Key: $INTERNAL_API_KEY" "localhost:8000/attrition/department/Research%20%26%20Development"
```

## 📊 Hasil & Demo · *Results & Demo*

`GET /attrition/department/Sales`

```json
{
  "department": "Sales",
  "total_employees": 446,
  "attrition_count": 92,
  "attrition_rate": 0.2063,
  "avg_income": 6959.17,
  "min_income": 1052,
  "max_income": 19847,
  "top_earners": [
    {"EmployeeNumber": 1282, "JobRole": "Manager", "MonthlyIncome": 19847},
    {"EmployeeNumber": 1038, "JobRole": "Manager", "MonthlyIncome": 19845},
    {"EmployeeNumber": 1740, "JobRole": "Manager", "MonthlyIncome": 19833}
  ]
}
```

| Uji · *Check* | Hasil · *Result* |
|---|---|
| `/articles/search` tanpa filter · *no filters* | 531 artikel · *articles*, 54 halaman · *pages* |
| `/articles/search?source=bbc&date_from=2026-11-01` | 38 artikel, 4 halaman |
| `/articles/stats` | 531 total, 8 *source* |
| `/attrition/risk-profile` | 82 karyawan *high-risk* · *high-risk employees* |
| `/attrition/department/Marketing` | `404` |
| Tanpa auth · *No auth* | `401` |

## 💡 Pelajaran · *Lessons Learned*

- Urutan *route* di FastAPI penting: `/articles/search` harus didaftarkan **sebelum** `/articles/{article_id}`, kalau tidak `"search"` dibaca sebagai `article_id` dan gagal validasi `int`.<br>
  *Route order matters in FastAPI: `/articles/search` must be registered **before** `/articles/{article_id}`, otherwise `"search"` is parsed as an `article_id` and fails `int` validation.*
- `published_at` bertipe `TIMESTAMP`, jadi `<= '2026-11-16'` hanya sampai pukul 00:00. Supaya `date_to` mencakup sehari penuh, pakai `< date_to + 1 hari`.<br>
  *`published_at` is a `TIMESTAMP`, so `<= '2026-11-16'` stops at midnight. To include the whole `date_to` day, use `< date_to + 1 day`.*
- Klausa `WHERE` dibangun sekali lalu dipakai bersama oleh *query* `COUNT` dan *query* data, sehingga `total_items` selalu konsisten dengan isi `data`.<br>
  *The `WHERE` clause is built once and shared by the `COUNT` query and the data query, so `total_items` always matches `data`.*
- Nilai filter selalu lewat *parameter binding* (`:source`, `:title`), bukan *f-string*, untuk mencegah SQL *injection*.<br>
  *Filter values always go through parameter binding (`:source`, `:title`), never f-strings, to prevent SQL injection.*
- Kode awal Sesi 11 punya dua *bug* yang ikut diperbaiki: *query* `by-department` kelebihan koma dan tidak menghitung `avg_income`, dan *query* `top-earners` tidak memilih kolom `JobRole`, `Attrition`, `income_rank` yang diminta model respons.<br>
  *The Session 11 starter code had two bugs, fixed here: the `by-department` query had a trailing comma and no `avg_income`, and the `top-earners` query didn't select the `JobRole`, `Attrition` and `income_rank` columns the response model expects.*

</div>

---

<div align="center">

<a href="../01-python-automation-tool/">← Project 1</a> &nbsp;·&nbsp; <a href="../">🗂️ Semua Proyek</a> &nbsp;·&nbsp; <a href="../03-ai-chatbot-rag-azure/">Project 3 →</a>

</div>
