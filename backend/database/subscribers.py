import aiosqlite
from backend.functions.emailvalidation import emailvalidation
from backend.functions.db_path import DB_PATH

# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()


async def add_subscriber(email):
    async with aiosqlite.connect(DB_PATH) as connection:
        if emailvalidation:
            await connection.execute(f'''INSERT INTO subscribers (email)
                        VALUES (?)''', (email,))
            await connection.commit()
            return {"data": {"status": "pending"}, "meta": {"double_opt_in": "true"}}
        else:
            return {"message": "poshelnahui"}