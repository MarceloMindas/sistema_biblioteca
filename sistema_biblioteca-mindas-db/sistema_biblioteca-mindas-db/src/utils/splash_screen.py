from conexion.mysql_queries import MySQLQueries
from utils import config


class SplashScreen:

    def __init__(self):
        # Corrigido: o nome do método é __init__, não _init_
        self.qry_total_leitores = config.QUERY_COUNT.format(tabela="leitor")
        self.qry_total_livros = config.QUERY_COUNT.format(tabela="livro")
        self.qry_total_emprestimos = config.QUERY_COUNT.format(tabela="emprestimo")

        self.created_by = "Alexsander, Ester, João Paulo, Marcelo e Vanderson"
        self.disciplina = "Banco de Dados"
        self.professor = "Prof. M.Sc. Howard Roatti"

    def get_total_leitores(self):
        mysql = MySQLQueries()
        mysql.connect()
        result = mysql.fetch(self.qry_total_leitores)[0][0]
        mysql.close()
        return result

    def get_total_livros(self):
        mysql = MySQLQueries()
        mysql.connect()
        result = mysql.fetch(self.qry_total_livros)[0][0]
        mysql.close()
        return result

    def get_total_emprestimos(self):
        mysql = MySQLQueries()
        mysql.connect()
        result = mysql.fetch(self.qry_total_emprestimos)[0][0]
        mysql.close()
        return result

    def get_updated_screen(self):
        return f"""
###################################################################
#              SISTEMA DE BIBLIOTECA                              #
#                                                                 #
#  TOTAL DE REGISTROS:                                            #
#     1 - LEITORES:     {str(self.get_total_leitores()).rjust(5)}                                     #
#     2 - LIVROS:       {str(self.get_total_livros()).rjust(5)}                                     #
#     3 - EMPRÉSTIMOS:  {str(self.get_total_emprestimos()).rjust(5)}                                     #
#                                                                 #
#  CRIADO POR: {self.created_by} #
#  DISCIPLINA: {self.disciplina}                                     #
#  PROFESSOR:   {self.professor}                         #
###################################################################
"""

    def show(self):
        """Exibe a splash screen e aguarda alguns segundos."""
        from utils.config import clear_console
        print(self.get_updated_screen())
        clear_console(4)