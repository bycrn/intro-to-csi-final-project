from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from pathlib import Path

app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/categories")
def get_categories():
    """
    Endpoint to serve waste categories for classification
    Returns just the categories section from taoyuan_rules.json
    """
    try:
        rules_path = Path(__file__).parent / "taoyuan_rules.json"
        
        if not rules_path.exists():
            raise HTTPException(
                status_code=404,
                detail=f"Rules file not found at: {rules_path}"
            )
        
        with open(rules_path, "r", encoding="utf-8") as f:
            rules = json.load(f)
        
        return rules.get("categories", [])
        
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid JSON format in rules file: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error loading categories: {str(e)}"
        )

@app.get("/rules")
def get_rules():
    """
    Endpoint to serve Taoyuan waste sorting rules
    Returns the content of taoyuan_rules.json
    """
    try:
        # FIXED: Use absolute path relative to main.py location
        rules_path = Path(__file__).parent / "taoyuan_rules.json"
        
        print(f"Looking for rules at: {rules_path}")  # Debug log
        
        if not rules_path.exists():
            raise HTTPException(
                status_code=404,
                detail=f"Rules file not found at: {rules_path}"
            )
        
        # Load and return the JSON file
        with open(rules_path, "r", encoding="utf-8") as f:
            rules = json.load(f)
        
        print("Rules loaded successfully!")  # Debug log
        return rules
        
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid JSON format in rules file: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error loading rules: {str(e)}"
        )

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
        "all_files": [f.name for f in base_dir.glob("*") if f.is_file()]
    }
