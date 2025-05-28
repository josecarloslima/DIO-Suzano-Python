from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Mensagem(BaseModel):
    texto: str

@app.post("/mensagem")
async def responder(mensagem: Mensagem):
    texto = mensagem.texto.lower()

    if "oi" in texto or "olá" in texto:
        return {"resposta": "Olá! Como posso te ajudar?"}
    elif "internet" in texto:
        return {"resposta": "Você já tentou reiniciar o roteador?"}
    elif "email" in texto:
        return {"resposta": "Verifique sua senha e tente acessar o webmail."}
    else:
        return {"resposta": "Desculpe, não entendi. Pode repetir?"}
