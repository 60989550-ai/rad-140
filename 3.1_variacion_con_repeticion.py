# Programa: variación V(n, k) con y sin repetición

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (lugares a ordenar): "))

print("Tipo de variación:")
print("1. Sin repetición (V(n, k) = n! / (n-k)!)")
print("2. Con repetición (V_r(n, k) = n^k)")

tipo = int(input("Elige 1 o 2: "))

if k < 0 or k > n and tipo == 1:
    print("Para variación SIN repetición, k debe estar entre 0 y n.")
else:
    if tipo == 1:
        # Variación sin repetición
        n_fact = factorial(n)
        n_k_fact = factorial(n - k)
        V = n_fact / n_k_fact
        print(f"V({n}, {k}) sin repetición =", V)

    elif tipo == 2:
        # Variación con repetición
        V_r = n ** k
        print(f"V_r({n}, {k}) con repetición =", V_r)

    else:
        print("La opción elegida no existe.")
