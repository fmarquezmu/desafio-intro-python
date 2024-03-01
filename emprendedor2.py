print("Para el buen funcionamiento del programa, ingrese los valores en números enteros")

P = int(input("Ingrese el Precio de Suscripción: "))
UNormal = int(input("Ingrese el Número de Usuarios Normales: "))
UPremium = int(input("Ingrese el Número de Usuarios Premium: "))
GT = int(input("Ingrese el Gasto Total: "))

Utilidades = ((P * UNormal) + (1.5 * P * UPremium)) - GT

print(f"Las utilidades son {Utilidades}.")