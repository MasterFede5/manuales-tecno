---
unidad: 2
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 02

::albatros{titulo="Limpia el dataset escolar con valores faltantes y duplicados" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si tu CSV tiene 480 filas declaradas pero 12 nulos, 8 duplicados y 3 outliers obvios, ¿cuántas filas terminan en tu modelo?

**Contexto del case.** El predictor escolar va a entrenarse con este dataset; basura entra, basura sale. Antes de modelar, **limpia con criterio**: cada decisión documentada con un comentario.

### Materiales

- Python 3 + pandas + numpy.
- Jupyter o Colab (recomendado por el output rico).
- Dataset simulado del taller U1 (`dataset_escolar.csv`) o uno nuevo.

### Pasos del taller (60 min)

**Paso 1 — Generar dataset con problemas a propósito (10 min).**

```python
import csv
import random

random.seed(42)
materias = ["Matemáticas", "Física", "Química"]

with open("dataset_escolar_sucio.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "materia", "horas_estudio", "asistencia",
                "cal_anterior", "cal_final"])
    for i in range(1, 481):
        materia = random.choice(materias)
        horas = round(random.uniform(0.5, 8), 1)
        asis = round(random.uniform(0.4, 1.0), 2)
        cal_ant = round(random.uniform(3, 10), 1)
        cal_fin = round(min(10, max(0,
            cal_ant * 0.6 + horas * 0.3 + asis * 2 + random.gauss(0, 0.7))), 1)
        # Inyectar nulos
        if i in {25, 47, 88, 162, 200, 250, 301, 333, 380, 410, 450, 470}:
            cal_fin = ""
        # Asistencia inválida
        if i in {15, 100, 333}:
            asis = 1.5
        w.writerow([i, materia, horas, asis, cal_ant, cal_fin])
    # Inyectar duplicados (8 filas repetidas)
    for dup_id in [50, 75, 130, 175, 220, 275, 320, 400]:
        w.writerow([dup_id, "Matemáticas", 5.0, 0.85, 7.0, 7.5])
print("✓ Dataset sucio generado: 488 filas escritas (480 + 8 dup)")
```

**Paso 2 — Inspección inicial (5 min).**

```python
import pandas as pd

df = pd.read_csv("dataset_escolar_sucio.csv")
print(f"Shape inicial: {df.shape}")
print(f"\nDtypes:\n{df.dtypes}")
print(f"\nNulos por columna:\n{df.isna().sum()}")
print(f"\nDuplicados por id: {df.duplicated(subset=['id']).sum()}")
print(f"\nFilas con asistencia > 1: {(df['asistencia'] > 1).sum()}")
print(f"\nDescribe numérico:\n{df.describe()}")
```

Output esperado:
```
Shape inicial: (488, 6)
Nulos por columna:
  cal_final     12
  resto:         0
Duplicados por id: 8
Filas con asistencia > 1: 3
```

**Paso 3 — Diseñar el pipeline de limpieza (10 min).**

Antes de escribir código, decide en papel/comentarios:

```python
# Decisiones documentadas (defendibles ante coordinación):
# 1. Duplicados por `id`: conservar primera ocurrencia. (drop_duplicates)
# 2. cal_final NaN: descartar fila (no podemos predecir sin label).
# 3. asistencia > 1: imposible — descartar.
# 4. asistencia < 0: imposible — descartar.
# 5. cal_final fuera de [0,10]: descartar.
# Total esperado: 488 - 8 - 12 - 3 ≈ 465 filas
```

**Paso 4 — Implementar pipeline con method chaining (15 min).**

```python
def limpiar(df):
    inicial = len(df)
    df_limpio = (df
        .drop_duplicates(subset=["id"], keep="first")
        .dropna(subset=["cal_final"])
        .query("0 <= asistencia <= 1")
        .query("0 <= cal_final <= 10")
        .reset_index(drop=True)
    )
    final = len(df_limpio)
    print(f"Limpieza: {inicial} → {final} filas (-{inicial-final})")
    return df_limpio

df_limpio = limpiar(df)
print(df_limpio.head())
print(df_limpio.describe())
```

Output esperado: `Limpieza: 488 → 465 filas (-23)`.

**Paso 5 — Reporte de limpieza (10 min).**

```python
def reporte_limpieza(df_original, df_limpio):
    return {
        "filas_original": len(df_original),
        "filas_limpias": len(df_limpio),
        "filas_eliminadas": len(df_original) - len(df_limpio),
        "porcentaje_perdido": round(
            (len(df_original) - len(df_limpio)) / len(df_original) * 100, 2),
        "duplicados_eliminados": int(df_original.duplicated(subset=["id"]).sum()),
        "nulos_eliminados": int(df_original["cal_final"].isna().sum()),
        "asistencia_invalida": int((df_original["asistencia"] > 1).sum() +
                                   (df_original["asistencia"] < 0).sum()),
    }

import json
reporte = reporte_limpieza(df, df_limpio)
with open("reporte_limpieza.json", "w", encoding="utf-8") as f:
    json.dump(reporte, f, indent=2, ensure_ascii=False)
print(json.dumps(reporte, indent=2, ensure_ascii=False))
```

**Paso 6 — Análisis grupal post-limpieza (5 min).**

```python
print("Por materia (limpio):")
print(df_limpio.groupby("materia").agg(
    n=("id", "count"),
    promedio=("cal_final", "mean"),
    aprobados=("cal_final", lambda x: (x >= 6).mean())
).round(2))

# Guardar
df_limpio.to_csv("dataset_escolar_limpio.csv", index=False)
print("✓ dataset_escolar_limpio.csv guardado")
```

**Paso 7 — Reto extra (5 min).** Agrega imputación inteligente: en lugar de descartar filas con `cal_anterior` NaN (si ocurriera), imputa con el promedio **de la misma materia**. Pista:

```python
df["cal_anterior"] = df.groupby("materia")["cal_anterior"].transform(
    lambda s: s.fillna(s.mean())
)
```

### Entregable

- Notebook o `.py` con las 7 secciones.
- `dataset_escolar_limpio.csv` (≈465 filas).
- `reporte_limpieza.json` con números defendibles.
- Comentarios documentando **cada decisión** de limpieza.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Inspección inicial | sin | shape + dtypes | + nulos + duplicados + describe |
| Decisiones documentadas | none | 1-2 comentadas | 5 con justificación |
| Pipeline method chaining | for-loops sueltos | algunos métodos | una sola expresión chained |
| Reporte cuantitativo | sin números | algunos | JSON completo |
| Reto extra (imputación) | no intentado | mal | imputación grupal funcional |

### Conexión con el case

El `dataset_escolar_limpio.csv` es **el dataset que va a alimentar U3 (visualización), U4 (estadística), U5 (modelo) y U7 (red neuronal)**. Cada decisión que documentaste hoy (por qué descartaste vs imputaste) deberás defenderla cuando coordinación pregunte por qué tu modelo da las predicciones que da.
::/albatros
