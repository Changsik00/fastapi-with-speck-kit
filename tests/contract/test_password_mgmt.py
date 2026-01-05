import pytest
from httpx import AsyncClient
from fastapi import status

from app.domain.models.user import User

@pytest.mark.asyncio
async def test_change_password_success(client: AsyncClient):
    # 1. Signup
    email = "changepw@example.com"
    password = "oldpassword"
    response = await client.post("/api/v1/auth/signup", json={"email": email, "password": password})
    assert response.status_code == 200
    
    # 2. Login to get token
    login_data = {"username": email, "password": password}
    response = await client.post("/api/v1/auth/login", data=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Change Password
    new_password = "newpassword"
    response = await client.post(
        "/api/v1/auth/password/change",
        headers=headers,
        json={"current_password": password, "new_password": new_password}
    )
    assert response.status_code == 200
    
    # 4. Login with OLD password (should fail)
    response = await client.post("/api/v1/auth/login", data={"username": email, "password": password})
    assert response.status_code == 401
    
    # 5. Login with NEW password (should success)
    response = await client.post("/api/v1/auth/login", data={"username": email, "password": new_password})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_change_password_wrong_current(client: AsyncClient):
    # 1. Signup & Login
    email = "wrongpw@example.com"
    password = "password"
    await client.post("/api/v1/auth/signup", json={"email": email, "password": password})
    
    login_res = await client.post("/api/v1/auth/login", data={"username": email, "password": password})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 2. Change Password with WRONG current
    response = await client.post(
        "/api/v1/auth/password/change",
        headers=headers,
        json={"current_password": "wrong", "new_password": "new"}
    )
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_password_recovery_flow(client: AsyncClient):
    # 1. Signup
    email = "reset@example.com"
    password = "oldpassword"
    await client.post("/api/v1/auth/signup", json={"email": email, "password": password})
    
    # 2. Request Recovery
    response = await client.post("/api/v1/auth/password/recover", json={"email": email})
    assert response.status_code == 200
    # Note: In real test, we might mock AuthService.create_password_reset_token to capture the token.
    # But here, we can't easily capture the printed token from console in this integration test 
    # unless we mock the service or capture stdout.
    # For now, let's verify the endpoint returns 200.
    
    # To test RESET, we need a valid token. 
    # Since we can't easily intercept the token generated inside the endpoint without mocking, 
    # we will rely on a separate unit test for `reset_password` service logic 
    # OR we can manually generate a token here using the same secret key?
    # Yes, we can generate a valid token manually for testing purposes.
    
    from app.core.config import settings
    from jose import jwt
    from datetime import datetime, timedelta
    
    delta = timedelta(minutes=15)
    expire = datetime.utcnow() + delta
    to_encode = {"exp": expire, "sub": email, "type": "reset"}
    fake_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    # 3. Reset Password
    new_password = "newresetpassword"
    response = await client.post(
        "/api/v1/auth/password/reset",
        json={"token": fake_token, "new_password": new_password}
    )
    assert response.status_code == 200
    
    # 4. Login with NEW password
    response = await client.post("/api/v1/auth/login", data={"username": email, "password": new_password})
    assert response.status_code == 200
