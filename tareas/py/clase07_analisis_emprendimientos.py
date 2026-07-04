"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""
"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""


from sedes import sedes
MiProyecto/
    clase07_analisis_emprendimientos.py
    sedes.py


def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(lista_ventas)


def calcular_promedio(lista_ventas):
    """Retorna el promedio de las ventas de la lista ventas"""
    return sum(lista_ventas) / len(lista_ventas)


def calcular_porcentaje(total_ventas, meta):
    """Calcula el porcentaje de cumplimiento de la meta"""
    return (total_ventas / meta) * 100


def calcular_clasificacion(porcentaje_logro):
    """Clasifica el emprendimiento según porcentaje de cumplimiento de meta de ventas."""
    if porcentaje_logro >= 100:
        clasificacion_emprendimiento = "Meta alcanzada, emprendimiento rentable"
    elif porcentaje_logro >= 80:
        clasificacion_emprendimiento = "Observación, no se logró la meta."
    else:
        clasificacion_emprendimiento = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCIÓN."

    return clasificacion_emprendimiento


def imprimir_reporte(reporte):
    """Imprime el reporte final de ventas por emprendimiento"""

    print("\nREPORTE FINAL")
    print("-" * 60)

    for fila in reporte:
        print(f"Emprendimiento: {fila['nombre'].upper()}")
        print(f"Provincia: {fila['provincia']}")
        print(f"Tipo: {fila['tipo']}")
        print(f"Total semanal: ₡{fila['total']:,.2f}")
        print(f"Promedio diario: ₡{fila['promedio']:,.2f}")
        print(f"Porcentaje cumplimiento: {fila['porcentaje']:.0f}%")
        print(f"Estado: {fila['estado']}")
        print("-" * 60)

    print(f"Cantidad de emprendimientos: {len(reporte)}")


reporte = []
provincias = set()

for emprendimiento in sedes:

    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]

    total_emprendimiento = calcular_total(ventas)
    promedio_diario = calcular_promedio(ventas)
    porcentaje_logro = calcular_porcentaje(total_emprendimiento, meta)
    clasificacion = calcular_clasificacion(porcentaje_logro)

    provincias.add(emprendimiento["provincia"])

    reporte.append(
        {
            "nombre": emprendimiento["nombre"],
            "provincia": emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],
            "total": total_emprendimiento,
            "promedio": promedio_diario,
            "porcentaje": porcentaje_logro,
            "estado": clasificacion,
        }
    )

# Mostrar reporte
imprimir_reporte(reporte)

# Mostrar provincias
print("\nProvincias registradas:")
for provincia in sorted(provincias):
    print("-", provincia)

print("\nCantidad de provincias:", len(provincias))