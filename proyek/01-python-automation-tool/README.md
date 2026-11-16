<div align="center">

<sub><a href="../../">🏠 Beranda · <i>Home</i></a> &nbsp;·&nbsp; <a href="../">🗂️ Proyek · <i>Projects</i></a></sub>

# 🛠️ Project 1 — Python Automation Tool

<img src="https://img.shields.io/badge/Project-1%20%2F%204-8A2BE2?style=for-the-badge" alt="Project"/> <img src="https://img.shields.io/badge/Sesi-07-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/> <img src="https://img.shields.io/badge/Automation-FF6F00?style=flat-square" alt="Automation"/>

</div>

---

<div align="justify">

## 📌 Ringkasan · *Overview*

**Retail Dataset Automation & Cleaning**: *script* Python yang membersihkan dataset transaksi retail mentah dengan satu perintah. Logika pembersihannya dibungkus dalam *class* `DataCleaner` berbasis OOP dengan *method chaining*, dikembangkan dulu di *notebook*, lalu diekspor menjadi *script* `.py`.<br>
***Retail Dataset Automation & Cleaning**: a Python script that cleans a raw retail transaction dataset with one command. The cleaning logic lives in an OOP `DataCleaner` class with method chaining, built first in a notebook and then exported as a `.py` script.*

📚 Materi sesi · *Session notes*: [Sesi 07](../../sesi-07-project-1-python-automation-tool/)

## ✨ Fitur · *Features*

- **Normalisasi teks**: menghapus spasi berlebih dan menyeragamkan ke *Title Case* pada `nama_produk`, `kategori`, `metode_bayar`, dan `kota_pembeli`, tanpa mengubah NaN menjadi teks `"Nan"`.<br>
  ***Text normalisation**: strips extra whitespace and converts to Title Case in four columns, without turning NaN into the text `"Nan"`.*
- **Hapus duplikat**: membuang baris yang identik persis, lalu merapikan ulang *index*.<br>
  ***Deduplication**: drops exact duplicate rows and resets the index.*
- **Imputasi**: mengisi NaN di `jumlah_beli` dengan 0 dan mengubah kolomnya ke `int`.<br>
  ***Imputation**: fills NaN in `jumlah_beli` with 0 and casts it to `int`.*
- **Log setiap langkah**: setiap *method* mencetak apa yang dikerjakannya (jumlah baris dibaca, duplikat dihapus, sel diisi, baris disimpan).<br>
  ***Step logging**: each method prints what it did (rows read, duplicates removed, cells filled, rows saved).*
- **Bisa dijalankan dari folder mana pun**: *path* data dihitung dari lokasi *script* (`Path(__file__)`), bukan dari folder terminal.<br>
  ***Runs from any folder**: data paths are resolved from the script's location (`Path(__file__)`), not the terminal's folder.*

## 📦 Berkas · *Files*

| Berkas · *File* | Isi · *Contents* |
|---|---|
| [retail_cleaning.ipynb](retail_cleaning.ipynb) | Eksplorasi data mentah, modifikasi *class* `DataCleaner`, uji coba setiap *method*, validasi `assert`, dan ekspor.<br>*Raw data exploration, the modified `DataCleaner` class, step-by-step testing, `assert` validation, and export.* |
| [clean_retail.py](clean_retail.py) | *Script* otomasi: definisi *class* + blok `if __name__ == "__main__":`.<br>*Automation script: the class definition plus an `if __name__ == "__main__":` block.* |
| `dataset_retail_homework.csv` | Data mentah dari tutor (input, tidak diunggah).<br>*Raw data from the tutor (input, not uploaded).* |
| `dataset_retail_clean.csv` | Hasil pembersihan (output, tidak diunggah).<br>*Cleaned result (output, not uploaded).* |

## 🧰 Tech Stack

Python 3 · Pandas · Jupyter Notebook · `pathlib`

## ▶️ Cara Menjalankan · *How to Run*

```bash
cd proyek/01-python-automation-tool
pip install pandas
# letakkan dataset_retail_homework.csv di folder ini · put dataset_retail_homework.csv in this folder
python clean_retail.py
```

## 📊 Hasil & Demo · *Results & Demo*

```
=== PIPELINE OTOMATISASI DATA RETAIL ===
✓ Berhasil membaca file 'dataset_retail_homework.csv' dengan 108 baris.
✓ Kolom teks ['nama_produk', 'kategori', 'metode_bayar', 'kota_pembeli'] telah dibersihkan.
✓ Berhasil menghapus 8 baris duplikat.
✓ 10 nilai kosong pada kolom 'jumlah_beli' diisi dengan 0.
✓ Data bersih berhasil disimpan ke: 'dataset_retail_clean.csv' (100 baris).
=== PROSES SELESAI ===
```

| | Sebelum · *Before* | Sesudah · *After* |
|---|:-:|:-:|
| Jumlah baris · *Rows* | 108 | **100** |
| Variasi `nama_produk` · *variants* | 10 | **7** |
| Variasi `metode_bayar` · *variants* | 7 | **4** |
| NaN di `jumlah_beli` | 12 | **0** |
| Tipe `jumlah_beli` · *dtype* | `float64` | **`int64`** |

## 💡 Pelajaran · *Lessons Learned*

- `astype(str)` diam-diam mengubah NaN menjadi teks `"nan"`. Untuk kolom teks yang punya nilai kosong, cukup pakai *accessor* `.str` yang otomatis melewati NaN.<br>
  *`astype(str)` silently turns NaN into the text `"nan"`. For text columns with missing values, the `.str` accessor already skips NaN.*
- Bersihkan teks **sebelum** menghapus duplikat, supaya baris yang hanya berbeda spasi atau kapitalisasi ikut terdeteksi.<br>
  *Clean text **before** dropping duplicates, so rows that only differ in spacing or case are caught too.*
- Validasi hasil dengan `assert` di akhir *pipeline*, jadi kesalahan langsung ketahuan, bukan baru terlihat saat data sudah dipakai.<br>
  *Validate with `assert` at the end of the pipeline, so mistakes show up right away instead of after the data is in use.*
- *Title Case* ikut mengubah singkatan (`COD` → `Cod`). Untuk laporan sungguhan perlu *mapping* koreksi.<br>
  *Title Case also changes acronyms (`COD` → `Cod`). A real report would need a correction mapping.*
- Kolom di luar *scope* (`harga_satuan`, `kota_pembeli`, format `tanggal_transaksi`) masih perlu ditangani jika data ini dipakai lebih lanjut, misalnya di [Project 2](../02-end-to-end-data-pipeline/).<br>
  *Out-of-scope columns (`harga_satuan`, `kota_pembeli`, the `tanggal_transaksi` format) still need work if this data goes further, e.g. in [Project 2](../02-end-to-end-data-pipeline/).*

</div>

---

<div align="center">

<span>&nbsp;</span> &nbsp;·&nbsp; <a href="../">🗂️ Semua Proyek</a> &nbsp;·&nbsp; <a href="../02-end-to-end-data-pipeline/">Project 2 →</a>

</div>
