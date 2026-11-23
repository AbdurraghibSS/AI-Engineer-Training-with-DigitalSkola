<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🔁 Sesi 11 — PROJECT 2 · End-to-End Data Pipeline

<img src="https://img.shields.io/badge/Sesi-11%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-20%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Data%20Pipeline-FF6F00?style=flat-square" alt="Data Pipeline"/> <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/> <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Jumat, 20 November 2026** · 19.15 – 21.15 WIB<br>
*Friday, November 20, 2026 · 7:15 – 9:15 PM (UTC+7)*

Proyek kedua: <i>pipeline</i> data utuh dari pengambilan, pembersihan, penyimpanan, sampai disajikan lewat API.<br>
*Second project: a complete data pipeline, from ingestion and cleaning to storage and serving through an API.*

🚀 **Halaman proyek · *Project page*:** [proyek/02-end-to-end-data-pipeline](../proyek/02-end-to-end-data-pipeline/)

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini menyambungkan [Sesi 09](../sesi-09-sql-scraping-data-cleaning-pipeline/) dan [Sesi 10](../sesi-10-api-fastapi-untuk-ai/): data yang sudah masuk PostgreSQL lewat *pipeline* ETL/ELT kini disajikan sebagai **News & HR Analytics API**, lengkap dengan autentikasi. Latihannya kembali berupa kode *starter* dengan `TODO` (melanjutkan penomoran Sesi 09), lalu ditutup dengan Mini Project 2.<br>
*This session joined [Session 09](../sesi-09-sql-scraping-data-cleaning-pipeline/) and [Session 10](../sesi-10-api-fastapi-untuk-ai/): the data that the ETL/ELT pipeline put into PostgreSQL is now served as a **News & HR Analytics API**, with authentication. The exercise was again starter code with `TODO`s (continuing Session 09's numbering), followed by Mini Project 2.*

```
                 ┌─ Path A (ETL): RSS / books / quotes → Pandas → tabel articles ─┐
Sumber · Sources ┤                                                               ├─▶ PostgreSQL ─▶ FastAPI ─▶ Postman / Swagger
                 └─ Path B (ELT): CSV IBM HR Attrition → tabel raw_attrition ─────┘        (SQL transform saat query · at query time)
```

### 🧱 1. Struktur Kode: `db.py` ↔ `main.py` · *Code Layout*

| Berkas · *File* | Tanggung jawab · *Responsibility* |
|---|---|
| `db.py` | Semua SQL: koneksi SQLAlchemy dan satu fungsi per pertanyaan (`get_articles`, `get_attrition_by_department`, …). Mengembalikan `dict`/`list[dict]`.<br>*All the SQL: the SQLAlchemy connection and one function per question. Returns `dict`/`list[dict]`.* |
| `main.py` | Lapisan HTTP: model Pydantic, autentikasi, dan *endpoint* yang hanya memanggil fungsi dari `db.py`.<br>*The HTTP layer: Pydantic models, auth, and endpoints that just call `db.py` functions.* |

Dengan pemisahan ini, *query* bisa dites tanpa menyalakan *server*, dan *endpoint* tetap pendek dan mudah dibaca.<br>
*With this split, queries can be tested without starting the server, and endpoints stay short and readable.*

### 🔎 2. Query Dinamis yang Tetap Aman · *Safe Dynamic Queries*

*Endpoint* `/articles` punya filter opsional (`source`, `title`, `limit`). Klausa `WHERE` disusun bertahap, tetapi **nilainya selalu lewat parameter**:<br>
*The `/articles` endpoint has optional filters. The `WHERE` clause is built step by step, but **values always go through bind parameters**:*

```python
query = f"SELECT * FROM {ARTICLES_TABLE} WHERE 1=1"   # 1=1 → setiap filter tinggal "AND ..."
params = {"limit": limit}
if source:
    query += " AND source = :source";  params["source"] = source
if title:
    query += " AND title ILIKE :title"; params["title"] = f"%{title}%"   # ILIKE = tidak peka huruf besar-kecil
query += " ORDER BY published_at DESC NULLS LAST LIMIT :limit"
rows = conn.execute(text(query), params).mappings().all()            # .mappings() → baris berperilaku seperti dict
```

⚠️ Nama tabel memang disisipkan dengan *f-string* karena tidak bisa jadi parameter, tetapi nilainya berasal dari konfigurasi *server*, **bukan** dari input pengguna. Nilai dari pengguna tidak pernah digabung langsung ke string SQL.<br>
*The table name is inserted with an f-string because it can't be a bind parameter, but it comes from server config, **not** user input. User values never get concatenated into the SQL string.*

### 📊 3. ELT: Transformasi Saat Query · *Transform at Query Time*

Tabel *attrition* tetap mentah seperti di Sesi 09. Setiap *endpoint* `/attrition/*` menjalankan transformasinya sendiri dengan SQL, memakai `COUNT(*) FILTER (WHERE ...)`, `CASE WHEN` untuk *bucket* masa kerja, dan `RANK() OVER (PARTITION BY "Department" ...)` di dalam *subquery* untuk mengambil N gaji tertinggi per departemen.<br>
*The attrition table stays raw, as in Session 09. Each `/attrition/*` endpoint runs its own SQL transform, using `COUNT(*) FILTER (WHERE ...)`, `CASE WHEN` tenure buckets, and `RANK() OVER (PARTITION BY "Department" ...)` inside a subquery to pick the top N earners per department.*

💡 Fungsi *window* tidak bisa difilter langsung di `WHERE` *query* yang sama, karena `WHERE` dijalankan sebelum `RANK()` dihitung. Karena itu *ranking*-nya dibungkus *subquery* (atau CTE) dulu, baru difilter `WHERE income_rank <= :n`.<br>
*A window function can't be filtered in the same query's `WHERE`, because `WHERE` runs before `RANK()` is computed. So the ranking is wrapped in a subquery (or CTE) first, then filtered with `WHERE income_rank <= :n`.*

### 🧾 4. `response_model`: Kontrak Keluaran · *The Output Contract*

Setiap *endpoint* punya model Pydantic untuk *response*-nya (`Article`, `ArticleStats`, `AttritionSummary`, `TopEarner`, …). FastAPI memfilter dan memvalidasi keluaran sesuai model itu, dan Swagger menampilkan bentuk JSON-nya.<br>
*Every endpoint has a Pydantic response model. FastAPI filters and validates the output against it, and Swagger shows the JSON shape.*

⚠️ Pelajaran dari *debugging*: **alias kolom di SQL harus sama persis dengan nama *field* di model**. Kalau *query* menulis `AS rank` padahal modelnya `income_rank`, atau lupa memilih kolom `JobRole`, *endpoint* gagal dengan `500` (*ResponseValidationError*). Kesalahan kecil di SQL (misalnya koma berlebih sebelum `FROM`) juga langsung muncul sebagai `500`. Karena itu setiap *endpoint* dicoba satu per satu, jangan hanya satu-dua.<br>
*A debugging lesson: **SQL column aliases must match the model's field names exactly**. If the query says `AS rank` but the model expects `income_rank`, or forgets to select `JobRole`, the endpoint fails with `500` (ResponseValidationError). A small SQL slip (e.g. a stray comma before `FROM`) also surfaces as `500`. So test every endpoint, not just one or two.*

### 🔐 5. Dua Metode Autentikasi: API Key & JWT · *Two Auth Methods*

| | API *Key* | JWT *Bearer* |
|---|---|---|
| **Cara kirim · *How it's sent*** | *Header* `X-API-Key: <key>` | `POST /token` (`client_id` + `client_secret`) → *header* `Authorization: Bearer <token>` |
| **Masa berlaku · *Lifetime*** | Tetap sampai diganti · *Until rotated* | Kedaluwarsa otomatis (`exp`, misalnya 30 menit) · *Expires automatically* |
| **Cocok untuk · *Suits*** | Antar-layanan internal · *Internal service-to-service* | Klien yang "login" dulu · *Clients that log in first* |

```python
def get_current_client(api_key=Depends(verify_api_key),
                       credentials=Depends(HTTPBearer(auto_error=False))):
    if api_key is not None:                                   # 1. API key valid
        return api_key
    if credentials is not None:                               # 2. JWT valid?
        payload = verify_jwt_token(credentials.credentials)
        return {"auth_method": "bearer", "client_id": payload["sub"]}
    raise HTTPException(401, "Authentication required")      # 3. tidak ada keduanya · neither
```

- **Isi JWT · *JWT claims*:** `sub` (pemilik *token*), `iat` (waktu terbit), `exp` (kedaluwarsa), `jti` (ID unik). Ditandatangani dengan HS256 dan `JWT_SECRET` dari `.env`. *Token* yang kedaluwarsa atau diubah → `401`.<br>
  *`sub` (owner), `iat` (issued at), `exp` (expiry), `jti` (unique ID). Signed with HS256 and `JWT_SECRET` from `.env`. An expired or tampered token → `401`.*
- **`hmac.compare_digest`** dipakai untuk membandingkan *key*/*secret*, bukan `==`. Waktu perbandingannya konstan sehingga penyerang tidak bisa menebak *key* huruf demi huruf dari lama respons (*timing attack*).<br>
  ***`hmac.compare_digest`** compares keys/secrets instead of `==`. It runs in constant time, so an attacker can't guess the key character by character from response times (a timing attack).*
- **`Depends` bisa bertingkat**: `get_current_client` memakai dua *dependency* lain, lalu dipasang di setiap *endpoint* data dengan `auth=Depends(get_current_client)`. `/` dan `/health` dibiarkan publik.<br>
  ***`Depends` can be nested**: `get_current_client` uses two other dependencies and is attached to every data endpoint. `/` and `/health` stay public.*
- Kode status yang tepat: tanpa/salah kredensial → `401`, ID artikel tidak ada → `404`, parameter di luar batas (`limit` > 100) → `422`.<br>
  *The right status codes: missing/wrong credentials → `401`, unknown article ID → `404`, out-of-range parameter → `422`.*

### 🧪 6. Testing dengan Postman Collection

Pengujian dilakukan lewat *collection* Postman yang dikelompokkan per folder (*Public*, *Auth*, *Articles*, *Attrition*, *JWT Flow*) dan memakai variabel `{{base_url}}`, sehingga alamat *server* cukup diganti di satu tempat. *Collection* ini juga berisi uji negatif: tanpa *auth* (harus `401`), API *key* salah (harus `401`), dan artikel yang tidak ada (harus `404`).<br>
*Testing used a Postman collection grouped into folders (Public, Auth, Articles, Attrition, JWT Flow) with a `{{base_url}}` variable, so the server address changes in one place. It also includes negative tests: no auth (must be `401`), wrong API key (must be `401`), and a missing article (must be `404`).*

🎯 **Kapan dipakai · *When to use*:** pola *pipeline* → *database* → API terautentikasi ini adalah fondasi hampir semua produk AI: sistem RAG mengambil dokumen dari *database* yang sama, dan *chatbot* memanggil API yang sama. Mulai [Sesi 12](../sesi-12-nlp-llm-azure-openai/), LLM akan ditambahkan di atas fondasi ini.<br>
*This pipeline → database → authenticated API pattern underlies almost every AI product: a RAG system pulls documents from the same database, and a chatbot calls the same API. From [Session 12](../sesi-12-nlp-llm-azure-openai/), an LLM gets added on top of this foundation.*

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Latihan kelas: melengkapi `TODO` di `db.py` (*query* artikel & *attrition*) dan `main.py` (model Pydantic, API *key*, JWT, *endpoint*)<br>*Class exercise: completing the `TODO`s in `db.py` (article & attrition queries) and `main.py` (Pydantic models, API key, JWT, endpoints)* | Versi lengkap & sudah diperbaiki ada di halaman proyek<br>*The complete, fixed version is on the project page*<br><sub>kode *starter*, *collection* Postman & *dataset* dari tutor tidak diunggah · *tutor starter code, Postman collection & dataset not uploaded*</sub> | ✅ |
| 2 | **Mini Project 2**: empat *endpoint* analitik baru, yaitu `GET /articles/search` (filter + *pagination*), `GET /articles/stats`, `GET /attrition/department/{dept_name}`, dan `GET /attrition/risk-profile` (CTE + `JOIN`)<br>***Mini Project 2**: four new analytics endpoints: search with pagination, stats, department detail, and a risk profile (CTE + `JOIN`)* | [proyek/02-end-to-end-data-pipeline](../proyek/02-end-to-end-data-pipeline/) | ✅ |

## 💡 Catatan & Referensi · *Notes & References*

- [FastAPI: Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI: Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [FastAPI: OAuth2 with Password, Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [PyJWT: Usage Examples](https://pyjwt.readthedocs.io/en/stable/usage.html)
- [Python Docs: `hmac.compare_digest`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest)
- [JWT.io: Introduction to JSON Web Tokens](https://jwt.io/introduction)
- [Postman: Variables](https://learning.postman.com/docs/sending-requests/variables/variables/)

</div>

---

<div align="center">

<a href="../sesi-10-api-fastapi-untuk-ai/">← Sesi 10</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-12-nlp-llm-azure-openai/">Sesi 12 →</a>

</div>
