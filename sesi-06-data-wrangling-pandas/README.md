<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🐼 Sesi 06 — Data Wrangling dengan Pandas

<img src="https://img.shields.io/badge/Sesi-06%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-9%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/> <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square" alt="Matplotlib"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Senin, 9 November 2026** · 19.15 – 21.15 WIB<br>
*Monday, November 9, 2026 · 7:15 – 9:15 PM (UTC+7)*

Membaca, membersihkan, mentransformasi, dan menggabungkan data tabular dengan Pandas.<br>
*Reading, cleaning, transforming, and joining tabular data with Pandas.*

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini membahas cara mengubah data mentah yang berantakan menjadi data yang siap dipakai model. Urutannya: NumPy sebagai fondasi, struktur data Pandas, pembersihan data, *feature engineering*, lalu *Exploratory Data Analysis* (EDA).<br>
*This session covered how to turn messy raw data into data a model can use. The order was: NumPy as the foundation, Pandas data structures, data cleaning, feature engineering, then Exploratory Data Analysis (EDA).*

### 🗑️ 1. Kenapa Data Wrangling? · *Why Data Wrangling?*

Prinsipnya ***garbage in, garbage out***: model secanggih apa pun akan menghasilkan keluaran buruk kalau datanya kotor. Dalam praktik, sebagian besar waktu kerja (kira-kira 60–80%) habis untuk membersihkan, mengubah, dan menggabungkan data. Sisanya baru untuk *modeling* dan evaluasi.<br>
*The rule is **garbage in, garbage out**: even the best model gives bad output if its data is dirty. In practice most of the work (roughly 60–80%) goes into cleaning, transforming, and joining data. Only the rest goes to modeling and evaluation.*

💡 *Analogi:* seperti memasak. Koki menghabiskan lebih banyak waktu mencuci dan memotong bahan daripada menggoreng. Bahan yang busuk tidak bisa diselamatkan oleh resep terbaik.<br>
*Analogy: like cooking. A chef spends more time washing and chopping than actually frying. No recipe can save spoiled ingredients.*

### 🔢 2. NumPy: Fondasi Komputasi Numerik · *The Numeric Foundation*

**NumPy** adalah *library* untuk operasi angka dalam bentuk *array*. Pandas, scikit-learn, PyTorch, dan TensorFlow semuanya dibangun di atasnya. Kelebihannya: jauh lebih cepat dari *loop* Python, hemat memori, dan bisa ditulis seperti rumus matematika (**vectorization**).<br>
***NumPy** is a library for number crunching on arrays. Pandas, scikit-learn, PyTorch, and TensorFlow are all built on top of it. Its strengths: much faster than Python loops, memory-efficient, and written like a math formula (**vectorization**).*

```python
import numpy as np

harga = np.array([100, 200, 300, 400, 500])
harga * 0.9                    # diskon 10% ke semua elemen, tanpa loop
harga.mean(), harga.max()      # agregasi

umur = np.array([25, 15, 45, 17])
umur[umur >= 18]               # boolean indexing -> [25 45]
np.where(umur >= 18, 'dewasa', 'anak')
```

| Konsep · *Concept* | Penjelasan · *Explanation* |
|---|---|
| `shape`, `dtype` | Ukuran *array* (baris, kolom) dan tipe datanya. Hal pertama yang dicek saat *debugging*.<br>*The array's size (rows, columns) and data type. The first thing to check when debugging.* |
| `np.zeros`, `np.ones`, `np.arange`, `np.linspace` | Membuat *array* khusus: isi nol, isi satu, deret dengan langkah tetap, atau deret dengan jumlah titik tertentu.<br>*Build special arrays: all zeros, all ones, a range with a fixed step, or a range with a set number of points.* |
| **Boolean indexing** | Membuat *mask* `True/False`, lalu memakainya untuk memilih elemen. Pola ini juga dipakai di Pandas untuk memfilter baris.<br>*Build a `True/False` mask and use it to pick elements. Pandas uses the same pattern to filter rows.* |
| `df.to_numpy()` / `pd.DataFrame(arr)` | Konversi bolak-balik Pandas ↔ NumPy. Model ML biasanya menerima *array* NumPy.<br>*Convert back and forth between Pandas and NumPy. ML models usually take NumPy arrays.* |

💡 *Analogi:* *loop* Python seperti kasir yang menghitung belanjaan satu per satu, sedangkan *vectorization* seperti mesin pemindai yang memproses seluruh keranjang sekaligus.<br>
*Analogy: a Python loop is a cashier ringing up items one at a time; vectorization is a scanner that handles the whole basket at once.*

### 📋 3. Pandas: Series & DataFrame

Kalau NumPy bekerja dengan angka, **Pandas** bekerja dengan **tabel berlabel**, mirip Excel atau tabel SQL.<br>
*Where NumPy works with numbers, **Pandas** works with **labelled tables**, much like Excel or an SQL table.*

- **Series**: satu kolom data 1D yang punya label (*index*).<br>*Series: one 1D column of data with labels (an index).*
- **DataFrame**: tabel 2D, yaitu kumpulan Series yang berbagi *index* yang sama.<br>*DataFrame: a 2D table, i.e. a set of Series sharing the same index.*

```python
import pandas as pd

df = pd.read_csv('users.csv')       # bisa juga dari dict, Excel, atau query SQL

df.head(); df.shape; df.info(); df.describe()      # inspeksi cepat

df['name']                          # 1 kolom  -> Series
df[['name', 'age']]                 # >=2 kolom -> DataFrame
df[(df['age'] > 25) & (df['city'] == 'Jakarta')]   # filter, mirip WHERE di SQL
df.loc[0, 'name']                   # pilih berdasarkan label
df.iloc[0:3, 0:2]                   # pilih berdasarkan posisi
```

⚠️ Kondisi ganda wajib memakai `&` / `|` dan **setiap kondisi diberi kurung**. `and` / `or` biasa akan *error* di Pandas.<br>
*Multiple conditions must use `&` / `|` with **each condition in parentheses**. Plain `and` / `or` raise an error in Pandas.*

### 🧽 4. Data Cleaning

Data nyata hampir selalu kotor: ada nilai kosong, baris ganda, penulisan tidak seragam (`"Jakarta"`, `"jakarta "`, `"JKT"`), tipe data salah (angka tersimpan sebagai teks), dan *outlier* yang tidak masuk akal (umur 200).<br>
*Real data is almost always dirty: missing values, duplicate rows, inconsistent spelling (`"Jakarta"`, `"jakarta "`, `"JKT"`), wrong types (numbers stored as text), and outliers that make no sense (age 200).*

| Masalah · *Problem* | Deteksi · *Detect* | Penanganan · *Fix* |
|---|---|---|
| **Missing values** | `df.isnull().sum()`<br>`df.isnull().mean() * 100` | Buang: `dropna()`, `dropna(subset=[...])`.<br>Isi: `fillna(mean/median)` untuk angka, `fillna('Unknown')` untuk kategori, `.ffill()` untuk *time series*.<br>*Drop, or fill: mean/median for numbers, a constant for categories, forward-fill for time series.* |
| **Duplikat · *Duplicates*** | `df.duplicated().sum()`<br>`df[df.duplicated(keep=False)]` | `drop_duplicates()` untuk baris identik, `drop_duplicates(subset=['user_id'])` untuk kunci unik.<br>*For identical rows, or by a unique key.* |
| **Teks tidak seragam · *Inconsistent text*** | `df['city'].unique()` | `.str.strip().str.lower()` atau `.str.title()`.<br>*Strip whitespace and normalise case.* |
| **Tipe data salah · *Wrong types*** | `df.dtypes` | `astype(int/float)`, `pd.to_datetime()`. |
| **Nilai tidak valid · *Invalid values*** | `~df['gender'].isin(['M', 'F'])` | `df['gender'].where(mask, np.nan)` mengganti nilai di luar daftar menjadi NaN.<br>*Turns values outside the allowed list into NaN.* |

Tidak ada strategi *missing value* yang berlaku untuk semua kasus. Buang baris kalau jumlahnya sedikit dan acak; isi (*impute*) kalau jumlahnya banyak tapi masih bisa diperkirakan. Yang penting, **catat alasan setiap keputusan**.<br>
*No missing-value strategy fits every case. Drop rows when there are few and they're random; impute when there are many but they can be estimated. What matters is to **document the reason for each decision**.*

⚠️ *Accessor* `.str` otomatis melewati NaN. Sebaliknya, `astype(str)` mengubah NaN menjadi teks `"nan"`, sehingga data kosong terlihat seperti nilai sungguhan. Saya menemui kasus ini langsung di [Mini Project Sesi 07](../sesi-07-project-1-python-automation-tool/).<br>
*The `.str` accessor skips NaN automatically. `astype(str)`, on the other hand, turns NaN into the text `"nan"`, so missing data looks like a real value. I ran into this myself in the [Session 07 Mini Project](../sesi-07-project-1-python-automation-tool/).*

⚠️ `fillna(method='ffill')` sudah *deprecated* di Pandas versi baru. Pakai `df['price'].ffill()`.<br>
*`fillna(method='ffill')` is deprecated in recent Pandas. Use `df['price'].ffill()` instead.*

### 🛠️ 5. Feature Engineering

Setelah data bersih, kita **membuat fitur baru** yang lebih mudah dipelajari model. Model tidak selalu bisa menemukan pola sendiri, jadi kita bantu menonjolkannya. Sering kali yang membuat model unggul justru fiturnya, bukan algoritmanya.<br>
*Once the data is clean, we **create new features** that are easier for a model to learn from. Models don't always find patterns on their own, so we help highlight them. Often what makes a model win is the features, not the algorithm.*

| Teknik · *Technique* | Kode · *Code* | Kapan · *When* |
|---|---|---|
| **One-hot encoding** | `pd.get_dummies(df, columns=['city'])` | Kategori **tanpa urutan** (kota, warna). Setiap kategori jadi kolom 0/1.<br>*Categories with **no order** (city, colour). Each category becomes a 0/1 column.* |
| **Ordinal / label encoding** | `df['size'].map({'S': 1, 'M': 2, 'L': 3})` | Kategori **berurutan** (S < M < L, *bronze* < *silver* < *gold*).<br>*Categories with **an order**.* |
| **Binning** | `pd.cut(age, bins=[...], labels=[...])`<br>`pd.qcut(spending, q=4)` | Mengubah angka kontinu menjadi kelompok, dengan batas sendiri (`cut`) atau berdasarkan kuartil (`qcut`).<br>*Turn a continuous number into groups, by custom edges (`cut`) or by quartiles (`qcut`).* |
| **Fitur waktu · *Datetime*** | `df['ts'].dt.hour`, `.dt.dayofweek`, `.dt.dayofweek >= 5` | *Timestamp* mentah tidak berguna bagi model. Pecah menjadi jam, hari, bulan, akhir pekan, jam kerja, dan sebagainya.<br>*A raw timestamp means nothing to a model. Break it into hour, weekday, month, weekend, business hours, etc.* |
| **Fungsi kustom · *Custom function*** | `df['email'].apply(fn)`<br>`df.apply(fn, axis=1)` | Logika yang tidak tersedia sebagai *method* bawaan, per kolom atau per baris (misalnya segmen pelanggan VIP/regular/new).<br>*Logic not available as a built-in method, per column or per row (e.g. VIP/regular/new customer segments).* |
| **Merge** | `orders.merge(users, on='user_id', how='left')` | Menggabungkan dua tabel, setara `JOIN` di SQL (`inner`, `left`, dst.).<br>*Join two tables, the same as SQL `JOIN` (`inner`, `left`, etc.).* |

Contoh transformasi · *Example transformations*: `'ani@gmail.com'` → `email_domain='gmail.com'`, `is_free_email=True` · `'2026-07-15 14:30'` → `hour=14`, `is_weekend=False`, `is_business_hour=True`.

⚠️ `df.apply(fn, axis=1)` sebenarnya *loop* per baris, jadi lambat untuk data besar. Kalau ada versi *vectorized*-nya (`np.where`, `pd.cut`, operasi kolom), pakai itu.<br>
*`df.apply(fn, axis=1)` is really a row-by-row loop, so it's slow on large data. If a vectorized version exists (`np.where`, `pd.cut`, column arithmetic), use that.*

### 🔍 6. Exploratory Data Analysis (EDA)

**EDA** adalah tahap mengenali data **sebelum** membangun model: distribusinya, hubungan antar-variabel, *outlier*, dan anomali. Model yang dibangun tanpa EDA sering gagal di *production* karena pembuatnya tidak benar-benar memahami datanya.<br>
***EDA** is getting to know the data **before** building a model: its distributions, how variables relate, outliers, and anomalies. Models built without EDA often fail in production because their builders never really understood the data.*

```python
df.describe()                         # count, mean, std, min, kuartil, max
df.describe(include='object')         # ringkasan kolom kategori
df['city'].value_counts(normalize=True)
df.groupby('segment').agg({'total_spending': ['mean', 'max', 'count'], 'age': 'mean'})
df.select_dtypes('number').corr()     # korelasi antar-kolom numerik
```

| Grafik · *Chart* | Untuk · *For* |
|---|---|
| Histogram `df['age'].hist()` | Bentuk distribusi angka: normal atau miring (*skewed*).<br>*Shape of a numeric distribution: normal or skewed.* |
| Bar chart `value_counts().plot(kind='bar')` | Frekuensi tiap kategori.<br>*Frequency of each category.* |
| Scatter `df.plot.scatter(x, y)` | Hubungan dua variabel numerik.<br>*Relationship between two numeric variables.* |
| Boxplot `df.boxplot(column=...)` | Mendeteksi *outlier*.<br>*Spotting outliers.* |

Daftar periksa EDA yang dipakai di kelas · *The EDA checklist used in class*:

1. Berapa persen *missing value* per kolom? · *What % of each column is missing?*
2. Berapa duplikat, baik baris utuh maupun per kunci? · *How many duplicates, by full row and by key?*
3. Distribusi target: normal atau *skewed*? · *Is the target normal or skewed?*
4. Kategori mana yang sampelnya terlalu sedikit (perlu digabung atau dibuang)? · *Which categories are too rare (merge or drop)?*
5. Ada korelasi > 0,8 antar-fitur (*multicollinearity*)? · *Any correlation > 0.8 between features?*
6. Ada *outlier* ekstrem yang perlu ditangani? · *Any extreme outliers to handle?*

Setiap temuan harus diikuti **keputusan**: *drop*, *impute*, *transform*, atau biarkan, beserta alasannya.<br>
*Every finding should end in a **decision**: drop, impute, transform, or leave it, with the reason.*

🎯 **Kapan dipakai · *When to use*:** setiap kali data masuk ke sistem AI, baik untuk melatih model ML, menyiapkan dokumen untuk RAG, maupun membersihkan hasil *scraping*. Pola `read → clean → transform → save` dari sesi ini langsung dipakai lagi di [Mini Project Sesi 07](../sesi-07-project-1-python-automation-tool/), dan padanan SQL-nya muncul di [Sesi 08](../sesi-08-sql-for-ai/).<br>
*Whenever data enters an AI system, whether to train an ML model, prepare documents for RAG, or clean scraped data. The `read → clean → transform → save` pattern from this session comes straight back in the [Session 07 Mini Project](../sesi-07-project-1-python-automation-tool/), and its SQL counterpart shows up in [Session 08](../sesi-08-sql-for-ai/).*

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Latihan di kelas: (1) membandingkan kecepatan *loop* Python vs NumPy *vectorized*, (2) membuat tiga fitur baru (*encoding*, waktu, logika kustom), (3) menjalankan *checklist* EDA beserta keputusannya<br>*In-class exercises: (1) compare a Python loop with NumPy vectorization, (2) build three new features (encoding, datetime, custom logic), (3) run the EDA checklist with decisions* | _(notebook kelas, tidak diunggah · *class notebook, not uploaded*)_ | ✅ |

## 💡 Catatan & Referensi · *Notes & References*

- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas: Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Pandas: Working with text data](https://pandas.pydata.org/docs/user_guide/text.html)
- [Pandas: Comparison with SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)

</div>

---

<div align="center">

<a href="../sesi-05-git-github/">← Sesi 05</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-07-project-1-python-automation-tool/">Sesi 07 →</a>

</div>
