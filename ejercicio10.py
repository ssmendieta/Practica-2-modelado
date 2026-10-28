import numpy as np
from scipy import stats

datos = np.array([17.392, 4.078, 3.151, 3.528, 2.440, 5.924, 3.461, 2.052, 10.369, 3.690, 10.870, 4.793, 2.498, 0.569,
                  8.281, 0.154, 5.959, 3.384, 12.877, 13.602, 5.244, 16.677, 5.977, 4.313, 4.767, 2.381, 6.443, 1.392,
                  1.578, 8.115, 4.891, 6.720, 7.728, 2.717, 10.451, 5.901, 0.818, 7.088, 2.637, 4.714, 3.032, 1.495, 15.733,
                  7.768, 2.333, 7.822, 3.708, 6.412, 1.290, 3.957, 5.285, 7.094, 3.078, 1.264, 2.630, 10.177, 2.155, 2.945,
                  7.552, 11.094, 4.772, 7.281, 14.344, 19.867, 0.119, 2.072, 1.486, 3.791, 4.214, 1.611, 1.781, 1.530, 3.280,
                  4.301, 0.202, 7.489, 1.422, 1.453, 0.022, 6.001, 9.269, 8.477, 3.043, 0.877, 6.966, 2.103, 1.816, 0.433,
                  2.547, 0.843, 1.182, 8.121, 2.007, 1.395, 4.661, 7.378, 5.300, 17.066, 12.171])

n = len(datos)
alfa = 0.10      
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