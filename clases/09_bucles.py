### Bucles ###

# bucle while

contador = 0
contador1 = 0
contador2 = 0

while contador < 5:
    print(contador)
    contador +=1

# Creando un el en un while con un else

while contador2 < 5:
    print(contador2)
    contador2 = contador2 + 1
else:
    print(f"Se detiene la ejecucion: {contador2}")

# Usando la break en los Bucles

while contador1 < 5:
    print(contador1)
    contador1 +=1
    if contador1 == 3:
        break # Detiene el bucle

# Usando la continue en los bucle

while contador1 < 5:
    print(contador1)
    contador1 +=1
    if contador1 == 3:
        continue # Detiene la iteracion actual y continuar con la siguiente
    print("contador1")
    contador1 = contador1 + 1

# Bucle for

# El bucle for nos sirve para iterar los elementos en python

numeros =[0, 1, 2, 3, 4, 5]

for i in numeros:
    print(i)

# Tambien podemos iterar cadenas de textos

lenguage = "Python"

for i in lenguage:
    print(i)


for i in range(len(lenguage)):
    print(lenguage[i])

# Con el bucle for podemos iterar tanto listas, tuplas, set, y cadenas de textos

# Iterando un diccionario

persona = {
    'Nombre':'Asabeneh',
    'Apellido':'Yetayeh',
    'edad':250,
    'ciudad':'Finland',
    'estado':True,
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'Direccion':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# imprimiendo solo las llaves

for key in persona:
    print(key)

# imprimiendo solo las llaves y los valores

for key, valor in persona.items():
    print(key, valor)

# Usadando la funcion rango para los bucle

# La funcion rango() acepta tres parametros (inicio,fin,paso)

lista = list(range(11)) # Esta empiesa en 0 y termina en 10 con un incremento de 1 en 1
print(lista)

lista2 = list(range(1,11)) # Esta empiesa en 1 y termina en 10 con un incremento de 1 en 1
print(lista)

lista3 = list(range(0,11,2)) # Esta empiesa en 0 y termina en 10 con un incremento de 2 en 2
print(lista)

# Usandola en un bucle for

for i in range(11):
    print(i)

# Bucles anidados

for key in persona: # iteramos todas las claves 
    if key == "habilidades": # Si encontramos una clave llamada Habilidades 
        for habilidad in persona["habilidades"]: # iteramos lo que tenga esa clave
            print(habilidad) # imprimimos las habilidades

# para ejecuar un mensaje cuando finaliza el bucle podemos usar el else

for key in persona: # iteramos todas las claves 
    if key == "habilidades": # Si encontramos una clave llamada Habilidades 
        for habilidad in persona["habilidades"]: # iteramos lo que tenga esa clave
            print(habilidad) # imprimimos las habilidades

else:
    print("La ejecucion se detiene")