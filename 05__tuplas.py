# CLASE DE TUPLA

# Creando una tupla 

mi_tuple = ()
mi_otra_tubla = tuple()

tpl = ("Coordenadas", "Valores costantes", "lista de compras")

# Longitud de una tupla 

print("Longitud de la lista: ",len(tpl))

# Acceder a elementos de tuplas

frutas = ("Uva", "Manzana", "Pera", "Sandia", "Melon", "Piña")

print(frutas[0])
print(frutas[1])
print(frutas[3])
print(frutas[4])
print(frutas[-1])

# por el indixe negativo

print(frutas[-1])
print(frutas[-3])
print(frutas[-4])


# Cortando tuplas 

frutas = ("Uva", "Manzana", "Pera", "Sandia", "Melon", "Piña")

tupla_1 = frutas[0:2]
tupla_2 = frutas[2:4]
tupla_3 = frutas[4:]
print(tupla_1)
print(tupla_2)
print(tupla_3)

print(frutas[::-1])

# Cambiar tuplas a listas 

frutas = list(frutas)
print(type(frutas))

frutas = tuple(frutas) # Cambiendo otra ves a tupla

# Comprobacion de un elemento en una tupla

print("Uva" in frutas)
print("guineo" in frutas)
print("Manzana" in frutas)
print("Melocoton" in frutas)

# Unir tuplas 

tecnologias = ("python","dejando","mysql","postgresql")
herramientas = ("Doker","git","githud","linux")

stend_tecnologico = tecnologias  + herramientas

print(stend_tecnologico)

# Eliminar tuplas 

del frutas

# print(frutas) NameError: nombre 'frutas' no esta  definido