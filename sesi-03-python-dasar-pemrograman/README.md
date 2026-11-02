<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# 🐍 Sesi 03 — Python I: Dasar Pemrograman

<img src="https://img.shields.io/badge/Sesi-03%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-2%20November%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Senin, 2 November 2026** · 19.15 – 21.15 WIB<br>
*Monday, November 2, 2026 · 7:15 – 9:15 PM (UTC+7)*

Dasar Python: variabel, tipe data, operator, percabangan, perulangan, dan struktur data bawaan (<i>list</i>, <i>dict</i>, <i>tuple</i>, <i>set</i>).<br>
*Python basics: variables, data types, operators, conditionals, loops, and built-in data structures (list, dict, tuple, set).*

## 🧠 Yang Dipelajari · *What I Learned*

Sesi ini dibagi menjadi empat bagian: variabel, tipe data, koleksi, serta percabangan dan perulangan.<br>
*The session was split into four parts: variables, data types, collections, and control flow with loops.*

### 📦 1. Variabel & Aturannya · *Variables & Their Rules*

Variabel adalah wadah bernama untuk menyimpan sebuah nilai. Nama variabel menunjuk ke nilai yang tersimpan di memori, jadi nilainya bisa dipanggil lagi dan diubah kapan saja.<br>
*A variable is a named container for a value. The name points to the value stored in memory, so you can recall it and change it at any time.*<br>
💡 *Analogi:* seperti toples berlabel di dapur. Labelnya "gula", isinya bisa diganti, dan kita cukup menyebut labelnya untuk mengambil isinya.<br>
*Analogy: like a labelled jar in the kitchen. The label says "sugar", the contents can change, and you only need the label to get what's inside.*

Aturan penamaan · *Naming rules*:

- Hanya boleh huruf kecil, huruf kapital, angka, dan *underscore* (`_`).<br>
  *Only lowercase letters, uppercase letters, digits, and underscores (`_`).*
- Tidak boleh diawali angka: `nilai1` valid, `1nilai` tidak.<br>
  *Cannot start with a digit: `nilai1` is valid, `1nilai` is not.*
- *Case sensitive*: `nama` dan `Nama` adalah dua variabel berbeda.<br>
  *Case sensitive: `nama` and `Nama` are two different variables.*
- Tidak boleh ada spasi. Gabungkan kata dengan salah satu gaya berikut:<br>
  *No spaces. Join words using one of these styles:*

| Gaya · *Style* | Contoh · *Example* | Dipakai untuk · *Used for* |
|---|---|---|
| `snake_case` | `total_price` | Variabel dan fungsi di Python (gaya yang dianjurkan PEP 8).<br>*Python variables and functions (the style PEP 8 recommends).* |
| `camelCase` | `totalPrice` | Umum di JavaScript dan Java.<br>*Common in JavaScript and Java.* |
| `PascalCase` | `TotalPrice` | Nama *class* di Python.<br>*Class names in Python.* |

Nama yang jelas membuat kode lebih mudah dibaca. `final_price = total_price - amount_disc` langsung bisa dipahami, sedangkan `c = a - b` tidak.<br>
*Clear names make code easier to read. `final_price = total_price - amount_disc` explains itself; `c = a - b` does not.*

### 🔢 2. Tipe Data · *Data Types*

Python mengenali tipe data dari nilai yang diisikan, tanpa perlu dideklarasikan lebih dulu (*dynamic typing*, sering dikaitkan dengan istilah *duck typing*). Cek tipenya dengan `type()`.<br>
*Python works out the data type from the value you assign, with no declaration needed (dynamic typing, often linked to the term duck typing). Check the type with `type()`.*

| Kelompok · *Group* | Tipe · *Type* | Contoh · *Example* |
|---|---|---|
| **Primitif** · *Primitive* | `int` | `10` |
| | `float` | `90.5` |
| | `str` | `"Andi"` |
| | `bool` | `True`, `False` |
| | `complex` | `3 + 2j` |
| **Non-primitif** · *Non-primitive* | `list` | `[1, 2, 3]` |
| | `tuple` | `(1, 2, 3)` |
| | `set` | `{1, 2, 3}` |
| | `dict` | `{"a": 1, "b": 2}` |

💡 *Analogi:* tipe primitif itu satu barang (satu apel), tipe non-primitif itu wadah berisi banyak barang (keranjang apel).<br>
*Analogy: a primitive type is a single item (one apple); a non-primitive type is a container of many items (a basket of apples).*

### 🗂️ 3. Mengenal Koleksi · *Deep Into Collections*

| Koleksi · *Collection* | Tanda · *Syntax* | Berurutan · *Ordered* | Bisa diubah · *Mutable* | Boleh duplikat · *Duplicates* |
|---|:-:|:-:|:-:|:-:|
| `list` | `[ ]` | ✅ | ✅ | ✅ |
| `tuple` | `( )` | ✅ | ❌ | ✅ |
| `set` | `{ }` | ❌ | ✅ | ❌ |
| `dict` | `{key: value}` | ✅ (sejak Python 3.7) | ✅ | *Key* ❌, *value* ✅ |

#### 📋 List

Kumpulan data yang berurutan, bisa diubah, boleh berisi duplikat, dan menerima tipe apa saja (bahkan campuran). Diakses lewat indeks: `a[0]` elemen pertama, `a[-1]` elemen terakhir.<br>
*An ordered, changeable collection that allows duplicates and accepts any type (even mixed). Access by index: `a[0]` is the first element, `a[-1]` the last.*

Perbedaan `append` dan `extend` · *`append` vs `extend`*:

```python
mylist = [1, 2]
mylist.append([3, 4])   # [1, 2, [3, 4]]  -> list dimasukkan utuh sebagai SATU elemen
mylist = [1, 2]
mylist.extend([3, 4])   # [1, 2, 3, 4]    -> isinya dibongkar satu per satu
```

💡 *Analogi:* `append` itu memasukkan satu kantong belanja ke dalam troli, kantongnya tetap utuh. `extend` itu membongkar kantong lalu menaruh barangnya satu per satu ke troli.<br>
*Analogy: `append` drops a whole shopping bag into the trolley, bag and all. `extend` empties the bag and puts each item into the trolley one by one.*

🎯 **Kapan dipakai · *When to use*:** data yang urutannya penting dan isinya akan sering bertambah atau berubah, misalnya daftar nilai siswa, antrean tugas, atau riwayat chat.<br>
*Data where order matters and the contents grow or change often, such as a list of student scores, a task queue, or chat history.*

#### 🔒 Tuple

Berurutan seperti *list*, tetapi **tidak bisa diubah** setelah dibuat. Masih bisa diakses dengan indeks, dan *list* bisa dikonversi menjadi *tuple* dengan `tuple([1, 2, 3])`.<br>
*Ordered like a list, but **cannot be changed** once created. It can still be accessed by index, and a list can be converted with `tuple([1, 2, 3])`.*

```python
koordinat = (-6.2, 106.8)   # lintang, bujur Jakarta
koordinat[0]                # -6.2
koordinat[0] = 0            # TypeError: tuple tidak bisa diubah
```

💡 *Analogi:* seperti tanggal lahir di KTP. Sudah tercetak dan tidak bisa diganti sembarangan.<br>
*Analogy: like the date of birth on an ID card. It's printed and can't just be changed.*

🎯 **Kapan dipakai · *When to use*:** data tetap yang tidak boleh berubah tanpa sengaja, misalnya koordinat (lintang, bujur), warna RGB `(255, 0, 0)`, atau konfigurasi tetap. *Tuple* juga dipakai untuk mengembalikan beberapa nilai dari fungsi dan bisa menjadi *key* di *dictionary* (*list* tidak bisa).<br>
*Fixed data that shouldn't change by accident, such as coordinates (latitude, longitude), an RGB colour `(255, 0, 0)`, or fixed settings. Tuples are also used to return several values from a function, and can serve as dictionary keys (lists can't).*

#### 🎯 Set

Kumpulan nilai **unik** dan **tidak berurutan**. Duplikat otomatis dibuang, dan karena tidak berurutan, *set* tidak bisa diakses dengan indeks. Urutan saat dicetak juga bisa berbeda dari urutan saat ditulis.<br>
*A collection of **unique**, **unordered** values. Duplicates are dropped automatically, and because there is no order, a set can't be indexed. The printed order may differ from the order you wrote.*

```python
s = {11, 222, 222, 33, 33}   # {11, 222, 33}
s.update([4, 5])             # menambah beberapa elemen sekaligus
s.update("halo")             # string diurai per karakter: 'h', 'a', 'l', 'o'
```

⚠️ `{}` kosong adalah *dict*, bukan *set*. Untuk *set* kosong gunakan `set()`.<br>
*An empty `{}` is a dict, not a set. Use `set()` for an empty set.*

💡 *Analogi:* seperti daftar hadir. Satu nama cukup tercatat sekali, berapa kali pun orangnya absen.<br>
*Analogy: like an attendance list. Each name is recorded once, no matter how many times the person signs in.*

🎯 **Kapan dipakai · *When to use*:** membuang duplikat (misalnya daftar email pelanggan), mengecek keanggotaan dengan cepat (`"andi" in peserta`), dan operasi himpunan seperti irisan `&`, gabungan `|`, atau selisih `-` (misalnya peserta yang ikut sesi 1 **dan** sesi 2).<br>
*Removing duplicates (for example a customer email list), fast membership checks (`"andi" in peserta`), and set operations such as intersection `&`, union `|`, or difference `-` (for example participants who attended session 1 **and** session 2).*

#### 🔑 Dictionary

Menyimpan pasangan *key*–*value*, bentuknya mirip JSON. Data dicari lewat *key*, bukan indeks. *Key* harus unik dan bertipe *immutable* (misalnya `str`, `int`, `tuple`), sedangkan *value* boleh apa saja.<br>
*Stores key–value pairs, much like JSON. You look data up by key, not by index. Keys must be unique and immutable (e.g. `str`, `int`, `tuple`); values can be anything.*

```python
nilai = {"Andi": 80, "Budi": 75}
nilai["Andi"]             # 80
nilai["Dewi"] = 85        # tambah key baru
nilai.update({"Budi": 70})  # ubah value yang sudah ada
dict([("id", 1), ("name", "Andi")])   # {'id': 1, 'name': 'Andi'} dari pasangan tuple
```

💡 *Analogi:* seperti kamus atau buku telepon. Cari namanya (*key*), langsung ketemu nomornya (*value*), tanpa membaca dari halaman pertama.<br>
*Analogy: like a dictionary or a phone book. Look up the name (key) and you get the number (value) straight away, without reading from page one.*

🎯 **Kapan dipakai · *When to use*:** data yang punya label, misalnya profil pengguna `{"nama": ..., "umur": ...}`, konfigurasi aplikasi, hitungan frekuensi kata, atau membaca respons API dalam format JSON. Ini akan sering dipakai nanti saat mengolah respons Azure OpenAI.<br>
*Labelled data, such as a user profile `{"nama": ..., "umur": ...}`, app settings, word frequency counts, or reading JSON API responses. This will come up often later when handling Azure OpenAI responses.*

### 🔀 4. Percabangan & Perulangan · *Control Flow & Loops*

**Percabangan (*conditional statement*)** menentukan baris kode mana yang dijalankan berdasarkan sebuah kondisi, memakai `if`, `elif`, dan `else`. Python membaca dari atas, dan berhenti di kondisi pertama yang bernilai `True`.<br>
***Conditional statements** decide which lines run based on a condition, using `if`, `elif`, and `else`. Python checks from the top and stops at the first condition that is `True`.*

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")   # <- ini yang dijalankan
else:
    print("Grade: C")
```

💡 *Analogi:* seperti persimpangan jalan dengan papan petunjuk. Kalau mau ke bandara belok kiri, kalau ke pusat kota lurus, selain itu belok kanan.<br>
*Analogy: like a junction with signposts. For the airport turn left, for downtown go straight, otherwise turn right.*

Percabangan bisa bersarang dan digabung dengan koleksi. Di latihan, saya memakai *dictionary* untuk mengecek apakah *username* terdaftar (`if username in data`) lalu apakah ia admin.<br>
*Conditions can be nested and combined with collections. In my practice notebook I used a dictionary to check whether a username exists (`if username in data`) and then whether it is an admin.*

**Perulangan (*loop*)** menjalankan blok kode berulang kali.<br>
***Loops** run a block of code repeatedly.*

| Jenis · *Type* | Cara kerja · *How it works* | 💡 Analogi · *Analogy* |
|---|---|---|
| `for` | Mengulang untuk setiap elemen dalam koleksi. `enumerate()` memberikan indeks sekaligus nilainya.<br>*Repeats once per element in a collection. `enumerate()` gives both the index and the value.* | Membagikan rapor ke setiap siswa di daftar kelas, satu per satu.<br>*Handing out a report card to every student on the class list, one by one.* |
| `while` | Terus mengulang selama kondisinya `True`. Pastikan kondisinya suatu saat menjadi `False` (misalnya dengan `count += 1`), atau perulangannya tidak akan berhenti.<br>*Keeps repeating while the condition is `True`. Make sure it eventually becomes `False` (e.g. with `count += 1`), or the loop never ends.* | Terus mengaduk adonan selama masih ada gumpalan.<br>*Keep stirring the batter while there are still lumps.* |

```python
for idx, nama in enumerate(["Andi", "Budi", "Caca"]):
    print(f"Index {idx}: {nama}")

count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
```

## 📝 Tugas · *Assignments*

| # | Tugas · *Assignment* | Berkas · *Files* | Status |
|:-:|---|---|:-:|
| 1 | Latihan mandiri: variabel, tipe data, koleksi, percabangan & perulangan<br>*Self practice: variables, data types, collections, conditionals & loops* | [Coba Sesi 3.ipynb](Coba%20Sesi%203.ipynb) | ✅ |

## 💡 Catatan & Referensi · *Notes & References*

- [Python Tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Tutorial: More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [PEP 8: Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

</div>

---

<div align="center">

<a href="../sesi-02-intro-azure-ai-engineering/">← Sesi 02</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-04-python-fungsi-oop/">Sesi 04 →</a>

</div>
