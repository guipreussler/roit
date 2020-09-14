

# Instalando pacotes que serão utilizados.
get_ipython().system('pip install mysql-connector-python')


# Importando as bibliotecas que serão utilizadas.
import mysql.connector

## EXERCICIO 3

def criar_conexao(host, usuario, senha, database):
	return mysql.connector.connect(host=host, user=usuario, password=senha, database=database)

def fechar_conexao(con):
	return con.close()
		



# Referência: https://www.youtube.com/watch?v=bX5NrUWHqyo -> aprendizado do código




