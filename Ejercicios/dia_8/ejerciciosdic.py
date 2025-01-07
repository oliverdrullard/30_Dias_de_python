# Ejercicios de diccionarios

# Crea un diccionario vacío llamado perro

perro = dict()

# Añade nombre, color, raza, patas y edad al diccionario de perros

perro["nombre"] = "Rex"
perro["raza"] = "chiguagua"
perro["patas"] = "pequeñas"
perro["edad"] = 5
perro["color"] = "negro"

print(type(perro))
print(perro)

# Cree un diccionario de estudiantes y agregue nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario

estudiantes = {
    "nombre":"Oliver",
    "apellido":"Drullard",
    "género":"masculino",
    "edad":23,
    "estado civil":"Soltero",
    "habilidades":["python","django","mysql","git"],
    "país":"Republica Dominicana",
    "ciudad ":"Santiago",
    "direccion":"calle/casa/sector"

}
print(estudiantes)

# Obtenga la longitud del diccionario del estudiante

print(len(estudiantes))

# Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista

print(estudiantes["habilidades"])
print(type(estudiantes["habilidades"]))

# Modifique los valores de las habilidades agregando una o dos habilidades

estudiantes["habilidades"].append("posgretsql") 
estudiantes["habilidades"].append("githud")
print(estudiantes)

# Obtenga las claves del diccionario como una lista

print(estudiantes.keys())

# Obtener los valores del diccionario como una lista

print(estudiantes.values())

# Cambie el diccionario a una lista de tuplas usando el método items()

list_tupla = estudiantes.items()
print(list_tupla)
print(type(list_tupla))

# Eliminar uno de los elementos del diccionario

estudiantes.pop("edad")
print(estudiantes)

# Eliminar uno de los diccionarios

del perro