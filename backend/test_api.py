#!/usr/bin/env python3
"""
Simple script to test the waste sorting API
Usage: python test_api.py [image_path]
"""
import sys
import requests
from pathlib import Path

API_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"✓ Health check: {response.json()}")
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        return False

def test_categories():
    """Test categories endpoint"""
    print("\nTesting categories endpoint...")
    try:
        response = requests.get(f"{API_URL}/categories")
        data = response.json()
        print(f"✓ Found {len(data['categories'])} categories:")
        for cat in data['categories']:
            print(f"  - {cat['name_en']}: {cat['color']}")
        return True
    except Exception as e:
        print(f"✗ Categories test failed: {e}")
        return False

def test_classify(image_path):
    """Test classification endpoint"""
    print(f"\nTesting classification with image: {image_path}")
    
    if not Path(image_path).exists():
        print(f"✗ Image file not found: {image_path}")
        return False
    
    try:
        with open(image_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{API_URL}/classify", files=files)
            
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"✓ Classification successful!")
                print(f"  Category: {data['category']['name_en']} ({data['category']['name']})")
                if data.get('primary_object'):
                    print(f"  Detected: {data['primary_object']}")
                    print(f"  Confidence: {data['confidence']:.1%}")
                print(f"  Instructions: {data['category']['instructions_en']}")
                return True
            else:
                print(f"✗ Classification failed: {data.get('message')}")
                return False
        else:
            print(f"✗ HTTP {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ Classification test failed: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("Taoyuan Waste Sorting API Test")
    print("=" * 60)
    
    # Test health
    if not test_health():
        print("\n❌ API is not running or not healthy")
        print("Make sure to start the backend with: uvicorn app.main:app --reload")
        sys.exit(1)
    
    # Test categories
    test_categories()
    
    # Test classification if image provided
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        test_classify(image_path)
    else:
        print("\nℹ️  To test classification, provide an image path:")
        print("   python test_api.py path/to/image.jpg")
    
    print("\n" + "=" * 60)
    print("✓ Tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
