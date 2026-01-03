import asyncio
from sqlalchemy import text
from app.core.database import engine
from sqlalchemy.exc import IntegrityError, DBAPIError

async def verify_db_enforcement():
    print("=== Verifying Database Enforcement ===\n")
    
    # Test 1: Regex
    try:
        async with engine.begin() as conn: # engine.begin() commits on exit
            print("1. Testing Regex Constraint ('Apple!')")
            await conn.execute(text("INSERT INTO item (name, description) VALUES ('Apple!', 'Desc')"))
            print("❌ FAILURE: Inserted invalid name 'Apple!'. Constraint is MISSING or INACTIVE.")
    except (IntegrityError, DBAPIError):
        print("✅ SUCCESS: DB rejected 'Apple!'.")
        
    print("-" * 30)

    # Test 2: Length
    try:
        async with engine.begin() as conn:
            long_name = "a" * 51
            print(f"2. Testing Length Constraint ({len(long_name)} chars)")
            await conn.execute(text(f"INSERT INTO item (name, description) VALUES ('{long_name}', 'Desc')"))
            print(f"❌ FAILURE: Inserted {len(long_name)} chars. Constraint is MISSING or INACTIVE.")
    except (IntegrityError, DBAPIError):
        print("✅ SUCCESS: DB rejected long name.")

    print("-" * 30)
    
    # Test 3: Valid Input
    try:
        async with engine.begin() as conn:
            print("3. Testing Valid Input ('맛있는 사과')")
            await conn.execute(text("INSERT INTO item (name, description) VALUES ('맛있는 사과', '굿')"))
            print("✅ SUCCESS: Inserted valid Korean name.")
    except Exception as e:
        print(f"❌ FAILURE: Valid insert failed: {e}")

if __name__ == "__main__":
    asyncio.run(verify_db_enforcement())
