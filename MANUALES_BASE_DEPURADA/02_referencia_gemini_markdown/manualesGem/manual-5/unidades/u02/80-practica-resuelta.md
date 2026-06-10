---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 02

::practica{titulo="Cargar, limpiar y analizar dataset escolar con pandas en 30 líneas"}
**Problema.** Replicar el script de U1 (50 líneas) usando pandas (objetivo: <30 líneas) y agregar análisis: estadísticas por materia, top 10 alumnos, identificación de outliers.

**Paso 1 — Datos.**
- `dataset_escolar.csv` con 480 filas: id, materia, horas_estudio, asistencia, cal_anterior, cal_final.
- Esperados ~10 nulos, ~5 duplicados, ~3 outliers.

**Paso 2 — Estrategia.** pandas: read_csv → limpiar → groupby → top → outliers → guardar.

**Paso 3 — Código completo.**

```python
import pandas as pd

# 1. Cargar
df = pd.read_csv("dataset_escolar.csv")
print(f"Inicial: {df.shape}")

# 2. Inspeccionar
print(df.info())
print(df.describe())

# 3. Limpiar
df = (df
    .drop_duplicates(subset=["id"])
    .dropna(subset=["cal_final"])
    .assign(asistencia=df["asistencia"].fillna(df["asistencia"].mean()))
    .query("0 <= cal_final <= 10")
    .query("0 <= asistencia <= 1")
    .reset_index(drop=True)
)
print(f"Limpio: {df.shape}")

# 4. Estadísticas globales
print(f"Promedio: {df['cal_final'].mean():.2f}")
print(f"Aprobados: {(df['cal_final'] >= 6).mean()*100:.1f}%")

# 5. Por materia
por_materia = df.groupby("materia").agg(
    n=("id", "count"),
    promedio=("cal_final", "mean"),
    aprobados=("cal_final", lambda x: (x >= 6).mean())
).round(2)
print("\nPor materia:")
print(por_materia)

# 6. Top 10
top = df.nlargest(10, "cal_final")[["id", "materia", "cal_final", "asistencia"]]
print("\nTop 10:")
print(top)

# 7. Outliers (fuera 1.5*IQR)
q1 = df["cal_final"].quantile(0.25)
q3 = df["cal_final"].quantile(0.75)
iqr = q3 - q1
outliers = df[(df["cal_final"] < q1 - 1.5*iqr) | (df["cal_final"] > q3 + 1.5*iqr)]
print(f"\nOutliers: {len(outliers)}")

# 8. Guardar
df.to_csv("dataset_limpio.csv", index=False)
por_materia.to_csv("estadisticas_materia.csv")
```

**Paso 4 — Ejecución.**
```
Inicial: (480, 6)
Limpio: (467, 6)
Promedio: 7.42
Aprobados: 81.2%

Por materia:
              n  promedio  aprobados
Física      155      7.42       0.81
Matemáticas 158      6.95       0.74
Química     154      7.65       0.85

Top 10:
[tabla con 10 alumnos top]

Outliers: 7
```

**Paso 5 — Verificación.** Total filas con limpias + duplicados + nulos + outliers = 480 ✓. Estadísticas coinciden con cálculo manual de muestra.

**Respuesta.** Script de **22 líneas efectivas** que reemplaza las 50+ del Episodio 1. Genera 2 archivos de salida + reporte en consola. Tiempo de desarrollo: 30 min con experiencia, 1.5 horas para principiante.

**Lección.** pandas no es solo "más corto": es **más expresivo**. Cada línea hace una cosa clara. Cada operación es vectorizada (rápida). Resultado: código que se lee como descripción de lo que hace, no como instrucciones paso a paso.
::/practica

---

## Práctica resuelta 2 — Crear feature derivada y exportar segmentado

::practica{titulo="Construir columna 'estado_riesgo' y exportar 3 archivos por nivel"}
**Problema.** Coordinación necesita que entregues 3 archivos: `riesgo_alto.csv`, `riesgo_medio.csv`, `riesgo_bajo.csv`, cada uno con los alumnos clasificados según una regla de negocio.

**Paso 1 — Regla de negocio.**
- **Riesgo alto:** `cal_final < 6` o `asistencia < 0.7`.
- **Riesgo medio:** `6 <= cal_final < 7.5` y `asistencia >= 0.7`.
- **Riesgo bajo:** `cal_final >= 7.5` y `asistencia >= 0.7`.

**Paso 2 — Estrategia.** Crear feature `estado_riesgo` con `np.select` y luego exportar por grupos con `groupby`.

**Paso 3 — Código.**

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_escolar_limpio.csv")

# Definir condiciones (orden importa: la primera que matchea gana)
condiciones = [
    (df["cal_final"] < 6) | (df["asistencia"] < 0.7),
    (df["cal_final"] >= 7.5) & (df["asistencia"] >= 0.7),
]
etiquetas = ["alto", "bajo"]

df["estado_riesgo"] = np.select(condiciones, etiquetas, default="medio")

# Verificar distribución
print("Distribución de riesgo:")
print(df["estado_riesgo"].value_counts())

# Exportar archivos separados
for nivel, sub in df.groupby("estado_riesgo"):
    nombre = f"riesgo_{nivel}.csv"
    sub.to_csv(nombre, index=False)
    print(f"✓ {nombre}: {len(sub)} alumnos")

# Tabla resumen para el reporte
resumen = df.groupby("estado_riesgo").agg(
    n=("id", "count"),
    cal_promedio=("cal_final", "mean"),
    asistencia_promedio=("asistencia", "mean"),
    horas_promedio=("horas_estudio", "mean")
).round(2)
print("\nResumen por nivel de riesgo:")
print(resumen)
resumen.to_csv("resumen_riesgo.csv")
```

**Paso 4 — Output esperado.**
```
Distribución de riesgo:
medio    245
bajo     158
alto      62

✓ riesgo_alto.csv: 62 alumnos
✓ riesgo_bajo.csv: 158 alumnos
✓ riesgo_medio.csv: 245 alumnos

Resumen por nivel de riesgo:
                  n  cal_promedio  asistencia_promedio  horas_promedio
estado_riesgo
alto             62          5.32                 0.74            2.85
bajo            158          8.42                 0.91            5.60
medio           245          6.85                 0.85            4.20
```

**Paso 5 — Verificación.**
- `len(df_alto) + len(df_medio) + len(df_bajo) == len(df)` ✓.
- Promedios coherentes con las reglas (alto debe tener promedio < bajo).
- Abrir `riesgo_alto.csv` y verificar que las 5 primeras filas cumplen las condiciones.

**Paso 6 — Bonus.** Mostrar % por materia en cada nivel:

```python
pivot = pd.crosstab(df["materia"], df["estado_riesgo"], normalize="index") * 100
print(pivot.round(1))
```

**Lección.** `np.select` es la herramienta correcta para múltiples condiciones excluyentes (vs `np.where` que solo hace if/else binario). Combinada con `groupby` + iteración, te permite generar **N archivos derivados con una sola pasada**. Esta es la mecánica que coordinación va a usar mes a mes para reportes operativos.
::/practica

---

## Práctica resuelta 3 — Auditar tipos y reportar inconsistencias

::practica{titulo="Auditor automático de calidad de datos antes de modelar"}
**Problema.** Antes de entregar el dataset al modelo de U5, generas un **reporte de auditoría** que detecta y cuantifica problemas: tipos incorrectos, rangos imposibles, valores raros.

**Paso 1 — Estrategia.** Función `auditar(df)` que devuelve dict con todas las banderas + función `print_reporte(auditoria)` que lo imprime legible.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np

def auditar(df):
    """Devuelve dict con problemas detectados en df."""
    problemas = {}

    # 1. Tipos esperados
    tipos_esperados = {
        "id": "int",
        "horas_estudio": "float",
        "asistencia": "float",
        "cal_anterior": "float",
        "cal_final": "float",
    }
    tipos_mal = {}
    for col, esperado in tipos_esperados.items():
        if col in df.columns:
            tipo_real = str(df[col].dtype)
            if esperado not in tipo_real:
                tipos_mal[col] = f"esperado {esperado}, encontrado {tipo_real}"
    problemas["tipos_incorrectos"] = tipos_mal

    # 2. Nulos
    nulos = df.isna().sum().to_dict()
    problemas["nulos_por_columna"] = {k: int(v) for k, v in nulos.items() if v > 0}

    # 3. Rangos imposibles
    rangos = {
        "asistencia": (0, 1),
        "cal_anterior": (0, 10),
        "cal_final": (0, 10),
        "horas_estudio": (0, 24),
    }
    fuera_rango = {}
    for col, (lo, hi) in rangos.items():
        if col in df.columns:
            n = ((df[col] < lo) | (df[col] > hi)).sum()
            if n > 0:
                fuera_rango[col] = int(n)
    problemas["fuera_de_rango"] = fuera_rango

    # 4. Duplicados por id
    if "id" in df.columns:
        problemas["duplicados_por_id"] = int(df.duplicated(subset=["id"]).sum())

    # 5. Outliers IQR (solo cal_final como ejemplo)
    if "cal_final" in df.columns:
        q1, q3 = df["cal_final"].quantile([0.25, 0.75])
        iqr = q3 - q1
        outliers = ((df["cal_final"] < q1 - 1.5*iqr) |
                    (df["cal_final"] > q3 + 1.5*iqr)).sum()
        problemas["outliers_cal_final_iqr"] = int(outliers)

    # 6. Salud general
    problemas["filas_total"] = int(len(df))
    problemas["columnas"] = list(df.columns)

    return problemas

def print_reporte(auditoria):
    print("=" * 50)
    print("REPORTE DE AUDITORÍA DE DATOS")
    print("=" * 50)
    print(f"Filas totales: {auditoria['filas_total']}")
    print(f"Columnas: {len(auditoria['columnas'])}")
    print()
    if auditoria["tipos_incorrectos"]:
        print("⚠ TIPOS INCORRECTOS:")
        for col, msg in auditoria["tipos_incorrectos"].items():
            print(f"  · {col}: {msg}")
    else:
        print("✓ Todos los tipos correctos.")
    print()
    if auditoria["nulos_por_columna"]:
        print("⚠ NULOS:")
        for col, n in auditoria["nulos_por_columna"].items():
            print(f"  · {col}: {n} nulos")
    else:
        print("✓ Sin nulos.")
    print()
    if auditoria["fuera_de_rango"]:
        print("⚠ VALORES FUERA DE RANGO:")
        for col, n in auditoria["fuera_de_rango"].items():
            print(f"  · {col}: {n} filas")
    else:
        print("✓ Todos los valores dentro de rango.")
    print()
    print(f"Duplicados por id: {auditoria['duplicados_por_id']}")
    print(f"Outliers IQR cal_final: {auditoria['outliers_cal_final_iqr']}")
    print("=" * 50)

# Uso
df = pd.read_csv("dataset_escolar_limpio.csv")
audit = auditar(df)
print_reporte(audit)

import json
with open("auditoria.json", "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)
```

**Paso 3 — Output esperado (sobre dataset ya limpio).**
```
==================================================
REPORTE DE AUDITORÍA DE DATOS
==================================================
Filas totales: 465
Columnas: 6

✓ Todos los tipos correctos.

✓ Sin nulos.

✓ Todos los valores dentro de rango.

Duplicados por id: 0
Outliers IQR cal_final: 7
==================================================
```

**Paso 4 — Verificación.** Corre el auditor sobre el **dataset sucio** original; debes ver 12 nulos, 3 fuera de rango, 8 duplicados — exactamente lo inyectado.

**Lección.** Antes de entrenar cualquier modelo (U5+), corre tu auditor. Es un **gate de calidad** que detecta regresiones cuando el dataset cambia (nuevo bimestre, nueva fuente). Sin auditor, los bugs de datos llegan al modelo y nadie los ve hasta que las predicciones son raras.
::/practica
