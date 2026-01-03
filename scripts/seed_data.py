import asyncio
from sqlalchemy import text
from app.core.database import engine

async def seed_data():
    print("=== Seeding Data (Recovery/Init) ===\n")
    
    async with engine.begin() as conn:
        # Check if data exists
        result = await conn.execute(text("SELECT count(*) FROM item"))
        count = result.scalar()
        
        if count > 0:
            print(f"⚠️  Data already exists ({count} items). Skipping seed.")
            return

        print("🌱 Seeding initial data...")
        
        items = [
            ("사과", "맛있는 빨간 사과"),
            ("바나나", "길고 노란 바나나"),
            ("포도", "달콤한 포도 송이")
        ]
        
        for name, desc in items:
            await conn.execute(
                text("INSERT INTO item (name, description) VALUES (:name, :desc)"),
                {"name": name, "desc": desc}
            )
            print(f"   Inserted: {name}")
            
    print("\n✅ Seeding complete.")

if __name__ == "__main__":
    asyncio.run(seed_data())
