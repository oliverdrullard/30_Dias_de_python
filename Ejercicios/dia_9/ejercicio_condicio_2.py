# Escriba un código que califique a los estudiantes según sus puntuaciones
estudiante = 1

if estudiante >= 90 or estudiante == 100:
    print("A")
elif estudiante >= 70 or estudiante == 89:
    print("B")
elif estudiante >= 60 or estudiante == 69:
    print("C")
elif estudiante >= 50 or estudiante == 59:
    print("D")
elif estudiante <= 49 or estudiante == 0:
    print("F")
else:
    print("El estudiante no tiene una calificacion asignada")