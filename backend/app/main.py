from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from .detector import WasteDetector
from .firebase_config import get_waste_categories, get_general_rules, seed_taoyuan_rules

app = FastAPI()

# Initialize Firebase rules once on startup
@app.on_event("startup")
async def startup_event():
    try:
        seed_taoyuan_rules()
    except Exception as e:
        print(f"⚠️  Firebase seed skipped (already seeded): {e}")

# Initialize the waste detector
detector = WasteDetector()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
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
    """Classify waste using YOLOv8 detection"""
    try:
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        result = detector.detect(image)
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Classification error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "category": {
                "id": "general_waste",
                "name": "一般垃圾",
                "name_en": "General Waste",
                "color": "#757575",
                "instructions": "請投入一般垃圾袋",
                "instructions_en": "Please put in general waste bag"
            },
            "confidence": 0.0,
            "message": f"分類失敗 (Classification failed: {str(e)})"
        }

@app.get("/api/categories")
async def get_categories():
    """Get waste categories from Firestore"""
    try:
        categories = get_waste_categories()
        rules = get_general_rules()
        return {
            "success": True,
            "categories": categories,
            "general_rules": rules,
            "detector_status": detector.is_loaded()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
