print("Para el buen funcionamiento del programa, ingrese los valores en números enteros")

P = int(input("Ingrese el Precio de Suscripción: "))
U = int(input("Ingrese el Número de Usuarios: "))
GT = int(input("Ingrese el Gasto Total: "))

Utilidades = P * U - GT

print(f"Las utilidades son {Utilidades}.")