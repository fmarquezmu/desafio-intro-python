print("Para el buen funcionamiento del programa, ingrese los valores en números enteros")

P = int(input("Ingrese el Precio de Suscripción: "))
U = int(input("Ingrese el Número de Usuarios: "))
GT = int(input("Ingrese el Gasto Total: "))
UAnterior = int(input("Ingrese las utilidades del año anterior: "))

UActuales = P * U - GT
RazonU = round(UActuales/UAnterior,2)

print(f"Las utilidades actuales son {UActuales}, están un razón de {RazonU} respecto a las del año anterior.")