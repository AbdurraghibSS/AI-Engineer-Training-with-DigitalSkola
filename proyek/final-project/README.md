<div align="center">

<sub><a href="../../">🏠 Beranda · <i>Home</i></a> &nbsp;·&nbsp; <a href="../">🗂️ Proyek · <i>Projects</i></a></sub>

# 🏆 Final Project — SIAGA NUSA

**Sistem Intelijen Agen Generatif untuk Analisis Bencana Nusantara**<br>
*"Lebih Cepat Memahami. Lebih Siap Menghadapi."*

<img src="https://img.shields.io/badge/Final%20Project-FFB900?style=for-the-badge" alt="Final Project"/> <img src="https://img.shields.io/badge/Periode-30%20Okt%20%E2%80%93%2023%20Des%202026-1B2A6B?style=for-the-badge" alt="Periode"/> <img src="https://img.shields.io/badge/Status-Akan%20Datang%20%C2%B7%20Upcoming-6E7681?style=for-the-badge" alt="Status"/>

<img src="https://img.shields.io/badge/Agentic%20AI-D63384?style=flat-square" alt="Agentic AI"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/> <img src="https://img.shields.io/badge/MLOps-0194E2?style=flat-square&logo=mlflow&logoColor=white" alt="MLOps"/> <img src="https://img.shields.io/badge/Prompt%20Injection%20Defense-DC3545?style=flat-square" alt="Prompt Injection Defense"/> <img src="https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik01LjQ4MyAyMS4zSDI0TDE0LjAyNSA0LjAxM2wtMy4wMzggOC4zNDcgNS44MzYgNi45MzhMNS40ODMgMjEuM3pNMTMuMjMgMi43TDYuMTA1IDguNjc3IDAgMTkuMjUzaDUuNTA1di4wMTRMMTMuMjMgMi43eiIvPjwvc3ZnPg%3D%3D" alt="Microsoft Azure"/>

</div>

---

> [!IMPORTANT]
> Kode Final Project ada di **repository terpisah**. Halaman ini berisi ringkasan, checklist kriteria, dan tautannya.<br>
> *The Final Project code lives in a **separate repository**. This page holds the summary, the criteria checklist, and the links.*

<div align="justify">

## 🔗 Tautan · *Links*

| | Tautan · *Link* |
|---|---|
| 📦 Repository | _(menyusul · *coming soon*)_ |
| 🌐 Demo live · *Live demo* | _(menyusul · *coming soon*)_ |
| 📈 Experiment tracking | _(menyusul · *coming soon*)_ |

## 💡 Ide Proyek · *Project Idea*

<div align="center">

### 🚨 SIAGA NUSA
**Sistem Intelijen Agen Generatif untuk Analisis Bencana Nusantara**<br>
*Generative Agent Intelligence System for Indonesian Disaster Analysis*

> **"Lebih Cepat Memahami. Lebih Siap Menghadapi."**<br>
> *"Understand Faster. Be Better Prepared."*

</div>

**Masalah.** Saat bencana, informasi resmi tersebar di banyak tempat dan formatnya teknis, sementara kabar palsu seperti "tsunami susulan" menyebar lebih cepat daripada data resmi.<br>
*Problem. During a disaster, official information is scattered across many sources in technical formats, while false alerts such as "an aftershock tsunami is coming" spread faster than official data.*

**Solusi.** Agen AI yang menjawab dalam bahasa sehari-hari lewat web dan Telegram. Agen menggabungkan data resmi, prediksi model, dan laporan warga, lalu memberi label sumber pada setiap informasi.<br>
*Solution. An AI agent that answers in plain language on the web and Telegram. It combines official data, model predictions, and citizen reports, and labels the source of every piece of information.*

| Komponen · *Component* | Fungsi · *Purpose* |
|---|---|
| 🌋 **Model A — Earthquake Impact Prediction** | Memprediksi apakah guncangan gempa mencapai intensitas MMI ≥ V.<br>*Predicts whether an earthquake's shaking reaches MMI ≥ V.* |
| 🌊 **Model B — Flood Occurrence Prediction** | Memprediksi peluang banjir per wilayah dalam 24 jam, bila data historis dan curah hujannya memadai.<br>*Predicts the probability of flooding per area within 24 hours, provided the historical and rainfall data are sufficient.* |
| 🤖 **SIAGA NUSA AI Agent** | Menggabungkan keluaran model, mengambil informasi resmi terbaru, menjelaskan hasil prediksi, dan menyusun ringkasan situasi berdasarkan sumbernya.<br>*Combines model outputs, fetches the latest official information, explains predictions, and builds source-labelled situation summaries.* |
| 💬 **Kanal · *Channels*** | Web dan bot Telegram.<br>*Web app and Telegram bot.* |

**Sumber data · *Data sources*:** BMKG, USGS, PetaBencana.id, Open-Meteo.

## ✅ Checklist Kriteria · *Criteria Checklist*

Status: ⬜ belum · *not yet* — 🔄 dikerjakan · *in progress* — ✅ terpenuhi · *met*

| # | Kriteria · *Criterion* | Keterangan · *Description* | Bukti · *Evidence* | Status |
|:-:|---|---|:-:|:-:|
| 1 | 🤖 **Agentic Generative AI** | Menyelesaikan satu masalah nyata dengan <i>Agentic Generative AI</i>.<br>*Solves one real problem using Agentic Generative AI.* | — | ⬜ |
| 2 | 📦 **Repo sendiri · <i>Own repository</i>** | Kode proyek ada di repository GitHub tersendiri.<br>*Project code lives in its own GitHub repository.* | — | ⬜ |
| 3 | 🔄 **Data pipeline otomatis · <i>Automated data pipeline</i>** | <i>Ingestion</i>, penyimpanan, dan pembersihan data berjalan otomatis dari ujung ke ujung.<br>*Data ingestion, storage, and cleaning run automatically end to end.* | — | ⬜ |
| 4 | 🧪 **Model & evaluasi · <i>Model & evaluation</i>** | Model dilatih, disimpan sebagai <i>artifact</i>, dan dievaluasi dengan <i>train/test split</i> yang benar serta metrik nyata.<br>*A model is trained, saved as an artifact, and evaluated with a proper train/test split and real metrics.* | — | ⬜ |
| 5 | 🔎 **Retrieval oleh agen · <i>Agent-driven retrieval</i>** | Bila memakai RAG, agen sendiri yang memutuskan kapan perlu <i>retrieval</i>, bukan selalu <i>retrieve-then-answer</i>.<br>*If RAG is used, the agent decides when to retrieve, rather than always retrieve-then-answer.* | — | ⬜ |
| 6 | 🐳 **Docker Compose** | <code>docker compose up</code> menjalankan seluruh aplikasi tanpa langkah manual.<br>*<code>docker compose up</code> runs the whole app with no manual steps.* | — | ⬜ |
| 7 | 🌐 **Live publik · <i>Publicly live</i>** | Aplikasi bisa diakses lewat IP/jaringan publik.<br>*The app is reachable on a public IP/network.* | — | ⬜ |
| 8 | 📈 **Experiment tracking** | Beberapa <i>run</i> eksperimen tercatat lengkap dengan parameter dan metrik, lalu model terbaik diregistrasi.<br>*Multiple experiment runs are logged with parameters and metrics, and the best model is registered.* | — | ⬜ |
| 9 | 🛡️ **Prompt injection** | Sistem diuji dengan minimal satu upaya <i>prompt injection</i> nyata; pertahanan dan <i>test case</i>-nya didokumentasikan.<br>*The system is tested against at least one real prompt injection attempt, with the defense and test case documented.* | — | ⬜ |

## 🏗️ Arsitektur · *Architecture*

_(menyusul · *coming soon*)_

## 🗓️ Jadwal · *Timeline*

| Sesi | Tanggal · *Date* | Agenda |
|:-:|---|---|
| 2 | Jumat, 30 Oktober 2026 | Mulai pengerjaan · *Project kickoff* |
| 22 | Rabu, 16 Desember 2026 | Integrasi + Mock Exam AI-901 · *Integration + AI-901 mock exam* |
| 23 | Rabu, 23 Desember 2026 | Final Project Showcase |

</div>

---

<div align="center">

<a href="../04-azure-ai-infrastructure/">← Project 4</a> &nbsp;·&nbsp; <a href="../">🗂️ Semua Proyek</a> &nbsp;·&nbsp; <span>&nbsp;</span>

</div>
