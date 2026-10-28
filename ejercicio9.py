import random
import math
import numpy as np
from scipy import stats

n = 100
valores = np.array([random.random() for _ in range(n)])
alfa = 0.05

media = valores.mean()
z = stats.norm.ppf(1 - alfa / 2)
li = 0.5 - z / math.sqrt(12 * n)
ls = 0.5 + z / math.sqrt(12 * n)
print(f"Media = {media:.4f}  intervalo [{li:.4f}, {ls:.4f}] ->",
      "ACEPTA" if li <= media <= ls else "RECHAZA")

var = sum((v - media) ** 2 for v in valores) / (n - 1)
li = stats.chi2.ppf(alfa / 2, n - 1) / (12 * (n - 1))
ls = stats.chi2.ppf(1 - alfa / 2, n - 1) / (12 * (n - 1))
print(f"Varianza = {var:.4f}  intervalo [{li:.4f}, {ls:.4f}] ->",
      "ACEPTA" if li <= var <= ls else "RECHAZA")

k = 10
obs = [0] * k
for v in valores:
    obs[int(v * k)] += 1
esp = n / k
chi = sum((o - esp) ** 2 / esp for o in obs)
crit = stats.chi2.ppf(1 - alfa, k - 1)
print(f"Uniformidad: obs={obs} chi={chi:.4f} critico={crit:.4f} ->",
      "ACEPTA" if chi <= crit else "RECHAZA")

k = 5
obs = np.zeros((k, k), dtype=int)
for i in range(n - 1):
    obs[int(valores[i] * k)][int(valores[i + 1] * k)] += 1
pares = n - 1
esp = pares / (k * k)
chi = (k * k / pares) * np.sum((obs - esp) ** 2)
crit = stats.chi2.ppf(1 - alfa, k * k - 1)
print(f"Series: chi={chi:.4f} critico={crit:.4f} ->",
      "ACEPTA" if chi <= crit else "RECHAZA")