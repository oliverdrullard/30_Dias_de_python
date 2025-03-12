### Ejercicios de  funciones nivel 1 ###
import math
# Declara una función add_two_numbers . Toma dos parámetros y devuelve una suma.

def add_two_numbers(num_1,num_2):
    suma = num_1 + num_2
    return suma

print(f"La suma de los dos numeros son: {add_two_numbers(4,5)}")

# El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .

def calculo_area_de_circulo():
    pi = 3.14
    radio = 425
    area = pi * radio ** 2
    return area

print(f"El calculo del area de un circulo es: {calculo_area_de_circulo()}")


# Escriba una función llamada add_all_nums que tome una cantidad arbitraria de argumentos y sume todos los argumentos. 
# Verifique si todos los elementos de la lista son de tipo numérico. Si no es así, proporcione una respuesta razonable.

def add_all_nums(*arkgs):
    total = 0
    for arkg in arkgs:
        if isinstance(arkg,int):
            total += arkg
        else: 
            print("En lista contiene datos str y no pueden ser sumados")
    return total
            
   
lista_mista = [1,"Oliver",1.3,True]
print()
print(f"La suma de todos los argumentos pasados son; {add_all_nums(1,2,3,4,5,6,7,8)}")
print(f"La suma de todos los argumentos pasados son; {add_all_nums(lista_mista)}")


# La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .

def converertir_C_a_F(celsius):

    f = (celsius * 9/5) + 32

    return f

print(f"La conversion de grados Celsius a fahrenheit es de: {converertir_C_a_F(25)}")


# Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.

def temporadas_del_year(mes):
    primavera = ["marzo", "abril", "mayo", "junio"]
    verano = ["julio", "agosto", "septiembre"]
    otoño = ["octubre", "noviembre", "diciembre"]
    invierno = ["enero", "febrero"]

    if mes in primavera:
        print("La estacion en la que te encuentras es: Primavera")

    elif mes in verano:
        print("La estacion en la que te encuentras es: Verano")

    elif mes in otoño:
        print("La estacion en la que te encuentras es: Otoño")

    elif mes in invierno:
        print("La estacion en la que te encuentras es: Invierno")

temporadas_del_year("marzo")


# Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal

def calculo_de_ecuacion_lineal(x,y):

    resultado = x + y 

    return resultado

print(f"La ecuacion lineal es de los valores x,y es: {calculo_de_ecuacion_lineal(2,3)}")


# La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn .

def ecuacion_cuadratica(a,b,c):

    resultado = a ** 2 + b + c

    return resultado

print(f"Resultado es de : {ecuacion_cuadratica(2,4,6)}")

# Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.

def listado(lista):
    for i in lista:
        print(i)

frutas = ["Zandia","Zanaoria","uva","mango"]
listado(frutas)


# Declara una función llamada reverse_list. Toma una matriz como parámetro y devuelve el inverso de la matriz (usa bucles).

def lista_inversa(lista):
    for i in lista[::-1]:
        print(i)

lista_inversa(frutas)

