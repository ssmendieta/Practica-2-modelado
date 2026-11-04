import numpy as np
from scipy import stats

intervalos = [
    "150-151", "151-152", "152-153", "153-154", "154-155",
    "155-156", "156-157", "157-158", "158-159", "159-160"
]

observadas = np.array([13, 8, 11, 15, 7, 8, 9, 11, 10, 8])

n = observadas.sum()
alfa = 0.05
k = len(observadas)


esperada = n / k

chi = np.sum((observadas - esperada) ** 2 / esperada)
gl = k - 1
crit = stats.chi2.ppf(1 - alfa, gl)

print("Intervalos y frecuencias observadas:")
for intervalo, frecuencia in zip(intervalos, observadas):
    print(f"{intervalo}: {frecuencia}")

print(f"\nTotal de datos = {n}")
print(f"Frecuencia esperada por intervalo = {esperada:.2f}")
print(f"Chi2 = {chi:.4f}  critico = {crit:.4f}  gl = {gl} ->",
      "NO RECHAZA" if chi <= crit else "RECHAZA")

if chi <= crit:
    print("Los datos siguen una distribución uniforme entre 150 y 160.")
else:
    print("Los datos no siguen una distribución uniforme entre 150 y 160.")
