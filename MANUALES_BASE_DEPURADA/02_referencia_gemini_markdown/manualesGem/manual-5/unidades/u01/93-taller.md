---
unidad: 1
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 01

::albatros{titulo="Tu primer dataset cargado y explorado en Python puro" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Cuántas líneas de código necesitas para "abrir" un dataset escolar y describirlo a coordinación con cifras reales?

**Contexto del case.** Coordinación te entregó `dataset_escolar.csv` (480 filas). Antes de meterte con pandas en U2, vas a manipular el archivo a mano usando solo la librería estándar. Esto te da intuición sólida sobre qué hace pandas por debajo.

### Materiales

- Python 3.10+ instalado (Anaconda) **o** Google Colab (recomendado para empezar).
- Editor: Jupyter Notebook, VS Code o Colab.
- Librerías: solo `csv`, `json` y `statistics` (todas vienen con Python).
- Archivo `dataset_escolar.csv` simulado (lo generas en el paso 1).

### Pasos del taller (60 min)

**Paso 1 — Generar el dataset simulado (10 min).**

Crea `generar_dataset.py` y ejecútalo una vez:

```python
import csv
import random

random.seed(42)
materias = ["Matemáticas", "Física", "Química"]

with open("dataset_escolar.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "materia", "horas_estudio", "asistencia", "cal_anterior", "cal_final"])
    for i in range(1, 481):
        materia = random.choice(materias)
        horas = round(random.uniform(0.5, 8), 1)
        asis = round(random.uniform(0.4, 1.0), 2)
        cal_ant = round(random.uniform(3, 10), 1)
        # cal_final correlacionada
        cal_fin = round(min(10, max(0, cal_ant * 0.6 + horas * 0.3 + asis * 2 + random.gauss(0, 0.8))), 1)
        # Inyectar 5 filas con error
        if i in {47, 162, 233, 301, 419}:
            cal_fin = "N/A"
        w.writerow([i, materia, horas, asis, cal_ant, cal_fin])
print("✓ dataset_escolar.csv generado con 480 filas (5 corruptas)")
```

**Paso 2 — Crear `eda_basico.py` con la estructura mínima (5 min).**

```python
import csv
import json
from statistics import mean, median, stdev

PATH = "dataset_escolar.csv"

def cargar(path):
    """TODO: paso 3."""
    pass

def resumir(estudiantes):
    """TODO: paso 4."""
    pass

if __name__ == "__main__":
    estudiantes, errores = cargar(PATH)
    print(f"Cargados: {len(estudiantes)} · Errores: {len(errores)}")
    resumen = resumir(estudiantes)
    print(json.dumps(resumen, indent=2, ensure_ascii=False))
```

**Paso 3 — Implementar `cargar` con manejo de errores (15 min).**

```python
def cargar(path):
    estudiantes, errores = [], []
    with open(path, "r", encoding="utf-8") as f:
        for i, fila in enumerate(csv.DictReader(f), start=2):
            try:
                estudiantes.append({
                    "id": int(fila["id"]),
                    "materia": fila["materia"],
                    "horas_estudio": float(fila["horas_estudio"]),
                    "asistencia": float(fila["asistencia"]),
                    "cal_anterior": float(fila["cal_anterior"]),
                    "cal_final": float(fila["cal_final"]),
                })
            except (ValueError, KeyError) as e:
                errores.append({"linea": i, "motivo": str(e)})
    return estudiantes, errores
```

**Paso 4 — Implementar `resumir` con estadísticas básicas (15 min).**

```python
def resumir(estudiantes):
    cals = [e["cal_final"] for e in estudiantes]
    horas = [e["horas_estudio"] for e in estudiantes]
    materias = {}
    for e in estudiantes:
        materias.setdefault(e["materia"], []).append(e["cal_final"])
    return {
        "n": len(estudiantes),
        "cal_final": {
            "media": round(mean(cals), 2),
            "mediana": round(median(cals), 2),
            "std": round(stdev(cals), 2),
            "min": min(cals),
            "max": max(cals),
        },
        "horas_promedio": round(mean(horas), 2),
        "tasa_aprobacion": round(sum(1 for c in cals if c >= 6) / len(cals), 3),
        "por_materia": {m: round(mean(v), 2) for m, v in materias.items()},
    }
```

**Paso 5 — Ejecutar y verificar el output (5 min).**

```
$ python eda_basico.py
Cargados: 475 · Errores: 5
{
  "n": 475,
  "cal_final": {"media": 7.42, "mediana": 7.5, "std": 1.49, "min": 3.5, "max": 9.9},
  "horas_promedio": 4.27,
  "tasa_aprobacion": 0.812,
  "por_materia": {"Matemáticas": 6.95, "Física": 7.42, "Química": 7.65}
}
```

**Paso 6 — Guardar reporte en JSON (5 min).**

Agrega al `__main__`:

```python
with open("reporte_eda.json", "w", encoding="utf-8") as f:
    json.dump({"resumen": resumen, "errores": errores}, f, indent=2, ensure_ascii=False)
print("✓ reporte_eda.json guardado")
```

**Paso 7 — Reto extra (5 min).** Agrega a `resumir` un campo `top_5` con los 5 estudiantes con `cal_final` más alta. Pista: usa `sorted(estudiantes, key=lambda e: e["cal_final"], reverse=True)[:5]`.

### Entregable

- `generar_dataset.py` y `dataset_escolar.csv`.
- `eda_basico.py` ejecutable.
- `reporte_eda.json` generado.
- Captura del output en consola.
- Notebook (o `.py` con comentarios) con tu razonamiento.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Dataset generado | no se generó | corre con warnings | 480 filas + 5 corruptas inyectadas |
| Carga con errores | crashea | atrapa pero no reporta | `(estudiantes, errores)` con línea y motivo |
| Estadísticas | una métrica | 3-4 métricas | nivel del paso 4 + `por_materia` |
| Reto extra (top 5) | sin intentar | intentado | implementado correctamente |
| JSON guardado | inexistente | mal formado | válido y legible |

### Conexión con el case

El `reporte_eda.json` que produjiste **es el primer entregable formal del Predictor de rendimiento escolar**. En U2 lo vas a regenerar en 5 líneas con pandas; en U3 lo vas a graficar; en U5 vas a entrenar el modelo sobre estos mismos datos. Guarda el archivo: lo necesitas las próximas 7 unidades.
::/albatros
