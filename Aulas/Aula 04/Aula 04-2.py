print("\nFaça uma adição: \n")
valor1 = int(input("Digite n°1: "))
valor2 = int(input("Digite n°2: "))

def adição(x,y):
    resultado = x + y
    return resultado

print("O resultado da adição:",adição(valor1,valor2))

print("\nFaça uma subtraçao: \n")
valor1 = int(input("Digite n°1: "))
valor2 = int(input("Digite n°2: "))

def subtração(x,y):
    resultado = x - y
    return resultado

print("O resultado da subtração:",subtração(valor1,valor2))

print("\nFaça uma multiplicação: \n")
valor1 = int(input("Digite n°1: "))
valor2 = int(input("Digite n°2: "))

def multiplicação(x,y):
    resultado = x * y
    return resultado

print("O resultado da multiplicação:",multiplicação(valor1,valor2))

print("\nFaça uma divisão: \n")
valor1 = int(input("Digite n°1: "))
valor2 = int(input("Digite n°2: "))

def divisão(x,y):
    resultado = x / y
    return resultado

print("O resultado da divisão:",divisão(valor1,valor2))