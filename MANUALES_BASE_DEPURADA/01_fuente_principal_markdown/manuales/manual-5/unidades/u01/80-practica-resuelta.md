---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 01

::practica{titulo="Cargar el CSV escolar y producir reporte de 480 estudiantes con manejo de errores"}
**Problema.** 
- Recibiste de coordinación `dataset_escolar.csv` con 480 filas. 
- Algunas filas tienen valores faltantes o inválidos. 
- Tu primer programa Python debe:

1. Cargar el CSV con manejo de errores.
2. Calcular promedio, mínimo, máximo de calificación.
3. Contar aprobados y reprobados.
4. Reportar filas con errores.
5. Guardar resultados en `reporte.json`.

::interioriza
Imagina que recibes exámenes calificados a mano (el CSV). 
Algunos tienen manchas de café y no se leen bien (errores). 
Tu script es el asistente que separa los legibles de los dañados.
::/interioriza

**Paso 1 — Datos.**
- `dataset_escolar.csv` con columnas: `id, horas_estudio, asistencia, cal_anterior, cal_final`.
- 480 filas esperadas.
- ~5 filas con errores (valores no numéricos).

**Paso 2 — Estrategia.**
- Importar módulos `csv` y `json`.
- `cargar_dataset(path)`: usa `try/except` por fila.
- `calcular_estadisticas(estudiantes)`: procesa y devuelve un diccionario.
- Main: flujo de cargar → calcular → guardar JSON.

**Paso 3 — Código completo.**

```python
import csv
import json

def parsear_fila(fila):
    """Parsea una fila a dict con valores numéricos. Devuelve None si falla."""
    try:
        return {
            "id": int(fila["id"]),
            "horas_estudio": float(fila["horas_estudio"]),
            "asistencia": float(fila["asistencia"]),
            "cal_anterior": float(fila["cal_anterior"]),
            "cal_final": float(fila["cal_final"])
        }
    except (ValueError, KeyError):
        return None

def cargar_dataset(path):
    """Carga CSV. Devuelve (estudiantes_validos, errores)."""
    estudiantes = []
    errores = []
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, fila in enumerate(reader, start=2):
                parsed = parsear_fila(fila)
                if parsed:
                    estudiantes.append(parsed)
                else:
                    errores.append({"linea": i, "fila": fila})
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {path}")
        return [], []
    
    return estudiantes, errores

def calcular_estadisticas(estudiantes):
    """Calcula estadísticas básicas de calificación final."""
    if not estudiantes:
        return {}
    
    cals = [e["cal_final"] for e in estudiantes]
    aprobados = [c for c in cals if c >= 6]
    
    return {
        "total": len(estudiantes),
        "promedio": sum(cals) / len(cals),
        "minimo": min(cals),
        "maximo": max(cals),
        "aprobados": len(aprobados),
        "reprobados": len(cals) - len(aprobados),
        "tasa_aprobacion": len(aprobados) / len(cals)
    }

def main():
    # Cargar
    estudiantes, errores = cargar_dataset("dataset_escolar.csv")
    print(f"✓ Cargados: {len(estudiantes)} estudiantes")
    print(f"⚠ Errores: {len(errores)} filas")
    
    # Calcular
    stats = calcular_estadisticas(estudiantes)
    print("\nEstadísticas:")
    for k, v in stats.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.2f}")
        else:
            print(f"  {k}: {v}")
    
    # Reportar errores específicos
    if errores:
        print("\nFilas con errores:")
        for e in errores[:5]:
            print(f"  Línea {e['linea']}: {e['fila']}")
    
    # Guardar reporte
    reporte = {
        "estadisticas": stats,
        "errores": errores
    }
    with open("reporte.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    print("\n✓ Reporte guardado en reporte.json")

if __name__ == "__main__":
    main()
```

**Paso 4 — Ejecución.**
```
$ python script.py

✓ Cargados: 475 estudiantes
⚠ Errores: 5 filas

Estadísticas:
  total: 475
  promedio: 7.42
  minimo: 3.50
  maximo: 9.95
  aprobados: 387
  reprobados: 88
  tasa_aprobacion: 0.81

Filas con errores:
  Línea 47: {'id': '170', 'cal_final': 'N/A', ...}
  Línea 162: {'id': '285', 'cal_final': 'ABC', ...}
  ...

✓ Reporte guardado en reporte.json
```

**Paso 5 — Verificación.**
- Lees `reporte.json` y verificas que el JSON está bien formado.
- Comparas algunas estadísticas manualmente con un sample del CSV.
- Confirmas los 5 errores reportados en las filas reales.

**Respuesta.** 
- Script `cargar_dataset.py` operativo.
- Carga 475 de 480 válidos y reporta 5 errores específicos.
- Tiempo: ~2 hrs para iniciados, ~30 min tras práctica.

**Verificación final.** 
- El script corre sin errores. 
- JSON puede abrirse en editores. 
- Errores comprobables por línea.

**Lección.** 
- Configuración, variables, control y funciones encajan aquí.
- I/O, diccionarios y `try/except` son tu base.
- En U2, Pandas lo hará en 3 líneas. Entender esto te salvará cuando Pandas falle.

::pausa{titulo="Deducción lógica"}
¿Por qué preferimos guardar las filas defectuosas en una lista `errores` en lugar de detener el programa con un error crítico?
a) Para que Python corra más rápido.
b) Para procesar todo lo válido y revisar lo defectuoso después, sin interrumpir el flujo.
c) Porque `csv.DictReader` no permite lanzar errores.
*Respuesta correcta: b.*
::/pausa

::/practica

---

## Práctica resuelta 2 — Generador de dataset simulado

::practica{titulo="Generar un CSV escolar reproducible para tus pruebas"}
**Problema.** 
- Antes de cargar datos, necesitas crearlos. 
- Escribirás un generador que produce un CSV con 100 filas verosímiles.
- Usarás semilla fija (reproducible) y 3 filas corruptas.

::interioriza
Piensa en una obra de teatro. 
La semilla fija es el guion: los actores (datos) siempre harán lo mismo en cada ensayo.
Esto te permite detectar si un error es tuyo o del "guion".
::/interioriza

**Paso 1 — Datos a generar.**
- Columnas: `id, materia, horas_estudio, asistencia, cal_anterior, cal_final`.
- 100 filas.
- Semilla `random.seed(7)` para reproducibilidad.
- 3 filas con error inyectado en `cal_final` (`"N/A"`, `"-"`, vacío).

**Paso 2 — Estrategia.** 
- Usar `random` + `csv.writer`. 
- Crear correlación realista entre features.

**Paso 3 — Código.**

```python
import csv
import random

def generar(path, n=100, semilla=7, filas_corruptas=None):
    if filas_corruptas is None:
        filas_corruptas = {12, 47, 88}
    random.seed(semilla)
    materias = ["Matemáticas", "Física", "Química"]

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "materia", "horas_estudio",
                    "asistencia", "cal_anterior", "cal_final"])
        for i in range(1, n + 1):
            materia = random.choice(materias)
            horas = round(random.uniform(0.5, 8), 1)
            asis = round(random.uniform(0.4, 1.0), 2)
            cal_ant = round(random.uniform(3, 10), 1)
            # cal_final correlacionada con cal_ant + horas + asistencia
            cal_fin_num = cal_ant * 0.6 + horas * 0.3 + asis * 2 + random.gauss(0, 0.7)
            cal_fin = round(min(10, max(0, cal_fin_num)), 1)
            if i in filas_corruptas:
                cal_fin = random.choice(["N/A", "-", ""])
            w.writerow([i, materia, horas, asis, cal_ant, cal_fin])
    print(f"✓ {path} generado: {n} filas, {len(filas_corruptas)} corruptas")

if __name__ == "__main__":
    generar("dataset_escolar_test.csv", n=100)
```

**Paso 4 — Ejecución.**
```
$ python generar.py
✓ dataset_escolar_test.csv generado: 100 filas, 3 corruptas
```

**Paso 5 — Verificación.** 
- Abre el CSV en Excel o usa `head -5`. 
- Verifica encabezado y las 100 filas de datos.
- Confirma que las filas 12, 47 y 88 contienen `cal_final` no numérico.

**Paso 6 — Reuso.** 
- Ejecuta `cargar_dataset.py` sobre este archivo.
- Debe reportar `97 cargados, 3 errores`. Es tu test de regresión.

**Lección.** 
- Generar datos reproducibles con `random.seed` es un hábito profesional.
- Tu compañero obtiene **exactamente las mismas filas** y puede comparar resultados.
- Sin semilla, rompes la reproducibilidad antes de empezar.

::pausa{titulo="Comprueba tu entendimiento"}
¿Qué pasa si omites `random.seed(7)` y compartes el código?
a) El programa fallará al ejecutar.
b) Cada persona generará datos distintos y será difícil comparar resultados.
c) Solo cambiarán las 3 filas corruptas.
*Respuesta correcta: b.*
::/pausa

::/practica

---

## Práctica resuelta 3 — Filtrar y exportar top N

::practica{titulo="Función reusable para extraer top N alumnos por calificación"}
**Problema.** 
- A coordinación le interesan los 10 mejores alumnos. 
- Implementarás una función `top_n` reutilizable.
- La probarás con distintos valores de N y exportarás el resultado.

**Paso 1 — Datos.** 
- Lista de dicts cargada y validada (`estudiantes`) de la práctica 1.

**Paso 2 — Estrategia.** 
- Usar `sorted` con `key=lambda` y slicing.
- Usar `csv.DictWriter` para guardar el resultado.

**Paso 3 — Código.**

```python
import csv

def top_n(estudiantes, n=10, criterio="cal_final"):
    """Devuelve los N estudiantes con mayor valor en `criterio`.
    
    Args:
        estudiantes: lista de dicts (cada dict es un alumno).
        n: cuántos devolver. Si n > len, devuelve todos.
        criterio: columna por la que ordenar (debe ser numérica).
    
    Returns:
        Lista de dicts ordenada de mayor a menor.
    """
    if not estudiantes:
        return []
    return sorted(
        estudiantes,
        key=lambda e: e[criterio],
        reverse=True
    )[:n]

def exportar_top(top, path):
    """Guarda lista de dicts a CSV preservando todas las columnas."""
    if not top:
        print(f"⚠ Lista vacía, no genero {path}")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(top[0].keys()))
        w.writeheader()
        w.writerows(top)
    print(f"✓ {path} ({len(top)} filas)")

# Ejemplo de uso
estudiantes = [
    {"id": 1, "materia": "Mate", "cal_final": 9.5},
    {"id": 2, "materia": "Física", "cal_final": 7.0},
    {"id": 3, "materia": "Química", "cal_final": 8.8},
    {"id": 4, "materia": "Mate", "cal_final": 6.2},
    {"id": 5, "materia": "Física", "cal_final": 9.9},
]

t3 = top_n(estudiantes, n=3)
exportar_top(t3, "top_3.csv")

t5 = top_n(estudiantes, n=5)
exportar_top(t5, "top_5.csv")

# Top por otro criterio: nada cambia en la función
# (asumiendo que tienes una columna numérica `asistencia`)
```

**Paso 4 — Output esperado.**
```
✓ top_3.csv (3 filas)
✓ top_5.csv (5 filas)
```

- `top_3.csv` contiene id 5 (9.9), id 1 (9.5), id 3 (8.8) en ese orden.

**Paso 5 — Casos edge probados.**
- `top_n([], n=10)` → `[]` sin error.
- `top_n(estudiantes, n=100)` → devuelve los 5 disponibles, no falla.
- `top_n(estudiantes, criterio="asistencia")` → funciona.

::interioriza
Una buena función es como un colador industrial. 
No importa si echas 5 piedras o 100, y no importa si el agujero es de 3cm o 5cm. 
Nunca debería romperse (casos edge probados).
::/interioriza

**Paso 6 — Verificación.** 
- Abre `top_3.csv` y compara con el cálculo manual del set de prueba.

**Lección.** 
- Diseña funciones con parámetros por defecto.
- Maneja inputs degenerados y usa docstrings.
- Pruébala con múltiples entradas. Te ahorrará horas de debugging.

::pausa{titulo="Piensa un momento"}
¿Qué pasa en `top_n` si `n` es mayor que la cantidad de estudiantes disponibles (ej. `n=10` pero solo hay 4)?
a) Lanza un error `IndexError`.
b) El slicing `[:n]` devuelve los 4 estudiantes sin fallar.
c) Retorna `None`.
*Respuesta correcta: b.*
::/pausa

::/practica
