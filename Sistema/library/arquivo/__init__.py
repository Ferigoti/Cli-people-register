import sqlite3
from Sistema.library.interface import cabecalho, leiaint, linha
from sys import exit

# --- Variáveis Globais para o Banco de Dados ---
DB_NAME = 'Sistema/cadastros.db'
conexao = None
cursor = None

# --- Funções de Controle do Banco de Dados ---

def iniciar_banco():
    """
    Conecta ao banco de dados.
    """
    global conexao, cursor
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nascimento TEXT NOT NULL,
                naturalidade TEXT NOT NULL,
                telefone TEXT NOT NULL
            );
        """)
    except sqlite3.Error as e:
        print(f'\033[31mOcorreu um erro ao conectar ao banco de dados: {e}\033[m')
        exit()


def fechar_banco():
    """Fecha a conexão com o banco de dados de forma segura."""
    if conexao:
        conexao.close()

# --- Funções de Manipulação de Dados (CRUD) ---

def lerarquivo():
    """
    Lê e exibe todas as pessoas cadastradas no banco de dados.
    """
    cabecalho('PESSOAS CADASTRADAS')
    try:
        cursor.execute("SELECT id, nome, nascimento, naturalidade, telefone FROM pessoas")
        pessoas = cursor.fetchall()
        if not pessoas:
            print("Nenhuma pessoa cadastrada no momento.")
        else:
            print(f'\033[33m{"ID":<4}{"NOME":<25}{"NASCIMENTO":<15}{"NATURALIDADE":<20}{"TELEFONE":<15}\033[m')
            print(linha())
            for pessoa in pessoas:
                print(f'{pessoa[0]:<4}'
                      f'\033[36m{pessoa[1]:<25}\033[m '
                      f'{pessoa[2]:<15} '
                      f'\033[32m{pessoa[3]:<20}\033[m '
                      f'{pessoa[4]:<15}')
    except sqlite3.Error as e:
        print(f'\033[31mErro ao ler os dados: {e}\033[m')


def cadastrar(nome, nascimento, naturalidade, telefone):
    """
    Cadastra uma nova pessoa no banco de dados
    """
    try:
        cursor.execute("""
            INSERT INTO pessoas (nome, nascimento, naturalidade, telefone) 
            VALUES (?, ?, ?, ?)
        """, (nome, nascimento, naturalidade, telefone))
        conexao.commit()
        print(f'Novo registro de {nome} adicionado.')
    except sqlite3.Error as e:
        print(f'\033[31mOcorreu um erro ao cadastrar: {e}\033[m')


def removercadastro():
    """
    Mostra as pessoas cadastradas com seus IDs e remove a selecionada.
    """
    cabecalho('REMOVER CADASTRO')
    lerarquivo()
    print(linha())
    
    try:
        cursor.execute("SELECT COUNT(*) FROM pessoas")
        if cursor.fetchone()[0] == 0:
            return
            
        id_remover = leiaint('\033[32mDigite o ID do cadastro que deseja remover (0 para cancelar): \033[m')
        if id_remover == 0:
            print("\033[33mOperação cancelada.\033[m")
            return

        cursor.execute("SELECT nome FROM pessoas WHERE id = ?", (id_remover,))
        resultado = cursor.fetchone()

        if resultado:
            nome_removido = resultado[0]
            cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_remover,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f'\033[32mCadastro de "{nome_removido}" (ID: {id_remover}) removido com sucesso.\033[m')
            else:
                 print(f'\033[31mOcorreu um erro e o cadastro de ID {id_remover} não foi removido.\033[m')
        else:
            print(f'\033[31mERRO! Não existe um cadastro com o ID {id_remover}.\033[m')

    except sqlite3.Error as e:
        print(f'\033[31mOcorreu um erro ao remover o cadastro: {e}\033[m')
