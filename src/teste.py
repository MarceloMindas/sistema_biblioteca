from conexion.mysql_queries import MySQLQueries

# Instancia a classe com permissão de escrita
db = MySQLQueries(can_write=True)
db.connect()

# Executa um comando DML
db.execute_dml("INSERT INTO Leitor (nome, cpf, telefone, email) VALUES ('Mindas', '123.456.789-00', '279999999', 'mindas@email.com')")

# Executa uma consulta
dados = db.fetch("SELECT * FROM Leitor;")
for linha in dados:
    print(linha)

# Fecha a conexão
db.close()
