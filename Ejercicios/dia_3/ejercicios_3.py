# Ejercicio 1

edad = 25
altur = 10.2
complejo = 1j

# Calculando el area de un rectangulo 

base = input("Ingrese la base: ")
altura = input("Ingrese la altura: ")
area = float(base) * float(altura)
print("El area del rectanculo es: ",area)

# Calculando el perimetro de un triangulo

a = input("Digite el lado a: ")
b = input("Digite el lado b: ")
c = input("Digite el lado c: ")
perimetro = a + b + c
print("El perimetro de un rectangulo es: ",perimetro)

# Calculando pero con los datos ingresados por el teclado de un rectangulo

oprecion = input("Ingrese la operacion a realizar,(perimetro o area)")

if oprecion == "perimetro":
    longitud = input("Ingrese la longitud: ")
    ancho = input("Ingrese el ancho: ")

    perimetro_cero = float(longitud) + float(ancho) ** 2
    print("El perimetro es: ",perimetro_cero)

elif oprecion == "area":
    longitud = input("Ingrese la longitud: ")
    ancho = input("Ingrese el ancho: ")

    area = float(longitud) * float(ancho)
    print("El area  es: ",area)

else :
    print("Esa opcion no esta disponible")

# Calculando el area de un circulo y su circunferencia

oprecion = input("Ingrese la operacion a realizar,(area o circunferencia)")

if oprecion == "circunferencia":
    radio = input("Ingrese el radio: ")

    circunferencia = 3.14 * float(radio) * 2
    print("El area es: ",circunferencia)

elif oprecion == "area":
    radio = input("Ingrese el radio: ")
   
    area_uno = 3.14 * float(radio) * float(radio)
    print("El area  es: ",area_uno)

else :
    print("Esa opcion no esta disponible")


# Comparando longitudes 

print(not len("python") and len("dragon"))

print("on" in "python" and "on" in "dragon")

print("jerga" in "Espero que este curso no este lleno de jerga")


# Convercion 

longitud_python  = len("python")
print(longitud_python)

longitud_flotante = float(longitud_python)
print(longitud_flotante)

longitud_str = str(longitud_flotante)
print(longitud_str)

# Encontrando los numeros para 

numero = 6

print(numero % 0)

# Comparacion de numeros

print(10 == "10")
print(int(9.8) == 10)

# Escriba un script que solicite al usuario que ingrese horas y tarifa por hora. ¿Cómo calcular el salario de la persona?

print("Calculo del salario")

horas = input("Ingrese sus horas trabajadas")
tarifa_horas = input("Ingrese la tarifa de las horas")

salario = horas * tarifa_horas
print(salario)

# Escriba un script que solicite al usuario que ingrese la cantidad de años. Calcule la cantidad de segundos que puede vivir una persona. Suponga que una persona puede vivir cien años.

print("Calculando los segundos por años")

yerst = input("Ingrese la cantidad de años: ")

segundos_años = 31,536,000

segundos_para_vivir = segundos_años * float(yerst)
print("Los segundos son: ",segundos_para_vivir)