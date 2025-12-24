import aiosqlite
from backend.functions.emailvalidation import emailvalidation
from backend.functions.db_path import DB_PATH
from fastapi import HTTPException
# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()


async def add_subscriber(email):
    async with aiosqlite.connect(DB_PATH) as connection:
        if emailvalidation:
            async with connection.execute(f'''SELECT * FROM subscribers WHERE email = ?''', (email.lower(),)) as cursor:
                row = await cursor.fetchone()
                if row:
                    raise HTTPException(status_code=403, detail="Email already subscribed")
                else:
                    await connection.execute(f'''INSERT INTO subscribers (email)
                                VALUES (?)''', (email,))
                    await connection.commit()
                    return {"data": {"status": "pending"}, "meta": {"double_opt_in": "true"}}
        else:
            raise HTTPException(status_code=400, detail="Invalid email address")