from Tabela import *


def adicionar():
    print("\nNOVO CADASTRO")
    print("=============")
    x = 0
    while (x == 0):
        cadNome = str(input("\nDigite o nome: "))
        cadIdade = str(input("Digite a idade: "))
        cadSexo = str(input("Digite o sexo: "))

        addTabela(cadNome, cadIdade, cadSexo)

        showTabela()

        print("\nDeseja adicionar novo cadastro?")
        x = int(input("Sim - 0 | Não - outros: "))
    menu()


def remover():
    print("\nREMOVER CADASTRO")
    print("================")
    x = 0
    while (x == 0):
        linha = int(input("Digite o n° da linha: "))

        delTabela(linha)

        showTabela()

        print("\nDeseja remover outro cadastro?")
        x = int(input("Sim - 0 | Não - outros: "))
    menu()


def atualizar():
    print("\nATUALIZAR CADASTRO")
    print("==================")
    x = 0
    while (x == 0):
        linha = int(input("Digite o n° da linha: "))

        updateTabela(linha)

        showTabela()

        print("\nDeseja atualizar outro cadastro?")
        x = int(input("Sim - 0 | Não - outros: "))
    menu()

def menu():
    print("\nEscolha a opção de cadastro abaixo:")
    x = int(input("1 - Adicionar | 2 - Deletar | 3 - Atualizar: "))
    if (x == 1):
        adicionar()
    if (x == 2):
        remover()
            
    if (x == 3):
        atualizar()
        
    else:
        r = "\nProcesso Concluido!"
        return r


menu()
