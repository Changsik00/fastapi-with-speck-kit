import asyncio
from sqlalchemy import text
from app.core.database import engine

async def check_constraints():
    async with engine.connect() as conn:
        # Query postgres catalog for constraints on 'item' table
        result = await conn.execute(text("""
            SELECT conname, pg_get_constraintdef(oid)
            FROM pg_constraint
            WHERE conrelid = 'item'::regclass;
        """))
        
        print("\n=== Constraints on 'item' table ===")
        rows = result.fetchall()
        if not rows:
            print("No constraints found (or table not found).")
        for row in rows:
            print(f"Name: {row[0]}")
            print(f"Definition: {row[1]}")
            print("-" * 30)

if __name__ == "__main__":
    asyncio.run(check_constraints())
