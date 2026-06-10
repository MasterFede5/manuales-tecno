---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 02

::practica{titulo="Cargar, limpiar y analizar dataset escolar con pandas en 30 líneas"}
**Problema.** Replicar el script de U1 (50 líneas) con pandas (<30 líneas).
- Debemos agregar estadísticas por materia.
- Obtener el top 10 de alumnos.
- Identificar los *outliers*.

**Paso 1 — Datos.**
- Archivo: `dataset_escolar.csv` (480 filas).
- Columnas: id, materia, horas_estudio, asistencia, cal_anterior, cal_final.
- Esperados: ~10 nulos, ~5 duplicados, ~3 outliers.

**Paso 2 — Estrategia.**
- `read_csv` → limpiar → `groupby` → `top` → outliers → guardar.

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
print("\nPor materia:\n", por_materia)

# 6. Top 10
top = df.nlargest(10, "cal_final")[["id", "materia", "cal_final", "asistencia"]]
print("\nTop 10:\n", top)

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

**Paso 4 — Ejecución y Verificación.**
- El output mostrará 467 filas limpias y 7 outliers.
- La suma de filas limpias, duplicados, nulos y outliers cuadra con las 480 iniciales.

::interioriza
Imagina que limpiar datos con Pandas es como colar café:
Pasas el filtro (`dropna`, `query`) y te quedas solo con el líquido puro, dejando los granos quemados (*outliers* y *nulos*) afuera. Todo en un solo movimiento fluido (métodos encadenados).
::/interioriza

::pausa{}
1. ¿Por qué usamos `reset_index(drop=True)` al final de la limpieza?
2. Si un alumno tiene calificación 12, ¿qué filtro lo eliminará?
::/pausa

**Lección.**
- Pandas no es solo más corto, es **más expresivo**.
- Cada línea hace una sola cosa clara usando operaciones vectorizadas rápidas.
- El código se lee como la descripción del proceso, no como instrucciones sueltas.
::/practica

---

## Práctica resuelta 2 — Crear feature y exportar

::practica{titulo="Construir columna 'estado_riesgo' y exportar 3 archivos por nivel"}
**Problema.** Coordinación pide 3 archivos CSV separados:
- `riesgo_alto.csv`, `riesgo_medio.csv` y `riesgo_bajo.csv`.
- Cada uno con alumnos clasificados según su rendimiento.

**Paso 1 — Regla de negocio.**
- **Alto:** `cal_final < 6` o `asistencia < 0.7`.
- **Medio:** `6 <= cal_final < 7.5` y `asistencia >= 0.7`.
- **Bajo:** `cal_final >= 7.5` y `asistencia >= 0.7`.

**Paso 2 — Estrategia y Código.**
- Usar `np.select` para clasificar según condiciones.
- Usar `groupby` para iterar y exportar archivos.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_escolar_limpio.csv")

# Condiciones excluyentes
condiciones = [
    (df["cal_final"] < 6) | (df["asistencia"] < 0.7),
    (df["cal_final"] >= 7.5) & (df["asistencia"] >= 0.7),
]
etiquetas = ["alto", "bajo"]

# Crear columna de riesgo
df["estado_riesgo"] = np.select(condiciones, etiquetas, default="medio")

# Exportar archivos separados
for nivel, sub in df.groupby("estado_riesgo"):
    nombre = f"riesgo_{nivel}.csv"
    sub.to_csv(nombre, index=False)
    print(f"✓ {nombre}: {len(sub)} alumnos")
```

**Paso 3 — Verificación.**
- Validar que la suma de filas de los 3 CSVs sea igual al total del dataset.
- Revisar que los promedios de calificación coincidan con el nivel de riesgo esperado.

::interioriza
`np.select` es como el semáforo de un club:
El guardia revisa tu credencial (primera condición). Si pasas, tienes pulsera VIP (etiqueta 1). Si no, vas a la fila regular (etiqueta 2). Si ninguna aplica, te mandan al patio (el `default`).
::/interioriza

::pausa{}
1. ¿Qué pasa si una fila cumple ambas condiciones en `np.select`?
2. ¿Por qué iteramos sobre `df.groupby()` en lugar de filtrar el DataFrame 3 veces?
::/pausa

**Lección.**
- `np.select` es ideal para múltiples condiciones excluyentes.
- Es mucho mejor que usar `np.where` anidados (que simula if/else binarios).
- Generar múltiples reportes derivados es una tarea operativa común.
::/practica

---

## Práctica resuelta 3 — Auditar calidad de datos

::practica{titulo="Auditor automático de calidad de datos antes de modelar"}
**Problema.** Antes de entrenar modelos, debes detectar:
- Tipos incorrectos.
- Valores fuera de rango.
- Datos anómalos o duplicados.

**Paso 1 — Estrategia.**
- Crear función `auditar(df)` que extraiga errores en un diccionario.
- Crear función `print_reporte(auditoria)` para leerlos fácilmente.

**Paso 2 — Código.**

```python
import pandas as pd

def auditar(df):
    problemas = {}
    
    # Nulos
    nulos = df.isna().sum().to_dict()
    problemas["nulos_por_columna"] = {k: v for k, v in nulos.items() if v > 0}
    
    # Rangos (Ej. asistencia 0-1)
    if "asistencia" in df.columns:
        fuera = ((df["asistencia"] < 0) | (df["asistencia"] > 1)).sum()
        if fuera > 0: problemas["fuera_de_rango"] = {"asistencia": int(fuera)}
        
    return problemas

def print_reporte(auditoria):
    print("=" * 30, "\nREPORTE DE AUDITORÍA\n", "=" * 30)
    for k, v in auditoria.items():
        print(f"{k.upper()}: {v}")

# Uso
df = pd.read_csv("dataset_escolar_limpio.csv")
print_reporte(auditar(df))
```

**Paso 3 — Verificación.**
- Ejecutar el script sobre el dataset original sin limpiar.
- Confirmar que detecta los 12 nulos y valores atípicos conocidos.

::interioriza
Tu script de auditoría es como el control de seguridad de un aeropuerto:
Nadie entra al avión (modelo de Machine Learning) sin que sus maletas (tipos de datos y rangos) pasen por los rayos X. Si algo está mal, suena la alarma antes de despegar.
::/interioriza

::pausa{}
1. ¿Por qué usar un diccionario para guardar los problemas detectados?
2. ¿Qué ocurriría si entrenas un modelo sin validar nulos y rangos imposibles?
::/pausa

**Lección.**
- El auditor automático es tu **puerta de calidad**.
- Protege a los modelos de problemas silenciosos (ej. datos nuevos corrompidos).
- Sin auditorías, los errores en datos se convierten en predicciones absurdas.
::/practica
