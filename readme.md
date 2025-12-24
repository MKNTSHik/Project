# Test Project
## Structure
```
Project/
├── frontend/          # html+css+js
└── backend/           # Python FastAPI Server
```

## Start
### Backend(пока не работает)
```
docker build -t backend .
docker run backend
```
### Backend 
```
uvicorn backend.main:app --port 8000 --reload
```
### Frontend
```
cd frontend
python -m http.server 3000
```

## Access 
```
backend: http://localhost:8000
frontend: http://localhost:3000
FastAPI Docs: http://localhost:8000/docs
```
