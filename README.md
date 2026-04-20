# 🍔 Food Recognition API

A REST API that identifies food dishes from images and returns their ingredients — powered by a Vision Transformer (ViT) model and TheMealDB.

<!-- Add a banner or demo screenshot here -->
<!-- ![Banner](images/banner.png) -->

---

## 📌 How It Works

1. Upload a food image (JPEG/PNG)
2. A pre-trained ViT model (`nateraw/food`) classifies the dish
3. The dish name is fuzzy-matched against TheMealDB
4. Returns the dish name, ingredients, and match confidence score

<!-- Add a flow diagram or architecture image here -->
<!-- ![Architecture](images/architecture.png) -->

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Siddhi-Naik18/Food-Recognition-API.git
cd food-recognition-api

# Create and activate virtual environment
python -m venv myenv

# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables (Optional)

```bash
cp .env.example .env
```

| Variable | Default | Description |
|---|---|---|
| `PORT` | `8000` | Server port |
| `DEVICE` | `cpu` | `cpu` or `cuda` |
| `FUZZ_THRESHOLD` | `75` | Minimum match score for ingredient lookup |
| `MODEL_NAME` | `nateraw/food` | HuggingFace model name |
| `MEALDB_BASE` | `https://www.themealdb.com/api/json/v1/1` | MealDB base URL |

### Run the Server

```bash
uvicorn app.main:app --reload --port 8000
```

> ⚠️ First run will download the `nateraw/food` model (~300MB) from HuggingFace.

---

## 📡 API Endpoints

### `GET /health`
Returns the API status and version.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0"
}
```

---

### `POST /predict`
Upload a food image and get the dish name + ingredients.

**Request:** `multipart/form-data` with a `file` field (JPEG/PNG)

**Response:**
```json
{
  "dish": "Burger",
  "ingredients": [
    "- Beef (200g)",
    "- Bun (1)",
    "- Lettuce (2 leaves)"
  ],
  "match_score": 90
}
```

**Error Responses:**

| Status | Reason |
|---|---|
| `400` | Unsupported file type (non JPEG/PNG) |
| `404` | No ingredients found for the detected dish |

---

## 🖼️ Demo

<!-- Add screenshots of the API response or Swagger UI here -->
<!-- ![Swagger UI](images/swagger_demo.png) -->
<!-- ![Predict Response](images/predict_response.png) -->

---

## 🧪 Testing

```bash
# Test model loading
python test_model.py

# Test image classification
python test_classify.py

# Test ingredient lookup
python test_mealdb.py
```

---

## 📁 Project Structure

```
API/
├── app/
│   ├── main.py        # FastAPI app and routes
│   ├── model.py       # ViT model loading and inference
│   ├── mealdb.py      # TheMealDB ingredient lookup
│   └── __init__.py
├── images/            # Sample test images
├── test_classify.py
├── test_mealdb.py
├── test_model.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [HuggingFace Transformers](https://huggingface.co/nateraw/food) — `nateraw/food` ViT model
- [TheMealDB API](https://www.themealdb.com/)
- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) — fuzzy string matching
- [PyTorch](https://pytorch.org/)
- [Pillow](https://python-pillow.org/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
