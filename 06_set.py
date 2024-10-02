# Clase de set 

# Creando un set vacio

st = set() # Para crear un set vacio solo se puede usar el constructor de set

# Creando un set con elementos iniciados 

hackers = {"Eliot","Mr.Robot","Anonimos","s4vitar"}

# Obteniendo la longitud del set

print("La longitud del set es: ",len(hackers))

# Accediendo a los elementos de un conjunto 

"""
Como los conjuntos o set son una estructura de dato 
no indexada no podemos acceder a los elementos con 
la notacion de corchetes. para poder acceder a los 
elementos temos que iterarlos con un bucle.
"""

for elementos in hackers:
    print(elementos)

# Verificando la existencia de un elemento en un set

hackers = {"Eliot","Mr.Robot","Anonimos","s4vitar"}
print("Eliot" in hackers)

# Agregar elementos a un conjunto o set

hackers.add("Black hat")
print(hackers)

# Agregar varios elementos a un set con la funcion update()

# Esta funcion recibe una lista como argumento

hackers.update(["white hat","grey hat"])
print(hackers)

# Eleminando elementos de un set con el metodo remove()

hackers.remove("Eliot") # Si el elemento no esta arrojara un error este metodo
print(hackers)

# Eleminando elementos de un set con el metodo discard()

hackers.discard("Mr.Robot")
hackers.discard("Oliv4r") # Si no encuentra el item el metodo solo ignora la accion

# Eleminando elementos de un set con el metodo pop()

hackers.pop() # Este metodo elimina un item aleatorio y lo duelve
hackers_eliminado = hackers.pop() # Asi podemos guardar el item eliminado
print(hackers_eliminado)
print(hackers)

# Eliminado todos los item de un comjunto o set

hackers.clear()
print(hackers)

# Eliminado el set 

#del hackers
#print(hackers) # NameError: name 'hackers' is not defined, esto sucede porque el "del" elimina la variable donde almacenamos la estructura del set

# Comvertir una lista en un set

grupos_de_hackers = ["REvil","DarkSide","Lazarus","Dragonfly","Lapsus$"]

grupos_de_hackers = set(grupos_de_hackers)
print(type(grupos_de_hackers))

# Uniendo set con el metodo union()
nombre_hackers = {"S4vitar","white hat","grey hat","Black hat","Eliot"}

organizaciones = nombre_hackers.union(grupos_de_hackers)
print(organizaciones)

# Uniendo set con el metodo update()

organizaciones_2 = grupos_de_hackers.union(nombre_hackers)
print(organizaciones_2)


# Interseccion en un set, esto devuelve los item que tienen en comun los dos set.

numeros_normales = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10,11,12,13}
print(numeros_normales.intersection(numeros_pares))

# Comprobando si un set es un superset o subset de otro set

print(numeros_normales.issubset(numeros_pares)) # False
print(numeros_normales.issuperset(numeros_pares)) # True

# Encontrando la diferencia entre dos set

diferencia_de_set = numeros_pares.difference(numeros_normales)
diferencia_de_set_2 = numeros_normales.difference(numeros_pares)

print(diferencia_de_set)
print(diferencia_de_set_2)

# Encontrando la diferencia simetrica de dos set con la funcion symmetric_differnce()

difetencia_simetrica = numeros_normales.symmetric_difference(numeros_pares)
print(difetencia_simetrica)

# Comparando si un set es disjunto o no con el metodo isdisjoint()

set_0 = {1,2,3}
set_1 = {1,2,3}
set_2 = {4,5,6}

set_disjunto = set_1.isdisjoint(set_2)
set_disjunto_2 = set_1.isdisjoint(set_0)
print(set_disjunto) # True
print(set_disjunto_2) # False
