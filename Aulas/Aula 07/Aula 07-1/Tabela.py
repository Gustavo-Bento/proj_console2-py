from Pessoa import *
cadastro = []


def addTabela(a, b, c):
    cadastro.append(Pessoa(a, b, c))
    r = "\nUsuario cadastrado com suceso!"
    return r


def showTabela():
    print("{:<5}{:<10}{:<7}{:<5}".format("\nN°", "Nome", "Idade", "Sexo"))
    print("======================")
    x = 0
    for v in cadastro:
        print("{:<5}{:<10}{:<7}{:<5}".format(x, v.nome, v.idade, v.sexo))
        x += 1


def delTabela(x):
    print("\nCerteza que deseja remover", cadastro[x].nome, " da tabela?")
    certeza = int(input("Sim - 1 | Não - outros: "))
    if (certeza == 1):
        del cadastro[x]
        r = "\nUsuario removido com suceso!"
        return r
    else:
        r = "\nAção cancelada com sucesso!"
        return r


def updateTabela(x):
    print("\nDeseja atualizar os dados de", cadastro[x].nome, "da tabela?")
    certeza = int(input("Sim - 1 | Não - outros: "))
    if (certeza == 1):
        option = int(
            input("\nO que deseja alterar?\n1 - Nome | 2 - Idade | 3 - Sexo: "))
    if (option == 1):
        cadastro[x].nome = str(input("Digite o nome: "))
        r = "\nNome atualizado com suceso!"
        return r
    if (option == 2):
        cadastro[x].idade = str(input("Digite a idade: "))
        r = "\Idade atualizada com suceso!"
        return r
    if (option == 3):
        cadastro[x].sexo = str(input("Digite o sexo: "))
        r = "\nSexo atualizado com suceso!"
        return r
    else:
        r = "\nAção cancelada com sucesso!"
        return r
