import random
import math 
import numpy as np
import matplotlib.pyplot as plt


def caso_A(rfinal):
   return -20 * math.log(rfinal)
def caso_B(rfinal):
   return -10 * math.log(rfinal)
def caso_C(rfinal):
   return -5 * math.log(rfinal)


def resultados(funcion, r):
    promedio_movil = 0
    resultado = []
    suma_acumulada = 0

    for i in range (1, 1001):
        rfinal = 1
        for j in range(r):
            ri = random.random()
            rfinal = rfinal * ri 
        match funcion:
            case "A":
                x = caso_A(rfinal)
            case "B":
                x = caso_B(rfinal)
            case "C":
                x = caso_C(rfinal)
        suma_acumulada += x

        promedio_movil = (suma_acumulada) / i
        resultado.append(promedio_movil)
    return resultado



plt.figure(figsize=(10,5))
plt.title("Promedio movil - caso A, B y C")
plt.plot(resultados("A",2), label="caso A", color="blue", linewidth=2)
plt.plot(resultados("B",4), label="caso B", color="red", linewidth=2)
plt.plot(resultados("C",8), label="caso C", color="green", linewidth=2)
plt.xlabel("Iteración")
plt.ylabel("Promedio Móvil")
plt.legend()
plt.grid(True)
plt.show()

'''
¿Cuál de las tres funciones llega a estado estable más rápidamente?

La función del inciso c) es la que llega más rápido al estado estable, seguida de la b) y, por último, la a)

¿En qué punto del tiempo llega cada una a un estado estable?

La función a) se estabiliza alrededor del mantenimiento número [750]
La función b) se estabiliza alrededor del mantenimiento número [350]
La función c) se estabiliza alrededor del mantenimiento número [325]

¿A qué valor converge el promedio en cada una?

Las tres funciones convergen aproximadamente a 40
'''

