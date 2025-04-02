import timeit

def suma_cuadrados_iterativa(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i ** 2
    return suma

def suma_cuadrados_recursiva(n):
    if n == 0:
        return 0
    return n**2 + suma_cuadrados_recursiva(n - 1)

def suma_cuadrados_formula(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

n = 100

print("Tiempo Iterativa:", timeit.timeit(lambda: suma_cuadrados_iterativa(n), number=1000), "segundos")
print("Tiempo Recursiva:", timeit.timeit(lambda: suma_cuadrados_recursiva(n), number=1000), "segundos")
print("Tiempo Fórmula:", timeit.timeit(lambda: suma_cuadrados_formula(n), number=1000), "segundos")