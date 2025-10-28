from fastapi import FastAPI, Request
import httpx
from config import AUVO_API_TOKEN, AUVO_API_KEY
import asyncio

BASE_URL = "https://api.auvo.com.br/v2/login/"
headers = {
    "Contet-Type" : "application/json"
}

async def login_auvo():                     #"async" -> Pode pausar a função no meio para fazer outra funcionalidade
    async with httpx.AsyncClient(timeout=10) as client:      #"with" -> Abre e fecha tudo direitinho sem eu precisar controlar
    #"httpx.AsyncClient" -> Faz a mesma coisa q o request só que é assíncrono, "Client" -> Apelido pra usar o cliente dentro do bloco
        params = {"apiKey": AUVO_API_KEY, "apiToken": AUVO_API_TOKEN}
        response = await client.get(BASE_URL, params=params, headers=headers)    #Manda a requisição get pra pagina do auvo com esses parametros
        data = response.json()                  #Transformando o dado em biblioteca 
        token = data["result"]["accessToken"]
        print(token)
        print(response.status_code)
        
asyncio.run(login_auvo())   #Chamando função assincrona 

