
#Compruebe si el diccionario de la persona tiene la clave de habilidades; de ser así, imprima la habilidad intermedia en la lista de habilidades.
#Verifique si el diccionario de la persona tiene la clave de habilidades; de ser así, verifique si la persona tiene la habilidad 'Python' e imprima el resultado.
#Si una persona tiene habilidades solo JavaScript y React, imprima ('Él es un desarrollador front-end'), si la persona tiene habilidades Node, Python, MongoDB, imprima ('Él es un desarrollador backend'), si la persona tiene habilidades React, Node y MongoDB, Print('Es un desarrollador fullstack'), de lo contrario print('título desconocido'): para obtener resultados más precisos, se pueden anidar más condiciones.
#Si la persona está casada y vive en Finlandia, imprima la información en el siguiente formato:

# Asabeneh Yetayeh vive en Finlandia. Está casado

persona={
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'ciudad': 'Finland',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Compruebe si el diccionario de la persona tiene la clave de habilidades; de ser así, imprima la habilidad intermedia en la lista de habilidades.

if "habilidades" in persona:
    print(persona["habilidades"][2])
else:
    print("Habilidades no esta en persona")
    

# Verifique si el diccionario de la persona tiene la clave de habilidades; de ser así, verifique si la persona tiene la habilidad 'Python' e imprima el resultado.
if "habilidades" in persona:
    if "Python" in persona["habilidades"]:
        print(f"La persona tiene la abilidad {persona["habilidades"][4]}")
    else:
        print("La persona no tiene la habilidad python")

else:
    print("No existe habilidades en persona")


# Si una persona tiene habilidades solo JavaScript y React, imprima ('Él es un desarrollador front-end'), 
# si la persona tiene habilidades Node, Python, MongoDB, imprima ('Él es un desarrollador backend'), si 
# la persona tiene habilidades React, Node y MongoDB, Print('Es un desarrollador fullstack'), de lo contrario 
# print('título desconocido'): para obtener resultados más precisos, se pueden anidar más condiciones.
    
if "JavaScript" in persona["habilidades"] and "React" in persona["habilidades"] and not {'Node', 'MongoDB', 'Python'}.intersection(persona["habilidades"]):
    print("Él es un desarrollador front-end")

elif {"Node","Python","MongoDB"}.issubset(persona["habilidades"]) and not "React":
    print("Él es un desarrollador backend")

elif "Node" in persona["habilidades"] and "MongoDB" in persona["habilidades"] and "React" in  persona["habilidades"]:
    print("Es un desarrollador fullstack")

else:
    print("Titulo desconocido")

