# Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.
suma = 0
for i in range(101):
    suma += i
    if i == 100:
        print(f"La suma de todos los numeros es:{suma}")

# Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números pares y la suma de todos los números impares.

suma_impar = 0
suma_par = 0

for i in range(101):

    if i % 2 == 0:
        suma_par += i 
        if i == 100:
            print(f"La suma de todos los numeros pares del 0 al 100 es: {suma_par}")
    elif i % 2 != 0:
        suma_impar += i 
        if i == 99:
            print(f"La suma de todos los numeros impares del 0 al 100 es: {suma_impar}")
