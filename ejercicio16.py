import random
import math


def raiz_cubica(valor):
    return math.copysign(abs(valor) ** (1 / 3), valor)


def caso_a(r):
    return raiz_cubica(28 * r - 1) - 1


def caso_b(r):
    return 9 + 3 * math.sqrt(r)


def caso_c(r):
    return 8 - 3 * math.sqrt(1 - r)


def caso_d(r):
    return 15 - 4 * math.sqrt(1 - r)


random.seed(16)
n = 100

resultado_a = [caso_a(random.random()) for _ in range(n)]
resultado_b = [caso_b(random.random()) for _ in range(n)]
resultado_c = [caso_c(random.random()) for _ in range(n)]
resultado_d = [caso_d(random.random()) for _ in range(n)]

print("a) X = raiz_cubica(28R - 1) - 1")
print(resultado_a)

print("\nb) X = 9 + 3sqrt(R)")
print(resultado_b)

print("\nc) X = 8 - 3sqrt(1 - R)")
print(resultado_c)

print("\nd) X = 15 - 4sqrt(1 - R)")
print(resultado_d)
