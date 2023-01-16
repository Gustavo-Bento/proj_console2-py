microcamp=[]
cadastro={}
x=0
while(x==0):
    cadastro['Escola']=str(input("\nDigite a escola: "))
    cadastro['Curso']=str(input("Digite o curso: "))
    cadastro['Ativo']=bool(input("Digite situação: "))
    microcamp.append(cadastro)
    x=int(input("\nDeseja novo cadastro?\nSim - 0 | Não - 1: "))
for i in range(0,len(microcamp),1):
    print(microcamp[i])