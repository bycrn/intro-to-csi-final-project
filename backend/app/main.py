from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

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

@app.get("/rules")
def get_rules():
    """
    Endpoint to serve Taoyuan waste sorting rules
    Returns the content of taoyuan_rules.json
    """
    try:
        # Check if file exists
        if not os.path.exists("taoyuan_rules.json"):
            raise HTTPException(
                status_code=404, 
                detail="Rules file not found. Please ensure taoyuan_rules.json is in the same directory."
            )
        
        # Load and return the JSON file
        with open("taoyuan_rules.json", "r", encoding="utf-8") as f:
            rules = json.load(f)
        
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
