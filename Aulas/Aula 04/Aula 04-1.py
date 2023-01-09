x = 0
nome = []
idade = []
salario = []
ativo = []

while (x == 0):
    n = str(input("Digite seu nome:"))
    i = int(input("Digite sua idade:"))
    s = float(input("Digite seu salario:"))
    a = bool(input("Digite se estiver ativo:"))
    
    if (a == 1):
        a = "ativo"
    else:
        a = "inativo"

    nome.append(n)
    idade.append(i)
    salario.append(s)
    ativo.append(a)
    y = len(nome)

    print("\n")
    print("{:<15}{:<7}{:<9}{:<9}"
          .format("Nome", "Idade", "Salario", "Atividade"))
    while (x < y):
        print("{:<15}{:<7}{:<9}{:<9}"
              .format(nome[x], idade[x], salario[x], ativo[x]))
        x += 1
        
    print("\n")
    x = int(input("Deseja mais um cadastro: \n 0 - Sim | 1 - Nâo:"))
