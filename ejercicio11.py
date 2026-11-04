import numpy as np
from scipy import stats

datos = np.array([
    12.561, 2.695, 12.082, 10.335, 13.260, 2.549, 4.594, 2.500,
    24.930, 7.805, 8.322, 7.422, 11.143, 20.599, 7.508, 4.367,
    1.544, 3.706, 8.185, 14.405, 4.057, 15.584, 9.049, 6.265,
    10.663, 10.257, 11.475, 4.688, 16.256, 4.688, 11.963, 5.599,
    19.204, 1.784, 25.998, 12.299, 10.317, 3.779, 18.993, 7.419,
    15.154, 9.579, 8.423, 6.934, 2.005, 13.234, 5.542, 5.271,
    12.831, 8.231, 15.330, 7.958, 7.103, 16.134, 0.189, 10.165,
    14.624, 15.696, 10.212, 0.891, 3.186, 9.051, 11.118, 4.449,
    17.901, 15.497, 6.645, 5.078, 11.555, 3.724, 21.500, 7.160,
    13.528, 3.372, 15.334, 7.603, 31.066, 1.992, 21.127, 10.784,
    3.643, 27.334, 3.178, 1.313, 10.962, 6.936, 3.140, 16.877,
    19.171, 6.620, 3.775, 16.675, 1.368, 17.583, 1.669, 11.157,
    16.432, 2.831, 7.844, 10.745
])

n = len(datos)
alfa = 0.05
k = 8

distribuciones = {
    "Exponencial": (stats.expon, 1),
    "Gamma":       (stats.gamma, 2),
    "Weibull":     (stats.weibull_min, 2),
    "Lognormal":   (stats.lognorm, 2),
    "Normal":      (stats.norm, 2),
}

for nombre, (dist, num_param) in distribuciones.items():
    if dist is stats.norm:
        p = dist.fit(datos)
    else:
        p = dist.fit(datos, floc=0)

    limites = dist.ppf(np.linspace(0, 1, k + 1), *p)
    limites[0] = -np.inf
    limites[-1] = np.inf

    obs = np.histogram(datos, bins=limites)[0]
    esp = n / k
    chi = np.sum((obs - esp) ** 2 / esp)
    gl = k - 1 - num_param
    crit = stats.chi2.ppf(1 - alfa, gl)

    print(f"{nombre:12s} chi2 = {chi:7.3f}  critico = {crit:6.3f}  gl = {gl} ->",
          "NO RECHAZA" if chi <= crit else "RECHAZA")
