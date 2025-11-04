from fastapi import FastAPI, Request
import httpx 
from auth import token, expires_at, ensure_token
import asyncio

BASE_URL = "https://api.auvo.com.br/v2/products/"
params = {"id": 10}
TotalStock = None

async def retrieve_product():
    await ensure_token()
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}
    async with httpx.AsyncClient(timeout=10) as client: 
        #response = await client.get(BASE_URL, params=params, headers=headers)
        response = await client.get('https://api.auvo.com.br/v2/products/10', headers=headers)
        data = response.json()
        #TotalStock = ["result"]["totalStock"]
        print(response.status_code)
        #print(TotalStock)
        print(data)

asyncio.run(retrieve_product())