import random
import math


def transformada_inversa(valores, probabilidades, cantidad=100):
    acumuladas = []
    suma = 0

    for probabilidad in probabilidades:
        suma += probabilidad
        acumuladas.append(suma)

    numeros = []
    for _ in range(cantidad):
        r = random.random()

        for valor, acumulada in zip(valores, acumuladas):
            if r <= acumulada:
                numeros.append(valor)
                break

    return numeros


def mostrar_resultados(inciso, numeros):
    print(f"\nInciso {inciso})")
    print(numeros)
    print("Frecuencias:")

    for valor in sorted(set(numeros)):
        print(f"x = {valor}: {numeros.count(valor)}")


random.seed(14)

# a) p(x) = 1/5(4/5)^(x-1), para x = 1, 2, 3, ...
resultado_a = [
    max(1, math.ceil(math.log(1 - random.random()) / math.log(4 / 5)))
    for _ in range(100)
]

# b) p(x) = 1/2(1/2)^x, para x = 0, 1, 2, 3, ...
resultado_b = [
    max(0, math.ceil(math.log(1 - random.random()) / math.log(1 / 2)) - 1)
    for _ in range(100)
]

# c) p(x) = (20 + 10x) / 200, para x = 0, 1, 2, 3, 4
valores_c = list(range(0, 5))
probabilidades_c = [(20 + 10 * x) / 200 for x in valores_c]
resultado_c = transformada_inversa(valores_c, probabilidades_c)

# d) p(x) = (18 - 4x) / 50, para x = 0, 1, 2, 3, 4
valores_d = list(range(0, 5))
probabilidades_d = [(18 - 4 * x) / 50 for x in valores_d]
resultado_d = transformada_inversa(valores_d, probabilidades_d)

# e) p(x) = (3x + 8) / 100, para x = 2, 3, 4, 5, 6
valores_e = list(range(2, 7))
probabilidades_e = [(3 * x + 8) / 100 for x in valores_e]
resultado_e = transformada_inversa(valores_e, probabilidades_e)

# f) p(x) = 1/6, para x = 6, 7, 8, 9, 10, 11
valores_f = list(range(6, 12))
probabilidades_f = [1 / 6] * 6
resultado_f = transformada_inversa(valores_f, probabilidades_f)

# g) Distribución geométrica truncada. Se pueden cambiar p y n.
p = 0.20
n = 10
valores_g = list(range(1, n + 1))
probabilidades_g = [
    p * (1 - p) ** (x - 1) / (1 - (1 - p) ** n)
    for x in valores_g
]
resultado_g = transformada_inversa(valores_g, probabilidades_g)

mostrar_resultados("a", resultado_a)
mostrar_resultados("b", resultado_b)
mostrar_resultados("c", resultado_c)
mostrar_resultados("d", resultado_d)
mostrar_resultados("e", resultado_e)
mostrar_resultados("f", resultado_f)
mostrar_resultados("g", resultado_g)
