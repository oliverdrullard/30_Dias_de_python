# Dia 3 con el reto de 30 dias de python

# Buolean

verdadero = True
Falso = False

print(verdadero)
print(Falso)
print(True)
print(False)

# Operadores de asignacion

x = 5
x += 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3
x %= 3
x |= 3
x ^= 3
x >>= 3
x <<= 3


# Operadores de aritmetica

nume_uno = 5
nume_dos = 4

addicion = nume_uno + nume_dos
subtracion = nume_uno - nume_dos
multiplicacion = nume_uno * nume_dos
divicion = nume_dos / nume_uno
modulos = nume_uno % nume_dos
exponente = nume_uno ** nume_dos
flor_divicion = nume_uno // nume_dos

print(addicion)
print(subtracion)
print(multiplicacion)
print(divicion)
print(modulos)
print(exponente)
print(flor_divicion)


# flooat

# Los numeros flotantes son todos aquellos que tengan punto decimal 

print(3.14)
print(2.1)
print(1.0)


# Ejemplos 

# Calcule el area de un circulo 

radio = 10 
area = 3.14 * radio ** 2
print("El area del circulo es: ",area)

# Calcule el area de un rectangulo

altura = 10
ancho = 20
area_rectangulo = altura * ancho
print("El area del rectangulo es: ",area_rectangulo)

# Calcule el peso de un objeto

masa = 75
gravedad = 9.81
peso = masa * gravedad
print("El peso del objeto es: ",peso)


# Calcule la dencidad de un liquido

masa = 75
volumen = 0.075
dencidad = masa / volumen
print("La dencidad del liquido es: ",)

# Operadores de comparacion 

x = 5
y = 4

print(x == y) # Igual que 
print(x != y) # Diferente de......
print(x > y) # Mayor que 
print(x < y) # Menor que 
print(x >= y) # Mayor o igual que 
print(x <= y) # Menor o igual que 

print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparacion entre True y False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# O peradores is, is not, in

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Operadores de comparacion 

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
