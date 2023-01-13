def entrada_1():
        v1 = int(input("\nDigite nº1:"))
        return v1
    
def entrada_2():
    v2 = int(input("Digite nº2:"))
    return v2

class Calculo:
    
    def switch(self, operacao):
        default = "Não encontrado"
        return getattr(self, 'case_'+str(operacao), lambda:default)()
    
    def case_1(self):
        adi = int(entrada_1()+entrada_2())
        return adi
    
    def case_2(self):
        sub = int(entrada_1()-entrada_2())
        return sub
    
    def case_3(self):
        mult=int(entrada_1()*entrada_2())
        return mult
    
    def case_4(self):
        div = round(float(entrada_1()/entrada_2()),2)
        return div

def menu():
    x=1
    while(x==1):
        s=Calculo()
        print("\nEscolha uma das operaçoes:")
        opcao = int(input("1 - adição (+)\n2 - subtraçao (-)\n3 - multiplicação (x)\n4 - Divisão (÷)\n\n"))
        print("\n o valor resultante é:",s.switch(opcao))
        x = int(input("\nDeseja nova conta?\nSim - 1 | Não - 0\n\n"))

menu()