"""
    Si una fruta no existe en la lista, 
    agregue la fruta a la lista e imprima 
    la lista modificada. Si la fruta existe 
    print('Esa fruta ya existe en la lista')
"""
frutas = ["sandia","fresa","limon"]

fruta = str(input("Ingresa El nombre de la fruta: "))

if fruta in frutas:
    print(f"Esta fruta existe en lista: {frutas}")
  
else:
    frutas.append(fruta)
    print("La fruta se agrego a la lista")
    print(frutas)
    
