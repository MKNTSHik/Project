import sqlite3
import json
from backend.models.categories import Categories
from backend.models.items import Items
from backend.models.subscribers import Subscribers
from backend.functions.db_path import DB_PATH
from backend.data.categories import CATEGORIES
from backend.data.items import ITEMS
from backend.data.subscribers import SUBSCRIBERS
# connection = sqlite3.connect("database.db")
# cursor = connection.cursor()


def seed_all():
    with sqlite3.connect(DB_PATH) as connection:
            for category in CATEGORIES:
                category = Categories(**category)
                connection.execute(f"""INSERT OR IGNORE INTO categories (id, name) 
                            VALUES (?, ?)""", (category.id, category.name))
            

            for item in ITEMS:
                item = Items(**item)
                connection.execute(f"""INSERT OR IGNORE INTO items (id, name, description, video_url, category_id) 
                            VALUES (?, ?, ?, ?, ?)""", (item.id, item.name, item.description, item.video_url, item.category_id))
            

            for subscriber in SUBSCRIBERS:
                subscriber = Subscribers(**subscriber)
                connection.execute(f"""INSERT OR IGNORE INTO subscribers (id, email)
                            VALUES (?, ?)""", (subscriber.id, subscriber.email))
            connection.commit()

    return 0

if __name__ == "__main__":
    seed_all()