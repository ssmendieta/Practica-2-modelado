import numpy as np


generador = np.random.default_rng(21)
dias = 300
produccion_maxima = 1000
horas_dia = 24
probabilidad_falla = 0.80
precio_pieza = 100
costo_reparacion_hora = 11
tipos_falla = np.array(["Leve", "Moderada", "Grave", "Fatal"])
probabilidades_tipo = np.array([10, 15, 25, 35]) / 85


def tiempo_reparacion(tipo):
    if tipo == "Leve":
        return generador.gamma(shape=4, scale=1)
    if tipo == "Moderada":
        return max(0, generador.normal(loc=3.5, scale=1.1))
    if tipo == "Grave":
        return 6 + np.sqrt(2 * generador.random())
    return generador.exponential(scale=1 / 0.2)


fallas = []
tiempos = []
producciones = []
utilidades = []

for _ in range(dias):
    if generador.random() < probabilidad_falla:
        tipo = generador.choice(tipos_falla, p=probabilidades_tipo)
        tiempo = tiempo_reparacion(tipo)
    else:
        tipo = "Sin falla"
        tiempo = 0

    tiempo_sin_producir = min(tiempo, horas_dia)
    produccion = produccion_maxima * (1 - tiempo_sin_producir / horas_dia)
    utilidad = produccion * precio_pieza - tiempo * costo_reparacion_hora

    fallas.append(tipo)
    tiempos.append(tiempo)
    producciones.append(produccion)
    utilidades.append(utilidad)

tiempos = np.array(tiempos)
producciones = np.array(producciones)
utilidades = np.array(utilidades)

print("Día | Tipo de falla | Reparación (h) | Producción | Utilidad")
for i in range(dias):
    print(
        f"{i + 1:3d} | {fallas[i]:12s} | {tiempos[i]:14.4f} | "
        f"{producciones[i]:10.4f} | ${utilidades[i]:12.2f}"
    )

print(f"\nProducción promedio diaria: {producciones.mean():.4f} piezas")
print(f"Utilidad promedio diaria: ${utilidades.mean():.2f}")
print(f"Producción total en 300 días: {producciones.sum():.4f} piezas")
print(f"Utilidad total en 300 días: ${utilidades.sum():.2f}")
