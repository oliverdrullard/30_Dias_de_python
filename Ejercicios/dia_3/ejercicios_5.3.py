

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


# Comparacion de numeros

print(10 == "10")
print(int(9.8) == 10)

# Escriba un script que solicite al usuario que ingrese horas y tarifa por hora. ¿Cómo calcular el salario de la persona?

print("Calculo del salario")

horas = input("Ingrese sus horas trabajadas")
tarifa_horas = input("Ingrese la tarifa de las horas")

salario = float(horas) * float(tarifa_horas)
print(salario)

# Escriba un script que solicite al usuario que ingrese la cantidad de años. Calcule la cantidad de segundos que puede vivir una persona. Suponga que una persona puede vivir cien años.

print("Calculando los segundos por años")

yerst = input("Ingrese la cantidad de años: ")

segundos_años = 31536000

segundos_para_vivir = segundos_años * int(yerst)
print("Los segundos son: ",segundos_para_vivir)