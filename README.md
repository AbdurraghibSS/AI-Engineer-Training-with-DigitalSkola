# AI Engineer Training — Digital Skola × Microsoft Azure

Catatan belajar, tugas, dan proyek selama pelatihan **AI Engineer** di Digital Skola yang berfokus pada ekosistem Microsoft Azure. Pelatihan berlangsung **23 sesi** (28 Oktober – 23 Desember 2026) dan ditutup dengan *mock exam* sertifikasi **AI-901**.

*Learning notes, assignments, and projects from the **AI Engineer** training at Digital Skola, focused on the Microsoft Azure ecosystem. The program runs for **23 sessions** (October 28 – December 23, 2026) and ends with a mock exam for the **AI-901** certification.*

---

## Daftar Isi · *Table of Contents*

- [Struktur Repositori · *Repository Structure*](#struktur-repositori--repository-structure)
- [Jadwal Ringkas · *Schedule at a Glance*](#jadwal-ringkas--schedule-at-a-glance)
- [Bagian 1 — Fondasi Python, Data & Azure · *Part 1 — Python, Data & Azure Foundations*](#bagian-1--fondasi-python-data--azure--part-1--python-data--azure-foundations)
- [Bagian 2 — LLM, RAG & Agentic AI · *Part 2 — LLM, RAG & Agentic AI*](#bagian-2--llm-rag--agentic-ai--part-2--llm-rag--agentic-ai)
- [Bagian 3 — Deployment, MLOps & Final Project · *Part 3 — Deployment, MLOps & Final Project*](#bagian-3--deployment-mlops--final-project--part-3--deployment-mlops--final-project)
- [Proyek · *Projects*](#proyek--projects)

---

## Struktur Repositori · *Repository Structure*

Setiap sesi punya foldernya sendiri untuk menyimpan catatan, *notebook*, dan tugas.

*Each session has its own folder for notes, notebooks, and assignments.*

```
.
├── README.md
├── sesi-01-get-to-know-digital-skola/
├── sesi-02-intro-azure-ai-engineering/
├── ...
└── sesi-23-final-project-showcase/
```

Isi yang disarankan untuk tiap folder · *Suggested contents for each folder*:

| Berkas · *File* | Isi · *Contents* |
|---|---|
| `README.md` | Ringkasan materi sesi · *Session summary* |
| `notebooks/` | *Jupyter notebook* latihan · *Practice notebooks* |
| `tugas/` | Tugas dan jawabannya · *Assignments and solutions* |
| `assets/` | Gambar, diagram, tangkapan layar · *Images, diagrams, screenshots* |

---

## Jadwal Ringkas · *Schedule at a Glance*

Semua sesi berlangsung pukul **19.15 – 21.15 WIB**.

*All sessions run from **7:15 PM to 9:15 PM (WIB, UTC+7)**.*

Status: ✅ selesai · *done* — 🔄 berlangsung · *in progress* — ⏳ akan datang · *upcoming*

| # | Tanggal · *Date* | Topik · *Topic* | Status | Folder |
|:-:|---|---|:-:|---|
| 1 | Rab, 28 Okt 2026 | Get to Know Digital Skola | 🔄 | [sesi-01](sesi-01-get-to-know-digital-skola/) |
| 2 | Jum, 30 Okt 2026 | Intro to Azure AI Engineering | ⏳ | [sesi-02](sesi-02-intro-azure-ai-engineering/) |
| 3 | Sen, 2 Nov 2026 | Python I: Dasar Pemrograman | ⏳ | [sesi-03](sesi-03-python-dasar-pemrograman/) |
| 4 | Rab, 4 Nov 2026 | Python II: Fungsi & OOP | ⏳ | [sesi-04](sesi-04-python-fungsi-oop/) |
| 5 | Jum, 6 Nov 2026 | Git & GitHub | ⏳ | [sesi-05](sesi-05-git-github/) |
| 6 | Sen, 9 Nov 2026 | Data Wrangling dengan Pandas | ⏳ | [sesi-06](sesi-06-data-wrangling-pandas/) |
| 7 | Rab, 11 Nov 2026 | **PROJECT 1:** Python Automation Tool | ⏳ | [sesi-07](sesi-07-project-1-python-automation-tool/) |
| 8 | Jum, 13 Nov 2026 | SQL for AI | ⏳ | [sesi-08](sesi-08-sql-for-ai/) |
| 9 | Sen, 16 Nov 2026 | SQL Scraping & Data Cleaning Pipeline | ⏳ | [sesi-09](sesi-09-sql-scraping-data-cleaning-pipeline/) |
| 10 | Rab, 18 Nov 2026 | API & FastAPI untuk AI | ⏳ | [sesi-10](sesi-10-api-fastapi-untuk-ai/) |
| 11 | Jum, 20 Nov 2026 | **PROJECT 2:** End-to-End Data Pipeline | ⏳ | [sesi-11](sesi-11-project-2-end-to-end-data-pipeline/) |
| 12 | Sen, 23 Nov 2026 | NLP & LLM di Azure OpenAI | ⏳ | [sesi-12](sesi-12-nlp-llm-azure-openai/) |
| 13 | Rab, 25 Nov 2026 | Azure AI Search & Semantic Search | ⏳ | [sesi-13](sesi-13-azure-ai-search-semantic-search/) |
| 14 | Jum, 27 Nov 2026 | RAG di Azure AI Foundry (LangChain) | ⏳ | [sesi-14](sesi-14-rag-azure-ai-foundry-langchain/) |
| 15 | Sen, 30 Nov 2026 | **PROJECT 3:** AI-Powered Chatbot (RAG) di Azure | ⏳ | [sesi-15](sesi-15-project-3-ai-chatbot-rag-azure/) |
| 16 | Rab, 2 Des 2026 | Speech & Information Extraction (Content Understanding) | ⏳ | [sesi-16](sesi-16-speech-information-extraction/) |
| 17 | Jum, 4 Des 2026 | Agentic AI + Azure AI Foundry Agent Service | ⏳ | [sesi-17](sesi-17-agentic-ai-foundry-agent-service/) |
| 18 | Sen, 7 Des 2026 | Docker untuk AI + Azure Container Registry | ⏳ | [sesi-18](sesi-18-docker-azure-container-registry/) |
| 19 | Rab, 9 Des 2026 | Azure Cloud Deployment | ⏳ | [sesi-19](sesi-19-azure-cloud-deployment/) |
| 20 | Jum, 11 Des 2026 | **PROJECT 4:** Azure-Based AI Infrastructure | ⏳ | [sesi-20](sesi-20-project-4-azure-ai-infrastructure/) |
| 21 | Sen, 14 Des 2026 | MLOps di Azure & AI Security | ⏳ | [sesi-21](sesi-21-mlops-azure-ai-security/) |
| 22 | Rab, 16 Des 2026 | **Final Project:** Integrasi + Mock Exam AI-901 | ⏳ | [sesi-22](sesi-22-final-project-mock-exam-ai-901/) |
| 23 | Rab, 23 Des 2026 | **Final Project Showcase** | ⏳ | [sesi-23](sesi-23-final-project-showcase/) |

---

## Bagian 1 — Fondasi Python, Data & Azure · *Part 1 — Python, Data & Azure Foundations*

### Sesi 1 — Get to Know Digital Skola
📅 Rabu, 28 Oktober 2026 · *Wednesday, October 28, 2026*

Perkenalan program, mentor, sesama peserta, alur belajar 23 sesi, serta aturan tugas dan penilaian.

*Introduction to the program, mentors, and fellow participants, the 23-session learning path, and the rules for assignments and grading.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-01-get-to-know-digital-skola](sesi-01-get-to-know-digital-skola/)

### Sesi 2 — Intro to Azure AI Engineering
📅 Jumat, 30 Oktober 2026 · *Friday, October 30, 2026*

Gambaran peran AI Engineer dan layanan AI di Azure: Azure OpenAI, AI Foundry, AI Search, dan AI Services.

*An overview of the AI Engineer role and Azure's AI services: Azure OpenAI, AI Foundry, AI Search, and AI Services.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-02-intro-azure-ai-engineering](sesi-02-intro-azure-ai-engineering/)

### Sesi 3 — Python I: Dasar Pemrograman
📅 Senin, 2 November 2026 · *Monday, November 2, 2026*

Dasar Python: variabel, tipe data, operator, percabangan, perulangan, dan struktur data bawaan (*list*, *dict*, *tuple*, *set*).

*Python basics: variables, data types, operators, conditionals, loops, and built-in data structures (list, dict, tuple, set).*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-03-python-dasar-pemrograman](sesi-03-python-dasar-pemrograman/)

### Sesi 4 — Python II: Fungsi & OOP
📅 Rabu, 4 November 2026 · *Wednesday, November 4, 2026*

Fungsi, modul, penanganan *error*, dan pemrograman berorientasi objek (*class*, *inheritance*, *encapsulation*).

*Functions, modules, error handling, and object-oriented programming (classes, inheritance, encapsulation).*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-04-python-fungsi-oop](sesi-04-python-fungsi-oop/)

### Sesi 5 — Git & GitHub
📅 Jumat, 6 November 2026 · *Friday, November 6, 2026*

*Version control* dengan Git (*commit*, *branch*, *merge*) dan kolaborasi lewat GitHub (*pull request*, *issue*).

*Version control with Git (commit, branch, merge) and collaboration on GitHub (pull requests, issues).*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-05-git-github](sesi-05-git-github/)

### Sesi 6 — Data Wrangling dengan Pandas
📅 Senin, 9 November 2026 · *Monday, November 9, 2026*

Membaca, membersihkan, mentransformasi, dan menggabungkan data tabular dengan Pandas.

*Reading, cleaning, transforming, and joining tabular data with Pandas.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-06-data-wrangling-pandas](sesi-06-data-wrangling-pandas/)

### Sesi 7 — PROJECT 1: Python Automation Tool
📅 Rabu, 11 November 2026 · *Wednesday, November 11, 2026*

Proyek pertama: membangun alat otomasi berbasis Python dari materi sesi 3–6.

*First project: building a Python automation tool using what was covered in sessions 3–6.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-07-project-1-python-automation-tool](sesi-07-project-1-python-automation-tool/)

### Sesi 8 — SQL for AI
📅 Jumat, 13 November 2026 · *Friday, November 13, 2026*

Query SQL untuk menyiapkan data AI: *SELECT*, *JOIN*, agregasi, dan *window function*.

*SQL queries for preparing AI data: SELECT, JOIN, aggregation, and window functions.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-08-sql-for-ai](sesi-08-sql-for-ai/)

### Sesi 9 — SQL Scraping & Data Cleaning Pipeline
📅 Senin, 16 November 2026 · *Monday, November 16, 2026*

Mengambil data dari web/sumber eksternal lalu membangun *pipeline* pembersihan data yang bisa diulang.

*Collecting data from the web or external sources, then building a repeatable data-cleaning pipeline.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-09-sql-scraping-data-cleaning-pipeline](sesi-09-sql-scraping-data-cleaning-pipeline/)

### Sesi 10 — API & FastAPI untuk AI
📅 Rabu, 18 November 2026 · *Wednesday, November 18, 2026*

Konsep REST API dan membangun *endpoint* layanan AI dengan FastAPI.

*REST API concepts and building AI service endpoints with FastAPI.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-10-api-fastapi-untuk-ai](sesi-10-api-fastapi-untuk-ai/)

### Sesi 11 — PROJECT 2: End-to-End Data Pipeline
📅 Jumat, 20 November 2026 · *Friday, November 20, 2026*

Proyek kedua: *pipeline* data utuh dari pengambilan, pembersihan, penyimpanan, sampai disajikan lewat API.

*Second project: a complete data pipeline, from ingestion and cleaning to storage and serving through an API.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-11-project-2-end-to-end-data-pipeline](sesi-11-project-2-end-to-end-data-pipeline/)

### Sesi 12 — NLP & LLM di Azure OpenAI
📅 Senin, 23 November 2026 · *Monday, November 23, 2026*

Dasar NLP dan LLM, *prompt engineering*, serta memanggil model lewat Azure OpenAI.

*NLP and LLM fundamentals, prompt engineering, and calling models through Azure OpenAI.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-12-nlp-llm-azure-openai](sesi-12-nlp-llm-azure-openai/)

---

## Bagian 2 — LLM, RAG & Agentic AI · *Part 2 — LLM, RAG & Agentic AI*

### Sesi 13 — Azure AI Search & Semantic Search
📅 Rabu, 25 November 2026 · *Wednesday, November 25, 2026*

Membuat indeks dokumen di Azure AI Search, *embedding*, *vector search*, dan *semantic ranking*.

*Building document indexes in Azure AI Search, embeddings, vector search, and semantic ranking.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-13-azure-ai-search-semantic-search](sesi-13-azure-ai-search-semantic-search/)

### Sesi 14 — RAG di Azure AI Foundry (LangChain)
📅 Jumat, 27 November 2026 · *Friday, November 27, 2026*

*Retrieval-Augmented Generation*: menggabungkan pencarian dokumen dengan LLM memakai LangChain di Azure AI Foundry.

*Retrieval-Augmented Generation: combining document retrieval with an LLM using LangChain on Azure AI Foundry.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-14-rag-azure-ai-foundry-langchain](sesi-14-rag-azure-ai-foundry-langchain/)

### Sesi 15 — PROJECT 3: AI-Powered Chatbot (RAG) di Azure
📅 Senin, 30 November 2026 · *Monday, November 30, 2026*

Proyek ketiga: *chatbot* berbasis RAG yang menjawab pertanyaan dari kumpulan dokumen sendiri.

*Third project: a RAG chatbot that answers questions from your own document collection.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-15-project-3-ai-chatbot-rag-azure](sesi-15-project-3-ai-chatbot-rag-azure/)

### Sesi 16 — Speech & Information Extraction (Content Understanding)
📅 Rabu, 2 Desember 2026 · *Wednesday, December 2, 2026*

Mengubah suara jadi teks (dan sebaliknya) serta mengekstrak informasi terstruktur dari dokumen, gambar, dan audio dengan Azure Content Understanding.

*Speech-to-text and text-to-speech, plus extracting structured information from documents, images, and audio with Azure Content Understanding.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-16-speech-information-extraction](sesi-16-speech-information-extraction/)

### Sesi 17 — Agentic AI + Azure AI Foundry Agent Service
📅 Jumat, 4 Desember 2026 · *Friday, December 4, 2026*

Konsep *AI agent* (*tool calling*, perencanaan, memori) dan membangunnya dengan Azure AI Foundry Agent Service.

*AI agent concepts (tool calling, planning, memory) and building agents with Azure AI Foundry Agent Service.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-17-agentic-ai-foundry-agent-service](sesi-17-agentic-ai-foundry-agent-service/)

### Sesi 18 — Docker untuk AI + Azure Container Registry
📅 Senin, 7 Desember 2026 · *Monday, December 7, 2026*

Mengemas aplikasi AI ke dalam *container* Docker dan menyimpan *image*-nya di Azure Container Registry.

*Packaging AI applications as Docker containers and storing the images in Azure Container Registry.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-18-docker-azure-container-registry](sesi-18-docker-azure-container-registry/)

---

## Bagian 3 — Deployment, MLOps & Final Project · *Part 3 — Deployment, MLOps & Final Project*

### Sesi 19 — Azure Cloud Deployment
📅 Rabu, 9 Desember 2026 · *Wednesday, December 9, 2026*

Men-*deploy* aplikasi AI ke Azure (mis. App Service atau Container Apps), termasuk konfigurasi dan *secret*.

*Deploying AI applications to Azure (e.g. App Service or Container Apps), including configuration and secrets.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-19-azure-cloud-deployment](sesi-19-azure-cloud-deployment/)

### Sesi 20 — PROJECT 4: Azure-Based AI Infrastructure
📅 Jumat, 11 Desember 2026 · *Friday, December 11, 2026*

Proyek keempat: merancang dan menyiapkan infrastruktur AI di Azure dari *container* sampai *deployment*.

*Fourth project: designing and provisioning AI infrastructure on Azure, from containers to deployment.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-20-project-4-azure-ai-infrastructure](sesi-20-project-4-azure-ai-infrastructure/)

### Sesi 21 — MLOps di Azure & AI Security
📅 Senin, 14 Desember 2026 · *Monday, December 14, 2026*

Siklus hidup model (pelacakan eksperimen, *deployment*, *monitoring*) serta keamanan dan *Responsible AI* di Azure.

*The model lifecycle (experiment tracking, deployment, monitoring) plus security and Responsible AI on Azure.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-21-mlops-azure-ai-security](sesi-21-mlops-azure-ai-security/)

### Sesi 22 — Final Project: Integrasi + Mock Exam AI-901
📅 Rabu, 16 Desember 2026 · *Wednesday, December 16, 2026*

Menyatukan seluruh materi dalam *final project* dan latihan ujian sertifikasi AI-901.

*Bringing all the material together in the final project, plus a practice exam for the AI-901 certification.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-22-final-project-mock-exam-ai-901](sesi-22-final-project-mock-exam-ai-901/)

### Sesi 23 — Final Project Showcase
📅 Rabu, 23 Desember 2026 · *Wednesday, December 23, 2026*

Presentasi *final project* di depan mentor dan peserta lain.

*Presenting the final project to mentors and fellow participants.*

**Yang dipelajari · *What I learned*:** _(diisi setelah sesi · *to be filled after the session*)_

📂 [sesi-23-final-project-showcase](sesi-23-final-project-showcase/)

---

## Proyek · *Projects*

| Proyek · *Project* | Sesi · *Session* | Deskripsi · *Description* | Tautan · *Link* |
|---|:-:|---|---|
| Project 1 — Python Automation Tool | 7 | _(menyusul · *coming soon*)_ | [sesi-07](sesi-07-project-1-python-automation-tool/) |
| Project 2 — End-to-End Data Pipeline | 11 | _(menyusul · *coming soon*)_ | [sesi-11](sesi-11-project-2-end-to-end-data-pipeline/) |
| Project 3 — AI-Powered Chatbot (RAG) | 15 | _(menyusul · *coming soon*)_ | [sesi-15](sesi-15-project-3-ai-chatbot-rag-azure/) |
| Project 4 — Azure-Based AI Infrastructure | 20 | _(menyusul · *coming soon*)_ | [sesi-20](sesi-20-project-4-azure-ai-infrastructure/) |
| Final Project | 22–23 | _(menyusul · *coming soon*)_ | [sesi-22](sesi-22-final-project-mock-exam-ai-901/) |

---

<sub>Materi pelatihan © Digital Skola. Repositori ini berisi catatan dan hasil kerja pribadi selama pelatihan.<br>*Training materials © Digital Skola. This repository contains my personal notes and work from the training.*</sub>
