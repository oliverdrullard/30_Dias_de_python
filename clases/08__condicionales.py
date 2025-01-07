# CONDICIONALES EN PYTHON

"""
    Una condicion en python es una regla que se tiene que complir para 
    que se ejecute una linea o bloque de codigo.
"""

# Sintaxis 

"""
    if condicion:
        Instrucciones a realisar
"""
# Ejemplo



a = 3
#Este bloque de codigo se ejecutara siempre que la condicion sea verdadera,si la condición es falsa no imprimira nada 
if a > 0:
    print("3 es mayor que 0")

# Para devolver algo cuando la candicion es falsa debemos hacer uso del (else)

# Sintaxis 

"""
    if condicion:
        Instrucciones a realisar
    else:
        Instrucciones a realisar

"""
# Ejemplo

a = 3

if a < 0:
    print("a es menor que 0")
else:
    print("a es mayor que 0")

# Si tenemos que hacer ultiples condiciones para determinar que es lo que pasara usamos (elif)

# Sintaxis 

"""
if condition:
    code
elif condition:
    code
else:
    code

"""

# Ejemplo

a = 0 

if a > 0:
    print("3 es mayor que 0")
elif(a < 0):
    print("a es menor que 0")
else:
    print("a es igual a 0")

# Las condicionales se pueden anidar 

# Ejemplo

a = 33

if a > 0:
    if a % 2 == 0:
        print("A es un numero positivo y en entero")
    else:
        print("A no es un numero positivo")
elif a == 0:
    print("A es igual a cero")
else:
    print("A es un nuemro negativo")

# Podemos evitar hacer condiciones anidadas utilizando el operador logico (Y)

a = -43

if a > 0 and a % 2 == 0:
    print("A es un numero positivo entero")
elif a > 0 and a % 2 != 0:
    print("A es un numero no entro positivo")
elif a == 0:
    print("A es igual a 0")
else:
    print("es un numero negativo")


# Tambien podemos usar el operador (or)

usuario = "Oliver"
clave_acceso = 3

if usuario == "admin" or clave_acceso >= 4:
    print("Acceso correcto")
else:
    print("La clave o el correo no es valido")
