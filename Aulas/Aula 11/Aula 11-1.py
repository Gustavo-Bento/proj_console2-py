x=0
while(x==0):
    print("\Escolha a opçao abaixo:")
    x = int(input("1 - (+)\n2 - (-)\n3 - (x)\n4 - (÷)\n\n"))
    a = int(input("\nDigite a: "))
    b = int(input("Digite b: "))

    adi = lambda a,b : a + b
    sub = lambda a,b : a - b
    mul = lambda a,b : a * b
    div = lambda a,b : a / b

    if(x==1):
        print(adi(a, b))
    else:
        if(x==2):
            print(sub(a, b))
        else:
            if(x==3):
                print(mul(a, b))
            else:
                if(x==4):
                    print(div(a, b))
                else:
                    print("Operaçao não encontrada")
    x=int(input("Deseja novo calculo?\n Sim - 0 | Não - 1:\n"))