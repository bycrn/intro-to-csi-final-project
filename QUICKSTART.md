# Quick Start Guide

Get the Taoyuan Waste Sorting application running in 5 minutes!

## Prerequisites

Make sure you have installed:
- Python 3.9+ ([Download](https://www.python.org/downloads/))
- Node.js 16+ ([Download](https://nodejs.org/))

## Quick Setup

### Option 1: Using Docker (Easiest)

If you have Docker installed:

```bash
# Clone the repository
git clone <repository-url>
cd intro-to-csi-final-project

# Start everything
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Manual Setup (Recommended for Development)

Open two terminal windows:

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Now visit: http://localhost:3000

## First Use

1. **Open the app** at http://localhost:3000
2. **Click "選擇圖片"** to upload a test image (or use your phone camera)
3. **Click "開始分類"** to classify the waste
4. **View results** with the waste category and disposal instructions
5. **Click "分類規則"** in the navigation to learn about Taoyuan's waste sorting rules

## Test Images

Try uploading images of:
- 🍎 Fruits (classified as kitchen waste)
- 🍾 Bottles (classified as recyclables)
- 📱 Electronics (classified as recyclables)
- 🎒 Bags (classified as general waste)

## Troubleshooting

### Backend won't start
- Make sure Python 3.9+ is installed: `python --version`
- Try installing dependencies again: `pip install -r requirements.txt`
- Check if port 8000 is available: `lsof -i :8000` (Mac/Linux) or `netstat -ano | findstr :8000` (Windows)

### Frontend won't start
- Make sure Node.js 16+ is installed: `node --version`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check if port 3000 is available

### Model download issues
On first run, YOLOv8 will download the model (~6MB). This requires internet connection and may take a minute.

### Can't connect to API
- Make sure backend is running on http://localhost:8000
- Check the browser console for errors
- Verify CORS settings in backend

## What's Next?

- Read the [full README](README.md) for detailed information
- Check the [API documentation](http://localhost:8000/docs) (after starting backend)
- Review the [deployment guide](DEPLOYMENT.md) for production deployment
- Customize the waste categories in `backend/app/detector.py`

## Development Tips

### Backend Hot Reload
The backend runs with `--reload` flag, so changes to Python files will automatically restart the server.

### Frontend Hot Reload
Vite provides instant updates - just save your Vue files and see changes in the browser immediately.

### API Testing
Visit http://localhost:8000/docs for interactive API testing with Swagger UI.

## Need Help?

- **API not working?** Check http://localhost:8000/health
- **Frontend blank?** Open browser console (F12) and check for errors
- **Camera not working?** Camera access requires HTTPS in production, use uploaded images for testing

## Features Overview

### Main Features
- 📸 Upload or take photos of waste items
- 🤖 AI-powered classification using YOLOv8
- 📚 Comprehensive rules page in Chinese and English
- 🎨 Beautiful, responsive design
- 📱 Mobile-friendly interface

### Supported Categories
- ♻️ **Recyclables** (可回收物): Bottles, cans, paper, electronics
- 🍎 **Kitchen Waste** (廚餘): Food scraps, fruits, vegetables
- 🗑️ **General Waste** (一般垃圾): Non-recyclable items

## Performance Notes

- First request may be slow (~5-10 seconds) as the YOLOv8 model loads
- Subsequent requests are much faster (~1-2 seconds)
- Recommended image size: under 5MB
- Supported formats: JPEG, PNG

## Architecture

```
┌─────────────┐      HTTP      ┌─────────────┐
│   Vue.js    │ ────────────> │   FastAPI   │
│  Frontend   │ <──────────── │   Backend   │
│ (Port 3000) │     JSON      │ (Port 8000) │
└─────────────┘               └──────┬──────┘
                                     │
                                     ▼
                              ┌─────────────┐
                              │   YOLOv8    │
                              │    Model    │
                              └─────────────┘
```

---

Enjoy classifying waste and helping keep Taoyuan clean! ♻️
