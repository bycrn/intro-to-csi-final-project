"""
FastAPI backend for waste sorting application in Taoyuan, Taiwan
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from PIL import Image
import io
import os
from typing import Dict, List
from .detector import WasteDetector

app = FastAPI(
    title="Taoyuan Waste Sorting API",
    description="API for detecting and classifying waste items in Taoyuan, Taiwan",
    version="1.0.0"
)

# CORS middleware to allow requests from frontend
# Configure allowed origins via environment variable
import os
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Configure via ALLOWED_ORIGINS env var
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize detector
detector = WasteDetector()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Taoyuan Waste Sorting API",
        "version": "1.0.0",
        "endpoints": {
            "/classify": "POST - Upload image for waste classification",
            "/categories": "GET - Get available waste categories",
            "/health": "GET - Health check"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "model_loaded": detector.is_loaded()}

@app.get("/categories")
async def get_categories():
    """Get available waste categories and their rules for Taoyuan"""
    return {
        "categories": [
            {
                "id": "recyclable",
                "name": "可回收物 (Recyclables)",
                "name_en": "Recyclables",
                "color": "#4CAF50",
                "description": "塑膠瓶、紙類、金屬罐、玻璃瓶等",
                "description_en": "Plastic bottles, paper, metal cans, glass bottles, etc.",
                "examples": ["plastic bottles", "paper", "cardboard", "metal cans", "glass"]
            },
            {
                "id": "kitchen_waste",
                "name": "廚餘 (Kitchen Waste)",
                "name_en": "Kitchen Waste",
                "color": "#FF9800",
                "description": "食物殘渣、果皮、菜葉等",
                "description_en": "Food scraps, fruit peels, vegetable leaves, etc.",
                "examples": ["food scraps", "fruit", "vegetables", "banana", "apple"]
            },
            {
                "id": "general_waste",
                "name": "一般垃圾 (General Waste)",
                "name_en": "General Waste",
                "color": "#757575",
                "description": "無法回收的物品",
                "description_en": "Non-recyclable items",
                "examples": ["tissue", "dirty paper", "styrofoam", "broken items"]
            }
        ],
        "rules": {
            "title": "桃園市垃圾分類規則 (Taoyuan Waste Sorting Rules)",
            "title_en": "Taoyuan Waste Sorting Rules",
            "general_rules": [
                "垃圾需要在指定時間投放 (Dispose waste at designated times)",
                "回收物品需要清洗乾淨 (Clean recyclables before disposal)",
                "廚餘需要瀝乾水分 (Drain kitchen waste)",
                "塑膠瓶需要壓扁並拆下瓶蓋 (Flatten plastic bottles and remove caps)"
            ]
        }
    }

@app.post("/classify")
async def classify_waste(file: UploadFile = File(...)):
    """
    Classify waste item from uploaded image
    
    Args:
        file: Image file (JPEG, PNG)
        
    Returns:
        Classification result with category and confidence
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Detect and classify
        result = detector.detect(image)
        
        return JSONResponse(content=result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Classification failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
