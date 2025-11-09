from pydantic import BaseModel


class Items(BaseModel):
    id: int
    name: str
    description: str
    video_url: str
    category_id: str