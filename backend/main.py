from fastapi import FastAPI
import backend.routes.items as items
import backend.routes.navigation as navigation
import backend.routes.subscribers as subscribers
#from database.createdb import create_tables


app = FastAPI()


@app.get("/")
async def home():
    return await {"message": "ебал я рот этой ебанины"}


@app.get("/health")
async def healthcheck():
    return await {"message": "все заебато"}


app.include_router(items.router)
app.include_router(subscribers.router)
app.include_router(navigation.router)






