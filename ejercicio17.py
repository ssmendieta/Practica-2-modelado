import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


precio = 6
costo = 3.5
horas = 100
numero_corridas = 5
demandas_posibles = np.array([0, 1, 2, 3, 4, 5, 6])
probabilidades = np.array([0.10, 0.15, 0.25, 0.20, 0.15, 0.08, 0.07])
margen = precio - costo
generador = np.random.default_rng(17)


def simular_corrida():
    demandas = generador.choice(demandas_posibles, size=horas, p=probabilidades)
    utilidades = margen * demandas
    cantidades = np.arange(1, horas + 1)
    promedios = np.cumsum(utilidades) / cantidades
    inferiores = np.full(horas, np.nan)
    superiores = np.full(horas, np.nan)

    for i in range(1, horas):
        muestra = utilidades[:i + 1]
        error = stats.sem(muestra)
        limite = stats.t.ppf(0.975, i) * error
        inferiores[i] = promedios[i] - limite
        superiores[i] = promedios[i] + limite

    return utilidades, promedios, inferiores, superiores


corridas = [simular_corrida() for _ in range(numero_corridas)]
promedios_finales = np.array([corrida[1][-1] for corrida in corridas])
intervalos_finales = []

for utilidades, promedios, inferiores, superiores in corridas:
    error = stats.sem(utilidades)
    limite = stats.t.ppf(0.975, horas - 1) * error
    intervalos_finales.append((promedios[-1] - limite, promedios[-1] + limite))

promedio_global = promedios_finales.mean()
error_global = stats.sem(promedios_finales)
limite_global = stats.t.ppf(0.975, numero_corridas - 1) * error_global
intervalo_global = (promedio_global - limite_global, promedio_global + limite_global)
demanda_teorica = np.sum(demandas_posibles * probabilidades)
utilidad_teorica = margen * demanda_teorica

print(f"Utilidad promedio teórica por hora: ${utilidad_teorica:.4f}")

for i, (promedio, intervalo) in enumerate(zip(promedios_finales, intervalos_finales), 1):
    print(
        f"Corrida {i}: promedio = ${promedio:.4f}  "
        f"IC 95% = [${intervalo[0]:.4f}, ${intervalo[1]:.4f}]"
    )

print(f"Promedio global: ${promedio_global:.4f}")
print(f"IC global 95%: [${intervalo_global[0]:.4f}, ${intervalo_global[1]:.4f}]")

figura, ejes = plt.subplots(numero_corridas, 1, figsize=(11, 15), sharex=True)
x = np.arange(1, horas + 1)

for i, (eje, corrida) in enumerate(zip(ejes, corridas), 1):
    utilidades, promedios, inferiores, superiores = corrida
    eje.plot(x, promedios, color="blue", label="Utilidad promedio acumulada")
    eje.fill_between(x, inferiores, superiores, color="blue", alpha=0.18, label="IC 95%")
    eje.axhline(utilidad_teorica, color="red", linestyle="--", label="Utilidad teórica")
    eje.set_title(f"Corrida {i}")
    eje.set_ylabel("Utilidad ($)")
    eje.grid(True)
    eje.legend(loc="best")

ejes[-1].set_xlabel("Horas simuladas")
figura.suptitle("Estabilización de la utilidad promedio por hora", fontsize=14)
figura.tight_layout()
figura.savefig("ejercicio17_estabilizacion.png", dpi=150, bbox_inches="tight")
plt.show()
