"""
    Comprueba si la estación es Otoño, Invierno, Primavera o Verano.
    Si la entrada del usuario es: Septiembre, Octubre o Noviembre,
    la estación es Otoño. Diciembre, Enero o Febrero, la estación 
    es Invierno. Marzo, Abril o Mayo, la estación es Primavera. 
    Junio, Julio o Agosto, la estación es Verano.
"""

estacion_del_yers_1 = "Otoño"
estacion_del_yers_2 = "Invierno"
estacion_del_yers_3 = "Primavera"
estacion_del_yers_4 = "Verano"

otoño = ["septiembre","octubre","nobiembre"]
Invierno = ["Diciembre","Enero","Febrero"]
Primavera = ["Marzo","Abril","Mayo"]
Verano = ["Junio","Julio","Agosto"]

estacion_yers = str(input("Ingrese la mes para saber que estacion del aÑo estamos: "))

estacion_yers = estacion_yers.capitalize()

if estacion_yers == otoño[0] or estacion_yers == otoño[1] or estacion_yers == otoño[2]:
    print(f"La estacion del yers es: {estacion_del_yers_1}")

elif estacion_yers == Invierno[0] or estacion_yers == Invierno[1] or estacion_yers == Invierno[2]:
    print(f"La estacion del yers es: {estacion_del_yers_2}")

elif estacion_yers == Primavera[0] or estacion_yers == Primavera[1] or estacion_yers == Primavera[2]:
    print(f"La estacion del yers es: {estacion_del_yers_3}")

elif estacion_yers == Verano[0] or estacion_yers == Verano[1] or estacion_yers == Verano[2]:
    print(f"La estacion del yers es: {estacion_del_yers_4}")

else:
    print("No es un mes del yers")