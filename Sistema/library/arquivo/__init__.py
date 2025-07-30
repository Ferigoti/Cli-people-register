from Sistema.library.interface import cabecalho
from sys import exit

def arquivoexiste(nome):
    try:
        with open(nome, 'rt'):
            return True
    except FileNotFoundError:
        return False


def criararquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except OSError:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        with open(nome, 'rt') as a:
            cabecalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.strip().split(';')
                if len(dado) == 2:
                    nome, idade = dado
                    print(f'\033[36m{nome:<30}\033[m \033[32m{idade:>3} anos\033[m')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')


def cadastrar(arq, nome, idade):
    try:
        with open(arq, 'a') as a:
            a.write(f'{nome};{idade}\n')
    except OSError:
        print('Houve um ERRO na abertura do arquivo!')
    except Exception as e:
        print(f'Erro ao gravar os dados: {e}')
    else:
        print(f'Novo registro de {nome} adicionado.')


def removercadastro(arq):
    try:
        with open(arq, 'rt') as arquivo:
            linhas = arquivo.readlines()
        if not linhas:
            print('\033[33mNão há cadastros para remover.\033[m')
            return
        print('\033[36mPessoas cadastradas:\033[m')
        for i, linha in enumerate(linhas):
            nome, idade = linha.strip().split(';')
            print(f'\033[33m{i + 1}\033[m - \033[34m{nome:<30}\033[m {idade:>3} anos')
        print('-' * 42)
        while True:
            try:
                escolha = int(input('\033[32mDigite o número do cadastro que deseja remover: \033[m'))
                if 1 <= escolha <= len(linhas):
                    break
                else:
                    print('\033[31mNúmero inválido. Tente novamente.\033[m')
            except ValueError:
                print('\033[31mDigite um número válido.\033[m')
            except KeyboardInterrupt:
                print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
                exit()
        nomeremovido, _ = linhas[escolha - 1].strip().split(';')
        del linhas[escolha - 1]
        with open(arq, 'wt') as arquivo:
            arquivo.writelines(linhas)
        print(f'\033[32mCadastro de "{nomeremovido}" removido com sucesso.\033[m')
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado.\033[m')