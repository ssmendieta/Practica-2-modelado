import numpy as np
from scipy import stats

intervalos = [
    "0-2", "2-4", "4-6", "6-8", "8-10", "10-12",
    "12-14", "14-16", "16-18", "18-20", "20-22"
]

observadas = np.array([39, 57, 47, 23, 18, 9, 2, 3, 1, 1, 0])
puntos_medios = np.arange(1, 22, 2)
datos = np.repeat(puntos_medios, observadas)

n = len(datos)
alfa = 0.10

distribuciones = {
    "Exponencial": (stats.expon, 1),
    "Gamma":       (stats.gamma, 2),
    "Weibull":     (stats.weibull_min, 2),
    "Lognormal":   (stats.lognorm, 2),
    "Normal":      (stats.norm, 2),
}

# Se agregan las colas para que las probabilidades cubran toda la distribución.
limites = np.concatenate(([-np.inf], np.arange(0, 24, 2), [np.inf]))
obs_originales = np.concatenate(([0], observadas, [0]))
resultados = []

for nombre, (dist, num_param) in distribuciones.items():
    if dist is stats.norm:
        p = dist.fit(datos)
    else:
        p = dist.fit(datos, floc=0)

    esperadas = np.diff(dist.cdf(limites, *p)) * n
    obs = obs_originales[esperadas > 0.000001].copy()
    esp = esperadas[esperadas > 0.000001].copy()

    # Se agrupan las colas hasta obtener frecuencias esperadas de al menos 5.
    while len(esp) > 1 and esp[-1] < 5:
        esp[-2] += esp[-1]
        obs[-2] += obs[-1]
        esp = esp[:-1]
        obs = obs[:-1]

    while len(esp) > 1 and esp[0] < 5:
        esp[1] += esp[0]
        obs[1] += obs[0]
        esp = esp[1:]
        obs = obs[1:]

    chi = np.sum((obs - esp) ** 2 / esp)
    gl = len(obs) - 1 - num_param
    crit = stats.chi2.ppf(1 - alfa, gl)
    resultados.append((nombre, chi, crit, gl))

    print(f"{nombre:12s} chi2 = {chi:7.3f}  critico = {crit:6.3f}  gl = {gl} ->",
          "NO RECHAZA" if chi <= crit else "RECHAZA")

aceptadas = [r for r in resultados if r[1] <= r[2]]
if aceptadas:
    mejor = min(aceptadas, key=lambda r: r[1])
    print(f"\nLa distribución con mejor ajuste es: {mejor[0]}")
else:
    print("\nNinguna de las distribuciones evaluadas se ajusta a los datos.")
