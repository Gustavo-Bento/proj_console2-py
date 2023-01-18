celsius = [7,10,12,17,20,24,30,35,40,50]
fahrenheit = [round(x*1.8+32,2) for x in celsius]
kelvin = [x+273.15 for x in celsius]

print("{:<4}{:<9}{:<12}{:<8}".format("Nº","Celsius","Fahrenheit","Kelvin"))
print("================================")
for v in range(0,len(celsius),1):
    print("{:<4}{:<9}{:<12}{:<8}".format(v,celsius[v],fahrenheit[v],kelvin[v]))