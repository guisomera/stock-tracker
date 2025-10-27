from fastapi import FastAPI, Request
import httpx
from config import AUVO_API_TOKEN, AUVO_API_KEY

app = FastAPI()

BASE_URL = "https://api.auvo.com.br/v2/login/"

@app.get("/login-auvo")
async def login_auvo():                     #"async" -> Pode pausar a função no meio para fazer outra funcionalidade
    params = {"apiKey": AUVO_API_KEY, "apiToken": AUVO_API_TOKEN}