from conexion.mysql_queries import MySQLQueries

class Relatorios:
    def __init__(self):
        # Lê os arquivos SQL e armazena as queries
        with open("sql/relatorio_1.sql", "r", encoding="utf-8") as f:
            self.query_relatorio_emprestimos = f.read()

        with open("sql/relatorio_2.sql", "r", encoding="utf-8") as f:
            self.query_relatorio_livros = f.read()

    # ------------------------------------------------------------
    def get_relatorio_emprestimos(self):
        mysql = MySQLQueries()
        mysql.connect()

        print("\n📘 RELATÓRIO DE EMPRÉSTIMOS DETALHADOS\n")
        resultado = mysql.fetch(self.query_relatorio_emprestimos)

        if len(resultado) == 0:
            print("Nenhum registro encontrado.")
        else:
            for linha in resultado:
                print(
                    f"ID: {linha[0]} | Leitor: {linha[1]} | Livro: {linha[2]} | "
                    f"Empréstimo: {linha[3]} | Devolvido em: {linha[4]}"
                )

        input("\nPressione Enter para sair do relatório.")
        mysql.close()

    # ------------------------------------------------------------
    def get_relatorio_livros(self):
        mysql = MySQLQueries()
        mysql.connect()

        print("\n📗 RELATÓRIO DE TOTAL DE EMPRÉSTIMOS POR LIVRO\n")
        resultado = mysql.fetch(self.query_relatorio_livros)

        if len(resultado) == 0:
            print("Nenhum registro encontrado.")
        else:
            for linha in resultado:
                print(f"Livro: {linha[0]} | Total de Empréstimos: {linha[1]}")

        input("\nPressione Enter para sair do relatório.")
        mysql.close()
