from conexao import criar_conexao, fechar_conexao


def insere_usuario(con, nome, email, senha):
	cursor = con.cursor()
	sql = "INSERT INTO usuario (nome, email, senha) values (%s, %s, %s)"
	valores = (nome, email, senha)
	cursor.executa(sql, valores)
	cursor.close()
	cursor.commit()

def main():
	con = criar_conexao("localhost", "root", "123", "database_roit")

	insere_usuario(con, "guilherme", "guilherme@gui.com.br", "gui123")

	fechar_conexao(con)




