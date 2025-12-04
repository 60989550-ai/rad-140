# Programa: combinación C(n, k)

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (elementos que eliges): "))

if k < 0 or k > n:
    print("k debe estar entre 0 y n.")
else:
    n_fact = factorial(n)
    k_fact = factorial(k)
    n_k_fact = factorial(n - k)

    C = n_fact / (k_fact * n_k_fact)

    print("C(", n, ",", k, ") =", C)