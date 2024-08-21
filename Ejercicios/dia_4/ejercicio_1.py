# Concatenado cadenas

# Ejercicio_1

string_1 = "Trenta"
string_2 = "Dias"
string_3 = "De"
string_4 = "Python"

string_cantenado = string_1 + " " + string_2 + " " + string_3 + " " + string_4

print(string_cantenado)

# Ejercicio_2

fracmento_1 = "Codificando"
fracmento_2 = "Para"
fracmento_3 = "Todos"

titulo_completo = fracmento_1 + " " + fracmento_2 + " " + fracmento_3

print(titulo_completo)

# Ejercicio_3

empresa = "Codificando para todos"

# Ejercico_4

print(empresa)

# Ejercicio_5

print(len(empresa))

# Ejercicio_6

empresa_mayusculas = empresa.upper()

print(empresa_mayusculas)

# Ejercicio_7

empresa_minusculas = empresa.lower()

print(empresa_minusculas)

# Ejercicio_8

print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

# Ejercicio_9

primera_palabra = empresa[0:11]

print(primera_palabra)

# Ejercico_10

concurenaci = empresa.find("Codificando")
print(concurenaci)

if concurenaci != -1:
    print(f"La cadena se encuenta {concurenaci}")
else:
    print(f"La cadena no encuenta {concurenaci}")


# Ejercicio_11

new_empresa = empresa.replace("Codificando","Python")

print(new_empresa)

# Ejercicio_12

new_1_empresa = empresa.replace("todos","principiantes")
print(new_1_empresa)

# Ejercicio_13

texto = "Coding For All"
cadena_dividida = texto.split()

print(cadena_dividida)

# Ejercicio_14 

empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_empresas = empresas.split(", " )

print(lista_empresas)

# Ejercicio_15

# ¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos ?

titulo_2 = "Codificando para  todos"

print("En el indice 0 esta la ",titulo_2[0]) # C

# Ejercicio_16

# ¿Cuál es el último índice de la cadena Codificación Para Todos ?

print("El ultimo indice es el",len(titulo_2))

# Ejercicio_17 

# ¿Qué carácter está en el índice 10 en la cadena "Codificación para todos"?

print("En el indice 10 esta la ",titulo_2[10]) # o

# Ejercicio_18

# Crea un acrónimo o una abreviatura para el nombre 'Python para todos'

lo_mejor = "Python para todos"

letra_1 = lo_mejor[0]
letra_2 = lo_mejor[7]
letra_3 = lo_mejor[12]

acronimo = letra_1 + letra_2 + letra_3

print(acronimo.upper())


# Ejercicio_19

# Crea un acrónimo o una abreviatura para el nombre 'Coding For All'

lo_mejor = "Coding For All"

letra_01 = lo_mejor[0]
letra_02 = lo_mejor[7]
letra_03 = lo_mejor[11]

acronimo_01 = letra_01 + letra_02 + letra_03

print(acronimo_01.upper())

# Ejercicio_20

# Utilice el índice para determinar la posición de la primera aparición de C en Codificación para todos

cadena_nueva = "Codificación para todos"

print("La Primera letra C se encuentra en el indice 0: " + cadena_nueva[0])

# Forma de hacerlo utilizando el ciclo for
for indice, caracter in enumerate(cadena_nueva):
    print(f"La letra:{caracter} se encuentra en el indice:{indice}" )


# Ejercicio_21

# Utilice el índice para determinar la posición de la primera aparición de F en Codificación para todos

cadena_nueva_01 = "Codificación para todos"

posicion_f = cadena_nueva_01[4]

print(f"La primera {posicion_f} que aprece en la cadena es la posicion numero 4" )


# Ejercicio_22

# Utilice rfind para determinar la posición de la última aparición de l en Coding For All People

cadena_nueva_02 = "Coding For All People"

ultima_aparicion_l = cadena_nueva_02.rfind("l")

print(f"La ultima l que aparece esta en la posicion {ultima_aparicion_l}")


# Ejercicio_23

# Utilice index o find para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

cadena_mas_larga = "No puedes terminar una oración con porque porque porque es una conjunción"

print(cadena_mas_larga.find("because"))

# Ejercicio_24

# Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

cadena_un_poco_mas_larga = "No puedes terminar una oración con porque porque porque es una conjunción"

print(cadena_un_poco_mas_larga.rindex("porque"))

# Ejercicio_25

# Elimina la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

cadena_para_reemplasar = "No puedes terminar una oración con porque porque porque es una conjunción"

nueva_cadena = cadena_para_reemplasar.replace("porque","")

print(nueva_cadena)

# Ejercicio_26

# Encuentra la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

cadena_nueva_03 = "No puedes terminar una oración con porque porque porque es una conjunción"

print(cadena_nueva_03.find("porque"))


# Ejercicio_30

# Codificación para todos', elimina los espacios finales izquierdo y derecho en la cadena dada

cadena_4 = "  Codificación para todos  "

print(cadena_4.strip())

# Ejercicio_31

# ¿Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier()?

variable_1 = "30 días de Python"
variable_2 = "Treinta días de Python"

print(variable_1.isidentifier()) # Las dos variables son falsas.
print(variable_2.isidentifier())


# Ejercicio_32

# La siguiente lista contiene los nombres de algunas bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacios.

librerias =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

cambiando = " # ".join(librerias)

print(cambiando)


# Ejercicio_33

# Utilice la secuencia de escape de nueva línea para separar las siguientes oraciones

oracion_1 = "I am enjoying this \n challenge"
oracion_2 = "I just wonder \n what is next"

print(oracion_1)
print(oracion_2)


# Ejercicio_34

# Utilice una secuencia de escape de tabulación para escribir las siguientes líneas

linea_1 = "Name\tAge\tCountry\tCity"
linea_2 = "Asabeneh\t250\tFinland\tHelsinki"

print(linea_1)
print(linea_2)

# Ejercicio_35

# Utilice el método de formato de cadena para mostrar lo siguiente

radio = 10 
area = 3.14 * radio ** 2

print(f"El area del circulo con un radio de {radio} es {area} metros")

# Ejercicio_36
# Realice lo siguiente utilizando métodos de formato de cadena

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

