import sqlite3
import json
from backend.models.categories import Categories
from backend.models.items import Items
from backend.models.subscribers import Subscribers
from backend.functions.db_path import DB_PATH

# connection = sqlite3.connect("database.db")
# cursor = connection.cursor()


def seed_all():
    with sqlite3.connect(DB_PATH) as connection:
            with open("backend/data/categories.json", "r") as file:
                categories = json.load(file)
            for category in categories:
                category = Categories(**category)
                connection.execute(f"""INSERT OR IGNORE INTO categories (id, name) 
                            VALUES (?, ?)""", (category.id, category.name))
            

            with open("backend/data/items.json", "r") as file:
                items = json.load(file)
            for item in items:
                item = Items(**item)
                connection.execute(f"""INSERT OR IGNORE INTO items (id, name, description, video_url, category_id) 
                            VALUES (?, ?, ?, ?, ?)""", (item.id, item.name, item.description, item.video_url, item.category_id))
            

            with open("backend/data/subscribers.json", "r") as file:
                subscribers = json.load(file)
            for subscriber in subscribers:
                subscriber = Subscribers(**subscriber)
                connection.execute(f"""INSERT OR IGNORE INTO subscribers (id, email)
                            VALUES (?, ?)""", (subscriber.id, subscriber.email))
            connection.commit()

    return 0


seed_all()