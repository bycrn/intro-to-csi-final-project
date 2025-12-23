import firebase_admin
from firebase_admin import credentials, firestore
import json
from pathlib import Path

# Initialize Firebase (you'll download the JSON key from Firebase Console)
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def seed_taoyuan_rules():
    """Load taoyuan_rules.json into Firestore (run once)"""
    rules_path = Path(__file__).parent / "taoyuan_rules.json"
    
    with open(rules_path, 'r', encoding='utf-8') as f:
        rules_data = json.load(f)
    
    # Store categories
    for category in rules_data.get('categories', []):
        db.collection('waste_categories').document(category['id']).set(category)
    
    # Store general rules
    db.collection('config').document('rules').set({
        'general_rules': rules_data.get('general_rules', [])
    })
    
    print("✅ Taoyuan rules seeded to Firestore")

def get_waste_categories():
    """Fetch categories from Firestore"""
    categories = []
    docs = db.collection('waste_categories').stream()
    for doc in docs:
        categories.append(doc.to_dict())
    return categories

def get_general_rules():
    """Fetch general rules from Firestore"""
    doc = db.collection('config').document('rules').get()
    if doc.exists:
        return doc.to_dict().get('general_rules', [])
    return []
