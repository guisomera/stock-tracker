from dotenv import load_dotenv
import os 
from pathlib import path 

load_dotenv(dotenv_path=path(__file__).parent / ".env")
#Va ate o arquivo env e pegue as variaveis de la

AUVO_API_KEY = os.getenv("AUVO_API_KEY")
AUVO_API_TOKEN = os.getenv("AUVO_API_TOKEN")

if not AUVO_API_KEY or not AUVO_API_TOKEN:
    raise RuntimeError("Faltam variáveis no AUVO_API_KEY ou no AUVO_API_TOKEN no .env")