# Programa: término n-ésimo de una progresión aritmética

a1 = float(input("Ingresa el primer término (a1): "))
d = float(input("Ingresa la diferencia (d): "))
n = int(input("Ingresa el número de término que quieres (n): "))

an = a1 + (n - 1) * d

print("El término número", n, "de la progresión aritmética es:", an)
