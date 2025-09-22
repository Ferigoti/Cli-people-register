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


def leianascimento(msg: str):
    while True:
        try:
            nascimento = input(msg).strip()
            if nascimento == '':
                print('\033[31mERRO! A data de nascimento não pode ser vazia.\033[m')
                continue
            return nascimento
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            exit()


def leianaturalidade(msg: str):
    while True:
        try:
            naturalidade = input(msg).strip()
            if naturalidade == '':
                print('\033[31mERRO! A naturalidade não pode ser vazia.\033[m')
                continue
            return naturalidade
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            exit()


def leiatelefone(msg: str):
    while True:
        try:
            telefone = input(msg).strip()
            if telefone == '':
                print('\033[31mERRO! O telefone não pode ser vazio.\033[m')
                continue
            return telefone
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


def linha(tam=80):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(80))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha(42))
    opc = leiaint('\033[32mSua opção:\033[m ')
    return opc