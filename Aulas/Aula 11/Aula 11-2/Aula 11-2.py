celsius = [7,10,12,17,20,24,30,35,40,50]
lista = lambda c: round(c*1.8+32,2)
fahrenheit = list(map(lista,celsius))
lista = lambda c: round(c+273.15)
kelvin = list(map(lista,celsius))

print("{:<10}{:<12}{:<10}".format("\nCelsius","Fahrenheit","Kelvin"))
print("===========================")

for i in range(0,len(celsius),1):
    print("{:<10}{:<12}{:<10}".format(celsius[i],fahrenheit[i],kelvin[i]))
