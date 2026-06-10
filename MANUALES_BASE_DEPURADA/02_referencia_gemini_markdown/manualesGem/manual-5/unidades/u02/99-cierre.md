---
unidad: 2
seccion: cierre
paginas_objetivo: 1
---

## Cierre y autoevaluación — Unidad 02

Cerraste la unidad de NumPy y Pandas. Ahora puedes:

1. **Operar arrays NumPy** vectorizadamente (10-100× más rápido que listas Python).
2. **Manejar Series y DataFrames** como tablas inteligentes.
3. **Cargar** CSV, Excel, JSON con una línea.
4. **Limpiar** datos: nulos, duplicados, tipos, outliers.
5. **Filtrar y seleccionar** con boolean indexing, .loc, .query, .isin.
6. **Agrupar** con groupby y producir estadísticas multi-categoría.

> **Frase puente.** Tienes datos limpios y agregados. Para entender lo que dicen, **necesitas verlos**. La Unidad 3 te lleva a Matplotlib y Seaborn: histogramas, dispersión, boxplots — los gráficos que convierten tablas en insights.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **NumPy** | desconozco | arrays básicos | vectorización | con axis y reshape | dominio de funciones np |
| **Pandas DF** | sin entender | crear y leer | head/info/describe | .loc/.iloc | encadenamiento idiomático |
| **Lectura archivos** | falla | CSV simple | + parámetros | + Excel + JSON | + URLs |
| **Limpieza** | sin tratar | dropna | + drop_duplicates + astype | + clip + replace | pipeline reusable |
| **Filtrado** | uno solo | boolean | + .loc + .query | + .isin + multi | encadenado |
| **Groupby** | desconozco | uno simple | + agg múltiple | + multi-col + transform | pivot_table profesional |

### Pregunta de cierre

> Tu pipeline trabaja con 480 estudiantes. Coordinación entrega ahora **48 millones** de registros (todo el sistema escolar nacional). pandas tarda 5 minutos. ¿Migras o no? Argumenta a favor o en contra usando los hallazgos del subtema de investigación.

### Conexión con la siguiente unidad

En **U3 — Visualización de Datos**, vas a tomar tu pipeline y **agregarle gráficas**: histogramas de calificaciones, dispersión horas-vs-cal, boxplots por materia. Una imagen comunica lo que 10 estadísticas no logran.
