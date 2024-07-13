# Nombre de variables correctas en python


"""
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if
year_2021
year2021
current_year_2021
birth_year
num1
num2
"""

# nombres de variables no validos

"""
first-name
first@name
first$name
num-1
1num

"""

# Declarando varibles con nombres significativos 

# Variables en pytho
nombe = "Oliver"
apellido = "Drullard"
pais= "Republica Dominicana"
ciudad = "Santiago"
edad = 25
licencia_para_conducir = True

lenguajes = ['HTML', 'CSS', 'JS', 'React', 'Python']

informacio_persona = {
   "nombre":"Oliver",
   "apellido":"Drullard",
   "pais":"Republica Dominicana",
   "ciudad":"Santiago"
   }

# Utilizando la funcion print() para inprimir los datos

print("Nombre:",nombe)
print("Apellido:",apellido)
print("Pais:",pais)
print("Ciudad:",ciudad)
print("Edad:",edad)
print("Licencia para conducir:",licencia_para_conducir)
print("Lenguajes:",lenguajes)
print("Informacion:",informacio_persona)

# Declaracion de variables en una sola linea

marca,procesador,pantalla,teclado,memoria = "Toshiba","i3",24,"mecanico",8.3

print(marca)
print(procesador)
print(pantalla)
print(teclado)
print(memoria)

# Utilizando la funcion input 

neme = input("Ingrese su nombre")
edad2 = input("Ingrese su edad")

print(neme)
print(edad2)

# Utilizando la funcion type() para saber los timos de datos

first_name = 'Olvier'     # str
last_name = 'Drullard'       # str
country = 'El cibao'         # str
city= 'Santiago'            # str
age = 25                 # int, it is not my real age, don't worry about it

# Printing out types
print(type('Olvier'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

# Convercion de tipos de datos a otro tipo de dato

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float no esposible 
#num_str = '10.6'
#print('num_int', int(num_str))      # 10
#print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

