from sys import exit


def leianome(msg: str):
    while True:
        try:
            nome = input(msg).strip()
            if nome == '':
                print('\033[31mERRO! O nome não pode ser vazio.\033[m')
                continue
            if any(char.isdigit() for char in nome):
                print('\033[31mERRO! O nome não pode conter números.\033[m')
                continue
            return nome
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            exit()


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            exit()
        else:
            return n


def linha(tam = 42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção:\033[m ')
    return opc

