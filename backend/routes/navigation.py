from fastapi import APIRouter
import json 


router = APIRouter(prefix="/navigation")


@router.get("")
def read_navigation():
    with open("/Users/mkntsh/Downloads/Project/backend/data/categories.json", "r") as file:
        navigation = json.load(file)
        return navigation