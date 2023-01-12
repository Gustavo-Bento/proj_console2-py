from Pessoa import *

cadastro = []
y = 0

def adicionar():
    x = 1
    y=len(cadastro)+1
    while(x==1):
        nome = str(input("\nDigite o nome: "))
        idade = int(input("Digite a idade: "))
        sexo = str(input("Digite o sexo: "))

        cadastro.append(Pessoa(y, nome, idade, sexo))
        mostrar()
        y += 1
        x = int(input("\nDeseja novo cadastro?\nSim - 1 | Nao - 0: "))
    menu()

def mostrar():
    print("{:<5}{:<10}{:<7}{:<5}".format("\nN°", "Nome", "Idade", "Sexo"))
    print("======================")

    for v in cadastro:
        print("{:<5}{:<10}{:<7}{:<5}".format(v.get_id(), v.get_nome(), v.get_idade(), v.get_sexo()))


def alterar(y, x):
    y -= 1
    if (x == 1):
        nome = str(input("\nDigite o nome: "))
        cadastro[y].set_nome(nome)
        mostrar()
    if (x == 2):
        idade = int(input("\nDigite a idade: "))
        cadastro[y].set_idade(idade)
        mostrar()
    if (x == 3):
        sexo = str(input("\nDigite  o sexo: "))
        cadastro[y].set_sexo(sexo)
        mostrar()


def menu():
    if (len(cadastro) == 0):
        adicionar()
    else:
        r = int(input("\nEscolha uma opção:\n1 - Adicionar\n2 - Alterar\n"))
        if(r==1):
            adicionar()
        if(r==2):
            linha = int(input("\nDigite o n° da linha: "))
            item = int(input("Escolha a opção\n1 - Nome\n2 - Idade\n3 - Sexo\n"))
            alterar(linha,item)
        else:
            r = "\nOpção não encontrada. Finalizando programa..."
            return r
menu()