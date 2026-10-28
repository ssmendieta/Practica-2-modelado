import numpy as np
from scipy import stats

valores = np.array([0.5858, 0.8863, 0.8378, 0.3203, 0.4115, 0.2710, 0.9238, 0.1959, 0.9268, 0.6702, 0.6213, 0.4360,
                    0.6279, 0.8415, 0.5786, 0.0543, 0.3567, 0.1655, 0.3880, 0.8080, 0.1931, 0.0843, 0.9152, 0.6093,
                    0.7587, 0.4515, 0.3203, 0.5139, 0.7070, 0.9123, 0.1242, 0.8826, 0.9921, 0.8523, 0.6723, 0.8540,
                    0.4722, 0.4781, 0.2101, 0.1680, 0.8658, 0.4028, 0.6136, 0.8720, 0.1126, 0.5857, 0.9172, 0.8943,
                    0.8095, 0.6408])

n = len(valores)
alfa = 0.10          
k = 5                

obs = np.zeros((k, k), dtype=int)
for i in range(n - 1):
    fila = int(valores[i] * k)
    col = int(valores[i + 1] * k)
    obs[fila][col] += 1

pares = n - 1
esp = pares / (k * k)
chi = (k * k / pares) * np.sum((obs - esp) ** 2)
crit = stats.chi2.ppf(1 - alfa, k * k - 1)

print("n =", n, " pares =", pares)
print(obs)
print(f"Esperada por celda: {esp:.4f}")
print(f"Chi2 = {chi:.4f}   critico = {crit:.4f}")
if chi <= crit:
    print("ACEPTA: los números son independientes")
else:
    print("RECHAZA: los números no son independientes")