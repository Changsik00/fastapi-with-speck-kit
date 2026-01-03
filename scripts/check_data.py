import asyncio
from sqlalchemy import text
from app.core.database import engine

async def check_data():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT count(*) FROM item"))
        count = result.scalar()
        print(f"Total items in DB: {count}")
        
        if count > 0:
            rows = await conn.execute(text("SELECT * FROM item LIMIT 5"))
            print("\nSample Data:")
            for row in rows:
                print(row)

if __name__ == "__main__":
    asyncio.run(check_data())
