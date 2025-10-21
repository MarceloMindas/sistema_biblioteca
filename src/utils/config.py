MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Empréstimos Detalhados
2 - Relatório de Total de Empréstimos por Livros
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - LEITORES
2 - LIVROS
3 - EMPRÉSTIMOS
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time: int = 3):
    '''
    Limpa a tela após alguns segundos.
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system('cls' if os.name == 'nt' else 'clear')
