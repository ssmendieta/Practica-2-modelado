import random
import math


def caso_a(r):
    return math.sqrt(-10 * math.log(1 - r))



def caso_b(r):
    return (-math.log(1 - r) / 12) ** (1 / 3)



def caso_c(r):
    return (-math.log(1 - r)) ** (1 / 4)


random.seed(15)
n = 100

resultado_a = [caso_a(random.random()) for _ in range(n)]
resultado_b = [caso_b(random.random()) for _ in range(n)]
resultado_c = [caso_c(random.random()) for _ in range(n)]

print("a) X = sqrt(-10 * ln(1 - R))")
print(resultado_a)

print("\nb) X = (-ln(1 - R) / 12)^(1/3)")
print(resultado_b)

print("\nc) X = (-ln(1 - R))^(1/4)")
print(resultado_c)
