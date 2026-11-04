import numpy as np
from scipy import stats


demandas_historicas = np.array([
    99, 94, 80, 73, 86, 95, 90, 70, 92, 83, 89, 93, 62, 94, 86, 62, 77, 72, 63, 88, 96,
    99, 98, 77, 96, 74, 86, 81, 94, 81, 70, 98, 78, 86, 74, 94, 95, 77, 79, 89, 65, 94,
    88, 72, 71, 70, 76, 95, 92, 96, 93, 72, 97, 75, 97, 72, 76, 69, 61, 69, 99, 83, 83,
    61, 64, 95, 80, 70, 79, 65, 80, 85, 72, 68, 83, 78, 84, 64, 72, 67, 94,
    100, 78, 93, 66, 99, 97, 74, 93, 95, 70, 93, 64, 86, 72, 80, 83, 65, 66, 96, 95, 84, 88, 68, 65,
    70, 88, 90, 85, 92, 81, 68, 92, 64, 84, 69, 73, 71, 98, 66, 68, 74, 93, 94, 86, 69,
    82, 71, 79, 100, 84, 65, 99, 100, 61, 78, 73, 80, 72, 100, 100, 98, 82, 60, 93,
    75, 84, 75, 76, 71, 94, 74, 84, 72, 71, 71, 85, 69, 88, 97, 93, 63, 91, 89, 89, 99, 93, 62,
    99, 77, 69, 82, 66, 91, 73, 88, 61, 63, 67, 76, 100, 93, 82, 72, 75, 92, 87,
    74, 60, 93, 77, 60, 84, 64, 83, 75, 68, 64, 97, 78
])

inspecciones_historicas = np.array([
    4, 2, 3, 0, 0, 2, 4, 1, 2, 0, 2, 2, 3, 3, 2, 1, 1, 1, 4, 2,
    1, 0, 3, 1, 2, 3, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 0, 0, 2, 1,
    1, 1, 3, 1, 0, 3, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 3, 1,
    2, 1, 1, 2, 1, 1, 1, 1, 3, 1, 0, 0, 1, 1, 2, 0, 0, 0, 1, 0,
    2, 0, 2, 1, 2, 0, 1, 1, 2, 0, 1, 2, 1, 2, 3, 0, 0, 0, 2, 2
])

generador = np.random.default_rng(22)
dias = 300
politicas = np.array([60, 70, 80, 90, 100])
costo_faltante = 40
costo_inventario = 20
probabilidad_rechazo = 0.03
costo_rechazo = 90
probabilidad_defecto_cliente = 0.05
costo_defecto_cliente = 120

demandas = generador.choice(demandas_historicas, size=dias)
inspecciones = generador.choice(inspecciones_historicas, size=dias)
uniformes_rechazo = generador.random((dias, politicas.max()))
defectos_cliente = generador.binomial(inspecciones, probabilidad_defecto_cliente)
resultados = []

for politica in politicas:
    rechazos = (uniformes_rechazo[:, :politica] < probabilidad_rechazo).sum(axis=1)
    disponibles = politica - rechazos
    faltantes = np.maximum(demandas - disponibles, 0)
    inventario = np.maximum(disponibles - demandas, 0)
    costos = (
        faltantes * costo_faltante
        + inventario * costo_inventario
        + rechazos * costo_rechazo
        + defectos_cliente * costo_defecto_cliente
    )

    promedio = costos.mean()
    error = stats.sem(costos)
    limite = stats.t.ppf(0.975, dias - 1) * error
    resultados.append((politica, promedio, promedio - limite, promedio + limite))

print("Política | Costo promedio diario | IC 95%")
for politica, promedio, inferior, superior in resultados:
    print(f"{politica:8d} | ${promedio:19.2f} | [${inferior:.2f}, ${superior:.2f}]")

mejor = min(resultados, key=lambda resultado: resultado[1])
print(f"\nPolítica recomendada: producir {mejor[0]} televisores por día")
print(f"Costo promedio mínimo: ${mejor[1]:.2f} por día")
