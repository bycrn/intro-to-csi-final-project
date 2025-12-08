# 桃園垃圾分類助手 | Taoyuan Waste Sorting Helper

A mobile-friendly web application to help foreigners understand waste sorting categories in Taoyuan, Taiwan. The app uses AI-powered object detection to classify waste items into appropriate categories: recyclables, kitchen waste, and general waste.

## 🎯 Features

- **📸 Image Upload/Camera**: Upload photos or take pictures of waste items
- **🤖 AI Classification**: YOLOv8-powered object detection for automatic waste categorization
- **📚 Rules Page**: Comprehensive guide on Taoyuan's waste sorting rules
- **🌐 Bilingual**: Interface in both Chinese (Traditional) and English
- **📱 Responsive Design**: Works on mobile devices and desktops

## 🏗️ Technology Stack

### Backend
- **FastAPI**: Python web framework for building the REST API
- **YOLOv8**: Object detection model (Ultralytics)
- **Python 3.9+**: Core programming language

### Frontend
- **Vue.js 3**: Progressive JavaScript framework
- **Vite**: Fast build tool and dev server
- **Axios**: HTTP client for API communication

### Infrastructure
- **Firebase**: (Optional) For user authentication and data storage

## 📋 Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- npm or yarn

## 🚀 Getting Started

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## 📖 API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI).

### Endpoints

- `GET /`: API information
- `GET /health`: Health check
- `GET /categories`: Get waste categories and rules
- `POST /classify`: Upload image for classification

## 🗂️ Project Structure

```
intro-to-csi-final-project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   └── detector.py      # YOLOv8 detection logic
│   ├── models/              # Model files directory
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # Vue components
│   │   ├── views/
│   │   │   ├── Home.vue     # Main classification page
│   │   │   └── Rules.vue    # Rules information page
│   │   ├── App.vue          # Root component
│   │   └── main.js          # Application entry point
│   ├── public/              # Static assets
│   ├── index.html           # HTML template
│   ├── package.json         # Node dependencies
│   └── vite.config.js       # Vite configuration
└── README.md
```

## 🎨 Waste Categories

### 可回收物 (Recyclables)
- Plastic bottles
- Paper and cardboard
- Metal cans
- Glass bottles
- **Color**: Green

### 廚餘 (Kitchen Waste)
- Food scraps
- Fruit peels
- Vegetable leaves
- **Color**: Orange

### 一般垃圾 (General Waste)
- Non-recyclable items
- Dirty paper
- Styrofoam
- **Color**: Gray

## 🔧 Configuration

### Backend Configuration

The YOLOv8 model is automatically downloaded on first run. You can customize the model by:
- Placing a custom trained model in `backend/models/`
- Updating the model path in `backend/app/detector.py`

### Frontend Configuration

API endpoint can be configured in `frontend/vite.config.js` proxy settings.

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest  # If tests are available
```

### Frontend Testing
```bash
cd frontend
npm run test  # If tests are configured
```

## 📱 Usage Guide

1. **Access the Application**: Open your browser to `http://localhost:3000`
2. **Upload or Take Photo**: Click "選擇圖片" to upload or "拍照" to take a photo
3. **Classify**: Click "開始分類" to analyze the image
4. **View Results**: See the waste category and disposal instructions
5. **Learn Rules**: Visit the "分類規則" page for detailed sorting guidelines

## 🌟 Future Enhancements

- [ ] Custom model training with Taoyuan-specific waste items
- [ ] Firebase authentication for user accounts
- [ ] History tracking of classified items
- [ ] Multi-language support (Japanese, Korean, etc.)
- [ ] QR code scanning for packaged items
- [ ] Offline mode with cached model
- [ ] Mobile app (iOS/Android)

## 📄 License

This project is created for educational purposes as a final project for Introduction to CSI course.

## 🤝 Contributing

This is a student project. If you have suggestions or find issues, please feel free to open an issue or submit a pull request.

## 👥 Authors

Created as a final project for helping foreigners understand waste sorting in Taoyuan, Taiwan.

## 📞 Contact

For questions about Taoyuan waste sorting rules:
- Taoyuan Environmental Protection Bureau: 1999
- Website: https://www.tyepb.gov.tw

---

Made with ♻️ for a cleaner Taoyuan
