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