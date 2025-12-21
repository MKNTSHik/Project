from fastapi import APIRouter, HTTPException
from backend.database import subscribers
from backend.functions import emailvalidation


router = APIRouter(prefix="/newsletter/subscribe")


@router.post("")
async def subscribe_newsletter(email):
    if emailvalidation.emailvalidation(email):
        return await subscribers.add_subscriber(email)
    else:
        raise HTTPException(status_code=400, detail="Invalid email address")
    
