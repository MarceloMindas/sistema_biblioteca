from conexion.mysql_queries import MySQLQueries  # Classe equivalente ao OracleQueries, mas para MySQL
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - início
        self.qry_total_alunos = config.QUERY_COUNT.format(tabela="alunos")
        self.qry_total_livros = config.QUERY_COUNT.format(tabela="livros")
        self.qry_total_emprestimos = config.QUERY_COUNT.format(tabela="emprestimos")
        # Consultas de contagem de registros - fim

        # Informações de créditos
        self.integrantes = "Alexsander, Ester, João Paulo, Marcelo e Vanderson"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"

    def get_total_alunos(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_alunos)["total_alunos"].values[0]

    def get_total_livros(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_livros)["total_livros"].values[0]

    def get_total_emprestimos(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_emprestimos)["total_emprestimos"].values[0]

    def get_updated_screen(self):
        return f"""
        ===========================================================================
        #               SISTEMA DE GERENCIAMENTO DE BIBLIOTECA                
        #                                                      
        #  TOTAL DE REGISTROS:                                 
        #      1 - ALUNOS:          {str(self.get_total_alunos()).rjust(5)}
        #      2 - LIVROS:          {str(self.get_total_livros()).rjust(5)}
        #      3 - EMPRÉSTIMOS:     {str(self.get_total_emprestimos()).rjust(5)}
        #
        #  INTEGRANTES DO GRUPO: {self.integrantes}
        #
        #  PROFESSOR:  {self.professor}
        #  
        #  DISCIPLINA: {self.disciplina}
        #
        ===========================================================================

        """