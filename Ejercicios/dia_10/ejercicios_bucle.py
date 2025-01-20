# NIVEL 1

# Itera de 0 a 10 usando el bucle for, haz lo mismo usando el bucle while.

for i in range(11):
    print(i)

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

# Itera de 10 a 0 usando el bucle for, haz lo mismo usando el bucle while. 

lista_1 = list(range(11))

for i in reversed(lista_1):
    print(i)

contador_1 = 10

while contador_1 >= 0:
    print(contador_1)
    contador_1 -= 1 

# Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo

"""
  #
  ##
  ###
  ####
  #####
  ######
  #######

"""
contador_2 = 1

while contador_2 <= 7:
    if contador_2 == 1:
        print("#")
    elif contador_2 == 2:
        print("##")
    elif contador_2 == 3:
        print("###") 
    elif contador_2 == 4:
        print("####")
    elif contador_2 == 5:
        print("#####") 
    elif contador_2 == 6:
        print("######") 
    elif contador_2 == 7:
        print("#######")   
    contador_2 += 1

# Utilice bucles anidados para crear lo siguiente:

"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

"""

filas = 8
columnas = 8

for i in range(filas):
    for j in range(columnas):
        print("#", end=" ")
    print()
    
# Imprima el siguiente patrón:

"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

"""

for i in range(11):
    if i == 0:
        print(f"{i} x {i} = {i * i}")

    elif i == 1:
        print(f"{i} x {i} = {i * i}")

    elif i == 2:
        print(f"{i} x {i} = {i * i}")

    elif i == 3:
        print(f"{i} x {i} = {i * i}")

    elif i == 4:
        print(f"{i} x {i} = {i * i}")

    elif i == 5:
        print(f"{i} x {i} = {i * i}")

    elif i == 6:
        print(f"{i} x {i} = {i * i}")

    elif i == 7:
        print(f"{i} x {i} = {i * i}")

    elif i == 8:
        print(f"{i} x {i} = {i * i}")

    elif i == 9:
        print(f"{i} x {i} = {i * i}")

    elif i == 10:
        print(f"{i} x {i} = {i * i}")

# Itere a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprima los elementos.

tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for i in tecnologias:
    print(i)

# Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares

for i in range(101):
    if i % 2 == 0:
        print(i)

# Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares

for i in range(101):
    if i % 2 != 0:
        print(i)