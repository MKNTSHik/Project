from pydantic import BaseModel


class Navigation(BaseModel):
    label: str
    href: str
    anchor: str