# Funciones 


# funcion sin parmetros

def nombre_full():
    nombre = "Oliver"
    apellido = "Drullard"
    space =" "
    nombre_completo = nombre + space + apellido
    print(nombre_completo)

nombre_full() # Aqui estamos llamando la funcion para poder usarla

# Si una funcion no tiene un valor de retorno su resultado es none 

def nombre_full():
    edad = 25
    nombre = "Oliver"
    apellido = "Drullard"
    space =" "
    nombre_completo = nombre + space + apellido
    return nombre_completo

nombre_full() # Si lo tramos de imprimir o retornar la funcion asi no funconara

print(nombre_full()) # Cuado usamos un return debemos imprimir el resultado con la funcion print


### Funcion con parametros ###

# En una función podemos pasar diferentes tipos de datos 
# (número, cadena, booleano, lista, tupla, diccionario o conjunto) 
# como parámetro.

def saludar(persona):  # persona que esta dentro del parentecis se conose como parametro
    mensaje = persona + "Bienvenido a python por siempre!"
    return mensaje

print(saludar("Oliver")) # Oliver es el argumento que va a tomar la funcion para crear el saludo

# Podemos hacer funcione como por ejemplo para sumar un numero con otro
# Las funcion pueden aceptar todos los argumentos que le queramos pasar 

def sumar(numero_1, numero_2):
    total = numero_1 + numero_2
    return total

print(sumar(5,2))

# Podemos hacer algo paresido a los diccionario con las funciones 
# pasandole clave valor

def nombre_full_clave_valor(nombre,apellido):
    space =" "
    nombre_completo = nombre + space + apellido
    return nombre_completo

print(nombre_full_clave_valor(nombre = "Oliver", apellido = "Drullard"))

# Funcion con parametros determinados

def saludando(nombre = "Oliver"):
    mensaje = nombre + " Bienvenido a python la pasaras bien!"
    return mensaje

print(saludando()) # Aunque la funcion acepte parametros, en este caso puedes pasarselo o no porque la le damos un valor en la definicion de la funcion
print(saludando("Drullard"))

# Funcion con argumentos infinitos

# podemos crear un funcion que tenga todos los argumentos que el pases

def sumando_numeros(*args): # El * lo que indica que va a aceptar todos los argumentos que le pasen
    total = 0
    for i in args:
        total += i
    return total

print(sumando_numeros(1,2,3,4))

