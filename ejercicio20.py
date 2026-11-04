import numpy as np
from scipy import stats


generador = np.random.default_rng(20)
dias = 300
duracion = 8 * 60
media_entre_llegadas = 60 / 15
media_por_transaccion = 2.2
tipos_transaccion = np.array([1, 2, 3, 4])
probabilidades = np.array([0.40, 0.30, 0.20, 0.10])


def simular_dia():
    llegadas = []
    tiempo = generador.exponential(media_entre_llegadas)

    while tiempo <= duracion:
        llegadas.append(tiempo)
        tiempo += generador.exponential(media_entre_llegadas)

    fin_servicio_anterior = 0
    esperas = []

    for llegada in llegadas:
        numero_transacciones = generador.choice(tipos_transaccion, p=probabilidades)
        tiempo_servicio = generador.exponential(
            media_por_transaccion, size=numero_transacciones
        ).sum()
        inicio_servicio = max(llegada, fin_servicio_anterior)
        esperas.append(inicio_servicio - llegada)
        fin_servicio_anterior = inicio_servicio + tiempo_servicio

    return np.array(esperas)


esperas_por_dia = [simular_dia() for _ in range(dias)]
promedios_diarios = np.array([esperas.mean() for esperas in esperas_por_dia])
todas_las_esperas = np.concatenate(esperas_por_dia)
promedio_global = promedios_diarios.mean()
error = stats.sem(promedios_diarios)
limite = stats.t.ppf(0.975, dias - 1) * error

print(f"Días simulados: {dias}")
print(f"Clientes simulados: {len(todas_las_esperas)}")
print(f"Clientes promedio por día: {len(todas_las_esperas) / dias:.4f}")
print(f"Tiempo promedio en la fila: {promedio_global:.4f} minutos")
print(f"IC 95% del promedio diario: [{promedios_diarios.mean() - limite:.4f}, {promedios_diarios.mean() + limite:.4f}] minutos")
