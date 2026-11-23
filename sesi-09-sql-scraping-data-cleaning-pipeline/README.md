<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🧹 Sesi 09 — SQL Scraping & Data Cleaning Pipeline

<img src="https://img.shields.io/badge/Sesi-09%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-16%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="SQL"/> <img src="https://img.shields.io/badge/Web%20Scraping-6E40C9?style=flat-square" alt="Web Scraping"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Senin, 16 November 2026** · 19.15 – 21.15 WIB<br>
*Monday, November 16, 2026 · 7:15 – 9:15 PM (UTC+7)*

Mengambil data dari web/sumber eksternal lalu membangun <i>pipeline</i> pembersihan data yang bisa diulang.<br>
*Collecting data from the web or external sources, then building a repeatable data-cleaning pipeline.*

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini menyatukan tiga materi sebelumnya (Python, Pandas, SQL) menjadi satu *pipeline* yang mengisi PostgreSQL di *cloud*. Ada dua jalur: **Path A (ETL)** mengambil data dari web, membersihkannya di Pandas, baru menyimpannya; **Path B (ELT)** memuat CSV apa adanya, lalu transformasinya dikerjakan dengan SQL di dalam *database*. Latihannya berupa kode *starter* dari tutor dengan bagian `TODO` yang kami lengkapi.<br>
*This session joined three earlier topics (Python, Pandas, SQL) into one pipeline that fills a cloud PostgreSQL database. There were two paths: **Path A (ETL)** pulls data from the web, cleans it in Pandas, then stores it; **Path B (ELT)** loads a CSV as-is and does the transformation with SQL inside the database. The exercise was tutor-provided starter code with `TODO` sections for us to complete.*

### 🔀 1. ETL vs ELT

Bedanya hanya pada **urutan**: kapan data dibersihkan, sebelum atau sesudah masuk *database*.<br>
*The only difference is **order**: whether data is cleaned before or after it lands in the database.*

```
Path A — ETL:  Extract (scrape web) → Transform (Pandas) → Load (data bersih · clean data)
Path B — ELT:  Extract (baca CSV · read CSV) → Load (data mentah · raw data) → Transform (SQL)
```

| | ETL | ELT |
|---|---|---|
| **Transformasi di · *Transform in*** | Python/Pandas, sebelum *load*<br>*Python/Pandas, before load* | SQL, sesudah *load*<br>*SQL, after load* |
| **Yang tersimpan · *What gets stored*** | Hanya data yang sudah bersih<br>*Only clean data* | Data mentah, bisa ditransformasi ulang kapan saja<br>*Raw data, re-transformable any time* |
| **Cocok untuk · *Good for*** | Sumber berantakan (HTML, RSS) yang harus dirapikan dulu<br>*Messy sources (HTML, RSS) that need tidying first* | Data sudah terstruktur (CSV, tabel) dan *database*-nya kuat<br>*Already-structured data (CSV, tables) and a capable database* |

💡 *Analogi:* ETL seperti mencuci sayur di rumah sebelum masuk kulkas; ELT seperti memasukkan belanjaan langsung ke kulkas, lalu mengolahnya sesuai resep saat akan dimasak.<br>
*Analogy: ETL is washing the vegetables at home before they go in the fridge; ELT is putting the shopping straight in the fridge and preparing it per recipe when you cook.*

### 🕷️ 2. Web Scraping dengan Requests + BeautifulSoup

Tiga sumber dipakai: *feed* RSS berita (NYT, BBC, CNN, Al Jazeera, Sky News, TechCrunch), `books.toscrape.com`, dan `quotes.toscrape.com`. Dua situs terakhir memang dibuat untuk latihan *scraping*.<br>
*Three sources were used: news RSS feeds (NYT, BBC, CNN, Al Jazeera, Sky News, TechCrunch), `books.toscrape.com`, and `quotes.toscrape.com`. The last two exist specifically for scraping practice.*

```python
resp = requests.get(url, headers={"User-Agent": "..."}, timeout=15)
resp.raise_for_status()                          # 4xx/5xx → exception
soup = BeautifulSoup(resp.text, "html.parser")   # RSS: BeautifulSoup(xml, "xml")

for pod in soup.select("article.product_pod"):   # CSS selector
    title = pod.select_one("h3 a")["title"]      # ambil atribut · read an attribute
    price = pod.select_one("p.price_color").get_text(strip=True)
```

| Teknik · *Technique* | Catatan · *Note* |
|---|---|
| **Inspect element dulu** | Struktur HTML dicari lewat DevTools browser, baru diterjemahkan jadi *selector* (`article.product_pod`, `span.text`, `div.tags a.tag`).<br>*Find the HTML structure in browser DevTools first, then turn it into selectors.* |
| `select` vs `select_one` | `select` → semua yang cocok (*list*); `select_one` → yang pertama atau `None`.<br>*`select` → every match (a list); `select_one` → the first or `None`.* |
| **RSS = XML** | Tiap artikel ada di `<item>` (`title`, `link`, `description`, `pubDate`). `description` sering berisi HTML, jadi di-*parse* sekali lagi untuk mengambil teksnya.<br>*Each article is an `<item>`. `description` often contains HTML, so it's parsed again to get plain text.* |
| `urljoin` | Mengubah *link* relatif (`catalogue/...`) jadi URL lengkap.<br>*Turns relative links into full URLs.* |
| **Pagination** | Loop `page-1`, `page-2`, … dan berhenti saat halaman kosong atau HTTP *error*.<br>*Loop through pages and stop on an empty page or an HTTP error.* |

🤝 ***Scraping* yang sopan · *Polite scraping*:** beri jeda antar-*request* (`time.sleep(1)`), pasang `User-Agent` yang jujur, selalu pakai `timeout`, dan cek `robots.txt` serta ketentuan situs. Satu sumber yang gagal di-*log* lalu dilewati, tidak menghentikan seluruh *pipeline*.<br>
*Pause between requests, send an honest `User-Agent`, always set a `timeout`, and check `robots.txt` and the site's terms. A failing source is logged and skipped rather than crashing the whole pipeline.*

### 🧽 3. Cleaning di Pandas (Transform pada ETL)

Semua sumber diseragamkan ke lima kolom yang sama (`title`, `url`, `source`, `content`, `published_at`) sebelum dibersihkan:<br>
*Every source is mapped to the same five columns before cleaning:*

| Langkah · *Step* | Kode · *Code* | Alasan · *Why* |
|---|---|---|
| Buang duplikat · *Drop duplicates* | `drop_duplicates(subset=["url"])` | URL adalah identitas unik artikel.<br>*The URL is the article's unique identity.* |
| Buang baris kosong · *Drop empties* | `dropna(subset=["title", "url"])` | Tanpa judul/URL, data tidak berguna.<br>*Without a title/URL the row is useless.* |
| Normalisasi teks · *Normalise text* | `.str.strip()`, `source` → `.str.lower()` | `"BBC "` dan `"bbc"` harus dianggap sama.<br>*`"BBC "` and `"bbc"` must count as the same.* |
| Tanggal · *Dates* | `pd.to_datetime(..., errors="coerce", utc=True)` lalu `.dt.tz_localize(None)` | Format tanggal tiap *feed* beda; yang gagal di-*parse* jadi `NaT`, bukan *crash*.<br>*Each feed formats dates differently; unparseable ones become `NaT` instead of crashing.* |
| Konten pendek · *Short content* | `df[df["content"].str.len() >= 20]` | Teks terlalu pendek tidak bernilai untuk analisis/RAG.<br>*Very short text has no value for analysis/RAG.* |

Setiap langkah mencatat berapa baris yang terbuang lewat `logging`, sehingga mudah dilacak kalau hasil akhirnya tiba-tiba sedikit.<br>
*Every step logs how many rows it dropped, which makes it easy to trace when the final count is suddenly low.*

### 🐘 4. Load ke PostgreSQL dengan SQLAlchemy

```python
class DBSettings(BaseSettings):          # pydantic-settings membaca .env
    database_url: str
    student_name: str

engine = create_engine(settings.database_url)
```

- **Kredensial di `.env`**, bukan di kode. `.env` masuk `.gitignore`; yang di-*commit* cukup `.env.example`.<br>
  ***Credentials live in `.env`**, not in code. `.env` is gitignored; only `.env.example` gets committed.*
- **`CREATE TABLE IF NOT EXISTS`** + *index* pada kolom yang sering difilter (`source`, `published_at DESC`) supaya *script* aman dijalankan berulang.<br>
  ***`CREATE TABLE IF NOT EXISTS`** plus indexes on frequently filtered columns, so the script is safe to re-run.*
- **`INSERT ... ON CONFLICT (url) DO NOTHING`**: URL diberi *constraint* `UNIQUE`, jadi menjalankan *pipeline* dua kali tidak menggandakan data (*idempotent*). `result.rowcount` memberi tahu berapa baris yang benar-benar baru.<br>
  ***`INSERT ... ON CONFLICT (url) DO NOTHING`**: the URL has a `UNIQUE` constraint, so running the pipeline twice doesn't duplicate data (idempotent). `result.rowcount` tells you how many rows were actually new.*
- **Parameter `:nama`** di `text()`, bukan *f-string*, untuk nilai data. Ini mencegah SQL *injection*.<br>
  ***`:name` bind parameters** in `text()`, not f-strings, for data values. This prevents SQL injection.*
- `engine.begin()` membuka transaksi yang otomatis *commit* (atau *rollback* kalau gagal); `engine.connect()` cukup untuk membaca.<br>
  *`engine.begin()` opens a transaction that auto-commits (or rolls back on failure); `engine.connect()` is enough for reads.*

### 🗃️ 5. ELT: Load Mentah, Transform dengan SQL

*Path* B memakai *dataset* IBM HR Attrition (1.470 karyawan). CSV-nya dimuat **tanpa dibersihkan sama sekali**:<br>
*Path B used the IBM HR Attrition dataset (1,470 employees). The CSV is loaded **without any cleaning**:*

```python
df = pd.read_csv(csv_path)
df.to_sql(table_name, engine, schema=SCHEMA, if_exists="replace", index=False)
```

⚠️ `to_sql` meminta nama tabel dan *schema* **terpisah**. Menulis `"schema.tabel"` sebagai nama tabel justru membuat tabel bernama persis begitu di *schema default*.<br>
*`to_sql` takes the table name and schema **separately**. Passing `"schema.table"` as the name creates a table literally called that in the default schema.*

Setelah data ada di *database*, pertanyaan bisnis dijawab dengan SQL:<br>
*Once the data is in the database, business questions are answered in SQL:*

| Pertanyaan · *Question* | Teknik SQL · *SQL technique* |
|---|---|
| Rata-rata gaji per departemen · *Average income per department* | `AVG(...)::numeric` + `ROUND` + `GROUP BY` |
| Persentase karyawan keluar · *Attrition rate* | `COUNT(*) FILTER (WHERE "Attrition" = 'Yes') / COUNT(*)` |
| Masa kerja vs *attrition* · *Tenure vs attrition* | `CASE WHEN` untuk membuat *bucket* · *to build buckets* |
| Lembur vs *attrition* · *Overtime vs attrition* | `GROUP BY` dua kolom (*cross-tab*) · *two columns* |
| Gaji tertinggi per departemen · *Top earners per department* | `RANK() OVER (PARTITION BY ... ORDER BY ... DESC)` |

💡 Nama kolom dari CSV memakai huruf kapital (`"MonthlyIncome"`), jadi di PostgreSQL **wajib** diberi tanda kutip ganda. Tanpa kutip, Postgres mengubahnya jadi huruf kecil dan kolomnya "tidak ditemukan".<br>
*CSV column names are capitalised (`"MonthlyIncome"`), so in PostgreSQL they **must** be double-quoted. Unquoted, Postgres lowercases them and reports the column as missing.*

🎯 **Kapan dipakai · *When to use*:** ETL ketika sumbernya berantakan dan hanya data bersih yang boleh masuk; ELT ketika data sudah terstruktur dan kita ingin menyimpan versi mentahnya agar bisa ditransformasi ulang. Data hasil kedua jalur ini disajikan lewat API di [Sesi 10](../sesi-10-api-fastapi-untuk-ai/)–[11](../sesi-11-project-2-end-to-end-data-pipeline/).<br>
*ETL when the source is messy and only clean data should get in; ELT when the data is already structured and you want to keep the raw version so you can re-transform it. The output of both paths gets served through an API in [Sessions 10](../sesi-10-api-fastapi-untuk-ai/)–[11](../sesi-11-project-2-end-to-end-data-pipeline/).*

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Latihan kelas: melengkapi `TODO` di *pipeline* ETL (*scraper*, *cleaner*) dan ELT (*load* CSV mentah, transformasi SQL)<br>*Class exercise: completing the `TODO`s in the ETL pipeline (scraper, cleaner) and ELT pipeline (raw CSV load, SQL transforms)* | Versi lengkapnya dipakai di [Project 2](../proyek/02-end-to-end-data-pipeline/)<br><sub>kode *starter* & *dataset* dari tutor tidak diunggah · *tutor starter code & dataset not uploaded*</sub> | ✅ |

## 💡 Catatan & Referensi · *Notes & References*

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests: Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Books to Scrape](https://books.toscrape.com/) · [Quotes to Scrape](https://quotes.toscrape.com/) (situs latihan · *practice sites*)
- [pandas: `DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [SQLAlchemy: Working with Transactions and the DBAPI](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html)
- [PostgreSQL Docs: `INSERT ... ON CONFLICT`](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT)
- [PostgreSQL Docs: Aggregate `FILTER` clause](https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-AGGREGATES)
- [PostgreSQL Docs: Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html)

</div>

---

<div align="center">

<a href="../sesi-08-sql-for-ai/">← Sesi 08</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-10-api-fastapi-untuk-ai/">Sesi 10 →</a>

</div>
