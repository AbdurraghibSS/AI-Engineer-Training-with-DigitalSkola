<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🗄️ Sesi 08 — SQL for AI

<img src="https://img.shields.io/badge/Sesi-08%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-13%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/> <img src="https://img.shields.io/badge/SQL-336791?style=flat-square" alt="SQL"/> <img src="https://img.shields.io/badge/DBeaver-382923?style=flat-square&logo=dbeaver&logoColor=white" alt="DBeaver"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Jumat, 13 November 2026** · 19.15 – 21.15 WIB<br>
*Friday, November 13, 2026 · 7:15 – 9:15 PM (UTC+7)*

Query SQL untuk menyiapkan data AI: <i>SELECT</i>, <i>JOIN</i>, agregasi, <i>CTE</i>, dan optimasi query di PostgreSQL.<br>
*SQL queries for preparing AI data: SELECT, JOIN, aggregation, CTEs, and query optimization in PostgreSQL.*

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini membahas cara mengambil data dari *database* relasional, tempat sebagian besar data perusahaan disimpan. Urutannya: alasan SQL penting untuk AI, PostgreSQL dan *tools*-nya, *query* dasar, JOIN & agregasi, lalu CTE dan optimasi *query*. Latihannya dilakukan langsung di *database sandbox* e-commerce milik kelas (`customers`, `products`, `orders`, `order_details`).<br>
*This session covered how to pull data out of relational databases, where most company data lives. The order was: why SQL matters for AI, PostgreSQL and its tooling, basic queries, JOINs & aggregation, then CTEs and query optimization. We practised directly on the class's e-commerce sandbox database (`customers`, `products`, `orders`, `order_details`).*

### 🤖 1. Kenapa AI Engineer Butuh SQL? · *Why Does an AI Engineer Need SQL?*

Sebelum ada model, harus ada data, dan data itu biasanya tersimpan di *database* relasional. Ada tiga kegunaan utama SQL bagi AI Engineer:<br>
*Before there's a model there has to be data, and that data usually lives in a relational database. SQL has three main uses for an AI Engineer:*

| Kegunaan · *Use* | Contoh · *Example* |
|---|---|
| 🔎 **Retrieval untuk RAG** | Mengambil katalog produk atau data pelanggan dari SQL sebelum diubah menjadi *embedding* dan dimasukkan ke *vector database*.<br>*Pulling the product catalogue or customer records from SQL before turning them into embeddings for a vector database.* |
| 🧪 **Persiapan data · *Data prep*** | *Dataset* latih ML hampir selalu berawal dari *query* yang menggabungkan dan meringkas beberapa tabel.<br>*An ML training set almost always starts as a query that joins and summarises several tables.* |
| 💬 **Integrasi produk · *Product integration*** | *Chatbot* yang menjawab "berapa saldo saya?" harus menjalankan *query* ke *database* secara *real-time*.<br>*A chatbot answering "what's my balance?" has to query the database in real time.* |

### 🐘 2. PostgreSQL & Tools

**PostgreSQL** (Postgres) adalah *database* relasional *open source* yang banyak dipakai di industri, termasuk perusahaan AI. Alasan memilihnya: fiturnya lengkap (JSON, *array*, *full-text search*, dan ekstensi **pgvector** untuk menyimpan *embedding*), patuh pada standar SQL sehingga *query*-nya mudah dipindah ke *database* lain, serta didukung langsung oleh LangChain dan LlamaIndex.<br>
***PostgreSQL** (Postgres) is an open-source relational database used widely in industry, AI companies included. Why it: it's feature-rich (JSON, arrays, full-text search, and the **pgvector** extension for storing embeddings), it sticks to standard SQL so queries port easily, and LangChain and LlamaIndex support it natively.*

| Istilah · *Term* | Arti · *Meaning* |
|---|---|
| **Database** | Kumpulan tabel yang saling terhubung, misalnya *database* `ecommerce`.<br>*A set of related tables, e.g. an `ecommerce` database.* |
| **Table** | Struktur mirip *spreadsheet* yang terdiri dari kolom dan baris.<br>*A spreadsheet-like structure of columns and rows.* |
| **Row / Record** | Satu entri data, misalnya satu baris di `customers` adalah satu pelanggan.<br>*One entry, e.g. one row in `customers` is one customer.* |
| **Column / Field** | Atribut data, misalnya kolom `email`.<br>*An attribute, e.g. the `email` column.* |

Untuk mengakses *database* kami memakai **DBeaver** (Community Edition), aplikasi GUI yang bisa terhubung ke banyak jenis *database*: *New Database Connection* → PostgreSQL → isi *host*, *port*, *user*, *password*, dan nama *database*.<br>
*To access the database we used **DBeaver** (Community Edition), a GUI client that connects to many kinds of databases: New Database Connection → PostgreSQL → fill in host, port, user, password, and database name.*

⚠️ Kredensial *database* (*host*, *password*) **tidak pernah** ditulis di kode atau README yang di-*commit*. Simpan di `.env` atau *secret manager*, lalu baca lewat *environment variable*.<br>
*Database credentials (host, password) **never** go into committed code or a README. Keep them in `.env` or a secret manager and read them from environment variables.*

### 🔤 3. SQL Dasar: SELECT, WHERE, ORDER BY, LIMIT · *SQL Basics*

```sql
SELECT name, email                    -- kolom yang diambil
FROM customers                        -- dari tabel mana
WHERE city IN ('Jakarta', 'Bandung')  -- filter baris
  AND email LIKE '%@gmail.com'        -- pola teks: % = karakter apa saja
ORDER BY name ASC                     -- urutkan (ASC default, DESC terbalik)
LIMIT 5;                              -- batasi jumlah baris
```

| Klausa · *Clause* | Fungsi · *Purpose* |
|---|---|
| `SELECT` | Memilih kolom. `SELECT *` mengambil semua kolom.<br>*Picks columns. `SELECT *` takes them all.* |
| `WHERE` | Memfilter baris dengan `=`, `>`, `AND`, `OR`, `IN`, `LIKE`.<br>*Filters rows.* |
| `ORDER BY` | Mengurutkan hasil berdasarkan satu atau lebih kolom.<br>*Sorts by one or more columns.* |
| `LIMIT` | Membatasi jumlah baris. Wajib saat mengintip tabel berisi jutaan baris.<br>*Caps the row count. A must when peeking at tables with millions of rows.* |

*Keyword* SQL tidak membedakan huruf besar dan kecil, tetapi konvensinya ditulis KAPITAL agar mudah dibaca. Setiap *statement* diakhiri `;`.<br>
*SQL keywords are case-insensitive, but by convention they're written in CAPITALS for readability. Every statement ends with `;`.*

### 🔗 4. JOIN

Data di dunia nyata tersebar di beberapa tabel. Tabel `orders` hanya menyimpan `customer_id`, sedangkan nama pelanggannya ada di `customers`. **JOIN** menyatukan tabel-tabel ini berdasarkan kolom penghubung (biasanya *foreign key*).<br>
*Real data is spread over several tables. `orders` only stores `customer_id`, while the customer's name is in `customers`. A **JOIN** brings them together on a linking column (usually a foreign key).*

```sql
SELECT c.name, o.order_id, o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```

| Jenis · *Type* | Hasil · *Result* |
|---|---|
| `INNER JOIN` | Hanya baris yang **punya pasangan** di kedua tabel.<br>*Only rows that **have a match** in both tables.* |
| `LEFT JOIN` | **Semua** baris tabel kiri. Yang tidak punya pasangan diisi `NULL`, misalnya pelanggan yang belum pernah memesan.<br>***All** rows from the left table. Unmatched ones get `NULL`, e.g. customers who never ordered.* |
| `RIGHT` / `FULL OUTER JOIN` | Ada, tetapi sebagian besar kebutuhan sudah tercukupi dengan `INNER` dan `LEFT`.<br>*They exist, but `INNER` and `LEFT` cover most needs.* |

💡 *Analogi:* JOIN seperti menempelkan nama dari buku kontak (`customers`) ke setiap struk belanja (`orders`) yang hanya mencantumkan nomor pelanggan.<br>
*Analogy: a JOIN is like copying names from a contact book (`customers`) onto every receipt (`orders`) that only shows a customer number.*

⚠️ **JOIN bisa menggandakan baris (*fan-out*).** Satu pesanan dengan tiga item di `order_details` akan muncul tiga kali setelah di-JOIN. Kalau kolom milik pesanan (misalnya `orders.total_amount`) lalu di-`SUM`, nilainya ikut terhitung tiga kali. Selalu cek tingkat detail (*grain*) setiap tabel sebelum melakukan agregasi.<br>
***JOINs can multiply rows (fan-out).** An order with three items in `order_details` shows up three times after the join. If an order-level column (e.g. `orders.total_amount`) is then `SUM`med, it's counted three times. Always check each table's grain before aggregating.*

### 📊 5. GROUP BY & Agregasi · *Aggregation*

`GROUP BY` mengelompokkan baris, lalu fungsi agregasi (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) meringkas setiap kelompok. `HAVING` adalah filter untuk **hasil** agregasi.<br>
*`GROUP BY` groups rows, then aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) summarise each group. `HAVING` filters the **aggregated** result.*

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 3            -- hanya pelanggan dengan > 3 pesanan
ORDER BY order_count DESC;
```

| | `WHERE` | `HAVING` |
|---|---|---|
| **Menyaring · *Filters*** | Baris mentah, **sebelum** dikelompokkan.<br>*Raw rows, **before** grouping.* | Kelompok, **setelah** agregasi.<br>*Groups, **after** aggregation.* |
| **Boleh pakai `SUM()` dkk? · *Can use `SUM()` etc.?*** | ❌ | ✅ |

Urutan eksekusi SQL berbeda dari urutan penulisannya. Memahami urutan ini menjelaskan kenapa `WHERE` tidak bisa memakai fungsi agregasi.<br>
*SQL runs in a different order from how it's written. Knowing this order explains why `WHERE` can't use aggregate functions.*

```
FROM / JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

### 🧩 6. CTE (Common Table Expression)

**CTE** adalah *query* sementara yang diberi nama dengan `WITH`, lalu dipakai seperti tabel biasa. Dengan CTE, *query* yang panjang bisa dipecah menjadi langkah-langkah bernama yang dibaca dari atas ke bawah.<br>
*A **CTE** is a temporary query named with `WITH` and then used like a normal table. It splits a long query into named steps that read top to bottom.*

```sql
WITH top_customers AS (
    SELECT customer_id, SUM(total_amount) AS spending
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total_amount) > 100000
)
SELECT c.name, t.spending
FROM top_customers t
JOIN customers c ON c.customer_id = t.customer_id;
```

Manfaatnya: lebih mudah dibaca, hasilnya bisa dipakai berkali-kali dalam *query* yang sama, dan setiap langkah bisa diuji sendiri saat *debugging*.<br>
*The benefits: easier to read, its result can be reused within the same query, and each step can be tested on its own when debugging.*

💡 *Analogi:* CTE seperti variabel di Python. Hasil antara diberi nama dulu, baru dipakai, daripada menulis satu ekspresi panjang yang bersarang.<br>
*Analogy: a CTE is like a variable in Python. Name the intermediate result first, then use it, instead of writing one long nested expression.*

### ⚡ 7. Optimasi Query · *Query Optimization*

*Query* yang benar belum tentu cepat. *Chatbot* yang menunggu 30 detik untuk satu *query* tidak layak dijadikan produk.<br>
*A correct query isn't necessarily a fast one. A chatbot that waits 30 seconds for one query isn't a shippable product.*

1. **Ambil kolom yang dibutuhkan saja.** Hindari `SELECT *` di *production*.<br>***Select only the columns you need.** Avoid `SELECT *` in production.*
2. **Buat INDEX** pada kolom yang sering dipakai di `WHERE` atau `JOIN`: `CREATE INDEX idx_customers_email ON customers(email);`<br>***Add an INDEX** on columns often used in `WHERE` or `JOIN`.*
3. **Filter dulu, agregasi kemudian.** Semakin sedikit baris yang lolos `WHERE`, semakin ringan kerja `GROUP BY`.<br>***Filter first, aggregate later.** The fewer rows pass `WHERE`, the less work `GROUP BY` has.*
4. **Ukur dengan `EXPLAIN ANALYZE`** untuk melihat rencana eksekusi Postgres dan waktu setiap tahapnya.<br>***Measure with `EXPLAIN ANALYZE`** to see Postgres's execution plan and the time each step takes.*

| Yang terlihat di `EXPLAIN ANALYZE` · *What you see* | Artinya · *Meaning* |
|---|---|
| `Seq Scan` pada tabel besar · *on a big table* | Postgres membaca seluruh tabel. Biasanya tanda perlu *index*.<br>*Postgres reads the whole table. Usually a sign an index is needed.* |
| `Index Scan` | Postgres langsung melompat ke baris yang dicari lewat *index*. Ini sudah baik.<br>*Postgres jumps straight to the matching rows via the index. Good.* |
| `actual time` | Waktu eksekusi sebenarnya dalam milidetik.<br>*Actual execution time in milliseconds.* |

💡 *Analogi:* *index* seperti daftar indeks di belakang buku. Tanpa indeks, kita harus membaca buku dari halaman pertama (*Seq Scan*). Dengan indeks, kita langsung membuka halaman yang tepat (*Index Scan*).<br>
*Analogy: an index is like the index at the back of a book. Without it you read from page one (Seq Scan); with it you open the right page straight away (Index Scan).*

Prinsipnya: ***measure first, optimize second***. Jangan menebak bagian mana yang lambat sebelum mengukurnya.<br>
*The rule: **measure first, optimize second**. Don't guess what's slow before measuring it.*

### 🔄 8. SQL ↔ Pandas

Hampir setiap operasi dari [Sesi 06](../sesi-06-data-wrangling-pandas/) punya padanan di SQL. Pilihan praktisnya: lakukan filter dan agregasi berat di *database* (lebih dekat ke data, lebih sedikit data yang dikirim), lalu lanjutkan di Pandas untuk *feature engineering* dan analisis.<br>
*Almost every operation from [Session 06](../sesi-06-data-wrangling-pandas/) has an SQL counterpart. A practical split: do the heavy filtering and aggregation in the database (closer to the data, less data to move), then continue in Pandas for feature engineering and analysis.*

| SQL | Pandas |
|---|---|
| `SELECT a, b FROM t` | `df[['a', 'b']]` |
| `WHERE x > 5` | `df[df['x'] > 5]` |
| `ORDER BY x DESC LIMIT 5` | `df.nlargest(5, 'x')` |
| `JOIN ... ON` | `df.merge(other, on=..., how=...)` |
| `GROUP BY k` + `SUM(v)` | `df.groupby('k')['v'].sum()` |
| `HAVING SUM(v) > 100` | `.groupby(...).filter(...)` atau filter setelah agregasi |
| `WITH cte AS (...)` | Variabel perantara · *an intermediate variable* |

```python
df = pd.read_sql("SELECT ... FROM orders WHERE ...", engine)   # SQLAlchemy engine
```

🎯 **Kapan dipakai · *When to use*:** setiap kali data sumber berada di *database*: menyiapkan *dataset* latih, mengambil dokumen untuk RAG, atau memberi *chatbot* akses ke data pengguna secara *real-time*. Di [Sesi 09](../sesi-09-sql-scraping-data-cleaning-pipeline/), SQL akan digabung dengan *scraping* dan pembersihan data menjadi satu *pipeline*.<br>
*Whenever the source data lives in a database: preparing a training set, fetching documents for RAG, or giving a chatbot real-time access to user data. In [Session 09](../sesi-09-sql-scraping-data-cleaning-pipeline/), SQL gets combined with scraping and cleaning into one pipeline.*

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Homework SQL for AI: latihan *query* di *database sandbox* e-commerce (JOIN, `GROUP BY`, `HAVING`)<br>*Homework SQL for AI: query practice on the e-commerce sandbox database (JOIN, `GROUP BY`, `HAVING`)* | _(menyusul · *coming soon*)_ | 🔄 |

## 💡 Catatan & Referensi · *Notes & References*

- [PostgreSQL Tutorial (dokumentasi resmi · *official docs*)](https://www.postgresql.org/docs/current/tutorial.html)
- [PostgreSQL Docs: WITH Queries (CTE)](https://www.postgresql.org/docs/current/queries-with.html)
- [PostgreSQL Docs: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- [DBeaver Community](https://dbeaver.io/)
- [pgvector](https://github.com/pgvector/pgvector)
- [SQLBolt (latihan interaktif · *interactive practice*)](https://sqlbolt.com/)

</div>

---

<div align="center">

<a href="../sesi-07-project-1-python-automation-tool/">← Sesi 07</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-09-sql-scraping-data-cleaning-pipeline/">Sesi 09 →</a>

</div>
