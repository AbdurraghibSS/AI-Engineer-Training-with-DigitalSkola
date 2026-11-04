<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🧩 Sesi 04 — Python II: Fungsi & OOP

<img src="https://img.shields.io/badge/Sesi-04%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-4%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/> <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Rabu, 4 November 2026** · 19.15 – 21.15 WIB<br>
*Wednesday, November 4, 2026 · 7:15 – 9:15 PM (UTC+7)*

Fungsi, modul, penanganan <i>error</i>, dan pemrograman berorientasi objek (<i>class</i>, <i>inheritance</i>, <i>encapsulation</i>).<br>
*Functions, modules, error handling, and object-oriented programming (classes, inheritance, encapsulation).*

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini membahas cara menyusun kode agar rapi dan bisa dipakai ulang, mulai dari fungsi, lalu OOP (*class*, *instance*, *inheritance*, jenis *method*), sampai *type hinting* dan validasi data dengan Pydantic.<br>
*This session covered how to structure code so it's tidy and reusable: functions first, then OOP (classes, instances, inheritance, method types), and finally type hinting and data validation with Pydantic.*

### 🛠️ 1. Fungsi · *Functions (`def`)*

Fungsi adalah blok kode bernama yang menjalankan satu tugas dan bisa dipanggil berulang kali. Ini penerapan prinsip **DRY** (*Don't Repeat Yourself*): tulis logikanya sekali, panggil di mana saja.<br>
*A function is a named block of code that does one job and can be called again and again. It applies the **DRY** principle (Don't Repeat Yourself): write the logic once, call it anywhere.*

💡 *Analogi:* seperti resep masakan. Bahan-bahannya adalah parameter, langkah memasaknya adalah isi fungsi, dan hidangan jadinya adalah nilai `return`.<br>
*Analogy: like a recipe. The ingredients are the parameters, the cooking steps are the function body, and the finished dish is the `return` value.*

| Bagian · *Part* | Penjelasan · *Explanation* |
|---|---|
| `def` | Kata kunci untuk mendefinisikan fungsi. Nama fungsi memakai `snake_case`.<br>*Keyword that defines a function. Function names use `snake_case`.* |
| Parameter · *Parameter* | Variabel input di definisi fungsi, misalnya `harga` pada `def diskon(harga)`.<br>*The input variable in the definition, e.g. `harga` in `def diskon(harga)`.* |
| Argumen · *Argument* | Nilai yang dikirim saat memanggil fungsi, misalnya `100000` pada `diskon(100000)`.<br>*The value passed when calling it, e.g. `100000` in `diskon(100000)`.* |
| `return` | Mengembalikan hasil. Tanpa `return`, fungsi otomatis mengembalikan `None`.<br>*Sends a result back. Without `return`, a function returns `None` automatically.* |

```python
def sapa(nama, waktu="pagi"):          # waktu punya nilai default
    return f"Selamat {waktu}, {nama}!"

sapa("Andi")                           # 'Selamat pagi, Andi!'
sapa(waktu="malam", nama="Budi")       # keyword argument, urutan bebas

def statistik(nilai):
    return min(nilai), max(nilai)      # beberapa nilai -> dikemas jadi tuple

terendah, tertinggi = statistik([80, 75, 90])
```

Fitur tambahan yang sering muncul · *Other features that come up often*:

- `*args` menampung banyak argumen posisi sebagai *tuple*, `**kwargs` menampung banyak argumen bernama sebagai *dict*.<br>
  *`*args` collects extra positional arguments as a tuple; `**kwargs` collects extra named arguments as a dict.*
- `lambda` adalah fungsi singkat satu baris, misalnya `sorted(data, key=lambda x: x[1])`.<br>
  *`lambda` is a short one-line function, e.g. `sorted(data, key=lambda x: x[1])`.*

⚠️ `print()` hanya menampilkan ke layar, sedangkan `return` mengirim nilai yang bisa disimpan ke variabel dan dipakai lagi.<br>
*`print()` only shows something on screen; `return` hands back a value you can store in a variable and reuse.*

### 🏗️ 2. Class & Instance

**OOP (*Object-Oriented Programming*)** menyusun kode di sekitar objek, yaitu gabungan **data** (atribut) dan **perilaku** (*method*).<br>
***OOP (Object-Oriented Programming)** organises code around objects, which bundle **data** (attributes) and **behaviour** (methods).*

- **Class**: cetakan (*blueprint*) yang mendefinisikan atribut dan *method*.<br>
  *Class: the blueprint that defines attributes and methods.*
- **Instance**: objek nyata yang dibuat dari *class*. Satu *class* bisa menghasilkan banyak *instance* dengan datanya masing-masing.<br>
  *Instance: a real object built from the class. One class can produce many instances, each with its own data.*
- **`__init__`** (*constructor*): *method* khusus yang otomatis jalan saat *instance* dibuat, untuk mengisi atribut awal.<br>
  *`__init__` (constructor): a special method that runs automatically when an instance is created, to set its starting attributes.*
- **`self`**: merujuk ke *instance* itu sendiri, sehingga setiap objek mengakses datanya sendiri.<br>
  *`self`: refers to the instance itself, so each object works with its own data.*

💡 *Analogi:* *class* itu cetakan kue, *instance* itu kue-kuenya. Cetakannya satu, kuenya bisa banyak, dan topping tiap kue boleh berbeda.<br>
*Analogy: a class is a cookie cutter and instances are the cookies. One cutter, many cookies, and each cookie can have a different topping.*

```python
class Rekening:
    bank = "Bank Nusantara"            # class attribute: dipakai bersama semua instance

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik         # instance attribute: milik tiap objek
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah

rek_andi = Rekening("Andi", 100000)
rek_budi = Rekening("Budi")
rek_andi.setor(50000)                  # saldo Andi 150000, saldo Budi tetap 0
```

| Atribut · *Attribute* | Disimpan di · *Stored on* | Contoh · *Example* |
|---|---|---|
| *Class attribute* | *Class*, sama untuk semua *instance*.<br>*The class, shared by every instance.* | `Rekening.bank` |
| *Instance attribute* | Masing-masing objek (dibuat lewat `self.` di `__init__`).<br>*Each object (set via `self.` in `__init__`).* | `rek_andi.saldo` |

🎯 **Kapan dipakai · *When to use*:** saat ada data dan aksi yang selalu berjalan bersama, misalnya akun pengguna (data + login/logout), sesi chat (riwayat + kirim pesan), atau klien API (konfigurasi + panggil *endpoint*).<br>
*When some data and its actions always go together, such as a user account (data + login/logout), a chat session (history + send message), or an API client (settings + call endpoint).*

### 🧬 3. Inheritance & Jenis Method · *Inheritance & Method Types*

**Inheritance (pewarisan)** membuat *child class* mewarisi atribut dan *method* dari *parent class*. *Child class* bisa menambah hal baru atau **menimpa** (*override*) *method* milik *parent*. `super()` dipakai untuk memanggil versi *parent*, biasanya `super().__init__(...)`.<br>
***Inheritance** lets a child class take on the attributes and methods of a parent class. The child can add new things or **override** the parent's methods. `super()` calls the parent's version, usually `super().__init__(...)`.*

```python
class Notifikasi:
    def __init__(self, penerima):
        self.penerima = penerima
    def kirim(self, pesan):
        return f"[UMUM] {self.penerima}: {pesan}"

class NotifikasiEmail(Notifikasi):
    def __init__(self, penerima, subjek):
        super().__init__(penerima)     # pakai __init__ milik parent
        self.subjek = subjek
    def kirim(self, pesan):            # override
        return f"[EMAIL] {self.penerima} | {self.subjek}: {pesan}"
```

💡 *Analogi:* seperti anak yang mewarisi rumah orang tuanya. Rumahnya sudah ada, tinggal ditambah kamar atau direnovasi sesuai kebutuhan, tanpa membangun dari nol.<br>
*Analogy: like a child inheriting their parents' house. The house is already there; you add a room or renovate what you need instead of building from scratch.*

Karena semua turunan punya `kirim()`, kita bisa memanggil `notif.kirim(...)` dalam satu *loop* tanpa peduli jenisnya. Konsep ini disebut **polymorphism**.<br>
*Because every subclass has `kirim()`, we can call `notif.kirim(...)` in one loop without caring which type it is. This is called **polymorphism**.*

Tiga jenis *method* · *Three method types*:

| Jenis · *Type* | Parameter pertama · *First parameter* | Fungsi · *Purpose* |
|---|:-:|---|
| *Instance method* | `self` | Bekerja dengan data milik objek, misalnya `rek.setor(5000)`.<br>*Works with the object's own data, e.g. `rek.setor(5000)`.* |
| `@classmethod` | `cls` | Bekerja di level *class*: mengelola *class attribute* atau menjadi *constructor* alternatif, misalnya `Suhu.dari_fahrenheit(50)`.<br>*Works at class level: manages class attributes or acts as an alternative constructor, e.g. `Suhu.dari_fahrenheit(50)`.* |
| `@staticmethod` | — | Fungsi biasa yang ditaruh di dalam *class* karena masih berkaitan, misalnya validasi `Suhu.wajar(60)`.<br>*A plain function kept inside the class because it's related, e.g. a check like `Suhu.wajar(60)`.* |

🎯 **Kapan dipakai · *When to use*:** *inheritance* cocok untuk beberapa jenis objek yang mirip tetapi berbeda di detail, misalnya kanal notifikasi (email, WhatsApp, SMS) atau beberapa penyedia LLM dengan antarmuka yang sama.<br>
*Inheritance suits several similar kinds of objects that differ in the details, such as notification channels (email, WhatsApp, SMS) or several LLM providers sharing one interface.*

### 🏷️ 4. Type Hinting

*Type hint* adalah anotasi tipe data pada variabel, parameter, dan nilai *return*. Kode jadi lebih mudah dibaca, dan IDE bisa memberi *autocomplete* serta peringatan lebih awal.<br>
*Type hints are type annotations on variables, parameters, and return values. They make code easier to read and let the IDE give autocomplete and early warnings.*

```python
def cari_suhu(kota: str, data: dict[str, float]) -> float | None:
    return data.get(kota)              # float, atau None kalau kota tidak ada

curah_hujan: list[float] = [12.5, 0.0, 30.2]
```

⚠️ Python **tidak** memeriksa *type hint* saat program berjalan. `kali_dua("ha")` pada fungsi `def kali_dua(x: int) -> int` tetap jalan dan menghasilkan `'haha'`. Untuk pengecekan yang benar-benar ditegakkan, kita butuh Pydantic.<br>
*Python does **not** check type hints at runtime. Calling `kali_dua("ha")` on `def kali_dua(x: int) -> int` still runs and returns `'haha'`. To actually enforce types, we need Pydantic.*

💡 *Analogi:* seperti label "Gula" di toples. Label membantu orang tahu isinya, tapi tidak mencegah orang memasukkan garam.<br>
*Analogy: like a "Sugar" label on a jar. It tells people what should be inside, but it doesn't stop anyone from pouring in salt.*

### ✅ 5. Pydantic

Pydantic adalah *library* untuk mendefinisikan skema data dengan *type hint*, lalu **memvalidasinya saat *runtime***. Caranya dengan membuat *class* turunan `BaseModel`.<br>
*Pydantic is a library that defines data schemas with type hints and **validates them at runtime**. You create a class that inherits from `BaseModel`.*

```python
from pydantic import BaseModel, Field, ValidationError

class PrakiraanCuaca(BaseModel):
    kota: str
    suhu: float
    kelembapan: int = Field(ge=0, le=100)   # aturan tambahan: 0–100
    hujan: bool = False                     # nilai default

PrakiraanCuaca(kota="Semarang", suhu="31.5", kelembapan=78)   # "31.5" -> 31.5 (coercion)
PrakiraanCuaca(kota="Bogor", suhu="panas", kelembapan=130)    # ValidationError
```

Hal penting · *Key points*:

- **Coercion**: nilai yang masih bisa dikonversi akan dikonversi otomatis, misalnya `"31.5"` menjadi `31.5`.<br>
  *Coercion: values that can be converted are converted automatically, e.g. `"31.5"` becomes `31.5`.*
- **`Field(...)`** menambah aturan seperti `ge`/`le` (≥/≤) dan `gt`/`lt` (>/<).<br>
  *`Field(...)` adds rules such as `ge`/`le` (≥/≤) and `gt`/`lt` (>/<).*
- **`ValidationError`** menyebutkan *field* mana yang salah dan alasannya.<br>
  *`ValidationError` names each invalid field and why it failed.*
- **`model_dump()`** / **`model_dump_json()`** mengubah model menjadi *dict*/JSON, dan **`model_validate_json()`** membaca langsung dari *string* JSON.<br>
  *`model_dump()` / `model_dump_json()` turn a model into a dict/JSON, and `model_validate_json()` reads straight from a JSON string.*
- Model bisa bersarang (*nested*) dan memakai `Literal[...]` untuk membatasi pilihan nilai.<br>
  *Models can be nested and can use `Literal[...]` to restrict allowed values.*

💡 *Analogi:* seperti petugas pemeriksa di pintu masuk. Setiap data dicek kelengkapan dan formatnya. Yang sedikit keliru dirapikan, yang salah ditolak beserta alasannya.<br>
*Analogy: like a checkpoint officer at the gate. Every piece of data gets checked for completeness and format. Minor slips are tidied up; anything wrong is turned away with a reason.*

🎯 **Kapan dipakai · *When to use*:** memvalidasi **output terstruktur dari LLM**, *request*/*response* API (FastAPI dibangun di atas Pydantic), dan file konfigurasi. Di latihan, saya membuat skema `PeringatanCuaca` untuk mengecek JSON jawaban LLM. Jika LLM mengarang nilai di luar pilihan (misalnya level "bahaya"), kesalahannya langsung ketahuan.<br>
*Validating **structured LLM output**, API requests/responses (FastAPI is built on Pydantic), and config files. In my practice notebook I built a `PeringatanCuaca` schema to check an LLM's JSON answer. If the LLM invents a value outside the allowed options (like level "bahaya"), the error is caught right away.*

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Latihan mandiri: fungsi, *class* & *instance*, *inheritance* & jenis *method*, *type hinting*, Pydantic, serta studi kasus validasi output LLM<br>*Self practice: functions, classes & instances, inheritance & method types, type hinting, Pydantic, plus an LLM-output validation case study* | [Latihan.ipynb](Latihan.ipynb) | ✅ |

## 💡 Catatan & Referensi · *Notes & References*

- [Python Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Tutorial: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Docs: typing (Type Hints)](https://docs.python.org/3/library/typing.html)
- [Pydantic Docs: Models](https://docs.pydantic.dev/latest/concepts/models/)

</div>

---

<div align="center">

<a href="../sesi-03-python-dasar-pemrograman/">← Sesi 03</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-05-git-github/">Sesi 05 →</a>

</div>
