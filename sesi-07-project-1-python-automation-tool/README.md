<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🛠️ Sesi 07 — PROJECT 1 · Python Automation Tool

<img src="https://img.shields.io/badge/Sesi-07%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-11%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/> <img src="https://img.shields.io/badge/Automation-FF6F00?style=flat-square" alt="Automation"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Rabu, 11 November 2026** · 19.15 – 21.15 WIB<br>
*Wednesday, November 11, 2026 · 7:15 – 9:15 PM (UTC+7)*

Proyek pertama: membangun alat otomasi berbasis Python dari materi sesi 3–6.<br>
*First project: building a Python automation tool using what was covered in sessions 3–6.*

🚀 **Halaman proyek · *Project page*:** [proyek/01-python-automation-tool](../proyek/01-python-automation-tool/)

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini menyatukan semua materi Python sebelumnya menjadi satu alat kerja. Di *hands-on*, kami membersihkan dataset pengiriman logistik: mulai dari fungsi-fungsi terpisah di *notebook*, dirapikan menjadi satu *class* `DataCleaner`, diberi dokumentasi, lalu diekspor menjadi *script* `.py` yang bisa dijalankan dengan satu perintah.<br>
*This session pulled all the earlier Python material together into one working tool. In the hands-on we cleaned a logistics shipment dataset: starting from separate functions in a notebook, refactoring them into a single `DataCleaner` class, documenting it, then exporting it as a `.py` script that runs with one command.*

### 🧱 1. Peta Fondasi · *Building Blocks*

| Dari sesi · *From session* | Bekal yang dipakai · *What we reuse* |
|---|---|
| 🐍 Sesi 03 · Python dasar | Tipe data, operasi *string* (`.strip()`, `.title()`), `if-else`.<br>*Data types, string operations, `if-else`.* |
| 🧩 Sesi 04 · Fungsi & OOP | `def`, nilai `return`, prinsip DRY (*Don't Repeat Yourself*), *class*, *type hint*.<br>*`def`, return values, the DRY principle, classes, type hints.* |
| 🐼 Sesi 06 · Pandas | `pd.read_csv()`, `fillna()`, `drop_duplicates()`. |

### 🩺 2. Diagnosis Data Mentah · *Diagnosing the Raw Data*

Langkah pertama selalu memeriksa data dengan `df.info()`, `df.head()`, dan `df.isna().sum()`. Dataset logistik *hands-on* (108 baris, 8 kolom) punya empat masalah yang ternyata sangat umum:<br>
*Step one is always to inspect the data with `df.info()`, `df.head()`, and `df.isna().sum()`. The hands-on logistics dataset (108 rows, 8 columns) had four very common problems:*

| # | Masalah · *Problem* | Contoh · *Example* | Solusi · *Fix* |
|:-:|---|---|---|
| 1 | Spasi berlebih · *Extra whitespace* | `" PT Maju Bersama "` | `.str.strip()` |
| 2 | Kapitalisasi tidak seragam · *Inconsistent case* | `DELIVERED`, `Delivered`, `delivered` | `.str.title()` |
| 3 | Baris duplikat · *Duplicate rows* | 8 baris identik · *8 identical rows* | `drop_duplicates()` |
| 4 | Nilai kosong · *Missing values* | `berat_kg` berisi NaN | `fillna(0.0)` |

### 🔁 3. Dari Fungsi ke Class OOP · *From Functions to an OOP Class*

**Tahap 1 — prosedural.** Setiap langkah dibuat sebagai fungsi terpisah, lalu dipanggil satu per satu. Cara ini cocok untuk uji coba, tetapi kita harus terus meneruskan variabel `df_clean` dari satu fungsi ke fungsi berikutnya secara manual.<br>
***Step 1: procedural.** Each step is a separate function, called one after another. Fine for experimenting, but we have to keep passing `df_clean` from one function to the next by hand.*

**Tahap 2 — class.** Semua fungsi dibungkus ke dalam *class* `DataCleaner`. Manfaatnya:<br>
***Step 2: a class.** All the functions are wrapped into a `DataCleaner` class. The benefits:*

| Manfaat · *Benefit* | Penjelasan · *Explanation* |
|---|---|
| 📦 **Encapsulation** | Data (`self.df`) dan semua *method* pembersihnya tersimpan dalam satu objek.<br>*The data (`self.df`) and all its cleaning methods live in one object.* |
| ♻️ **Reusability** | *Class* yang sama bisa dipakai untuk CSV lain (logistik → retail) tanpa menulis ulang kode.<br>*The same class works on another CSV (logistics → retail) without rewriting code.* |
| ⛓️ **Method chaining** | Langkah pembersihan bisa dirangkai dalam satu kalimat kode yang mudah dibaca.<br>*Cleaning steps can be chained into one readable line of code.* |

Kuncinya adalah **`return self`** di akhir setiap *method*. Karena *method* mengembalikan objeknya sendiri, *method* berikutnya bisa langsung dipanggil di belakangnya:<br>
*The key is **`return self`** at the end of every method. Because a method returns its own object, the next method can be called right after it:*

```python
class DataCleaner:
    def __init__(self, file_path: str):
        self.df: pd.DataFrame = pd.read_csv(file_path)

    def hapus_duplikat(self) -> "DataCleaner":
        """Menghapus baris yang terduplikasi persis."""
        self.df = self.df.drop_duplicates()
        return self                      # <- ini yang membuat chaining bisa jalan

cleaner = DataCleaner("data_mentah.csv")
cleaner.bersihkan_teks([...]).hapus_duplikat().isi_nilai_kosong("berat_kg").simpan_hasil("data_bersih.csv")
```

💡 *Analogi:* *method chaining* seperti jalur perakitan pabrik. Barang yang keluar dari satu mesin langsung masuk ke mesin berikutnya, tanpa perlu diangkut manual oleh operator.<br>
*Analogy: method chaining is like a factory assembly line. What comes out of one machine goes straight into the next, with no operator carrying it over by hand.*

### 📝 4. Dokumentasi: Type Hint & Docstring · *Documentation*

- **Type hint** (`file_path: str`, `-> "DataCleaner"`) memberi tahu pembaca dan IDE tipe data yang diharapkan. Python tidak memaksakannya saat *runtime*, tetapi IDE bisa memberi peringatan dan *autocomplete*.<br>
  ***Type hints** tell readers and the IDE what type is expected. Python doesn't enforce them at runtime, but the IDE can warn and autocomplete.*
- **Docstring** (`"""..."""`) menjelaskan fungsi sebuah *method*. Teksnya bisa dibaca lewat `help()` atau saat kursor diarahkan ke nama *method* di editor.<br>
  ***Docstrings** explain what a method does. They show up in `help()` and when hovering over the method in the editor.*

### 📤 5. Dari Notebook ke Script `.py` · *From Notebook to Script*

*Notebook* bagus untuk eksplorasi, tetapi otomasi membutuhkan *script* yang bisa dijalankan tanpa membuka Jupyter, misalnya lewat *cron*, *scheduler*, atau *pipeline* CI.<br>
*Notebooks are great for exploring, but automation needs a script that runs without opening Jupyter, e.g. from cron, a scheduler, or a CI pipeline.*

- `%%writefile clean_logistik.py` di awal *cell* menyimpan isi *cell* itu menjadi berkas `.py`.<br>
  *`%%writefile clean_logistik.py` at the top of a cell saves that cell as a `.py` file.*
- Blok `if __name__ == "__main__":` hanya berjalan saat berkas dijalankan langsung (`python clean_logistik.py`), **tidak** saat berkas di-*import* oleh kode lain. Jadi *class*-nya tetap bisa dipakai ulang di tempat lain.<br>
  *The `if __name__ == "__main__":` block only runs when the file is executed directly, **not** when it's imported by other code, so the class can still be reused elsewhere.*

⚠️ *Path* relatif seperti `"data.csv"` dibaca dari **folder tempat terminal berada**, bukan folder *script*. Di *mini project* saya memakai `Path(__file__).resolve().parent` supaya *script* tetap menemukan datanya dari folder mana pun ia dijalankan.<br>
*A relative path like `"data.csv"` is resolved from **the terminal's current folder**, not the script's folder. In the mini project I used `Path(__file__).resolve().parent` so the script finds its data no matter where it's run from.*

🎯 **Kapan dipakai · *When to use*:** setiap kali ada proses data yang berulang, seperti laporan harian, pembersihan data masuk, atau persiapan data untuk model. Pola *class* + *method chaining* + *script* ini menjadi dasar *data pipeline* di [Project 2](../proyek/02-end-to-end-data-pipeline/).<br>
*Whenever a data task repeats: daily reports, cleaning incoming data, or preparing data for a model. This class + method chaining + script pattern is the basis for the data pipeline in [Project 2](../proyek/02-end-to-end-data-pipeline/).*

## 🚀 Mini Project: Retail Dataset Automation & Cleaning

Tugas sesi ini menerapkan *class* `DataCleaner` dari *hands-on* ke dataset transaksi retail yang berbeda.<br>
*This session's assignment applies the `DataCleaner` class from the hands-on to a different dataset: retail transactions.*

**Kriteria · *Requirements*:** rapikan spasi dan ubah ke *Title Case* pada `nama_produk`, `kategori`, `metode_bayar`, dan `kota_pembeli`; hapus baris duplikat persis; isi NaN pada `jumlah_beli` dengan 0; simpan hasilnya ke `dataset_retail_clean.csv`; dan pastikan *script* bisa dijalankan dengan `python clean_retail.py`.<br>
*Strip whitespace and convert to Title Case in `nama_produk`, `kategori`, `metode_bayar`, and `kota_pembeli`; drop exact duplicate rows; fill NaN in `jumlah_beli` with 0; save to `dataset_retail_clean.csv`; and make the script runnable with `python clean_retail.py`.*

**Hasil · *Results*:**

| | Sebelum · *Before* | Sesudah · *After* |
|---|:-:|:-:|
| Jumlah baris · *Rows* | 108 | **100** (8 duplikat dihapus · *8 duplicates removed*) |
| Variasi `nama_produk` · *variants* | 10 | **7** |
| Variasi `metode_bayar` · *variants* | 7 | **4** |
| NaN di `jumlah_beli` | 12 | **0** (10 diisi, 2 ikut terhapus bersama duplikat · *10 filled, 2 went with the duplicates*) |
| Tipe `jumlah_beli` · *dtype* | `float64` (`5.0`) | **`int64`** (`5`) |

**Modifikasi dari versi *hands-on* · *Changes from the hands-on version*:**

| Method | Perubahan · *Change* | Alasan · *Why* |
|---|---|---|
| `bersihkan_teks` | Menghapus `.astype(str)` | `astype(str)` mengubah NaN menjadi teks `"nan"`, lalu `.title()` menjadikannya `"Nan"`. Akibatnya, 18 pembeli tanpa kota terlihat seperti tinggal di kota bernama "Nan". *Accessor* `.str` sudah otomatis melewati NaN.<br>*`astype(str)` turns NaN into the text `"nan"`, which `.title()` makes `"Nan"`, so 18 buyers with no city looked like they lived in a city called "Nan". The `.str` accessor already skips NaN.* |
| `bersihkan_teks` | Peringatan jika kolom tidak ada · *Warn on missing column* | Salah ketik nama kolom langsung terlihat, tidak dilewati diam-diam.<br>*A typo in a column name shows up instead of being silently skipped.* |
| `hapus_duplikat` | `+ reset_index(drop=True)` | Nomor *index* kembali berurutan setelah baris dihapus.<br>*The index is sequential again after rows are dropped.* |
| `isi_nilai_kosong` | Melaporkan jumlah sel yang diisi, lalu mengubah ke `int` · *Report count, cast to `int`* | Kolom yang mengandung NaN dibaca sebagai *float*, padahal jumlah barang selalu bilangan bulat.<br>*A column with NaN is read as float, but item counts are always whole numbers.* |

**Pelajaran dari tugas ini · *Lessons from this assignment*:**

- **Urutan langkah itu penting.** Teks dibersihkan **sebelum** menghapus duplikat, supaya baris yang hanya berbeda spasi atau kapitalisasi juga terdeteksi sebagai duplikat.<br>
  ***Order matters.** Text is cleaned **before** dropping duplicates, so rows that only differ in spacing or case are also caught as duplicates.*
- **Validasi dengan `assert`.** Di akhir *notebook*, setiap kriteria dicek otomatis (tidak ada duplikat, tidak ada NaN di `jumlah_beli`, teks sudah rapi, tidak ada teks `"Nan"`). Kalau ada yang gagal, *notebook* langsung berhenti.<br>
  ***Validate with `assert`.** At the end of the notebook every requirement is checked automatically (no duplicates, no NaN in `jumlah_beli`, tidy text, no `"Nan"` text). If one fails, the notebook stops right there.*
- **Title Case punya efek samping.** Singkatan ikut berubah: `COD` → `Cod`, `ROG` → `Rog`, `iPhone` → `Iphone`. Ini sesuai *brief*, tetapi untuk laporan sungguhan perlu *mapping* koreksi tambahan.<br>
  ***Title Case has side effects.** Acronyms get changed too. That matches the brief, but a real report would need an extra correction mapping.*
- **Kolom di luar *scope* tetap dicatat.** `harga_satuan` dan `kota_pembeli` masih punya NaN, dan format `tanggal_transaksi` bercampur (`2026-02-01`, `2026/02/03`, `04-02-2026`). Tidak diubah karena di luar kriteria, tetapi dicatat untuk tahap berikutnya.<br>
  ***Out-of-scope columns are still noted.** `harga_satuan` and `kota_pembeli` still have NaN, and `tanggal_transaksi` mixes formats. Left untouched as they're outside the brief, but noted for the next stage.*

**Cara menjalankan · *How to run*:**

```bash
cd proyek/01-python-automation-tool
pip install pandas
# letakkan dataset_retail_homework.csv di folder yang sama (dataset dari tutor, tidak diunggah)
# put dataset_retail_homework.csv in the same folder (tutor dataset, not uploaded)
python clean_retail.py
```

```
=== PIPELINE OTOMATISASI DATA RETAIL ===
✓ Berhasil membaca file 'dataset_retail_homework.csv' dengan 108 baris.
✓ Kolom teks ['nama_produk', 'kategori', 'metode_bayar', 'kota_pembeli'] telah dibersihkan.
✓ Berhasil menghapus 8 baris duplikat.
✓ 10 nilai kosong pada kolom 'jumlah_beli' diisi dengan 0.
✓ Data bersih berhasil disimpan ke: 'dataset_retail_clean.csv' (100 baris).
=== PROSES SELESAI ===
```

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Mini Project: Retail Dataset Automation & Cleaning, yaitu eksplorasi data, modifikasi *class* `DataCleaner`, uji coba interaktif, validasi, dan *script* otomasi<br>*Mini Project: Retail Dataset Automation & Cleaning, i.e. data exploration, a modified `DataCleaner` class, interactive testing, validation, and an automation script* | [retail_cleaning.ipynb](../proyek/01-python-automation-tool/retail_cleaning.ipynb) · [clean_retail.py](../proyek/01-python-automation-tool/clean_retail.py) · `dataset_retail_homework.csv` · `dataset_retail_clean.csv`<br><sub>dataset tidak diunggah · *datasets not uploaded*</sub> | ✅ |
| 2 | Learning Progress Review Sesi 1–6 bersama Kelompok **Blast Off**: presentasi rangkuman enam sesi pertama. Saya menyiapkan opsi desain slide (tema *code editor*) dan menjadi PIC materi Sesi 3<br>*Learning Progress Review of Sessions 1–6 with the **Blast Off** group: a presentation summarising the first six sessions. I prepared the slide design options (a code-editor theme) and was PIC for the Session 3 material* | _(presentasi kelompok · *group presentation*)_ | ✅ |

## 💡 Catatan & Referensi · *Notes & References*

- [Python Docs: `__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
- [PEP 257: Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python Docs: pathlib](https://docs.python.org/3/library/pathlib.html)
- [IPython: `%%writefile` magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-writefile)
- [Pandas: Method chaining with `.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html)

</div>

---

<div align="center">

<a href="../sesi-06-data-wrangling-pandas/">← Sesi 06</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-08-sql-for-ai/">Sesi 08 →</a>

</div>
