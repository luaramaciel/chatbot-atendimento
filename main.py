from fastapi import FastAPI
from pydantic import BaseModel
from chat_logic import chamar_openai

app = FastAPI()

class PedidoPergunta(BaseModel):
    pergunta: str

@app.post("/perguntar")
def receber_pergunta(pedido: PedidoPergunta):
    resposta_ia = chamar_openai(pedido.pergunta)
    return {"resposta": resposta_ia}
