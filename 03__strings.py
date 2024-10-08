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

# count(): devuelve las ocurrencias de la subcadena

print(saludando.count("o"))
print(saludando.count("a"))
print(saludando.count("o",4,14))
print(saludando.count("ho"))

# endeswit():comprueba si una cadena termina  con  algo en especifico

print(saludando.endswith("as"))
print(saludando.endswith("H"))


# expandtabs(): reemplaza el caracter de tabulacion  con espacio

print(saludando.expandtabs())
print(saludando.expandtabs(10))

# find(): devuelve el indice de la primera  aparicion de una subcadena, si no se encuentra devuelve -1

print(saludando.find("h"))
print(saludando.find("as"))

# rfind():Devuelve el indece de la ultima aparicion de la subcadena si no se encuentra  devulve -1

print("Usando la funcion rfind()")

print(saludando.rfind("o"))
print(saludando.rfind("c"))


# format(): formatea la cadena para tenner una salida mas agradable

print("Usando la funcion format() y el formateo con la f delante")

nom = "oliver"
apell = "drullard"
ege = 250

cadena_formateda = "Mi nombre es {} {} y tengo {} años".format(nom,apell,ege)
cadena_format2 = f"Mi nombre es {nom} {apell} y tengo {ege} años"

print(cadena_formateda)
print(cadena_format2)

# index(): devuelve el indice mas bajo de una subcadena

print("Usando la funcion index()")

sup_string = "como"

print(saludando.index("como"))
print(saludando.index(sup_string))

# rindex(): devuelve el indice mas alto de una subcadena

print("Usando la funcion rindex()")

print(saludando.rindex("como"))
print(saludando.rindex(sup_string))

# isalnum(): comprueba caracteres alfanumericos

print("Usando la funcion isalnum()")

reto = "trentaDiasdepython"
reto2 = "30Diasdepython"

print(reto.isalnum())
print(reto2.isalnum())

# isalpha(): comprueba si todos los elementos de la cadena son carecteres alfabeticos(az-AZ)

print("Usando la funcion isalpha()")

num = "123456789"

print(saludando.isalpha())
print(num.isalpha())


# isdecimal(): comprueba si todos los caracteres de una cadena son decimales(0-9)

print("Usando la funcion isdecimal()")

print(saludando.isdecimal())
print(num.isdecimal())

# isdegit():comprueba si todos los carecteres de una cadena son numeros(0-9)

print("Usando la funcion isdegit()")

num2 = "30"

print(saludando.isdigit())
print(num2.isdigit())


# isnumeric(): compueba si todos los caracteres de una cadena son numeros  o estan relacionados con numros

print("Usando la funcion isnumeric()")

num3 = '10'
print(num3.isnumeric()) # True
num4 = '\u00BD' # ½
print(num4.isnumeric()) # True
num5 = '10.5'
print(num5.isnumeric()) # False

# isidentifier(): comprueba si hay un identificador valido: comprueva si una cadena es un nombre de variable valido

print("Usando la funcion isidentifier()")

proyec = "30DiasEnPython"
proyec1 = "trenta Dias En Python"

print(proyec.isidentifier())
print(proyec1.isidentifier())

# islower(): comprueba si todos los  caracteres del alfabeto en la cadena estan en minusculas

print("Usando la funcion islower()")

print(proyec.islower())
print(proyec1.islower())

# isupper(): comprueba si todos los caracteres del alfabeto en la cadena estan en mayusculas

print("Usando la funcion islower()")

print(proyec.isupper())
print(proyec1.isupper())

# join(): devuelve una cadena con una separacion indicada.

print("Usando la funcion join()")

leng = ["HTML","CSS","JAVASCRIPT","REACT"]
obje = "Con la nota alta"
union = ",".join(leng)

print(union)
print("#".join(obje))
print(" ".join(obje))


# strip(): elimina todos los caracteres dados comenzando desde el principio u el final de la cadena y tambien puede eliminar espacios en blaco

# NOTA: si le pasas un carecter que esta en medio no lo eliminara, solo elimina el principio y el final de una cadena y los espacios en blanco


print("Usando la funcion strip()")

print(obje.strip("Con"))
print(obje.strip("alta"))
print(obje.strip()) # este elimina los espacios en blanco pero solo del principo y el final de la cadena

# replace(): se utiliza para  reemplazar partes de una cadena por otra cadena

print("Usando la funcion replace()")

cadena_normal = "Hoy es un lindo dia para morir"
cadena_nueva = cadena_normal.replace("morir","Vivir al maximo")
print("La cadena normal es:",cadena_normal)
print("La cadena nueva es:",cadena_nueva)

# split(): divide la cadena, utilizando la cadena dada o el espacio como separador
print("Usando la funcion split()")

reto = "trenta dias en python"
print(reto.split())

reto_2 = "trenta dias en python"
print(reto_2.split(", "))


# title(): Esta funcion se utiliza para convertir la primera letra  de una cadena a mayuscula y la podemos utilizar para los titulos y los nombres propios.
print("Usando la funcion title()")

texto_corto = "hola mundo"
titulo_3 = texto_corto.title()
print(titulo_3)

# swapcase(): Esta funcion se utiliza para invertir las cadenas de mayusculas a minusculas y de minusculas a mayusculas dependiendo el caso.
print("Usando la funcion swapcase()")

texto = "Hola Mundo"
resultado = texto.swapcase()
print(resultado)

# La función startswith() en Python se utiliza para verificar si una cadena comienza con un prefijo específico. Retorna True si la cadena comienza con el prefijo dado y False en caso contrario.
print("Usando la funcion startswith()")
texto = "Hola Mundo"
resultado = texto.startswith("Hola")
print(resultado) 

resultado = texto.startswith("Mundo")
print(resultado)  






























