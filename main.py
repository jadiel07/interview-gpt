from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def chat(mensagem: str):

    if "python" in mensagem.lower():
        resposta = "Python é uma linguagem muito usada para backend, dados e IA."

    elif "fastapi" in mensagem.lower():
        resposta = "FastAPI é um framework moderno para criação de APIs."

    else:
        resposta = "Ainda estou aprendendo."

    return {
        "usuario": mensagem,
        "ia": resposta
    }