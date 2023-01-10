import math

def bhaskara(a,b,c):
    delta = -b + 4*a*c
    if(a==0):
        resultado = "Não é possivel realizar operação. A = 0"
    else:
        if(delta<=0):
            resultado  = "Não é possivel realizar operação. Delta <= 0"
        else:
            x1 = round((-b + math.sqrt(delta))/2*a,2)
            x2 = round((-b - math.sqrt(delta))/2*a,2)
            resultado = "O resultado é x1:",x1,"e x2: é:",x2
    return resultado

a = int(input("Digite a:"))
b = int(input("Digite b:"))
c = int(input("Digite c:"))
print(bhaskara(a,b,c))