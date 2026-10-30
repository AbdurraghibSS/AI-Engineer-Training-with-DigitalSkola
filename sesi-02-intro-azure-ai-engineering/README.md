<div align="center">

<sub><a href="../">🏠 Beranda · <i>Home</i></a></sub>

# ☁️ Sesi 02 — Intro to Azure AI Engineering

<img src="https://img.shields.io/badge/Sesi-02%20%2F%2023-1B2A6B?style=for-the-badge" alt="Sesi"/> <img src="https://img.shields.io/badge/Tanggal-30%20Oktober%202026-0078D4?style=for-the-badge" alt="Tanggal"/> <img src="https://img.shields.io/badge/Status-Selesai%20%C2%B7%20Done-2EA043?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik01LjQ4MyAyMS4zSDI0TDE0LjAyNSA0LjAxM2wtMy4wMzggOC4zNDcgNS44MzYgNi45MzhMNS40ODMgMjEuM3pNMTMuMjMgMi43TDYuMTA1IDguNjc3IDAgMTkuMjUzaDUuNTA1di4wMTRMMTMuMjMgMi43eiIvPjwvc3ZnPg%3D%3D" alt="Microsoft Azure"/> <img src="https://img.shields.io/badge/Azure%20AI%20Foundry-0078D4?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik01LjQ4MyAyMS4zSDI0TDE0LjAyNSA0LjAxM2wtMy4wMzggOC4zNDcgNS44MzYgNi45MzhMNS40ODMgMjEuM3pNMTMuMjMgMi43TDYuMTA1IDguNjc3IDAgMTkuMjUzaDUuNTA1di4wMTRMMTMuMjMgMi43eiIvPjwvc3ZnPg%3D%3D" alt="Azure AI Foundry"/>

<sub>🐍 Fase 1 · Fondasi Python, Data & Azure · <i>Phase 1 · Python, Data & Azure Foundations</i></sub>

</div>

---

<div align="justify">

## 📌 Tentang Sesi · *About This Session*

📅 **Jumat, 30 Oktober 2026** · 19.15 – 21.15 WIB<br>
*Friday, October 30, 2026 · 7:15 – 9:15 PM (UTC+7)*

Gambaran peran AI Engineer dan layanan AI di Azure: Azure OpenAI, AI Foundry, AI Search, dan AI Services.<br>
*An overview of the AI Engineer role and Azure's AI services: Azure OpenAI, AI Foundry, AI Search, and AI Services.*

## 🧠 Yang Dipelajari · *What I Learned*

### 🤖 Cara Kerja Generative AI · *How Generative AI Works*

- **Menebak kata berikutnya.** Pada dasarnya model generatif memprediksi *token* (potongan kata) berikutnya, satu per satu, berdasarkan konteks yang diberikan. Masukannya disebut *prompt*, keluarannya disebut *response*.<br>
  *Predicting the next word. At its core, a generative model predicts the next token (a piece of a word), one at a time, based on the context it is given. The input is called the prompt and the output is called the response.*<br>
  💡 *Analogi:* seperti fitur *autocomplete* di keyboard HP, tetapi jauh lebih pintar karena membaca seluruh kalimat dan paragraf sebelumnya, bukan hanya satu kata terakhir.<br>
  *Analogy: like your phone keyboard's autocomplete, only far smarter, because it reads the whole sentence and paragraph before it, not just the last word.*
- **Embedding.** Sebelum diproses, *prompt* diubah menjadi deretan angka (*vector*). Kata yang maknanya mirip punya angka yang berdekatan.<br>
  *Embedding. Before processing, the prompt is turned into a list of numbers (a vector). Words with similar meanings end up with numbers close to each other.*<br>
  💡 *Analogi:* seperti memberi setiap kata koordinat di peta. "Kucing" dan "anjing" tinggal di kompleks yang sama, sedangkan "kucing" dan "kulkas" berjauhan.<br>
  *Analogy: like giving every word coordinates on a map. "Cat" and "dog" live in the same neighbourhood, while "cat" and "fridge" are far apart.*
- **Positional encoding.** Model juga diberi tahu posisi tiap token, supaya urutan kata ikut diperhitungkan dan kalimatnya masuk akal.<br>
  *Positional encoding. The model is also told the position of each token, so word order is taken into account and the sentence makes sense.*<br>
  💡 *Analogi:* seperti nomor kursi di bioskop. Kata-katanya sama, tetapi "anjing menggigit orang" dan "orang menggigit anjing" punya arti yang sangat berbeda.<br>
  *Analogy: like seat numbers in a cinema. The words are the same, but "dog bites man" and "man bites dog" mean very different things.*
- **Attention.** Saat menebak token berikutnya, model menimbang token-token masukan mana yang paling relevan.<br>
  *Attention. When predicting the next token, the model weighs which input tokens matter most.*<br>
  💡 *Analogi:* seperti stabilo saat membaca. Untuk menjawab "Budi pergi ke pasar, lalu **dia** membeli apel", model menandai bahwa "dia" merujuk ke "Budi".<br>
  *Analogy: like a highlighter while reading. To make sense of "Budi went to the market, then **he** bought apples", the model marks that "he" refers to "Budi".*

### 🎲 Memilih Token Keluaran · *Choosing the Output Token*

Model menghasilkan daftar peluang untuk setiap kemungkinan token berikutnya. Cara memilih dari daftar itu menentukan seberapa kaku atau kreatif jawabannya.<br>
*The model produces a probability for every possible next token. How we pick from that list decides how rigid or creative the answer is.*

| Metode · *Method* | Cara kerja · *How it works* | 💡 Analogi · *Analogy* |
|---|---|---|
| **Greedy search** | Selalu mengambil token dengan peluang tertinggi. Hasilnya deterministik (selalu sama) dan kaku.<br>*Always picks the most likely token. The result is deterministic (always the same) and rigid.* | Selalu memesan menu terlaris di restoran. Aman, tetapi tidak pernah mencoba yang baru.<br>*Always ordering the best-seller at a restaurant. Safe, but you never try anything new.* |
| **Temperature** | Mengatur tingkat keacakan. Nilai 0 berarti deterministik, makin tinggi makin kreatif. Umumnya 0–1 (sebagian layanan, termasuk Azure OpenAI, mengizinkan sampai 2).<br>*Controls randomness. 0 is deterministic; higher is more creative. Usually 0–1 (some services, including Azure OpenAI, allow up to 2).* | Kenop "keberanian" koki. Rendah: resep persis seperti buku. Tinggi: koki mulai berimprovisasi.<br>*A chef's "boldness" knob. Low: follows the recipe exactly. High: the chef starts improvising.* |
| **Top-K** | Hanya mempertimbangkan K token dengan peluang tertinggi, lalu memilih secara acak di antara mereka.<br>*Only considers the K most likely tokens, then picks randomly among them.* | Mengambil undian dari 5 finalis teratas, bukan dari semua peserta.<br>*Drawing a winner from the top 5 finalists instead of every entrant.* |
| **Top-P** | Mengambil token teratas sampai akumulasi peluangnya mencapai P (misalnya 90%), lalu memilih secara acak di antara mereka. Jumlah kandidatnya bisa berubah-ubah.<br>*Takes the top tokens until their combined probability reaches P (e.g. 90%), then picks randomly among them. The number of candidates can vary.* | Mengisi keranjang belanja sampai anggaran habis. Kadang muat 2 barang mahal, kadang 10 barang murah.<br>*Filling a basket until the budget runs out. Sometimes that's 2 pricey items, sometimes 10 cheap ones.* |

### ⚖️ Responsible AI

Enam prinsip yang perlu dipegang saat membangun solusi AI:<br>
*Six principles to uphold when building AI solutions:*

| Prinsip · *Principle* | Artinya · *Meaning* | 💡 Analogi · *Analogy* |
|---|---|---|
| **Fairness** | Tidak bias atau merugikan individu maupun kelompok tertentu.<br>*No bias against, or harm to, any person or group.* | Wasit yang tidak memihak tim mana pun.<br>*A referee who doesn't favour either team.* |
| **Inclusiveness** | Bisa dipakai oleh siapa saja, termasuk penyandang disabilitas.<br>*Usable by everyone, including people with disabilities.* | Gedung yang punya tangga sekaligus *ramp* kursi roda.<br>*A building with both stairs and a wheelchair ramp.* |
| **Reliability & safety** | Berjalan sesuai fungsinya dan tetap aman di kondisi tak terduga.<br>*Works as intended and stays safe in unexpected conditions.* | Rem mobil yang harus berfungsi, hujan ataupun panas.<br>*Car brakes that must work, rain or shine.* |
| **Privacy & security** | Lindungi data. Samarkan (*mask*) data pribadi kalau memakai data asli.<br>*Protect data. Mask personal data when working with real records.* | Dokter yang menjaga rahasia rekam medis pasien.<br>*A doctor keeping a patient's medical records confidential.* |
| **Transparency** | Jelas data dipakai untuk apa dan sampai mana batas kemampuannya.<br>*Clear about what the data is used for and where the system's limits are.* | Label komposisi di kemasan makanan.<br>*The ingredients label on food packaging.* |
| **Accountability** | Pembuatnya bertanggung jawab atas dampak sistem yang dibuat.<br>*The builders are answerable for the system's impact.* | Arsitek yang tetap bertanggung jawab atas bangunan rancangannya.<br>*An architect who remains responsible for the building they designed.* |

### 🧩 Kemampuan AI · *AI Capabilities*

- **Agentic AI.** AI yang tidak hanya menghasilkan teks, tetapi juga bisa merencanakan dan menjalankan aksi memakai *tools*, misalnya *coding agent*.<br>
  *Agentic AI. AI that doesn't just generate text but can also plan and take actions using tools, such as a coding agent.*<br>
  💡 *Analogi:* AI generatif biasa itu konsultan yang memberi saran. *Agentic AI* itu asisten yang langsung mengerjakannya.<br>
  *Analogy: plain generative AI is a consultant who gives advice; agentic AI is an assistant who actually does the work.*
- **Natural Language Processing (NLP).** Memahami bahasa manusia sehari-hari.<br>
  *Understanding everyday human language.*
- **Speech.** Mengubah suara menjadi teks dan teks menjadi suara.<br>
  *Turning speech into text and text into speech.*
- **Computer vision.** Menganalisis gambar dan video.<br>
  *Analysing images and video.*
- **Information retrieval.** Mencari informasi yang relevan dari sumber data, misalnya dengan RAG (*Retrieval-Augmented Generation*).<br>
  *Finding relevant information from data sources, for example with RAG (Retrieval-Augmented Generation).*<br>
  💡 *Analogi:* ujian *open book*. Model tidak perlu hafal semuanya, cukup mencari di buku yang tepat sebelum menjawab.<br>
  *Analogy: an open-book exam. The model doesn't need to memorise everything; it just looks things up in the right book before answering.*

### 🎯 Memilih Model · *Choosing a Model*

Pertimbangkan empat hal ini:<br>
*Weigh these four things:*

1. **Use case.** Kebutuhannya apa: chat, ringkasan, kode, gambar?<br>
   *What is it for: chat, summarising, code, images?*
2. **Context window.** Seberapa panjang teks yang bisa diproses sekaligus.<br>
   *How much text the model can take in at once.*
3. **Ukuran model vs latensi vs biaya.** Model yang lebih besar umumnya lebih pintar, tetapi lebih lambat dan lebih mahal.<br>
   *Model size vs latency vs cost. Bigger models are usually smarter but slower and pricier.*
4. **Privasi & keamanan data.** Di mana data diproses dan siapa yang bisa mengaksesnya.<br>
   *Data privacy & security. Where the data is processed and who can access it.*

💡 *Analogi:* seperti memilih kendaraan. Tidak perlu truk untuk mengantar satu surat, dan motor tidak cukup untuk pindahan rumah.<br>
*Analogy: like choosing a vehicle. You don't need a truck to deliver one letter, and a motorbike won't do for moving house.*

### 🛠️ Persiapan Tools · *Tool Setup*

| Tool | Kegunaan · *Purpose* |
|---|---|
| **Git & GitHub** | *Version control* dan tempat menyimpan kode.<br>*Version control and a home for the code.* |
| **VS Code** | *Code editor* utama.<br>*Main code editor.* |
| **Google Colab** | *Notebook* Python di *cloud*, tanpa instalasi.<br>*Cloud Python notebooks, no install needed.* |
| **Azure CLI** | Dibutuhkan untuk memakai Azure AI Foundry dan persiapan sertifikasi.<br>*Needed for Azure AI Foundry and certification prep.* |

## 📝 Tugas & Quiz · *Assignments & Quiz*

</div>

> [!TIP]
> Tidak ada tugas di sesi ini. Ada quiz berisi 10 soal pilihan ganda.<br>
> *No assignment for this session. There was a 10-question multiple-choice quiz.*

<div align="justify">

## 💡 Catatan & Referensi · *Notes & References*

- [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)
- [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

</div>

---

<div align="center">

<a href="../sesi-01-get-to-know-digital-skola/">← Sesi 01</a> &nbsp;·&nbsp; <a href="../">🏠 Beranda</a> &nbsp;·&nbsp; <a href="../sesi-03-python-dasar-pemrograman/">Sesi 03 →</a>

</div>
