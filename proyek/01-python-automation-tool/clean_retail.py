from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

INPUT_CANDIDATES = ["dataset_retail_homework.csv", "dataset_retail.csv"]
OUTPUT_FILE = "dataset_retail_clean.csv"

KOLOM_TEKS = ["nama_produk", "kategori", "metode_bayar", "kota_pembeli"]


class DataCleaner:
    
    # Inisialisasi class dan membaca file CSV.
    def __init__(self, file_path: str):
        self.file_path: str = str(file_path)
        self.df: pd.DataFrame = pd.read_csv(file_path)
        print(f"✓ Berhasil membaca file '{Path(file_path).name}' dengan {len(self.df)} baris.")

    # Menghilangkan spasi berlebih dan merapikan format teks (Title Case).
    def bersihkan_teks(self, daftar_kolom: list[str]) -> "DataCleaner":
        for col in daftar_kolom:
            if col in self.df.columns:
                self.df[col] = self.df[col].str.strip().str.title()
            else:
                print(f"⚠ Kolom '{col}' tidak ditemukan, dilewati.")
        print(f"✓ Kolom teks {daftar_kolom} telah dibersihkan.")
        return self

    # Menghapus seluruh baris yang terduplikasi persis.
    def hapus_duplikat(self) -> "DataCleaner":
        jumlah_awal = len(self.df)
        self.df = self.df.drop_duplicates().reset_index(drop=True)
        jumlah_terhapus = jumlah_awal - len(self.df)
        print(f"✓ Berhasil menghapus {jumlah_terhapus} baris duplikat.")
        return self

    # Mengisi nilai yang hilang/kosong pada kolom numerik.
    def isi_nilai_kosong(self, kolom_angka: str, nilai_default: float = 0.0) -> "DataCleaner":
        if kolom_angka in self.df.columns:
            jumlah_kosong = self.df[kolom_angka].isna().sum()
            self.df[kolom_angka] = self.df[kolom_angka].fillna(nilai_default)
            if (self.df[kolom_angka] % 1 == 0).all():
                self.df[kolom_angka] = self.df[kolom_angka].astype(int)
            print(
                f"✓ {jumlah_kosong} nilai kosong pada kolom '{kolom_angka}' "
                f"diisi dengan {nilai_default}."
            )
        return self

    # Menyimpan dataframe yang sudah bersih ke file CSV baru.
    def simpan_hasil(self, output_path: str) -> "DataCleaner":
        self.df.to_csv(output_path, index=False)
        print(f"✓ Data bersih berhasil disimpan ke: '{Path(output_path).name}' ({len(self.df)} baris).")
        return self

# Mengembalikan path dataset mentah pertama yang ditemukan di folder script.
def cari_file_input() -> Path:
    for nama in INPUT_CANDIDATES:
        path = BASE_DIR / nama
        if path.exists():
            return path
    raise FileNotFoundError(
        f"File data mentah tidak ditemukan. Letakkan salah satu dari {INPUT_CANDIDATES} "
        f"di folder {BASE_DIR}"
    )


if __name__ == "__main__":
    print("=== PIPELINE OTOMATISASI DATA RETAIL ===")
    cleaner = DataCleaner(cari_file_input())
    cleaner.bersihkan_teks(KOLOM_TEKS) \
           .hapus_duplikat() \
           .isi_nilai_kosong("jumlah_beli", nilai_default=0) \
           .simpan_hasil(BASE_DIR / OUTPUT_FILE)
    print("=== PROSES SELESAI ===")
