from fastapi import FastAPI
from fastapi.responses import JSONResponse
import re

app = FastAPI()

def ler_m3u(path):
    canais = []
    nome = None
    with open(path, encoding="utf-8", errors="ignore") as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith("#EXTINF"):
                nome = linha.split(",")[-1]
            elif linha.startswith("http"):
                canais.append({
                    "nome": nome,
                    "url": linha
                })
    return canais

@app.get("/api/canais")
def canais():
    lista = ler_m3u("m3u/lista.m3u")
    return JSONResponse(lista)
