# Programa: variación V(n, k)

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (lugares a ordenar): "))

if k < 0 or k > n:
    print("k debe estar entre 0 y n.")
else:
    n_fact = factorial(n)
    n_k_fact = factorial(n - k)

    V = n_fact / n_k_fact

    print("V(", n, ",", k, ") =", V)