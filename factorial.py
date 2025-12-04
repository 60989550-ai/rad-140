# Programa: cálculo de factorial

n = int(input("Ingresa un número entero n (n >= 0): "))

if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    print("El factorial de", n, "es:", resultado)
