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