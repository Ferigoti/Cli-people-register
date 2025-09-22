from Sistema.library.interface import *
from Sistema.library.arquivo import *
from time import sleep

# 1. Inicia a conexão com o banco de dados e cria a tabela se não existir
iniciar_banco()

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Remover cadastro', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do banco de dados.
        lerarquivo()
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa com os novos campos.
        cabecalho('NOVO CADASTRO')
        nome = leianome('Nome: ')
        nascimento = leianascimento('Data de Nascimento (DD/MM/AAAA): ')
        naturalidade = leianaturalidade('Naturalidade (Ex: São Paulo/SP): ')
        telefone = leiatelefone('Telefone (Ex: (11) 99999-8888): ')
        cadastrar(nome, nascimento, naturalidade, telefone)
    elif resposta == 3:
        # Opção de remover cadastro.
        removercadastro()
    elif resposta == 4:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        fechar_banco()
        sleep(0.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)