# Dia 2 de 30 en programcion en python 

# Declaracion de variables

# Ejercicios nivel 1

nombre = "Oliver"
apellido = "Drullard"
nombre_completo = "Oliver Drullard"
pais = "Republica Dominicana"
ciudad = "Santiago"
edad = 25
year = 2024
is_married = 30
is_true = True
is_light_on = False

auto,casa,luces,cosas = "toshiba",25,True,"nada bueno"


# Ejercicio nivel 2 

# 1

print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(auto))
print(type(casa))
print(type(luces))
print(type(cosas))

# 2 

print(len(nombre))
print(len(apellido))

# 3

print(len(nombre) == len(apellido))

# 4

num_uno = 5 
num_dos = 4

total = num_uno + num_dos

diferencia = num_dos - num_uno

producto = num_dos * num_uno

divicion = num_uno / num_dos

modludo = num_uno % num_dos

exp = num_uno ** num_dos

floor_division = num_uno // num_dos

print(total)
print(diferencia)
print(producto)
print(divicion)
print(modludo)
print(exp)
print(floor_division)


# 5

# Radio de un circulo 

area_del_circulo = 3.14 * 30 ** 2

# Circunferencia de un circulo

circum_del_circulo = 3.14 * 30

# Tomando los datos desde el teclado 

radio = input("Ingrese el radio del circulo: ")

area = 3.14 * pow(float(radio),2)

print(area_del_circulo)
print(circum_del_circulo)
print(radio)
print(area)

# 6

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su pais: ")
edad = input("Ingrese su edad: ")

print("Su nombre es: ",nombre,"Su apellido es: ",apellido,"Su pais es: ",pais,"y tiene: ",edad,"años")

# 7

# Entrar a la shell y ejecutar el comando help y luego keywords para saber las palabras recervasas del lenguaje

"""
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


"""
