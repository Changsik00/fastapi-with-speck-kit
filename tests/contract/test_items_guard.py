import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_create_item_unauthorized_fail(client: AsyncClient):
    """
    Test that creating an item without a token fails with 401 Unauthorized.
    This verifies the Auth Guard is working.
    """
    response = await client.post(
        "/api/v1/items/",
        json={"name": "Forbidden Item", "description": "This should not be created"}
    )
    # Expect 401 Unauthorized
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
