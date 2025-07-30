from Sistema.library.interface import *
from Sistema.library.arquivo import *
from time import sleep

arq = 'Cadastros.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Remover cadastro', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = leianome('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de remover cadastro.
        cabecalho('REMOVER CADASTRO')
        removercadastro(arq)
    elif resposta == 4:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        sleep(0.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(0.5)