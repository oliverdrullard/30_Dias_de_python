# Ejercicios de tupla

# Nivel 1

#1 Crea una tupla vacia

my_tuple = tuple()
my_nw_tuple = ()

#2 Crea dos tupla que contenga los nombres de tus hermanas y hermanos

hermanos = ("mr.Robot","Linux Torvalds","Nicolas Churman","Brais moured")
hermanas = ("Mary Kenneth Keller","Evelyn Berezin","Margaret Hamilton","Adele Goldberg")

print(hermanos)
print(hermanas)

#3 Unir tuplas de hermanos y hermanas y asignarlas a hermanos

hermanos = hermanos + hermanas
print(hermanos)

#4 Cuantos hermanos tienes?

print(len(hermanos))

#5 Modifica la lista de hermanos y agregale el nombre de tu padre y madre y signalo a familia_miembros

hermanos = list(hermanos)

hermanos.append("Ada Lovelace")
hermanos.append("Alan turing")

familia_miembros = tuple(hermanos)
print(familia_miembros)

# Nivel 2

#1 Desempaqueta hermanos y padres de familia

her_1, her_2, her_3, her_4, her_5, her_6, her_7, *her_8, = hermanos 

print(her_1)
print(her_2)
print(her_3)
print(her_4)
print(her_5)
print(her_6)
print(her_7)
print(her_8)

#2 Crea tuplas de frutas, verduras, y productos animales. une las  tres frutas y asignalas a una variable llamada food_stuff_tp 


frutas = ("Manzana","guineo","Pera","Zandia","Melon")
verduras  = ("Lechuga","Espinaca","cilantro","","Brocoli")
productos_animales = ("Manzana","guineo","Pera","Zandia","Melon")

food_stuff_tp = frutas + verduras + productos_animales
print(food_stuff_tp)

#3 Cambia la tupla food_stuff_tp a una lista food_stuff_lt

food_stuff_lt = list(food_stuff_tp) 
print(type(food_stuff_lt))

#4 Extraiga el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista  food_stuff_lt

print(food_stuff_lt[7:8])

#5 Separe los primeros tres elementos y los ultumos tres elementos de la lista food_staff_lt

primeros_item = food_stuff_lt[0:4]
ultimos_item = food_stuff_lt[12:15]

print(primeros_item)
print(ultimos_item)

#6 Elimia la tupla food_staff_tp por completo

del food_stuff_tp
# print(food_staff_tp) NameError: name 'food_staff_tp' is not defined. Did you mean: 'food_stuff_lt'?

#7 Comprueba si un elemeto existe en una lista

frutas = ("Manzana","guineo","Pera","Zandia","Melon")
print("Manzana" in frutas)

#8 Comprueba si Estonia es un pais nordico

paieses_nordicos = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in paieses_nordicos)

#9 Comprueba si Islandia es un pais nordico
print("Islandia" in paieses_nordicos)


#10 Impreme el index de un item de paieses_nordicos

print(paieses_nordicos.index("Finland"))


#10 Encuentra la concurencia de un item en paises nosdicos

print(paieses_nordicos.count("Iceland"))


