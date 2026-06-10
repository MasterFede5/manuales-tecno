---
unidad: 2
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 02

::act-mcq{titulo="Repaso conceptual"}
1. La diferencia clave entre lista de Python y np.array es:
   - [ ] np.array es más fácil de imprimir
   - [x] np.array es homogéneo y vectorizado, ~100× más rápido
   - [ ] No hay diferencia
   - [ ] np.array no soporta float

2. Para filtrar alumnos con calificación >= 8 Y asistencia >= 0.85:
   - [ ] `df[df["cal"] >= 8 and df["asis"] >= 0.85]`
   - [x] `df[(df["cal"] >= 8) & (df["asis"] >= 0.85)]`
   - [ ] `df[df["cal"] >= 8 || df["asis"] >= 0.85]`
   - [ ] `df.filter(cal>=8, asis>=0.85)`

3. Para calcular promedio de calificación por materia en una sola línea:
   - [ ] for-loop con if
   - [x] `df.groupby("materia")["cal"].mean()`
   - [ ] `df.pivot()`
   - [ ] No es posible

4. ¿Qué método elimina filas con valores NaN solo en una columna específica?
   - [ ] `df.dropna()`
   - [x] `df.dropna(subset=["columna"])`
   - [ ] `df.fillna()`
   - [ ] `df.drop()`

5. La función `pd.read_csv` con CSV europeo (separador `;`, decimales `,`) requiere:
   - [ ] Convertir el archivo primero
   - [x] Parámetros `sep=";"` y `decimal=","`
   - [ ] No funciona con europeo
   - [ ] Usar `csv` module
::/act-mcq

::act-table{titulo="Completa la tabla — operación pandas para cada caso"}
| Caso | Operación pandas |
|---|---|
| Promedio de calificación por materia |  |
| Top 5 alumnos por calificación |  |
| Eliminar filas duplicadas por id |  |
| Convertir columna "edad" a int |  |
| Filtrar materias específicas |  |
| Crear columna "aprobado" según calificación |  |
::/act-table

::act-match{titulo="Relaciona método pandas con uso"}
| Método | Uso |
|---|---|
| 1. `df.head()` | a) Eliminar duplicados |
| 2. `df.describe()` | b) Estadísticas básicas |
| 3. `df.groupby()` | c) Primeras 5 filas |
| 4. `df.dropna()` | d) Agrupar y agregar |
| 5. `df.drop_duplicates()` | e) Eliminar NaN |
| 6. `df.pivot_table()` | f) Tabla dinámica tipo Excel |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. NumPy puede tener arrays con tipos mezclados (int + str). ( ) ____________________________________________

2. `df.iloc[0]` y `df.loc[0]` siempre devuelven la misma fila. ( ) ____________________________________________

3. `df.dropna()` por defecto elimina cualquier fila con al menos un NaN. ( ) ____________________________________________

4. `groupby` es más rápido que iterar con loop sobre categorías. ( ) ____________________________________________

5. `pd.read_csv` siempre infiere tipos correctos automáticamente. ( ) ____________________________________________
::/act-tf

::albatros{titulo="Tu segundo programa: dataset escolar limpio en pandas con análisis grupal" tipo="taller" tiempo="3 h"}
**Pregunta detonadora.** Si tu programa de U1 (50 líneas) se reduce a 25 con pandas, ¿qué otras 5 cosas podrías agregar al análisis sin más tiempo?

::interioriza
Imagina que limpias tu cuarto. Pandas es como una aspiradora robot:
- Hace el trabajo pesado en menos líneas.
- Te deja tiempo para pensar y analizar tus resultados.
::/interioriza

**Lo que harás.**
- Toma el script de U1 y reescríbelo con pandas (<30 líneas).
- Agrega 5 análisis nuevos:
  - Estadísticas por materia y top 10 alumnos.
  - Distribución de notas y tasa de aprobación.
  - Outliers con IQR.
- Genera un reporte en CSV y un resumen en JSON.
- Documenta los métodos en el README y sube a GitHub.

::pausa{}
1. ¿Por qué es útil exportar el reporte en JSON además de CSV?
2. ¿Qué pasa si no identificamos a los outliers antes de calcular los promedios?
::/pausa

**Materiales y Entregable.**
- **Materiales:** Colab/Anaconda, pandas, GitHub (3 horas).
- **Entregable:** Script (`analisis_escolar.py`), CSV+JSON y README.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Reducción de líneas | <20% reducción | 50% reducción | <30 líneas con 5 análisis nuevos |
| Limpieza | sin tratar | dropna básico | pipeline con .drop_duplicates + dropna + clip |
| Análisis grupal | sin groupby | un groupby | múltiples agg + pivot_table |
| Outliers | sin detectar | manual | IQR documentado |
| Reportes | un archivo | dos | CSV + JSON con estructura clara |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="Convierte tipos en una columna mal tipada"}
La columna `cal_final` viene como string por filas con `'N/A'`. Limpia y convierte:

```python
import pandas as pd

df["cal_final"] = pd.___________(df["cal_final"], errors="___________")
# Ahora 'N/A' se volvió NaN. Filtra:
df = df.dropna(subset=["___________"]).reset_index(drop=True)
print(df["cal_final"].dtype)   # → ___________
```
::/act-fill

::act-order{titulo="Pipeline pandas óptimo: 6 pasos en orden"}
[ ] `groupby` para agregaciones por materia
[ ] `dropna` para nulos en columnas críticas
[ ] `read_csv` cargar
[ ] `to_csv` exportar limpio
[ ] `query` para filtrar rangos válidos (`0 <= cal_final <= 10`)
[ ] `drop_duplicates` por id
::/act-order

::act-case{titulo="Caso — agregación con bug sutil" lineas=12}
Tu compañera te muestra esto y dice "no entiendo por qué el promedio es raro":

```python
prom_por_materia = df.groupby("materia")["cal_final"].mean()
print(prom_por_materia)
# Matemáticas    7.05
# Física         NaN     ← ¿?
# Química        7.42
```

**Pregunta.** 
- ¿Por qué la materia `Física` da `NaN`?
- ¿Cómo lo arreglarías?
- Da 2 estrategias distintas con su respectiva implicación.
::/act-case

::act-mindmap{titulo="Mapa mental abierto" centro="LIMPIEZA DE DATOS" nodos_primarios=5 nodos_secundarios=10}
- **Nodos sugeridos:** Detectar, Decidir, Implementar, Documentar, Validar.
- **Acción:** Por cada nodo, anota 2 ejemplos concretos del taller.
::/act-mindmap

::act-table{titulo="Decisiones de limpieza y consecuencias"}
| Estrategia | Cuándo aplicar | Riesgo | Ejemplo en el case |
|---|---|---|---|
| `dropna` |  |  |  |
| `fillna(0)` |  |  |  |
| `fillna(media)` |  |  |  |
| `fillna(media por grupo)` |  |  |  |
| Imputación con modelo (KNN) |  |  |  |
::/act-table

::albatros{titulo="Reto Albatros — pipeline reusable como módulo importable" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.** Si tu pipeline de limpieza debiera correr **automáticamente cada lunes** con un nuevo CSV, ¿qué tan reusable está hoy?

::interioriza
Un notebook es como un borrador en sucio.
Un pipeline importable es como un filtro de agua instalado:
- Entra el flujo de agua sucia.
- Sale limpia automáticamente sin que interactúes cada vez.
::/interioriza

**Lo que harás.**
- Convierte tu notebook a módulo `data_pipeline.py` (funciones puras).
- Documenta con docstrings estilo NumPy.
- Añade tests con `assert` (casos: normal, basura, duplicados).
- Crea `main.py` para procesar el CSV y pruébalo.

::pausa{}
1. ¿Por qué es vital incluir un test de un dataset que sea "pura basura"?
2. ¿Qué beneficio técnico logras al separar `data_pipeline.py` de `main.py`?
::/pausa

**Estructura sugerida y Entregable.**

```
proyecto/
├── data_pipeline.py  # Funciones puras de ETL
├── main.py           # Script orquestador
└── test_pipeline.py  # Archivo de pruebas
```

- **Entregables:** Repositorio Git con módulo, script principal, tests y un README.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Modularidad | todo en main | algunas funciones | módulo importable |
| Docstrings | sin | una línea | NumPy style en todas |
| Tests | sin | uno | 3 casos cubiertos |
| Reusabilidad | hardcoded | parámetros básicos | totalmente parametrizable |
::/albatros
