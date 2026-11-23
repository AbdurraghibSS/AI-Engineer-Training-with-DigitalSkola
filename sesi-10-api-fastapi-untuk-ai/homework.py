"""
Homework Sesi 10 — API & FastAPI untuk AI

Jalankan:
    uvicorn homework:app --reload
Lalu buka:
    http://localhost:8000/docs
"""

from typing import Annotated, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

# =====================================================================
# Soal 4 — Metadata aplikasi supaya /docs terlihat profesional
# =====================================================================
app = FastAPI(
    title="AI Prediction API: Homework Sesi 10",
    description=(
        "REST API sederhana untuk layanan AI: cek kesehatan server, "
        "mengambil data dummy dengan filter, dan memprediksi label "
        "sentimen dari input teks."
    ),
    version="1.0.0",
)


# =====================================================================
# Soal 1 — GET /health
# =====================================================================
@app.get(
    "/health",
    tags=["System"],
    summary="Cek status server",
    description="Mengembalikan status server. Jika server berjalan normal, hasilnya `{\"status\": \"ok\"}`.",
)
def health():
    return {"status": "ok"}


# =====================================================================
# Soal 2 — GET /data dengan query parameter opsional
# =====================================================================
DATA = [
    {"id": 1, "category": "electronics", "name": "Laptop Ultrabook 14 inci"},
    {"id": 2, "category": "electronics", "name": "Headphone Bluetooth"},
    {"id": 3, "category": "electronics", "name": "Smartwatch"},
    {"id": 4, "category": "books", "name": "Belajar FastAPI dari Nol"},
    {"id": 5, "category": "books", "name": "Pengantar Machine Learning"},
    {"id": 6, "category": "fashion", "name": "Batik Tulis Solo"},
    {"id": 7, "category": "fashion", "name": "Sepatu Lari"},
]


@app.get(
    "/data",
    tags=["Data"],
    summary="Ambil daftar data dummy",
    description=(
        "Mengembalikan list data dummy. Bisa difilter dengan `category` "
        "dan dibatasi jumlahnya dengan `limit`. Tanpa parameter, semua data dikembalikan."
    ),
)
def get_data(
    category: Annotated[
        Optional[str], Query(description="Filter kategori, mis. electronics")
    ] = None,
    limit: Annotated[
        Optional[int], Query(ge=1, description="Jumlah maksimal data yang dikembalikan")
    ] = None,
):
    hasil = DATA

    if category is not None:
        hasil = [item for item in hasil if item["category"] == category.lower()]

    if limit is not None:
        hasil = hasil[:limit]

    return hasil


# =====================================================================
# Soal 3 — POST /predict dengan JSON body tervalidasi
# =====================================================================
class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=500, description="Teks yang akan diprediksi")
    threshold: float = Field(ge=0.0, le=1.0, description="Ambang batas confidence (0.0–1.0)")

    # Soal 4 — contoh payload valid yang tampil di Swagger UI
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Pelayanan di kantor ini sangat cepat dan petugasnya ramah sekali",
                    "threshold": 0.7,
                }
            ]
        }
    }


class PredictResponse(BaseModel):
    label: str
    confidence: float
    input_text: str


# Kata kunci sederhana untuk prediksi dummy (bukan model sungguhan)
KATA_POSITIF = {"bagus", "baik", "cepat", "ramah", "puas", "senang", "mantap", "suka", "keren"}
KATA_NEGATIF = {"buruk", "jelek", "lambat", "kecewa", "marah", "rusak", "lama", "benci", "mahal"}


@app.post(
    "/predict",
    tags=["Prediction"],
    summary="Prediksi label sentimen dari teks",
    description=(
        "Endpoint ini menerima input teks lalu memprediksi label sentimennya "
        "(`positif`, `negatif`, atau `netral`) beserta nilai confidence. "
        "Jika confidence di bawah `threshold`, label dikembalikan sebagai `netral`. "
        "Prediksi masih dummy (berbasis kata kunci), belum memakai model AI sungguhan."
    ),
    response_model=PredictResponse,
    status_code=200,
)
def predict(req: PredictRequest):
    kata = req.text.lower().split()
    skor_pos = sum(k.strip(".,!?") in KATA_POSITIF for k in kata)
    skor_neg = sum(k.strip(".,!?") in KATA_NEGATIF for k in kata)
    total = skor_pos + skor_neg

    if total == 0:
        label, confidence = "netral", 0.5
    elif skor_pos >= skor_neg:
        label, confidence = "positif", 0.5 + 0.5 * skor_pos / total
    else:
        label, confidence = "negatif", 0.5 + 0.5 * skor_neg / total

    if confidence < req.threshold:
        label = "netral"

    return PredictResponse(
        label=label,
        confidence=round(confidence, 2),
        input_text=req.text,
    )
