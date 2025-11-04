from fastapi import FastAPI, Request
import httpx
from config import AUVO_API_TOKEN, AUVO_API_KEY
import asyncio
from datetime import datetime

BASE_URL = "https://api.auvo.com.br/v2/login/"
headers = {
    "Content-Type" : "application/json"
}

token = None
expires_at = None

async def login_auvo():                     #"async" -> Pode pausar a função no meio para fazer outra funcionalidade
    global token, expires_at
    async with httpx.AsyncClient(timeout=10) as client:      #"with" -> Abre e fecha tudo direitinho sem eu precisar controlar
    #"httpx.AsyncClient" -> Faz a mesma coisa q o request só que é assíncrono, "Client" -> Apelido pra usar o cliente dentro do bloco
        params = {"apiKey": AUVO_API_KEY, "apiToken": AUVO_API_TOKEN}
        response = await client.get(BASE_URL, params=params, headers=headers)    #Manda a requisição get pra pagina do auvo com esses parametros
        data = response.json()                  #Transformando o dado em biblioteca 
        expiration_str = data["result"]["expiration"]     #Armazena data de expiração
        expires_at= datetime.strptime(expiration_str, "%Y-%m-%d %H:%M:%S")     #Muda de string pro formato datetime 
        token = data["result"]["accessToken"]
        print(token)
        print(response.status_code)
        return token, expires_at

async def ensure_token():
    global token, expires_at
    if token is None or datetime.now() > expires_at:
        await login_auvo()
    return token, expires_at

#print(token)
#print(expires_at)
asyncio.run(login_auvo())   #Chamando função assincrona 
