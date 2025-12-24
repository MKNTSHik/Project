from fastapi import FastAPI
import backend.routes.items as items
import backend.routes.navigation as navigation
import backend.routes.subscribers as subscribers
import backend.routes.leads as leads
from backend.database.createdb import create_tables
from backend.database.seed import seed_all
from fastapi.middleware.cors import CORSMiddleware


def lifespan(app: FastAPI):
    create_tables()
    seed_all()
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins = "http://localhost:3000",
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
    expose_headers = ["*"]
)


@app.get("/")
async def home():
    return {"message": "oke"}


@app.get("/health")
async def healthcheck():
    return {"message": "healthy"}


app.include_router(items.router)
app.include_router(subscribers.router)
app.include_router(navigation.router)
app.include_router(leads.router)
