from conexion.mysql_queries import MySQLQueries

class Relatorios:
    def __init__(self):
        # Associação dos arquivos de consulta SQL aos métodos
        with open("sql/relatorio_1.sql") as f:
            self.relatorio_emprestimo_query = f.read()
        with open("sql/relatorio_2.sql") as f:
            self.relatorio_livro_query = f.read()

    def get_relatorio_emprestimo(self):
        mysql_queries = MySQLQueries()
        mysql_queries.connect()
        print("Relatório de Empréstimos Detalhados:")
        resultado = mysql_queries.run_query(self.relatorio_emprestimo_query)
        for linha in resultado:
            print(linha)
        input("Pressione Enter para continuar...")

    def get_relatorio_livro(self):
        mysql_queries = MySQLQueries()
        mysql_queries.connect()
        print("Relatório de Total de Empréstimos por Livro:")
        resultado = mysql_queries.run_query(self.relatorio_livro_query)
        for linha in resultado:
            print(linha)
        input("Pressione Enter para continuar...")
