# Clases en python 

# Como definimos una Clases en python ?

class MyClase:
    pass


print(MyClase())
print(MyClase)

# Como poduco usar una clase para crear un objeto?

class Persona:
    def __init__(self,nombre,apellido,edad,estatura,sexo):
        # En esta parte creamos la instancia de los datos que vamos almacer en la clase persona
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
        self.sexo = sexo

# persona = Persona("oliver","Drullard",19,5.7,"Masculino") pasamos los datos en el mismos orden en que los creamos en la clase

print(persona.nombre) # Imprimimos el dato nombre porconsola accediendo a el con la notacion de punto y el nombre de la variable donde al macenamos la clase persona
