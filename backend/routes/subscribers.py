from fastapi import APIRouter, HTTPException, Request
from backend.database import subscribers
from backend.functions import emailvalidation


router = APIRouter(prefix="/newsletter/subscribe")


@router.post("/api")
async def subscribe_newsletter(request: Request):
    body = await request.body()
    email = body.decode().strip()
    if emailvalidation.emailvalidation(email):
        return await subscribers.add_subscriber(email)
    else:
        raise HTTPException(status_code=400, detail="Invalid email address")
    
