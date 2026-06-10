---
unidad: 3
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 03

::interioriza
Diseñar gráficos es como emplatar en alta cocina:
- Menos es más: no uses demasiados colores.
- La presentación guía la mirada.
- Si debes explicarlo mucho, el diseño falló.
::/interioriza

::pausa{}
**Reflexión rápida:**
- ¿Por qué evitar un pie chart con 8 secciones?
- ¿Qué pasa si truncas el eje Y de un gráfico de barras?
::/pausa{}

::act-mcq{titulo="Repaso conceptual"}
1. Para mostrar la distribución de una variable continua, el gráfico ideal es:
   - [ ] Bar chart
   - [x] Histograma
   - [ ] Pie chart
   - [ ] Línea

2. Para comparar 3 grupos en distribución de calificaciones, lo mejor es:
   - [ ] 3 histogramas separados
   - [x] Boxplot por grupo
   - [ ] Scatter
   - [ ] Heatmap

3. Para ver correlaciones entre 5 variables numéricas, el más eficiente es:
   - [ ] 10 scatter plots
   - [x] Heatmap de correlación
   - [ ] Boxplot
   - [ ] Pie chart

4. Una regla básica de storytelling con datos:
   - [ ] Más gráficos = mejor
   - [x] Una historia por gráfico, destaca lo importante
   - [ ] Usar tantos colores como puedas
   - [ ] 3D siempre se ve más profesional

5. ¿Cuándo seaborn es preferible a matplotlib puro?
   - [ ] Nunca
   - [ ] Para subplots complejos
   - [x] Para gráficos estadísticos rápidos con pandas DataFrames
   - [ ] Solo en Colab
::/act-mcq

::act-table{titulo="Completa la tabla — qué gráfico para qué pregunta"}
| Pregunta | Gráfico recomendado | Justificación |
|---|---|---|
| ¿Cómo se distribuyen las calificaciones? |  |  |
| ¿Hay diferencia de promedios entre materias? |  |  |
| ¿Más horas correlaciona con mejor cal? |  |  |
| ¿Qué variables predicen calificación? |  |  |
| ¿Cómo cambia el promedio mes a mes? |  |  |
| ¿Cuál materia tiene más outliers? |  |  |
::/act-table

::act-match{titulo="Relaciona seaborn con uso"}
| Función | Uso |
|---|---|
| 1. sns.histplot | a) Comparar distribución entre grupos |
| 2. sns.scatterplot | b) Distribución de variable continua |
| 3. sns.boxplot | c) Relación entre 2 variables numéricas |
| 4. sns.heatmap | d) Matriz de correlaciones |
| 5. sns.pairplot | e) Todas las combinaciones de variables |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Eje y siempre debe empezar en 0 en gráfico de barras. ( ) ____________________________________________

2. Pie chart con 8 secciones es buena práctica. ( ) ____________________________________________

3. seaborn ya incluye paletas accesibles para daltónicos. ( ) ____________________________________________

4. Una buena visualización requiere mínimo 5 colores. ( ) ____________________________________________

5. Storytelling con datos es solo para presentaciones, no para reportes. ( ) ____________________________________________
::/act-tf

::albatros{titulo="Dashboard del dataset escolar para presentación al consejo" tipo="taller" tiempo="3 h"}
**Pregunta detonadora.** Si tuvieras 10 minutos para presentar el diagnóstico inicial del rendimiento escolar al consejo, ¿qué 5 gráficos elegirías y por qué?

**Lo que harás.**
1. Carga el dataset escolar de U2.
2. Produce 5 gráficos siguiendo la estructura de la práctica resuelta.
3. Personaliza cada uno con paleta institucional, títulos descriptivos, anotaciones.
4. Ensambla en una presentación de 7 slides.
5. Practica presentar a un compañero en 10 min.
6. Recolecta feedback y refina.

**Entregable.**
- 5 gráficos guardados como PNG (200 dpi).
- Presentación PDF/PPT con storytelling.
- Reporte de retroalimentación de tu test piloto.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Calidad técnica | gráfico básico | con personalización | publicable |
| Storytelling | sin orden | secuencia lógica | 3 actos claros |
| Personalización | default | paleta consistente | institucional + anotaciones |
| Comunicación | "vean los datos" | mensaje por gráfico | mensaje único final |
| Test con persona real | no probado | un compañero | con feedback documentado |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="Personaliza un scatter publicable"}
```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="horas_estudio",
    y="cal_final",
    hue="___________",                    # colorear por materia
    alpha=0.6,
    ax=ax
)
ax.set_title("Horas vs calificación por materia", fontsize=14, fontweight="bold")
ax.set_xlabel("Horas/sem")
ax.set_ylabel("Calificación final")
plt.savefig("scatter.png", dpi=___________, bbox_inches="___________")
```
::/act-fill

::act-order{titulo="Pasos para una visualización publicable"}
[ ] Guardar con `dpi=200, bbox_inches="tight"`
[ ] Cargar datos con pandas
[ ] Llamar `plt.show()` o cerrar la figura
[ ] Crear figura con `plt.subplots(figsize=...)`
[ ] Configurar tema (`sns.set_theme`)
[ ] Plotear los datos (sns.X o ax.X)
[ ] Etiquetar título, ejes y leyenda
::/act-order

::act-case{titulo="Caso — el gráfico engaña" lineas=10}
Tu colega presenta este boxplot al consejo:
- Eje Y empieza en 5 (no en 0).
- Sin título.
- Tres colores random.
- Outliers no marcados.

El consejo aprueba "porque la mediana se ve aceptable". Tú detectas el problema.

**Pregunta.** 
- Lista los 4 errores específicos.
- Describe cómo cada error **engaña al lector** (1 línea c/u). 
- Bonus: ¿qué ley o principio ético invocarías?
::/act-case

::act-mindmap{titulo="Mapa mental abierto" centro="VISUALIZAR DATOS" nodos_primarios=5 nodos_secundarios=10}
5 nodos sugeridos: tipos de gráfico, librerías, personalización, storytelling, ética. Por cada uno, 2 ejemplos.
::/act-mindmap

::act-tf{titulo="Ética visual"}
1. Truncar el eje Y para "magnificar" diferencias es legítimo si lo declaras. ( ) ____________________
2. Usar 3D en pie charts mejora la percepción del lector. ( ) ____________________
3. Una paleta accesible para daltónicos es opcional. ( ) ____________________
4. Cualquier gráfico debe poder leerse en blanco y negro (impresión). ( ) ____________________
::/act-tf

::albatros{titulo="Reto Albatros — refactoriza un gráfico defectuoso" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Si te pasaran un gráfico hecho rápido por un colega, ¿podrías mejorarlo en 30 minutos para que sea publicable?

**Lo que harás.** Recibes este código:

```python
import matplotlib.pyplot as plt

x = ["Mate", "Fis", "Qui"]
y = [60, 78, 82]

plt.bar(x, y, color=["red", "blue", "green"])
plt.show()
```

**Tu tarea.**
1. Identifica los 6 problemas:
   - Figura sin tamaño y sin título.
   - Sin ejes etiquetados ni valores anotados.
   - Paleta no institucional y sin meta.
2. Refactoriza con patrón profesional:
   - Configura `figsize`, `ax`, `title`, `xlabel`, `ylabel`.
   - Añade anotaciones y colores condicionales (<80).
3. Antes/después con screenshots.
4. Documenta cada cambio y por qué.

**Entregable.** Notebook con código original, refactorizado, antes/después y comentarios.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Problemas identificados | <2 | 3-4 | 6 con explicación |
| Refactor | parcial | publicable | + colores condicionales + anotaciones |
| Documentación | sin | comentarios | antes/después con justificación |
::/albatros
