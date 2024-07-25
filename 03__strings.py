# String o cadenas de texto

# Creando una cadena 

nombre = "Oliver"
print(nombre)
print(len(nombre))

un_caracter = "O"
print(un_caracter)
print(len(un_caracter))

saludo = "Hola mundo"
print(saludo)
print(len(saludo))

mas_texto = "Esto es una cadena mas larga que las demas"
print(mas_texto)
print(len(mas_texto))

# Creando una variable en varias lineas

variable_de_varias_lineas = """
Esto es una variable de varias linas donde 
puedes poner todas las lineas y saltos de 
linas que quieras y el programa no dara error
"""
print(variable_de_varias_lineas)
print(len(variable_de_varias_lineas))


# Comcatenacion de cadenas

nombre2 = "Oliver"
apellido = "Drullard"
concat = nombre2 + apellido

print(concat)
print(len(concat))

# Secuencias de escape en una linea

# * \n: nueva línea
# * \t: Tab significa (8 espacios)
# * \\: Barra invertida
# * \': Una frase (')
# * \": Comillas dobles (")

print("Esto es un salto de linea en \n python")
print('Hoy\tEs\tViernes') 
print('Esto es genial 1\tPorque es\tMagico')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') 
print('Mi primer lengua de programacion \"Hello, python!\"')

# Formateo de cadenas 

# Formateo de cadenas del tipo antiguo

nombre3 = "Oliver"
apellido2 = "apellido"
lenguaje = "python"

formateo =  "Mi nombre es %s %s y mi lenguaje favorito es %s" %(nombre3,apellido2,lenguaje)
print(formateo)

# Strings y numeros

edad = 24
estatura = 1.58

formateo2 = "Tengo %d y mi estatura es de %f" %(edad,estatura)
print(formateo2)

# Pasandoselo a una lista 

librerias_de_python = ["Django', 'Flask', 'NumPy', 'Matplotlib','Pandas"]

formateo3 = "Las librerias en python son: %s" %(librerias_de_python)
print(formateo3)


# Nueva forma de formatear en python

nombre4 = "Oliver"
apellido3 = "apellido"
lenguaje1 = "python"

formateo4 = "Mi nombre es {} {} y mi lengua de programacion favorito es {}".format(nombre4,apellido3,lenguaje1)
print(formateo4)


a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Interpolacion de cadenas (f-strings)

nombre5 = "Oliver"
apellido6 = "apellido"
lenguaje2 = "python"

print(f'Hola soy {nombre5} {apellido6}, y me gusta {lenguaje2}')

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Cadenas de python con seguencia de caracteres

language = 'Python'
a,b,c,d,e,f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Acsediendo a los carecteres de un por su indice

lenguage7 = "python"

letre_1 = lenguage7[0] #p
letre_2 = lenguage7[1] #y
letre_3 = lenguage7[2] #t
letre_4 = lenguage7[3] #h
letre_5 = lenguage7[4] #o
letre_6 = lenguage7[5] #n

print(letre_1)
print(letre_2)
print(letre_3)
print(letre_4)
print(letre_5)
print(letre_6)

# Divicion de cadenas en subcadenas

lenguage8 = "python"

cadena1 = lenguage8[0:3]
cadena2 = lenguage8[3:6]
cadena3 = lenguage8[-3:]
cadena4 = lenguage8[3:]

print(cadena1)
print(cadena2)
print(cadena3)
print(cadena4)

# Invertir una cadena 

saludo2 =  "Hola mundo"
print(saludo2[::-1])

# Saltar caracteres al cortar

lenguage9 = "python"

pto = lenguage9[0:6:2]

# MeTODOS DE CADE

# capitalize(): combierte el primer caracter en letra mayuscula

saludando = "hola como estas"
print(saludando.capitalize())

# count(): devuelve lasocurrencias de la subcadena

print(saludando.count("o"))
print(saludando.count("a"))
print(saludando.count("o",4,14))
print(saludando.count("ho"))

# endeswit():comprueba si una cadena termina  con  algo en especifico

print(saludando.endeswit("as"))
print(saludando.endeswit("como"))


# expandtabs(): reemplaza el caracter de tabulacion  con espacio

print(saludando.expandtabs())
print(saludando.expandtabs(10))

# find(): devuelve el indice de la primera  aparicion de una subcadena, si no se encuentra devuelve -1

print(saludando.find("h"))
print(saludando.find("as"))
























