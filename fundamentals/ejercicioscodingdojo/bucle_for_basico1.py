# 0 al 150
for i in range(151):
    print(i)

# Imprimir todos los múltiplos de 5 entre 5 y 1,000
for i in range(5, 1001, 5):
    print(i)


# 1 al 100, Si es divisible por 5 "Coding", Si es divisible por 10 "Coding Dojo"
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# enteros impares del 0 al 500,000
# Imprimir la suma final
suma = 0
for i in range(1, 500001, 2):
    print(i)
    suma += i
print(suma)

# positivos comenzando desde 2018
# En cuenta regresiva de 4 en 4
for i in range(2018, 0, -4):
    print(i)

#enteros múltiplos de mult en el rango de lowNum a highNum
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
