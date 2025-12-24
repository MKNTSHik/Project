from fastapi import APIRouter, HTTPException, Request
from backend.database import leads
from backend.functions import emailvalidation


router = APIRouter(prefix="/leads")


@router.post("")
async def add_lead(request: Request):
    data = await request.json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    if emailvalidation.emailvalidation(email):
        return await leads.add_lead(name, email, message)
    else:
        raise HTTPException(status_code=400, detail="Invalid email address")
    
