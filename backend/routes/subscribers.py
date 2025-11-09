from fastapi import APIRouter
from backend.database import subscribers
from backend.functions import emailvalidation
import sqlite3


router = APIRouter(prefix="/newsletter/subscribe")


# connection = sqlite3.connect("database.db")
# cursor = connection.cursor()


@router.post("")
async def subscribe_newsletter(email):
    if emailvalidation.emailvalidation(email):
        return await subscribers.add_subscriber(email)
    else:
        return {"message": "poshel nahui"}
    
