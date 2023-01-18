met=[60,100,15,12,26,55,47,89,60,35,67]
met.sort()
pol =[round(x*39.37,2) for x in met]
pes =[round(x*3.28,2) for x in met]
jar =[round(x*1.09,2) for x in met]
mil =[round((x*0.6214)/1000,3) for x in met]

print("{:<5}{:<5}{:<10}{:<9}{:<8}{:<8}".format("Nº","m","in","ft","yd","mi"))
print("==========================================")
for v in range(0,len(met),1):
    print("{:<5}{:<5}{:<10}{:<9}{:<8}{:<8}".format(v,met[v],pol[v],pes[v],jar[v],mil[v]))