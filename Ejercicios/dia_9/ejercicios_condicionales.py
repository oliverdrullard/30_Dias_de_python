### EJERCICIO NIVEL 1 ###

"""
Obtenga la entrada del usuario mediante input(“Ingrese su edad: ”). 
Si el usuario tiene 18 años o más, proporcione comentarios: 
Tiene la edad suficiente para conducir. Si es menor de 18 años, 
proporcione comentarios para esperar la cantidad de años faltantes. 
"""

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para condicir")
else:
    print("Eres menor, no puedes conducir")


### EJERCICIO NIVEL 2 ###

"""
Compara los valores de my_age y your_age usando if … else. 
¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad: ”) 
para obtener la edad como entrada. Puedes usar una condición 
anidada para imprimir 'year' para una diferencia de edad de 1 año,
'years' para diferencias mayores y un texto personalizado
si my_age = your_age.

"""

mi_edad = int(input("Ingresa tu edad: "))
otra_edad = int(input("Ingresa la edad a comparar: "))

if mi_edad > otra_edad:
    print("Yo soy mayor que tu")
elif mi_edad < otra_edad:
    print("Soy menor que tu")
elif mi_edad == otra_edad:
    print("Tenomos la misma edad")
else:
    print("Edades no validadas")