# CLASE DE DICCIONARIO

# Creando un diccionario

my_diccionario = dict()
my_otro_dict = {}

print(type(my_diccionario))
print(type(my_otro_dict))

# Longitud de un diccionario

my_otro_dict = {
    "nombre":"Oliver",
    "apellido":"Drullard",
    "correo":"gmail.com"
}
print(len(my_otro_dict))

# Accediendo a los elementos de un diccionario

# Con la notacion de corchetes []

print(my_otro_dict["nombre"]) # Si no encuentra la clave dara un error 

# Con el .get()

print(my_otro_dict.get("apellido")) # Con esto manejamos el error, el programa no se detiene si no lo encuentra 
print(my_otro_dict.get("calle","No se encontre el items")) # Con este segundo parametro si el item no se encuentra el resultado sera lo que se indique en el parameto 2

# Agregando elementos a un diccionario 

my_otro_dict["calle"] = "Contreras"
print(my_otro_dict)

# Modificando un elemento del diccionario en python 

my_otro_dict["correo"] = "Contreras.gmail.com"
print(my_otro_dict)

# Comprobando si una clave esta en un diccionario 

print("correo" in my_otro_dict)
print("Direcion" in my_otro_dict)

# Eliminando elementos de un diccionario 

# Con el metodo pop(). Elimina la clave especificada

my_otro_dict.pop("calle")
print(my_otro_dict)

# Con el metodo popitem(). Elimina el ultimo elemento del diccionario 

my_otro_dict.popitem()
print(my_otro_dict)

# Con la funcion del. Elimina un elemento con la clave que se le pase 

del my_otro_dict["apellido"]
print(my_otro_dict)

# Limpiar un diccionario con el metodo clear()

my_otro_dict.clear()
print(my_otro_dict)

# Eliminar un diccionario por completo 

del my_otro_dict
# print(my_otro_dict) NameError: name 'my_otro_dict' is not defined

# Copiar un diccionario 

dicc_productos = {
    "correa":100,
    "zapato":400,
    "camisa":250,
    "reloj":300

}

dicc_productos_copia = dicc_productos.copy()
print(dicc_productos_copia)

# Obtener las claves de un diccionario en forma de lista 
claves = dicc_productos.keys()
print(claves)

# Obtener los valores  de un diccionario en forma de lista 

valores = dicc_productos.values()
print(valores)


