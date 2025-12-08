# Architecture Documentation

## Overview

The Taoyuan Waste Sorting Helper is a full-stack web application that helps users classify waste items using AI-powered image recognition. The application follows a clean separation between frontend and backend with a REST API interface.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Client Layer                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                    Vue.js 3 SPA                       │   │
│  │  - Home (Classification Interface)                    │   │
│  │  - Rules (Information Page)                           │   │
│  │  - Responsive Design (Mobile + Desktop)               │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────────┘
                            │ HTTP/JSON
                            │ (Port 3000 → 8000)
┌───────────────────────────▼─────────────────────────────────┐
│                         API Layer                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              FastAPI REST API Server                  │   │
│  │  - /health (Health Check)                             │   │
│  │  - /categories (Waste Categories & Rules)             │   │
│  │  - /classify (Image Classification)                   │   │
│  │  - CORS Middleware                                    │   │
│  │  - Error Handling                                     │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                      Business Logic Layer                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │               WasteDetector Class                     │   │
│  │  - Model Loading                                      │   │
│  │  - Object Detection                                   │   │
│  │  - Category Mapping                                   │   │
│  │  - Result Processing                                  │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                       ML Model Layer                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              YOLOv8 Neural Network                    │   │
│  │  - Object Detection                                   │   │
│  │  - COCO Dataset Classes (80 classes)                 │   │
│  │  - Confidence Scoring                                 │   │
│  │  - Bounding Box Detection                             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### Frontend Architecture

```
frontend/
├── src/
│   ├── main.js              # Application entry point
│   │   - Vue app initialization
│   │   - Router setup
│   │   - App mounting
│   │
│   ├── App.vue              # Root component
│   │   - Layout structure
│   │   - Navigation
│   │   - Global styles
│   │   - Router view
│   │
│   └── views/
│       ├── Home.vue         # Classification page
│       │   - Image upload UI
│       │   - Camera capture
│       │   - Preview display
│       │   - API integration
│       │   - Results display
│       │
│       └── Rules.vue        # Information page
│           - Categories display
│           - Rules listing
│           - Tips section
│           - Contact info
│
├── public/                  # Static assets
├── index.html              # HTML template
├── vite.config.js          # Build configuration
└── package.json            # Dependencies
```

### Backend Architecture

```
backend/
├── app/
│   ├── main.py             # FastAPI application
│   │   - App initialization
│   │   - CORS middleware
│   │   - Route definitions
│   │   - Error handling
│   │
│   └── detector.py         # Detection logic
│       - WasteDetector class
│       - Model management
│       - Inference logic
│       - Category mapping
│
├── models/                 # Model storage
│   └── yolov8n.pt         # YOLOv8 weights (auto-downloaded)
│
├── requirements.txt        # Python dependencies
└── Dockerfile             # Container config
```

## Data Flow

### Classification Flow

```
1. User Action
   └─> Upload image or take photo
       │
2. Frontend Processing
   └─> Create FormData with image
       └─> Send POST to /classify
           │
3. Backend Reception
   └─> Validate file type
       └─> Read image data
           └─> Convert to PIL Image
               │
4. Model Inference
   └─> Pass image to YOLOv8
       └─> Get detections with bounding boxes
           └─> Extract class names and confidence scores
               │
5. Category Mapping
   └─> Map detected objects to waste categories
       └─> Determine primary category
           └─> Get category information
               │
6. Response Formation
   └─> Create JSON response with:
       - Success status
       - Category details
       - Detected objects list
       - Confidence scores
       - Instructions
       │
7. Frontend Display
   └─> Parse response
       └─> Update UI with results
           └─> Show category badge
               └─> Display instructions
```

## API Endpoints

### GET /health
**Purpose**: Health check and model status
**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### GET /categories
**Purpose**: Get available waste categories and rules
**Response**:
```json
{
  "categories": [
    {
      "id": "recyclable",
      "name": "可回收物",
      "name_en": "Recyclables",
      "color": "#4CAF50",
      "description": "...",
      "examples": ["..."]
    }
  ],
  "rules": {
    "title": "...",
    "general_rules": ["..."]
  }
}
```

### POST /classify
**Purpose**: Classify waste item from image
**Request**: multipart/form-data with image file
**Response**:
```json
{
  "success": true,
  "category": {
    "id": "recyclable",
    "name": "可回收物",
    "name_en": "Recyclables",
    "color": "#4CAF50",
    "instructions": "...",
    "instructions_en": "..."
  },
  "detected_objects": [
    {
      "object": "bottle",
      "confidence": 0.95,
      "category": "recyclable"
    }
  ],
  "confidence": 0.95,
  "primary_object": "bottle",
  "message": "..."
}
```

## Technology Stack Details

### Backend Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.9+ | Programming language |
| FastAPI | 0.104+ | Web framework |
| Uvicorn | 0.24+ | ASGI server |
| Ultralytics | 8.0+ | YOLOv8 library |
| PyTorch | 2.1+ | Deep learning framework |
| Pillow | 10.1+ | Image processing |
| OpenCV | 4.8+ | Computer vision |

### Frontend Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Vue.js | 3.3+ | Frontend framework |
| Vite | 5.0+ | Build tool |
| Vue Router | 4.2+ | Routing |
| Axios | 1.6+ | HTTP client |

### ML Model

| Aspect | Details |
|--------|---------|
| Model | YOLOv8n (nano) |
| Size | ~6 MB |
| Classes | 80 (COCO dataset) |
| Input | RGB images |
| Output | Bounding boxes + class predictions |

## Waste Category Mapping

### Category Definitions

**1. Recyclables (可回收物)**
- Color: Green (#4CAF50)
- Examples: Bottles, cans, paper, electronics
- COCO classes: bottle, cup, bowl, laptop, cell phone, book

**2. Kitchen Waste (廚餘)**
- Color: Orange (#FF9800)
- Examples: Food scraps, fruits, vegetables
- COCO classes: banana, apple, sandwich, orange, broccoli, carrot

**3. General Waste (一般垃圾)**
- Color: Gray (#757575)
- Examples: Non-recyclable items
- Default category for unmapped classes

### Mapping Logic

```python
# Object detected by YOLOv8
detected_class = "bottle"

# Map to waste category
category = waste_category_map.get(detected_class, "general_waste")

# Get category information
category_info = {
    "id": category,
    "name": "可回收物",
    "name_en": "Recyclables",
    "color": "#4CAF50",
    "instructions": "Please clean and recycle"
}
```

## Security Considerations

### Current Implementation
- CORS enabled for all origins (development)
- File type validation (images only)
- Error handling and sanitization
- No authentication required

### Production Recommendations
- Restrict CORS to specific domains
- Add rate limiting
- Implement file size limits
- Add authentication for user tracking
- Use HTTPS only
- Sanitize all inputs
- Add request validation
- Implement logging and monitoring

## Performance Considerations

### Optimization Points
1. **Model Loading**: Lazy loading on first request
2. **Caching**: Cache category data
3. **Image Processing**: Resize large images
4. **Response Time**: 
   - First request: ~5-10s (model loading)
   - Subsequent: ~1-2s (inference only)

### Scalability Options
1. **Horizontal Scaling**: Multiple backend instances
2. **Load Balancing**: Nginx or cloud load balancer
3. **Caching Layer**: Redis for frequent queries
4. **CDN**: Static assets delivery
5. **Database**: Add for user data and history

## Deployment Architecture

### Docker Deployment
```
┌─────────────────┐
│   Docker Host   │
│  ┌───────────┐  │
│  │ Frontend  │  │ :3000
│  │ Container │  │
│  └─────┬─────┘  │
│        │        │
│  ┌─────▼─────┐  │
│  │ Backend   │  │ :8000
│  │ Container │  │
│  └───────────┘  │
└─────────────────┘
```

### Production Deployment
```
┌──────────────┐
│     CDN      │ (Frontend static files)
└──────┬───────┘
       │
┌──────▼───────┐
│ Load Balancer│
└──────┬───────┘
       │
┌──────▼───────────────────┐
│  Backend Instances (N)   │
│  ┌────────┐  ┌────────┐  │
│  │ API #1 │  │ API #2 │  │
│  └────────┘  └────────┘  │
└──────────────────────────┘
```

## Future Architecture Enhancements

### Phase 2
- Firebase Authentication
- User accounts and profiles
- Classification history storage
- Firestore for data persistence

### Phase 3
- Custom trained model with Taiwan-specific waste
- Real-time notifications
- Community features
- Analytics dashboard

### Phase 4
- Native mobile apps (React Native / Flutter)
- Offline mode with cached model
- PWA support
- Multi-region deployment

## Development Workflow

```
Developer
    │
    ├─> Edit code
    │
    ├─> Hot reload (Vite/Uvicorn)
    │
    ├─> Test in browser
    │
    ├─> Commit changes
    │
    └─> Deploy
        │
        ├─> Build containers
        │
        ├─> Push to registry
        │
        └─> Deploy to production
```

## Monitoring and Logging

### Recommended Tools
- **Backend**: Python logging, Sentry
- **Frontend**: Browser console, Google Analytics
- **Infrastructure**: Docker logs, Prometheus
- **Uptime**: UptimeRobot, Pingdom

### Key Metrics
- API response time
- Model inference time
- Error rates
- User engagement
- Classification accuracy

---

This architecture provides a solid foundation for the waste sorting application with room for future enhancements and scaling.
