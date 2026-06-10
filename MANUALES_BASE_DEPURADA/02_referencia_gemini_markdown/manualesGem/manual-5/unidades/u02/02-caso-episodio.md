---
unidad: 2
seccion: caso-episodio
paginas_objetivo: 1
---

::caso{episodio=2}
**Caso Albatros — Episodio 2: Limpiar el dataset escolar (nulos, duplicados, tipos).**

En el Episodio 1 cargaste el CSV con código manual y reportaste 5 errores. La coordinación responde: *"Cool, pero el dataset real tiene 12 problemas: 47 calificaciones nulas, 8 estudiantes duplicados, columnas con tipos mezclados, fechas en formato inconsistente."*. Resolverlo en código manual sería 200 líneas. Con NumPy y Pandas, son 15.

El Episodio 2 te lleva del Python "puro" a las **dos librerías que dominan datos en Python**: NumPy (arrays vectorizados, base de todo) y Pandas (Series y DataFrames, la herramienta principal de cualquier data scientist). Cubrirás concepto de array, DataFrame, lectura desde 3 formatos, limpieza (nulos, duplicados, tipos), filtrado y selección, y agrupación con groupby. Al final, dataset escolar limpio listo para visualizar y modelar.

> *La pregunta gancho:* tu loop manual recorre 480 filas en 30 segundos. NumPy lo hace en 0.001 segundos. ¿Cómo? Porque opera en C bajo la capa de Python. Esa es la diferencia que cambia tu carrera técnica.
::/caso

