import numpy as np
import math
from scipy import stats

valores = np.array([0.8797, 0.9848, 0.4557, 0.9170, 0.8376, 0.3884, 0.3469, 0.1592, 0.2204, 0.6235, 0.6289, 0.7977, 0.8536, 0.5991, 
                    0.3681, 0.8750, 0.5844, 0.8846, 0.5461, 0.2088, 0.5999, 0.8147, 0.3410, 0.5739, 0.8589, 0.9996, 0.6431, 0.1492, 
                    0.3254, 0.1525, 0.2006, 0.7387, 0.8681, 0.0856, 0.4720, 0.2415, 0.5613, 0.5291, 0.2258, 0.4272, 0.3808, 0.0318,
                    0.3188, 0.4603, 0.6360, 0.9606, 0.7401, 0.5992, 0.5027, 0.0954 ])

suma_acumulada = 0 
for valor in valores:
    suma_acumulada += valor

n = len(valores)

r = suma_acumulada/n
alfa = 0.05
z = stats.norm.ppf(1 - alfa/2)
li = 0.5 - z/math.sqrt(12 * n)
ls = 0.5 + z/math.sqrt(12 * n)

if r >= li and r <= ls:
    print(f"La media muestral {r:.4f} este dentro del intervalo de confianza [{li:.4f}, {ls:.4f}]")
else:
    print("La media muestral no esta dentro del intervalo de confianza")  

var = sum((v - r)**2 for v in valores) / (n -1)

li = stats.chi2.ppf(alfa/2, n-1) / (12*(n-1))
ls = stats.chi2.ppf(1-alfa/2, n-1) / (12*(n-1))
if li <= var <= ls :
    print(f"La varianza muestral {var:.4f} este dentro del intervalo de confianza [{li:.4f}, {ls:.4f}]")
else:
    print(f"La varianza muestral {var:.4f} no esta dentro del intervalo de confianza [{li:.4f}, {ls:.4f}]")  

k = 10
obs = [0]*k
for v in valores:
    obs[int(v*k)] += 1
esp = n / k
chi = sum((o - esp)**2 / esp for o in obs)
crit = stats.chi2.ppf(1 - alfa, k - 1)
print(f"Chi2: obs={obs}  chi={chi:.4f}  critico={crit:.4f}  ->",
      "ACEPTA" if chi <= crit else "RECHAZA")