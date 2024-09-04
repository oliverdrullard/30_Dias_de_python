# Creando sin datos listas

lst = list() # Creando listas con el constructor de listas
my_lst = [] # Creando listas con el la sintaxis de coorchetes

# Imprimiendo la longitud   y el tipo de dato de las listas 

print(len(lst))
print(len(my_lst))

print(type(lst))
print(type(my_lst))

# Creando listas con datos

fruta = ["uva","manzana","mango","aguacate"]
vegetales = ['Tomate', 'zanaoria', 'aji','ajo', 'apio']     
animal = ['perro', 'caballo', 'gato', 'gallo']             
tecnologias = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 
paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

print("Lista de Frutas: ",fruta)
print("Lista de Vegetales: ",vegetales)
print("Lista de Animal: ",animal)
print("Lista de Tecnologias: ",tecnologias)
print("Lista de paises: ",paises)

print("Fruta_logitud: ",len(fruta))
print("Vegetales_logitud: ",len(vegetales))
print("Animal_logitud: ",len(animal))
print("Tecnologias_logitud: ",len(tecnologias))
print("Paises_logitud: ",len(paises))

# Creando listas con diferentes tipos de datos

lst = ["Oliver", 50, 1.25, True,]

print("lst ",lst)

# Accediendo a los elementos de una lista por los index positivos

fruta = ["uva","manzana","mango","aguacate"]

print(fruta[0]) # Esto imprimira el primer elemento de la lista
print(fruta[1]) # Esto imprimira el segundo elemento de la lista

last_index = len(fruta) - 1 # Esta sintaxis cuenta los elementos de la lista exculendo al uno de los elementos
print(last_index)

# Accediendo a los elementos de una lista por los index negativos

tecnologias = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
print(tecnologias[-1])
print(tecnologias[-2])
print(tecnologias[-3])

# Desempaquetando elementos de una lista 

vegetales = ['Tomate', 'zanaoria', 'aji','ajo', 'apio'] 

itm_1, itm_2, itm_3, itm_4, itm_5, = vegetales

print(itm_1)
print(itm_2)
print(itm_3)
print(itm_4)
print(itm_5)

# Si no conoses el numero de elementos que tiene la lista puedes usar lo sigiente o para ahorar escritura usa lo siguiente

paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

itm_1, itm_2, itm_3, itm_4, *itm_5, = paises

print(itm_1)
print(itm_2)
print(itm_3)
print(itm_4)
print(itm_5)

# Separando elementos de una lista con index positivos

animal = ['perro', 'caballo', 'gato', 'gallo']  

print(animal[0:4]) # Tomar en cuenta que esto excluye el ultimo uno menos del rando 
print(animal[0:]) # Esta imprime la lista completa
print(animal[1:3]) # Esta solo imprime el elemento 1 y el dos ya que el tres python lo excluye
print(animal[1:]) # Esta imprime todos los elementos excluendo al primero que es en el indexe 0
print(animal[::2]) # lista[inicio:fin:paso]

# Separando elementos de una lista con index negativos

paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

print(paises[-1:])
print(paises[-4:])  
print(paises[-3:-1]) 
print(paises[-3:]) 
print(paises[::-1]) 

# Modificacion de una lista 

paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

# En esta parte se esta modificando la lista por el numero de posicion en la que se encuentra

paises[0] = "Republica Dominicana" 
print(paises)

paises[1] = "japon"
print(paises)

# Comprobando elementos en una lista 
# NOTA: La palabra tiene que estar escrita como esta en la lista, si esta en mayusculas y la buscas en minusculas dara false 
paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

print("Filandi" in paises) # El (in) se usa para comprobar si el elemento se encuentra en la lista 

iten = "Autralia" in paises
print(iten)

# Agregando elementos a una lista 

# Para agragar un elemento a las lista se usa el metodo append(), con el punto delante
animal = ['perro', 'caballo', 'gato', 'gallo']

animal.append("Vaca")
animal.append("Lobo")
print(animal)

# Insertar elementos en una lista

# Usando el metodo insert(), esta funcion recibe dos argumentos, el primero la pocion donde se va a insertar el elemento y el segundo el elemento que se quiere insertar

vegetales = ['Tomate', 'zanaoria', 'aji','ajo', 'apio']  

vegetales.insert(0,"lechuga")
vegetales.insert(3,"silantro")

print(vegetales)

# Eliminando elementos de una lista mediante el remove()

tecnologias = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']

tecnologias.remove("Redux")
print(tecnologias)

# Eliminando elementos de una lista mediante el pop(), esta elimina el index especificado o el ultimo de la lista si no se especifica.

tecnologias = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']

tecnologias.pop() # Este elimina el ultimo de la lista
tecnologias.pop(0) # Este elimina el elemento que esta en la posicion 0  de la lista
print(tecnologias)

# Eliminando elementos de una lista mediante el del(),La palabra clave del elimina el índice especificado y también se puede utilizar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.

paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

del paises[0] # Eliminando el primer elemento
print(paises)

del paises[1] # Eliminando el segundo  elemento 
print(paises)

del paises[2:3] # Eliminando un rando de itens
print(paises)

del paises # Eliminando la lista completa, al imprimir la lista en este punto no saldra nada en consolo o un error porque la lista no estara definida


# Vaciendo un lista o borrando los itens que tiene dentro, metodo a utilizar .clear()
            
tecnologias = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 

tecnologias.clear() # Esto vacia la mista por completo

print("Lista de tecnologia",tecnologias)

# Copiando un lista

"""
Es posible copiar una lista reasignándola a una nueva variable 
de la siguiente manera: list2 = list1. Ahora, list2 es una referencia 
de list1, cualquier cambio que hagamos en list2 también modificará la 
original, list1. Pero hay muchos casos en los que no queremos modificar 
la original, sino que queremos tener una copia diferente. Una forma de 
evitar el problema anterior es usar copy() .

"""

fruta = ["uva","manzana","mango","aguacate"]

fruta_dos = fruta.copy()

print(fruta_dos)


# Unirse a listas

# Uniendo lista o concatenando con el operador (+)

tecnologias = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 
paises = ['Filandi', 'Estados unidos', 'Canada', 'Mexico', 'Nueva zelanda']

print(tecnologias + paises)

#  Uniendo lista o concatenando con el operador .extend()

nun_1 = [1,2,3,4,5]
nun_2 = [-1,-2,-3,-4,-5]

nun_1.extend(nun_2)

print(nun_1)

# Contando elementos en una lista, el metodo .count() devuelve el numero de veces que parese un elemento en una lista 

fruta = ["uva","manzana","mango","aguacate","uva"]
vegetales = ['Tomate', 'zanaoria', 'aji','ajo', 'apio'] 

print(fruta.count("uva"))
print(vegetales.count("zanaoria"))

# Cómo encontrar el índice de un elemento, para esto se utiliza el metodo .index()

vegetales = ['Tomate', 'zanaoria', 'aji','ajo', 'apio']

print(vegetales.index("aji"))

edades = [22, 19, 24, 25, 26, 24, 25, 24]

print(edades.index(24))

# Invertir una lista

# Invertir una lista con el metodo .reverse()

animal = ['perro', 'caballo', 'gato', 'gallo']  

animal.reverse()

print(animal)

edades = [22, 19, 24, 25, 26, 24, 25, 24]

edades.reverse()

print(edades)

# Ordenar elementos de la lista

# Utilizando el metodo sort()

lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = ["alfabeto","brazo","casa","desorden","eficiente","felis"]

lista_1.sort() # Deforma acendente
print(lista_1)

lista_1.sort(reverse = True) # Deforma decendente
print(lista_1)

lista_2.sort()  # Deforma acendente
print(lista_2)

lista_2.sort(reverse = True) # Deforma decendente
print(lista_2)

# Utilizando el metodo sorted(),devuelve la lista ordenada sin modificar la lista original

lista_1 = [10,3,2,4,5,6,8,7,9,1]


print(sorted(lista_1,reverse=True))
print(sorted(lista_1))


"""
Para ordenar listas podemos utilizar el método sort() o las 
funciones integradas de sorted() . El método sort() reordena 
los elementos de la lista en orden ascendente y modifica la 
lista original. Si un argumento del método sort() reverse es 
igual a true, ordenará la lista en orden descendente.

"""


























