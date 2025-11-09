from backend.database.items import get_all_by_category_id, get_one_by_category_id
from fastapi import APIRouter
#import sqlite3

router = APIRouter(prefix="/categories")


# connection = sqlite3.connect("database.db")
# cursor = connection.cursor()


@router.get("{category_id}")
async def read_items_by_category(category_id):
    return await get_all_by_category_id(category_id)


@router.get("/{category_id}/{id}")
async def read_item_by_category(category_id, id):
    return await get_one_by_category_id(id, category_id)
    
