import sqlite3

conexao = sqlite3.connect("basededados.db")
cursor = conexao.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS clientes ("
#                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                "nome TEXT, "
#                "peso REAL"
#                ")") uma vez criada a tabela posso comentar pra nao ficar executando toda vez

cursor.execute("INSERT INTO clientes (nome, peso) VALUES (?, ?)", ("Nathaly", 55.2))
cursor.execute("INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)", {"nome": "Eduarda", "peso": 65.9})
cursor.execute("INSERT INTO clientes VALUES (:id, :nome, :peso),",
               {"id":None, "nome": "Daniel", "peso": 84.3}
               )

conexao.commit()

cursor.execute("SELECT * FROM clientes")

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)






cursor.close()
conexao.close()
