# src/create_tables_and_records.py

from conexion.mysql_queries import MySQLQueries

def create_tables(query: str):
    list_of_commands = query.split(";")
    mysql = MySQLQueries(can_write=True)
    mysql.connect()

    for command in list_of_commands:
        command = command.strip()
        if command:
            try:
                mysql.execute_ddl(command)
                print(f"✅ Executado com sucesso:\n{command[:60]}...")
            except Exception as e:
                print(f"❌ Erro ao executar comando:\n{command}\n{e}")
    mysql.close()


def generate_records(query: str, sep: str = ";"):
    list_of_commands = query.split(sep)
    mysql = MySQLQueries(can_write=True)
    mysql.connect()

    for command in list_of_commands:
        command = command.strip()
        if command:
            try:
                mysql.execute_dml(command)
                print(f"✅ Registro inserido:\n{command[:60]}...")
            except Exception as e:
                print(f"❌ Erro ao inserir registro:\n{command}\n{e}")
    mysql.close()


def run():
    # 1️⃣ Cria as tabelas
    with open("src/sql/create_tables_biblioteca.sql", encoding="utf-8") as f:
        query_create = f.read()
    print("🧱 Criando tabelas...")
    create_tables(query_create)
    print("✅ Tabelas criadas com sucesso!\n")

    # 2️⃣ Gera registros de exemplo (opcional)
    try:
        with open("src/sql/inserting_sample_records.sql", encoding="utf-8") as f:
            query_generate = f.read()
        print("📦 Inserindo registros de exemplo...")
        generate_records(query_generate)
        print("✅ Registros inseridos com sucesso!")
    except FileNotFoundError:
        print("⚠️ Nenhum arquivo de inserção encontrado (pulando etapa).")


if __name__ == "__main__":
    run()
