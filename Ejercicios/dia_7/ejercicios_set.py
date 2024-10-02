# Jercicios de set

# NIVEL 1

#1 Encuentra la longitud de un set it_compani

it_compani = {"Facebook","Microsoof","Appel","Cisco"}
print(len(it_compani))

#2 Añadir Twitter a it_compani

it_compani.add("Twitter")
print(it_compani)

#3 Añadir varias empresas de TI a la vez en el set it_compani

it_compani.update(["Alphabet ","Amazon","Samsung","Tencent "])
print(it_compani)

#4 Eliminar  una de las empresas del set de it_compani

it_compani.remove("Cisco")
print(it_compani)

#5 Cual es la diferencia de eliminar un elemento con discard() y remove()

# El remove arroja un error si no encuentra el item que va a eliminar  y el discard no

it_compani.discard("Alphabet") 
it_compani.discard("oliver") # Esto no romperia el programa
# it_compani.remove("oliver")  Esto romperia el programa
print(it_compani)

# NIVEL 2 ####

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1 Unir A y B

union_set = A.union(B)
print(union_set)

#2 Encuentra la interseccion de A y B 

interseccion_it = A.intersection(B)
print(interseccion_it)

#3 A es un subconjunto de B

print(A.issubset(B))

#4 Son A y B set disjuntos?

print(A.isdisjoint(B))

#5 Unir A con B y B con A

unir_A_B = A.union(B)
unir_B_A = B.union(A)
print(unir_A_B)
print(unir_B_A)

#6 Cual es la diferencia simetrica entre A y B ?

difetencia_simetrica = A.symmetric_difference(B)
print(difetencia_simetrica)

#7 Elimina por completo los dos set

del A,B

# NIVEL 3

edad = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?

edad_set = set(edad)
print("La longitud de la lista es: ",len(edad)) # La longitud de la lista es mayor
print("La longitud del set es: ",len(edad_set)) 

#2 Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y set.

"""
Una cadena es un texto. Una lista es un conjunto de datos, mutable, indexada, y
acepta repetidos. Una tubla es un conjunto de datos inmutable, indexada y acepta
repetidos. Un set es un conjunto de datos que no es indexada, no acepta repetidos
y es mutable.

"""
#3 Ejercicio

"""
Soy profesor y me encanta inspirar y enseñar a la gente.
¿Cuántas letras únicas se han utilizado en la oración? 
Utilice los métodos de división y de configuración para 
obtener las palabras únicas.

"""
texto = "Soy profesor y me encanta inspirar y enseñar a la gente"
texto_set = set(texto)
palabras_unicas = len(texto_set)
print("La cantidad de palabras unicas son: ",palabras_unicas)
print(texto_set)