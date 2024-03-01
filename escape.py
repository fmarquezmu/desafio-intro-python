import math

radio = int(input("Ingrese el radio en Kilómetros: "))
gravedad = float(input("Ingrese la aceleración de gravedad: "))

v_escape = round(math.sqrt(2*(radio*1000)*gravedad), 1)

print(f"la velocidad de escape es {v_escape}[m/s]")
