from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorios
from controller.controller_leitor import ControllerLeitor
from controller.controller_livro import ControllerLivro
from controller.controller_emprestimo import ControllerEmprestimo

tela_inicial = SplashScreen()
relatorio = Relatorios()
ctrl_leitor = ControllerLeitor()
ctrl_livro = ControllerLivro()
ctrl_emprestimo = ControllerEmprestimo()

def reports(opcao: int):
    if opcao == 1:
        relatorio.get_relatorio_emprestimos_detalhados()
    elif opcao == 2:
        relatorio.get_relatorio_total_emprestimos_por_livro()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console(3)

    while True:
        print(config.MENU_PRINCIPAL)
        try:
            opcao = int(input("Escolha uma opção [1-5]: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            print(config.MENU_RELATORIOS)
            op = int(input("Escolha uma opção: "))
            if op == 0:
                continue
            reports(op)
        elif opcao == 2:
            print(config.MENU_ENTIDADES)
            print("→ Inserção ainda não implementada.")
        elif opcao == 3:
            print(config.MENU_ENTIDADES)
            print("→ Atualização ainda não implementada.")
        elif opcao == 4:
            print(config.MENU_ENTIDADES)
            print("→ Exclusão ainda não implementada.")
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

        input("Pressione Enter para continuar...")
        config.clear_console()

if __name__ == "__main__":
    run()
