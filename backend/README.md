# Backend API - Taoyuan Waste Sorting

FastAPI backend with YOLOv8 object detection for waste classification.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn app.main:app --reload
```

Or with Python:
```bash
python -m app.main
```

## API Endpoints

### GET /
Returns API information and available endpoints.

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### GET /categories
Returns waste categories and sorting rules for Taoyuan.

**Response:**
```json
{
  "categories": [
    {
      "id": "recyclable",
      "name": "可回收物 (Recyclables)",
      "name_en": "Recyclables",
      "color": "#4CAF50",
      "description": "塑膠瓶、紙類、金屬罐、玻璃瓶等",
      "examples": ["plastic bottles", "paper", "metal cans"]
    }
  ],
  "rules": {
    "title": "桃園市垃圾分類規則",
    "general_rules": [...]
  }
}
```

### POST /classify
Classifies waste item from uploaded image.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: Image file (JPEG, PNG)

**Response:**
```json
{
  "success": true,
  "category": {
    "id": "recyclable",
    "name": "可回收物",
    "name_en": "Recyclables",
    "color": "#4CAF50",
    "instructions": "請清洗乾淨後投入藍色回收桶"
  },
  "detected_objects": [
    {
      "object": "bottle",
      "confidence": 0.95,
      "category": "recyclable"
    }
  ],
  "confidence": 0.95,
  "primary_object": "bottle"
}
```

## YOLOv8 Model

The application uses YOLOv8n (nano) by default. On first run, the model will be automatically downloaded.

### Custom Model

To use a custom trained model:

1. Place your model file in the `models/` directory
2. Update the model path in `app/detector.py`:
```python
detector = WasteDetector(model_path="models/your_model.pt")
```

## Category Mapping

The detector maps COCO dataset classes to waste categories:

- **Kitchen Waste**: banana, apple, sandwich, orange, broccoli, carrot, etc.
- **Recyclables**: bottle, cup, bowl, laptop, cell phone, book, etc.
- **General Waste**: backpack, umbrella, handbag, furniture, etc.

For production use, train a custom model with Taiwan-specific waste items.

## Error Handling

All endpoints return appropriate HTTP status codes:
- 200: Success
- 400: Bad request (invalid file type)
- 500: Server error (classification failure)

## CORS

CORS is configured to allow all origins in development. Update `main.py` for production:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],
    ...
)
```
