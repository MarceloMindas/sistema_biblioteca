# config.py
# Configurações globais para o sistema de Biblioteca

# Menus para interação do sistema
MENU_PRINCIPAL = """ 
========== MENU PRINCIPAL ==========
1 - INSERIR REGISTROS
2 - EDITAR REGISTROS
3 - EXCLUIR REGISTROS
4 - RELATÓRIOS
0 - SAIR
====================================
"""

MENU_INSERIR = """
========== MENU DE REGISTROS ==========
1. REGISTRAR ALUNO
2. REGISTRAR LIVRO
3. REGISTRAR EMPRÉSTIMO
0. VOLTAR AO MENU PRINCIPAL
=======================================
"""

MENU_EDITAR = """
=========== MENU DE EDIÇÃO ===========
1. EDITAR ALUNO
2. EDITAR LIVRO
3. EDITAR EMPRÉSTIMO
0. VOLTAR AO MENU PRINCIPAL
=======================================
"""

MENU_EXCLUIR = """
=========== MENU DE EXCLUSÃO ==========
1. EXCLUIR ALUNO
2. EXCLUIR LIVRO
0. VOLTAR AO MENU PRINCIPAL
=======================================
"""

MENU_RELATORIOS = """
=========== MENU DE RELATÓRIOS ===========
1 - RELATÓRIO DE EMPRÉSTIMOS DETALHADOS
2 - RELATÓRIO DE TOTAL DE EMPRÉSTIMOS POR LIVROS
0 - VOLTAR AO MENU PRINCIPAL
=========================================
"""

# Template para contagem de registros por tabela
QUERY_COUNT = "select count(1) as total_{tabela} from {tabela}"

# Função para limpar a tela do console
def limpar_tela(wait_time=3):
    from time import sleep
    import os
    sleep(wait_time)
    os.system('cls' if os.name == 'nt' else 'clear')
