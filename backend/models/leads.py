from pydantic import BaseModel


class Leads(BaseModel):
    id: int
    name: str
    email: str
    message: str