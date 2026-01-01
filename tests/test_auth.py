import pytest
from httpx import AsyncClient
from backend.main import app


@pytest.mark.asyncio
async def test_register():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/auth/register",
            json={
                "email": "[email protected]",
                "password": "testpass123",
                "full_name": "Test User"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as client:
        await client.post(
            "/api/auth/register",
            json={
                "email": "[email protected]",
                "password": "testpass123",
                "full_name": "Test User"
            }
        )
        
        response = await client.post(
            "/api/auth/login",
            json={
                "email": "[email protected]",
                "password": "testpass123"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
