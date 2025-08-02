from fastapi import FastAPI
from pydantic import BaseModel
from .fluxo import conversa

app = FastAPI()

class Mensagem(BaseModel):
    etapa: str
    resposta: str

@app.post("/chat")
def chat(msg: Mensagem):
    return conversa(msg.etapa, msg.resposta)