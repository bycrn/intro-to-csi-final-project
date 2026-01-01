# Waste Sorting App (Taoyuan Rules) — Week 17 Submission

Web app to classify waste using an AI detector (YOLO) and display Taoyuan waste-sorting rules. 

## Live Demo (URL)
Frontend: <https://wastesorting-nk7y.onrender.com>   
Backend (FastAPI): <https://wastesortingapp.onrender.com> 


## Features
- Upload/take a photo and classify waste (AI model). 
- Browse Taoyuan sorting rules and categories (JSON rules file). 
- Bilingual UI (ZH/EN). 

## Tech Stack
- Frontend: Vue + Vite.   
- Backend: FastAPI (Python). 
- Model: YOLO weights included in backend folder (project asset). 

## API Endpoints
- `GET /` health check. 
- `POST /api/classify` upload image (`multipart/form-data`, field name `file`). 
- `GET /rules` returns full Taoyuan rules JSON. 
- `GET /api/categories` returns the categories list. [file:54]

## Local Setup

### 1) Backend (FastAPI)
From project root: 

```bash
# macOS/Linux
cd backend
python -m venv .venv
source .venv/bin/activate   

pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

> Then open: API docs: http://localhost:8000/docs

2) Frontend (Vue/Vite)

From project root:

```bash
cd frontend
npm install
npm run dev
```

> Then open: Frontend: http://localhost:517