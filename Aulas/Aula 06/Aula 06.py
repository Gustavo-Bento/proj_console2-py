class Pessoa:
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

cadastro = []

def cadastrar():
    x = 0
    while(x==0):
        cadNome = str(input("\nDigite seu nome:"))
        cadIdade = str(input("Digite sua idade:"))
        cadSexo = str(input("Digite seu sexo:"))

        cadastro.append(Pessoa(cadNome,cadIdade,cadSexo))

        x = int(input("\nDeseja novo cadastro:\n0 - sim | 1 - não: "))

def mostrar():
    print("{:<10}{:<7}{:<5}".format("\nNome","Idade","Sexo"))
    for v in cadastro:
        print("{:<10}{:<7}{:<5}".format(v.nome,v.idade,v.sexo))

cadastrar()
mostrar()