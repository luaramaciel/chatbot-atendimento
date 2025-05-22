from fastapi import FastAPI
from pydantic import BaseModel
from chat_logic import gerar_resposta  # importa do outro módulo

app = FastAPI()

# Rota básica
@app.get("/")
def read_root():
    return {"message": "Olá, mundo!"}

# Define o formato esperado da requisição
class Mensagem(BaseModel):
    texto: str

# Nova rota para conversar com a IA
@app.post("/chat")
def chat(mensagem: Mensagem):
    resposta = gerar_resposta(mensagem.texto)
    return {"resposta": resposta}
