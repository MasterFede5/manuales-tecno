---
unidad: 2
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Pipeline pandas del dataset escolar"}
**Objetivo.** Construir pipeline reutilizable de **carga + limpieza + análisis** del dataset escolar usando pandas exclusivamente. Resultado: módulo Python `data_pipeline.py` con funciones que cualquier compañero pueda usar.

**Materiales.** Colab/Anaconda, pandas, repo Git, 6-8 horas.

**Pasos.**

1. **Estructura del módulo** (1 h):
   ```
   data_pipeline.py
     ├── cargar(path)
     ├── limpiar(df)
     ├── analizar_global(df)
     ├── analizar_por_materia(df)
     ├── detectar_outliers(df)
     └── exportar(df, stats, dest)
   ```
2. **Implementación** (3 h): cada función con docstring y ejemplo.
3. **Tests manuales** (1 h): verificar con datasets de 50, 480 y 4800 filas.
4. **Reporte ejemplo** (1 h): genera 5 reportes diferentes con el mismo módulo.
5. **Documentación** (1 h): README con cómo usar.
6. **Compartir** (30 min): GitHub público + ejemplo de notebook.

**Entregable.**
- Módulo `data_pipeline.py` con 6 funciones documentadas.
- Notebook ejemplo `analisis_escolar.ipynb`.
- README con instalación y uso.
- 3 reportes generados (CSV + JSON + tabla bonita en notebook).

**Rúbrica.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Funciones modulares | todo en main | algunas | 6+ con docstrings |
| Limpieza | dropna sin pensar | con criterio | pipeline reusable + edge cases |
| Análisis | uno básico | 3 análisis | 5+ análisis con groupby |
| Documentación | mínima | docstrings | README + notebook ejemplo |
| Reusabilidad | hardcoded | config básica | parametrizable |

**Próximo paso.** En **U3** vas a usar `matplotlib` y `seaborn` para **visualizar** los resultados que tu pipeline produce. Una imagen vale más que una tabla en juntas con dirección.

### Hitos intermedios

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u2-h1-numpy` | Operaciones vectorizadas funcionando sobre 1 array |
| H2 | `u2-h2-pandas-load` | `pd.read_csv` carga el dataset y muestra `df.head()` |
| H3 | `u2-h3-clean` | Pipeline de limpieza con method chaining ejecutándose |
| H4 | `u2-h4-groupby` | Reporte por materia con `.agg(...)` correcto |
| H5 | `u2-h5-modulo` | `data_pipeline.py` importable desde notebook externo |
| H6 | `u2-h6-tests` | 3 tests con `assert` pasando |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — Schema strict con pandera.** Instala `pandera` y define un schema que valide tipos, rangos y unicidad. Si el CSV viola el schema, lanza error claro. Esfuerzo: 60 min.

```python
import pandera as pa
from pandera import Column, DataFrameSchema, Check

schema = DataFrameSchema({
    "id": Column(int, Check.gt(0), unique=True),
    "asistencia": Column(float, Check.in_range(0, 1)),
    "cal_final": Column(float, Check.in_range(0, 10)),
})
schema.validate(df)
```

**Reto bonus 2 — Procesamiento por chunks (datasets grandes).** Si el CSV tuviera 10M filas y no cabe en RAM, usa `pd.read_csv(path, chunksize=10000)` para procesar bloque por bloque y agregar resultados. Esfuerzo: 60 min.

**Reto bonus 3 — Comparar 2 versiones del dataset.** Crea función `diff(df_v1, df_v2)` que reporta filas nuevas, filas eliminadas y filas modificadas (mismo id, columnas distintas). Útil para auditar cambios entre bimestres. Esfuerzo: 90 min.
::/implementacion

---

::albatros{titulo="Caso bonus — pipeline operativo mensual" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Tu pipeline aguanta correr **automáticamente cada mes** sin que tú estés presente?

**Contexto.** Coordinación quiere que el día 5 de cada mes se procese automáticamente el `dataset_escolar_AAAA-MM.csv` y se publique un reporte. Un cron job correrá tu script. Tú no vas a estar para arreglar nada cuando falle.

**Lo que harás.**
1. Diseña en una página **qué pasa cuando**:
   - El archivo de entrada **no existe** ese mes.
   - El esquema cambió (alguien renombró una columna).
   - El dataset está vacío (0 filas).
   - El reporte ya existe (ejecución duplicada).
   - Hay un error inesperado a mitad de proceso.
2. Para cada caso, define: detección, log, fallback, notificación.
3. Diseña la estructura de `logs/AAAA-MM.log` que tu script generaría.
4. Identifica las 3 alertas que deberían despertarte a las 3 AM (vs las que pueden esperar al lunes).

**Entregable.** Documento de 1 página: matriz casos × respuestas + estructura de log + lista de alertas críticas.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Casos cubiertos | <3 | 4-5 | los 5 con detección y fallback |
| Logging diseñado | sin formato | timestamp + msg | + nivel + contexto |
| Priorización alertas | sin distinguir | una lista | crítico/no-crítico justificado |
::/albatros
