from model.emprestimo import Emprestimo
from model.leitor import Leitor
from model.livro import Livro
from conexion.mysql_queries import MySQLQueries

class ControllerEmprestimo:
    def __init__(self):
        pass

    def registrar_emprestimo(self) -> Emprestimo:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_leitor = input("Digite o ID do leitor: ")
            id_livro = input("Digite o ID do livro: ")
            data_emprestimo = input("Data do empréstimo (YYYY-MM-DD): ")
            data_devolucao_prevista = input("Data prevista de devolução (YYYY-MM-DD): ")
            data_devolucao_realizada = input("Data da devolução realizada (YYYY-MM-DD) :")

            # Insere os dados no banco
            query = f"""
                INSERT INTO emprestimo (
                    id_leitor, id_livro, data_emprestimo, data_devolucao_prevista, data_devolucao_realizada
                ) VALUES (
                    {id_leitor}, {id_livro}, '{data_emprestimo}', '{data_devolucao_prevista}', '{data_devolucao_realizada}'
                );
            """
            mysql.execute_dml(query)
            print("✅ Empréstimo registrado com sucesso.")

            # Cria objeto para representar o empréstimo no sistema
            emprestimo = Emprestimo(
                id_emprestimo=None,
                leitor=Leitor(id_leitor),
                livro=Livro(id_livro),
                data_emprestimo=data_emprestimo,
                data_devolucao_prevista=data_devolucao_prevista,
                data_devolucao_realizada=data_devolucao_realizada
            )
            print(emprestimo.to_string())
            return emprestimo

        except Exception as e:
            print(f"❌ Erro ao registrar empréstimo: {e}")
        finally:
            mysql.close()

    # ---------------------------------------------------------------------
    def devolver_livro(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_emprestimo = input("Digite o ID do empréstimo: ")
            data_real = input("Data real de devolução (YYYY-MM-DD): ")

            query = f"""
                UPDATE emprestimo
                SET data_devolucao_realizada = '{data_real}'
                WHERE id_emprestimo = {id_emprestimo};
            """
            mysql.execute_dml(query)
            print("✅ Devolução registrada com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao registrar devolução: {e}")
        finally:
            mysql.close()

    # ---------------------------------------------------------------------
    def excluir_emprestimo(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_emprestimo = input("Digite o ID do empréstimo: ")

            query = f"DELETE FROM emprestimo WHERE id_emprestimo = {id_emprestimo};"
            mysql.execute_dml(query)
            print("🗑️ Empréstimo excluído com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao excluir empréstimo: {e}")
        finally:
            mysql.close()
