# Test Project
## Structure
```
Project/
├── frontend/          # only html+css (пока что)
├── backend/           # Python FastAPI Server
└── docker/ # Docker configs
```

## Start (only backend)
```
docker build -t backend
docker run backend
```

## Access 
```
* backend: http://localhost:8000
* FastAPI Docs: http://localhost:8000/docs
```