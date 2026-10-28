import math
from scipy import stats

valores = []
x0 = 23
valores.append(x0)
vistos = {x0}
i = 1
m = 177
ciclo = 0

while True:
    xi = (553+121*valores[i-1]) % 177 
    if xi in vistos:
        ciclo = i
        break
    else:
        vistos.add(xi)
    valores.append(xi)
    if i == 177:
        break
    i += 1
    
print(f"El ciclo de vida es de: {ciclo}")

n = len(valores)                 
r = [v / m for v in valores]     
alfa = 0.05 

media = sum(r) / n
z = stats.norm.ppf(1 - alfa/2)
li = 0.5 - z / math.sqrt(12*n)
ls = 0.5 + z / math.sqrt(12*n)
print(f"Media: {media:.4f}  intervalo [{li:.4f}, {ls:.4f}]  ->",
      "ACEPTA" if li <= media <= ls else "RECHAZA")

var = sum((ri - media)**2 for ri in r) / (n - 1)
li = stats.chi2.ppf(alfa/2, n-1) / (12*(n-1))
ls = stats.chi2.ppf(1 - alfa/2, n-1) / (12*(n-1))
print(f"Varianza: {var:.4f}  intervalo [{li:.4f}, {ls:.4f}]  ->",
      "ACEPTA" if li <= var <= ls else "RECHAZA")

k = 10
obs = [0]*k
for ri in r:
    obs[int(ri*k)] += 1
esp = n / k
chi = sum((o - esp)**2 / esp for o in obs)
crit = stats.chi2.ppf(1 - alfa, k - 1)
print(f"Chi2: obs={obs}  chi={chi:.4f}  critico={crit:.4f}  ->",
      "ACEPTA" if chi <= crit else "RECHAZA")

