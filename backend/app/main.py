from typing import Union

from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import json
from pathlib import Path
from PIL import Image
import io

from .detector import WasteDetector

app = FastAPI()

# Initialize the waste detector
detector = WasteDetector()

# ✅ CORS (Production-safe)
# Add your deployed frontend(s) here:
FRONTEND_ORIGINS = [
    "https://wastesorting-nk7y.onrender.com",  # ✅ Your actual frontend URL
    # Development origins - add these for local development
    "http://localhost:3000",
    "http://localhost:5173", 
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Taoyuan Waste AI API",
        "status": "running",
        "detector_loaded": detector.is_loaded()
    }

@app.post("/api/classify")
async def classify_waste(file: UploadFile = File(...)):
    """
    Classify waste item from uploaded image
    """
    try:
        # Check if detector is loaded
        if not detector.is_loaded():
            raise HTTPException(status_code=503, detail="AI model not available")

        # Validate file type
        if not file.content_type or not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Please upload an image file")

        # Read and process image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Convert to RGB if necessary
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Run detection
        result = detector.detect(image)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Classification failed: {str(e)}")

@app.get("/api/categories")
def get_categories():
    """
    Endpoint to serve waste categories for classification
    Returns just the categories section from taoyuan_rules.json
    """
    try:
        rules_path = Path(__file__).parent / "taoyuan_rules.json"
        if not rules_path.exists():
            raise HTTPException(status_code=404, detail=f"Rules file not found at: {rules_path}")

        with open(rules_path, "r", encoding="utf-8") as f:
            rules = json.load(f)

        return rules.get("categories", [])

    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Invalid JSON format in rules file: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading categories: {str(e)}")

@app.get("/rules")
def get_rules():
    """
    Endpoint to serve Taoyuan waste sorting rules
    Returns the content of taoyuan_rules.json
    """
    try:
        rules_path = Path(__file__).parent / "taoyuan_rules.json"
        if not rules_path.exists():
            raise HTTPException(status_code=404, detail=f"Rules file not found at: {rules_path}")

        with open(rules_path, "r", encoding="utf-8") as f:
            rules = json.load(f)

        return rules

    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Invalid JSON format in rules file: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading rules: {str(e)}")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/debug")
def debug():
    """Debug endpoint - shows file locations"""
    base_dir = Path(__file__).parent
    rules_path = base_dir / "taoyuan_rules.json"
    return {
        "base_dir": str(base_dir),
        "rules_path": str(rules_path),
        "rules_exists": rules_path.exists(),
        "all_files": [f.name for f in base_dir.glob("*") if f.is_file()],
    }
