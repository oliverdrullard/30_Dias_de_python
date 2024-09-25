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

print(len(it_companies))

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

#14 Unir it_companies con una lita '#; '

nw_list_separador = "#;".join(it_companies)
print(nw_list_separador)

#15 Comprueba si una determinada empresa existe en la lista it_companies.

print("Diversity" in it_companies) # Flase
print("Microsoft" in it_companies) # True

#16 Ordenar la lista usando el método sort()

it_companies.sort()
print(it_companies)

#17 Invierta la lista en orden descendente utilizando el método reverse()

it_companies.reverse()
print(it_companies)

it_companies.sort(reverse = True)
print(it_companies)

#18 Separa las primeras 3 empresas de la lista

empresas_primarias = it_companies[0:3]
print(empresas_primarias)

#19 Elimina las últimas 3 empresas de la lista

del it_companies[5:8]
print(len(it_companies))
print(it_companies)

#20 Elimina de la lista las empresas de TI intermedias

it_companies.pop(2)
print(it_companies)

#21 Eliminar la primera empresa de TI de la lista

it_companies.remove("Microsoft")
print(it_companies)

#22 Eliminar la última empresa de TI de la lista

it_companies.pop(2)
print(it_companies)

#23 Eliminar todas las empresas de TI de la lista

it_companies.clear()
print(it_companies)

#24 Destruir la lista de empresas de TI

del it_companies

#25 Únete a las siguientes listas

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

#26 Después de unir las listas de la pregunta 26, copie la lista unida y asígnela a una variable full_stack. Luego inserte Python y SQL después de Redux.

full_stack = front_end.copy()
print(full_stack)