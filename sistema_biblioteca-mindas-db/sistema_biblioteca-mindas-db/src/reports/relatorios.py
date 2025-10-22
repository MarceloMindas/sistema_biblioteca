from conexion.mysql_queries import MySQLQueries
import os

class Relatorios:
    def __init__(self):
        # Caminho base dinâmico — compatível com Linux e Windows
        base_path = os.path.join(os.path.dirname(__file__), "..", "sql")

        # Abre os arquivos com as consultas SQL e associa aos atributos da classe
        with open(os.path.join(base_path, "relatorio_1.sql"), encoding="utf-8") as f:
            self.query_relatorio_emprestimos = f.read()

        with open(os.path.join(base_path, "relatorio_2.sql"), encoding="utf-8") as f:
            self.query_relatorio_livros = f.read()

    # -------------------------------------------------------------------------
    def get_relatorio_emprestimos(self):
        """
        Exibe o relatório de empréstimos detalhados
        """
        mysql = MySQLQueries()
        mysql.connect()
        
        print("\n=== RELATÓRIO DE EMPRÉSTIMOS DETALHADOS ===\n")
        resultado = mysql.fetch(self.query_relatorio_emprestimos)

        if not resultado:
            print("Nenhum empréstimo encontrado.")
        else:
            for linha in resultado:
                print(
                    f"ID: {linha[0]} | Leitor: {linha[1]} | Livro: {linha[2]} | "
                    f"Data Empréstimo: {linha[3]} | Devolvido em: {linha[4]}"
                )

        mysql.close()

    # -------------------------------------------------------------------------
    def get_relatorio_livros(self):
        """
        Exibe o relatório de total de empréstimos por livro
        """
        mysql = MySQLQueries()
        mysql.connect()

        print("\n=== RELATÓRIO DE LIVROS MAIS EMPRESTADOS ===\n")
        resultado = mysql.fetch(self.query_relatorio_livros)

        if not resultado:
            print("Nenhum registro encontrado.")
        else:
            for linha in resultado:
                print(f"Livro: {linha[0]} | Total de Empréstimos: {linha[1]}")

        mysql.close()
