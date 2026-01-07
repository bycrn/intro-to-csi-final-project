"""
YOLOv8-based waste detection and classification
"""
from ultralytics import YOLO
from PIL import Image
import numpy as np
from typing import Dict, List
import os

class WasteDetector:
    """Waste item detector using YOLOv8"""
    
    def __init__(self, model_path: str = None, confidence_threshold: float = 0.15):
        """
        Initialize the detector
        Args:
            model_path: Path to custom YOLOv8 model. If None, uses pretrained YOLOv8s
            confidence_threshold: Minimum confidence score (default: 0.2)
        """
        self.model = None
        self.model_path = model_path or "yolo11m.pt"
        self.confidence_threshold = confidence_threshold
        
        # Mapping from COCO classes to waste categories
        self.waste_category_map = {
            # Kitchen waste
            "banana": "kitchen_waste",
            "apple": "kitchen_waste",
            "sandwich": "kitchen_waste",
            "orange": "kitchen_waste",
            "broccoli": "kitchen_waste",
            "carrot": "kitchen_waste",
            "hot dog": "kitchen_waste",
            "pizza": "kitchen_waste",
            "donut": "kitchen_waste",
            "cake": "kitchen_waste",
            "bubble tea": "kitchen_waste",
            
            # Recyclables
            "bottle": "recyclable",
            "wine glass": "recyclable",
            "can": "recyclable",
            "cup": "recyclable",
            "fork": "recyclable",
            "knife": "recyclable",
            "spoon": "recyclable",
            "bowl": "recyclable",
            "laptop": "recyclable",
            "keyboard": "recyclable",
            "cell phone": "recyclable",
            "book": "recyclable",
            "vase": "recyclable",
            "scissors": "recyclable",
        }
        
        self._load_model()
    
    def _load_model(self):
        """Load YOLOv8 model"""
        try:
            self.model = YOLO(self.model_path)
            print(f"Model loaded successfully: {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None
    
    def is_loaded(self) -> bool:
        """Check if model is loaded"""
        return self.model is not None
    
    def _get_waste_category(self, class_name: str) -> str:
        """
        Map detected object class to waste category
        Args:
            class_name: Detected object class name
        Returns:
            Waste category: recyclable, kitchen_waste, or general_waste
        """
        class_lower = class_name.lower()
        
        # Containers = recyclable
        container_keywords = ["bottle", "vase", "cup", "glass", "bowl", "jar", "can"]
        if any(word in class_lower for word in container_keywords):
            return "recyclable"
        
        # Food items
        food_keywords = ["banana", "apple", "sandwich", "orange", "pizza", "cake", "donut", "broccoli", "carrot", "bubble tea"]
        if any(word in class_lower for word in food_keywords):
            return "kitchen_waste"
        
        return self.waste_category_map.get(class_lower, "general_waste")
    
    def _get_category_info(self, category: str) -> Dict:
        """Get category information with Chinese and English names"""
        category_info = {
            "recyclable": {
                "id": "recyclable",
                "name": "可回收物",
                "name_en": "Recyclables",
                "color": "#4CAF50",
                "instructions": "請清洗乾淨後投入藍色回收桶",
                "instructions_en": "Please clean and put in blue recycling bin"
            },
            "kitchen_waste": {
                "id": "kitchen_waste",
                "name": "廚餘",
                "name_en": "Kitchen Waste",
                "color": "#FF9800",
                "instructions": "請瀝乾水分後投入廚餘桶",
                "instructions_en": "Please drain and put in kitchen waste bin"
            },
            "general_waste": {
                "id": "general_waste",
                "name": "一般垃圾",
                "name_en": "General Waste",
                "color": "#757575",
                "instructions": "請投入一般垃圾袋",
                "instructions_en": "Please put in general waste bag"
            }
        }
        
        return category_info.get(category, category_info["general_waste"])
    
    def detect(self, image: Image.Image) -> Dict:
        """
        Detect and classify waste item in image
        Args:
            image: PIL Image (RGB)
        Returns:
            Detection result with category, confidence, and detected objects
        """
        if not self.is_loaded():
            return {
                "success": False,
                "error": "Model not loaded",
                "category": self._get_category_info("general_waste"),
                "detected_objects": [],
                "message": "無法載入模型 (Model unavailable)"
            }
        
        try:
            # Run inference
            results = self.model(image, conf=self.confidence_threshold, verbose=False)
            
            if not results or len(results) == 0:
                return {
                    "success": True,
                    "category": self._get_category_info("general_waste"),
                    "detected_objects": [],
                    "confidence": 0.0,
                    "message": "未檢測到物品 (No objects detected)"
                }
            
            # Get detections
            result = results[0]
            detections = []
            
            # Process each detection
            if result.boxes is not None and len(result.boxes) > 0:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = result.names[class_id]
                    
                    category = self._get_waste_category(class_name)
                    detections.append({
                        "object": class_name,
                        "confidence": round(confidence, 3),
                        "category": category
                    })
            
            # Determine primary category (highest confidence detection)
            if detections:
                detections.sort(key=lambda x: x["confidence"], reverse=True)
                primary_detection = detections[0]
                primary_category = primary_detection["category"]
                
                return {
                    "success": True,
                    "category": self._get_category_info(primary_category),
                    "detected_objects": detections,
                    "confidence": primary_detection["confidence"],
                    "primary_object": primary_detection["object"],
                    "message": f"檢測到 {primary_detection['object']} (Detected {primary_detection['object']})"
                }
            else:
                return {
                    "success": True,
                    "category": self._get_category_info("general_waste"),
                    "detected_objects": [],
                    "confidence": 0.0,
                    "message": "未檢測到高置信度物品 (No high-confidence objects)"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "category": self._get_category_info("general_waste"),
                "detected_objects": [],
                "message": f"檢測失敗: {str(e)} (Detection failed)"
            }
