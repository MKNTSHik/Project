import aiosqlite
#import sqlite3
from backend.models.items import Items
from backend.functions.db_path import DB_PATH
from fastapi import HTTPException


#connection = sqlite3.connect('database.db')
#cursor = connection.cursor()


#def get_one_by_category_id(id, category_id):
#    cursor.execute(f"SELECT * FROM items WHERE id = {id} AND category_id = {category_id}")
#    row = cursor.fetchone()
#    item = Items(id=row[0], name=row[1], description=row[2], video_url=row[3], category_id=row[4])
#    connection.close()
#    return item


# def get_all_by_category_id(category_id):
#     cursor.execute(f"SELECT * FROM items WHERE category_id = {category_id}")
#     rows = cursor.fetchall()
#     items = [Items(id=row[0], name=row[1], description=row[2], video_url=row[3], category_id=row[4]) for row in rows]
#     connection.close()
#     return items
    

async def get_one_by_category_id(id, category_id):
    async with aiosqlite.connect(DB_PATH) as connection:
        async with connection.execute(f"SELECT * FROM items WHERE id = ? AND category_id = ?", (id, category_id)) as cursor:
            row = await cursor.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail="Item not found")
            else:
                item = Items(id=row[0], name=row[1], description=row[2], video_url=row[3], category_id=row[4])
                connection.close()
                return item


async def get_all_by_category_id(category_id):
    async with aiosqlite.connect(DB_PATH) as connection:
        async with connection.execute(f"SELECT * FROM items WHERE category_id = ?", (category_id,)) as cursor:
            rows = await cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No items found for this category")
            else:
                items = [Items(id=row[0], name=row[1], description=row[2], video_url=row[3], category_id=row[4]) for row in rows]
                connection.close()
                return items
    