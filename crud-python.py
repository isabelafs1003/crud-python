# para integrar mysql com python é necessario um driver, que facilita essa integração, para isso, é neccessario executar codigo no terminal: 
#     - pip install mysql-connector-python

# importando driver
import mysql.connector

# conexao
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'crud_python_vendas',
)

# o cursor vai possibilitar o python a fazer as devidas alterações
cursor = conexao.cursor()
# print('conexão bem sucedida')     # para uma conexao bem sucedida, ele não deve notificar nenhuma mensagem, apenas essa

# CRUD:
# CREATE
# comando em aspas simples e textos em aspas duplas
nome_produto = "todynho"
valor = 3
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'  #comando para inserir algo no bd
cursor.execute(comando)  # comando usado quando vai ser editado alguma coisa no BD
conexao.commit() # edita banco de dados (cria, deleta ou faz update)


# READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando) 
resultado = cursor.fetchall()  # comando usado quando vai ser lida e armazenada alguma informacao no BD



# UPDATE 
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
print(resultado)



# DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()



# final do código, para encerrar conexao e cursor
cursor.close()
conexao.close()