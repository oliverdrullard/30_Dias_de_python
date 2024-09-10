#  EJERCICIOS DE LISTAS EN PYTHON

#1 Declarar una lista vacía
lista_1 = []

#2 Declarar una lista con más de 5 elementos
lista_2 = [1,2,3,4,5,6,7,8]

#3 Encuentra la longitud de tu lista
lista_2 = [1,2,3,4,5,6,7,8]
print(len(lista_2))

#4 Obtener el primer elemento, el elemento del medio y el último elemento de la lista
lista_2 = [1,2,3,4,5,6,7,8]

print(lista_2[0])
print(lista_2[3])
print(lista_2[7])

#5 Declara una lista llamada mixed_data_types, coloca tu(nombre, edad, altura, estado civil, dirección)

mixed_data_types = ["Oliver",24,5.9,"Soltero","Calle 46 casa 38 cienfuegos"]

#6 Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Amazon"]

#7 Imprima la lista usando print()

print(mixed_data_types)

#8 Imprima el número de empresas en la lista

print(it_companies)

#9 Imprima la primera, la segunda y la última empresa.

print(it_companies[0:3])

#10 Imprima el listado después de modificar una de las empresas

it_companies[4] = "Cisco"
print(it_companies)

#11 Añadir una empresa de TI a it_companies

it_companies.append("Ablerex Latam")
print(it_companies)

#12 Insertar una empresa de TI en el medio de la lista de empresas

it_companies.insert(3,"ADATEC SAS")
print(it_companies)

#13 Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)

it_companies[0] = it_companies[0].upper()
print(it_companies)

