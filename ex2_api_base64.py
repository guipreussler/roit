

# Instalando pacotes que serão utilizados.
get_ipython().system('pip install fastapi')
get_ipython().system('pip install uvicorn')


# Importando as bibliotecas que serão utilizadas.
from fastapi import FastAPI
import base64

## EXERCICIO 2
# Rota API
@app.get("/imagem")  # Caminho utilizado para acessar a rota ('localhost:8080/imagem').
def imagem_base64(imagem_base64: varchar(max)): # Inserção da imagem base64 no campo de leitura.
	if(imagem_base64 == NULL): # Condição e mensagem de erro caso o campo esteja vazio.
		return {"Status": Erro, "Mensagem": "Insira um código base64 válido!"}
	else(

		## return "Classe da imagem"

		)



# Referência: https://www.youtube.com/watch?v=bX5NrUWHqyo -> aprendizado do código




