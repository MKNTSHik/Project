import aiosqlite
from backend.functions.emailvalidation import emailvalidation
from backend.functions.db_path import DB_PATH
from fastapi import HTTPException


async def add_lead(name, email, message):
    async with aiosqlite.connect(DB_PATH) as connection:
        if emailvalidation:
            async with connection.execute(f'''SELECT * FROM leads WHERE email = ?''', (email.lower(),)) as cursor:
                row = await cursor.fetchone()
                if row:
                    raise HTTPException(status_code=403, detail="Email already leaded")
                else:
                    await connection.execute(f'''INSERT INTO leads (name, email, message)
                                VALUES(?, ?, ?)''', (name, email, message))
                    await connection.commit()
                    return {"data": "ok"}
        else:
            raise HTTPException(status_code=400, detail="Invalid email address")
