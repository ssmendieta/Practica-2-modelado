import numpy as np


generador = np.random.default_rng(19)
n = 300
limite_inferior = 40
limite_superior = 50

x1 = generador.normal(loc=30, scale=np.sqrt(0.81), size=n)
x2 = generador.gamma(shape=10, scale=14.5 / 10, size=n)
longitudes = x1 + x2

fuera = (longitudes < limite_inferior) | (longitudes > limite_superior)
cantidad_fuera = np.sum(fuera)
probabilidad_fuera = np.mean(fuera)

media = np.mean(longitudes)
desviacion = np.std(longitudes, ddof=1)
cp = (limite_superior - limite_inferior) / (6 * desviacion)
cpk_inferior = (media - limite_inferior) / (3 * desviacion)
cpk_superior = (limite_superior - media) / (3 * desviacion)
cpk = min(cpk_inferior, cpk_superior)

print(f"Barras simuladas: {n}")
print(f"Longitud promedio: {media:.4f} cm")
print(f"Desviación estándar: {desviacion:.4f} cm")
print(f"Barras fuera de especificaciones: {cantidad_fuera}")
print(f"Probabilidad estimada fuera de especificaciones: {probabilidad_fuera:.4f}")
print(f"Cp = {cp:.4f}")
print(f"Cpk = {cpk:.4f}")
print("Proceso bajo control: SÍ" if cp >= 1 and cpk >= 1 else "Proceso bajo control: NO")
