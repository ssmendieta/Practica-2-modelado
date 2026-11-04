import math
import numpy as np
from scipy import stats


precios = np.array([125.50, 132.75, 120.80, 138.20, 127.50])
n = len(precios)
media = precios.mean()
desviacion = precios.std(ddof=1)

nivel_a = 0.95
alfa_a = 1 - nivel_a
t = stats.t.ppf(1 - alfa_a / 2, n - 1)
exactitud = t * desviacion / math.sqrt(n)
limite_inferior = media - exactitud
limite_superior = media + exactitud

nivel_b = 0.90
alfa_b = 1 - nivel_b
z = stats.norm.ppf(1 - alfa_b / 2)
exactitud_deseada = 0.35
replicas_necesarias = math.ceil((z * desviacion / exactitud_deseada) ** 2)

print(f"Media muestral: ${media:.4f}")
print(f"Desviación estándar muestral: ${desviacion:.4f}")
print(f"a) Exactitud lograda al 95%: ±${exactitud:.4f}")
print(f"   Intervalo de confianza: [${limite_inferior:.4f}, ${limite_superior:.4f}]")
print(f"b) Réplicas necesarias para una exactitud de ±$0.35 al 90%: {replicas_necesarias}")
print(f"   Réplicas adicionales: {max(0, replicas_necesarias - n)}")
