import math

def pitagoras(x):
    if(x==1):
        b = int(input("Digite b:"))
        c = int(input("Digite c:"))
        a = round(math.sqrt(pow(b,2)+pow(c,2)),2)
        return a
    else:
        if(x==2):
            a = int(input("Digite a:"))
            c = int(input("Digite c:"))
            b = round(math.sqrt(pow(a,2)-pow(c,2)),2)
            return b
        else:
            a = int(input("Digite a:"))
            b = int(input("Digite b:"))
            c = round(math.sqrt(pow(a,2)-pow(b,2)),2)
            return c
        
print("\n|{:<6}|{:<6}|{:<7}|".format("Opção","Busca","Expres."))
print("|======+======+=======|")
print("|{:>6}|{:>6}|{:>7}|".format(1,"a","b²+c²"))
print("|------+------+-------|")
print("|{:>6}|{:>6}|{:>7}|".format(2,"b","a²-c²"))
print("|------+------+-------|")
print("|{:>6}|{:>6}|{:>7}|".format(3,"c","a²-b²"))
print("|---------------------|\n")
x = int(input("Digite uma opção:"))
print(pitagoras(x),"\n")