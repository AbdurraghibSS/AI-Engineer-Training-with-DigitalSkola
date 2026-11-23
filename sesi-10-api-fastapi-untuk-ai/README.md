<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# ⚡ Sesi 10 — API & FastAPI untuk AI

<img src="https://img.shields.io/badge/Sesi-10%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-18%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic"/> <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" alt="Postman"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Rabu, 18 November 2026** · 19.15 – 21.15 WIB<br>
*Wednesday, November 18, 2026 · 7:15 – 9:15 PM (UTC+7)*

Konsep REST API dan membangun <i>endpoint</i> layanan AI dengan FastAPI.<br>
*REST API concepts and building AI service endpoints with FastAPI.*

## 🧠 Yang Dipelajari · *What I Learned*

Model AI yang hanya hidup di *notebook* tidak bisa dipakai orang lain. Supaya jadi produk, model perlu "dibungkus" menjadi layanan yang bisa dipanggil lewat jaringan, dan itulah peran API. Sesi ini membahas konsep REST, membangun *endpoint* dengan FastAPI, mengamankan konfigurasi dengan `.env`, dan menghasilkan dokumentasi API otomatis.<br>
*An AI model that only lives in a notebook can't be used by anyone else. To become a product it has to be wrapped as a service callable over the network, which is what an API does. This session covered REST concepts, building endpoints with FastAPI, keeping configuration safe with `.env`, and generating API docs automatically.*

```
Frontend (web/mobile) ──HTTP request──▶ API (FastAPI) ──▶ Model (LLM / ML)
                      ◀──JSON response──               ◀──
```

### 🌐 1. REST API

REST adalah gaya arsitektur API di atas HTTP. API berfungsi sebagai **kontrak**: klien mengirim *request* dengan bentuk tertentu, *server* membalas dengan *response* yang bentuknya juga sudah disepakati.<br>
*REST is an architectural style for APIs over HTTP. An API is a **contract**: the client sends a request of an agreed shape and the server replies with a response of an agreed shape.*

- **Berbasis *resource*** · *Resource-based*: URL menunjuk "benda", bukan aksi, misalnya `/users`, `/users/42`, `/users/42/orders`.<br>*URLs name things, not actions.*
- ***Stateless***: *server* tidak mengingat *request* sebelumnya, jadi setiap *request* harus membawa semua info yang dibutuhkan (termasuk *token*/API *key*).<br>*The server remembers nothing between requests, so each request carries everything it needs (tokens/API keys included).*
- Format datanya umumnya **JSON**.<br>*Data is usually **JSON**.*

| Method | Fungsi · *Purpose* | Idempotent? |
|---|---|:-:|
| `GET` | Membaca data, tidak mengubah apa pun · *Read, changes nothing* | ✅ |
| `POST` | Membuat *resource* baru · *Create a new resource* | ❌ dua kali = dua data · *twice = two records* |
| `PUT` | Mengganti seluruh *resource* · *Replace the whole resource* | ✅ |
| `PATCH` | Mengubah sebagian · *Change part of it* | — |
| `DELETE` | Menghapus · *Delete* | ✅ |

| Kode · *Code* | Arti · *Meaning* |
|---|---|
| **2xx** | Berhasil · *Success*: `200 OK`, `201 Created`, `204 No Content` |
| **4xx** | Salah di klien · *Client error*: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`, `429 Too Many Requests` |
| **5xx** | Salah di *server* · *Server error*: `500 Internal Server Error`, `503 Service Unavailable` |

⚠️ Kesalahan klasik: membalas `200` padahal terjadi *error* (misalnya `{"status": 200, "error": "..."}`). Klien jadi tidak bisa mendeteksi kegagalan dari status HTTP-nya.<br>
*Classic mistake: replying `200` for an error. The client can no longer detect failure from the HTTP status.*

### ⚡ 2. FastAPI: Endpoint, Parameter, Validasi

FastAPI dipilih karena memakai *type hints* Python untuk validasi otomatis, membuat dokumentasi sendiri, mendukung `async` (berguna saat memanggil LLM yang lambat), dan sudah lazim di ekosistem AI.<br>
*FastAPI uses Python type hints for automatic validation, generates its own docs, supports `async` (handy when calling slow LLMs), and is common across the AI ecosystem.*

```bash
pip install fastapi uvicorn
uvicorn main:app --reload        # main.py, objek bernama app · object named app
```

| Jenis input · *Input type* | Contoh · *Example* | Cara FastAPI mengenalinya · *How FastAPI recognises it* |
|---|---|---|
| **Path parameter** | `GET /product/42` | Nama di `{}` pada *path*: `def get(product_id: int)`<br>*Name in `{}` in the path* |
| **Query parameter** | `GET /products?category=food&limit=2` | Argumen fungsi yang tidak ada di *path*, beri *default* `None` agar opsional<br>*A function argument not in the path; default `None` makes it optional* |
| **Request body** | `POST /users` + JSON | Argumen bertipe model Pydantic<br>*An argument typed as a Pydantic model* |

```python
class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(ge=0, le=120)          # ge/le = batas bawah/atas · lower/upper bound

@app.post("/users", status_code=201)
def create_user(user: UserCreate):          # di sini user PASTI valid · user is guaranteed valid here
    ...
```

Kalau tipe tidak cocok (`/product/abc`, `age: "dua puluh"`, `limit=abcsds`), FastAPI langsung membalas **`422`** beserta lokasi dan alasan *error*-nya, tanpa satu baris kode validasi pun dari kita.<br>
*If a type doesn't match, FastAPI replies **`422`** with the location and reason of the error, without us writing a single line of validation code.*

💡 Pydantic yang dikenalkan di sesi sebelumnya baru terasa manfaatnya di sini: model Pydantic sekaligus menjadi validator, dokumentasi *schema*, dan contoh *payload*.<br>
*Pydantic, introduced in earlier sessions, really pays off here: one model is the validator, the schema docs, and the example payload all at once.*

Untuk *endpoint* AI, polanya sama: *request* dan *response* sama-sama didefinisikan sebagai model, lalu `response_model=` memastikan keluaran API tidak menyimpang dari kontrak. Panggilan LLM sungguhan baru diisi mulai Sesi 12.<br>
*For an AI endpoint the pattern is the same: request and response are both models, and `response_model=` keeps the output on-contract. The real LLM call gets filled in from Session 12.*

### 🔐 3. `.env` & Keamanan API · *`.env` & API Security*

API *key* dan *password* **tidak boleh** ditulis di kode. Kode masuk ke Git, dan API *key* yang bocor ke *repo* publik bisa dipakai *bot* orang lain hingga tagihannya membengkak. Prinsipnya: **pisahkan kode dan konfigurasi**.<br>
*API keys and passwords must **never** be written in code. Code goes into Git, and a key leaked to a public repo can be abused by bots until the bill explodes. The principle: **separate code from config**.*

```python
class Settings(BaseSettings):                # pip install pydantic-settings
    openai_api_key: str
    internal_api_key: str
    app_env: str = "development"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()                        # gagal di awal kalau variabel wajib tidak ada · fails fast if a required var is missing
```

`.env` dimasukkan ke `.gitignore`; yang di-*commit* cukup `.env.example` berisi nama variabel tanpa nilai aslinya.<br>
*`.env` goes in `.gitignore`; only `.env.example`, with variable names but no real values, gets committed.*

*Minimum viable security* untuk API:<br>
*Minimum viable security for an API:*

1. **API *key*** lewat *header* (`X-API-Key`), dicek di sebuah *dependency* dan dipasang dengan `Depends(...)`. *Key* salah → `401`.<br>***API key** in a header, checked in a dependency attached with `Depends(...)`. Wrong key → `401`.*
2. ***Rate limiting*** (misalnya dengan `slowapi`) untuk membatasi *request* per pengguna/IP.<br>***Rate limiting** (e.g. with `slowapi`) to cap requests per user/IP.*
3. **HTTPS** di *production*, biasanya diterminasi di *reverse proxy* (nginx) atau layanan *cloud*.<br>***HTTPS** in production, usually terminated at a reverse proxy (nginx) or the cloud provider.*
4. ***Never trust client input***: validasi dengan Pydantic dan pakai *parameterized query* untuk SQL.<br>*Validate with Pydantic and use parameterised SQL queries.*

### 📖 4. Dokumentasi Otomatis & Testing · *Auto Docs & Testing*

Begitu *server* jalan, FastAPI langsung menyediakan dua halaman dokumentasi dari kode:<br>
*As soon as the server runs, FastAPI serves two documentation pages generated from the code:*

| URL | Isi · *What it is* |
|---|---|
| `/docs` | **Swagger UI**: interaktif, bisa mencoba *endpoint* langsung (*Try it out*)<br>*Interactive; you can call endpoints right there* |
| `/redoc` | **ReDoc**: lebih rapi untuk dibaca, tidak interaktif<br>*Cleaner to read, not interactive* |

Dokumentasi bisa dibuat terlihat seperti spesifikasi produk dengan menambahkan metadata: `title`/`description`/`version` di `FastAPI(...)`, `tags`/`summary`/`description` di tiap *decorator*, `Field(description=...)` per kolom, dan `json_schema_extra` untuk contoh *payload*.<br>
*The docs can look like a product spec by adding metadata: `title`/`description`/`version` on `FastAPI(...)`, `tags`/`summary`/`description` on each decorator, `Field(description=...)` per field, and `json_schema_extra` for example payloads.*

Untuk menguji API, ada tiga cara yang fungsinya sama: **Swagger UI** (`/docs`), **Postman** (GUI; *body* → *raw* → JSON, tambahkan *header* bila perlu), atau **curl** di terminal:<br>
*There are three equivalent ways to test an API: **Swagger UI**, **Postman**, or **curl** in the terminal:*

```bash
curl -v http://localhost:8000/health
curl -v -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Pelayanannya cepat dan ramah", "threshold": 0.7}'
```

💡 Uji juga kasus negatif (input salah, tanpa *key*), bukan hanya yang berhasil. Status `422`/`401` yang muncul di saat yang tepat adalah bukti validasi bekerja.<br>
*Test the negative cases too (bad input, missing key), not just the happy path. A `422`/`401` at the right moment proves validation works.*

🎯 **Kapan dipakai · *When to use*:** setiap kali model atau data perlu diakses aplikasi lain, misalnya *frontend chatbot*, aplikasi *mobile*, atau layanan lain. Di [Sesi 11](../sesi-11-project-2-end-to-end-data-pipeline/), FastAPI dipakai untuk menyajikan data hasil *pipeline* [Sesi 09](../sesi-09-sql-scraping-data-cleaning-pipeline/), lengkap dengan autentikasi.<br>
*Whenever a model or data needs to be reached by another app, e.g. a chatbot frontend, a mobile app, or another service. In [Session 11](../sesi-11-project-2-end-to-end-data-pipeline/), FastAPI serves the data from the [Session 09](../sesi-09-sql-scraping-data-cleaning-pipeline/) pipeline, with authentication.*

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Homework API & FastAPI: membangun **AI Prediction API** dengan `/health`, `/data`, `/predict`, dan dokumentasi Swagger yang lengkap<br>*Homework API & FastAPI: building an **AI Prediction API** with `/health`, `/data`, `/predict`, and complete Swagger docs* | [homework.py](homework.py) · [requirements.txt](requirements.txt)<br><sub>soal & *starter code* dari tutor tidak diunggah · *tutor brief & starter code not uploaded*</sub> | ✅ |

### 🏠 Homework: AI Prediction API

| Soal · *Task* | Implementasi · *Implementation* |
|:-:|---|
| 1 | `GET /health` → `{"status": "ok"}`; terdaftar di `/docs`.<br>*Returns `{"status": "ok"}` and shows up in `/docs`.* |
| 2 | `GET /data` dengan *query* opsional `category` (str) dan `limit` (int, `ge=1`) atas 7 item *dummy*. `?limit=abcsds` ditolak otomatis dengan `422`.<br>*Optional `category` and `limit` query params over 7 dummy items. `?limit=abcsds` is rejected automatically with `422`.* |
| 3 | `POST /predict` dengan `PredictRequest` (`text` 1–500 karakter, `threshold` 0.0–1.0) dan `response_model=PredictResponse` (`label`, `confidence`, `input_text`). Body `{"text": "", "threshold": 1.5}` → `422`.<br>*Validated body and response model. An invalid body returns `422`.* |
| 4 | Metadata Swagger: `version="1.0.0"`, *tag* `System`/`Data`/`Prediction`, *summary* & *description* berbahasa Indonesia, serta contoh *payload* lewat `json_schema_extra`.<br>*Swagger metadata: version, tags, Indonesian summaries & descriptions, and an example payload via `json_schema_extra`.* |

Supaya `/predict` tidak sekadar membalas nilai tetap, saya membuat prediksi sentimen *dummy* berbasis kata kunci: kata positif/negatif dihitung, `confidence = 0.5 + 0.5 × (porsi kata dominan)`, dan label diturunkan menjadi `netral` kalau `confidence` di bawah `threshold`. Ini belum model AI sungguhan, tetapi sudah memakai `threshold` sesuai fungsinya.<br>
*So that `/predict` doesn't just return a fixed value, I wrote a keyword-based dummy sentiment predictor: positive/negative words are counted, `confidence = 0.5 + 0.5 × (dominant share)`, and the label falls back to `netral` when `confidence` is below `threshold`. It isn't a real AI model yet, but `threshold` already does its job.*

```bash
cd sesi-10-api-fastapi-untuk-ai
pip install -r requirements.txt
uvicorn homework:app --reload            # buka · open http://localhost:8000/docs
```

| Uji · *Test* | Hasil · *Result* |
|---|:-:|
| `GET /health` | `200` `{"status":"ok"}` |
| `GET /data` | `200` (7 item) |
| `GET /data?category=electronics&limit=2` | `200` (2 item) |
| `GET /data?limit=abcsds` | `422` |
| `POST /predict` `{"text":"Pelayanan di kantor ini sangat cepat dan petugasnya ramah sekali","threshold":0.7}` | `200` `positif`, `1.0` |
| `POST /predict` `{"text":"","threshold":1.5}` | `422` |

## 💡 Catatan & Referensi · *Notes & References*

- [FastAPI Tutorial: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI: Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
- [FastAPI: Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI: Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
- [FastAPI: Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)
- [MDN: HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Postman Learning Center](https://learning.postman.com/docs/getting-started/overview/)

</div>

---

<div align="center">

<a href="../sesi-09-sql-scraping-data-cleaning-pipeline/">← Sesi 09</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-11-project-2-end-to-end-data-pipeline/">Sesi 11 →</a>

</div>
