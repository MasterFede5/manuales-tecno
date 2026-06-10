---
unidad: 4
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 04

::act-mcq{titulo="Repaso conceptual"}
1. Para datos asimétricos con outliers, lo más representativo es:
   - [ ] Media
   - [x] Mediana
   - [ ] Moda
   - [ ] Suma

2. Una correlación r = 0.42 indica:
   - [ ] No hay relación
   - [x] Relación moderada lineal positiva
   - [ ] Causalidad fuerte
   - [ ] Outliers presentes

3. La regla 68-95-99.7 aplica a:
   - [ ] Cualquier distribución
   - [x] Distribución normal solamente
   - [ ] Solo grandes muestras
   - [ ] Solo datos enteros

4. Para detectar outliers en datos no normales, lo recomendable es:
   - [ ] Z-score con umbral 3
   - [x] IQR con factor 1.5
   - [ ] Visualizar y eliminar a ojo
   - [ ] Eliminar el 5% superior siempre

5. Encontrar correlación 0.7 entre A y B significa:
   - [ ] A causa B con 70% de certeza
   - [x] A y B varían juntos linealmente; la causalidad requiere más evidencia
   - [ ] A predice B perfectamente
   - [ ] Hay relación cuadrática
::/act-mcq

::act-table{titulo="Completa la tabla — interpretar correlaciones del case escolar"}
| Pareja | Correlación r | Fortaleza | Posible causalidad / confounder |
|---|---|---|---|
| horas_estudio – cal_final | 0.42 |  |  |
| asistencia – cal_final | 0.55 |  |  |
| cal_anterior – cal_final | 0.72 |  |  |
| horas_estudio – asistencia | 0.20 |  |  |
::/act-table

::act-match{titulo="Relaciona estadístico con uso"}
| Estadístico | Uso |
|---|---|
| 1. Mediana | a) Posición individual en grupo |
| 2. Desviación estándar | b) Centro robusto a outliers |
| 3. Percentil | c) Dispersión absoluta en mismas unidades |
| 4. Pearson r | d) Fuerza de relación lineal |
| 5. IQR | e) Detección de outliers |
::/act-match

::act-tf{titulo="Verdadero o falso"}
1. Pearson r=0.95 confirma causalidad fuerte. ( ) ____________________________________________

2. La media puede estar lejos de la mediana en datos asimétricos. ( ) ____________________________________________

3. Z-score > 3 implica outlier en cualquier distribución. ( ) ____________________________________________

4. R² es interpretado como porcentaje de varianza explicada. ( ) ____________________________________________

5. Outliers siempre deben eliminarse antes de modelar. ( ) ____________________________________________
::/act-tf

::interioriza
**Correlación vs. Causalidad**
- Imagina que el canto del gallo correlaciona con el amanecer.
- ¿Obligar al gallo a cantar hará que salga el sol? No.
- Igual pasa en los datos: dos variables juntas no implican causalidad.
::/interioriza

::pausa{}
¿Qué variables ocultas (confounders) podrían afectar tus análisis escolares?
::/pausa

::albatros{titulo="Análisis estadístico defendible del dataset escolar" tipo="reto" tiempo="3 h"}
**Pregunta detonadora.**
- Imagina que debes defender "qué predice el rendimiento" ante un consejo.
- ¿Qué métricas mostrarías con total seguridad?
- ¿Cuáles **no afirmarías** aunque haya alta correlación?

**Lo que harás.**
1. Carga dataset escolar limpio.
2. Aplica los 6 análisis: descriptivos, distribución normal (verificar), percentiles, correlaciones, outliers.
3. Construye reporte de 1 página con números defendibles + sus advertencias éticas (causalidad).
4. Identifica 3 confounders posibles para cada correlación principal.
5. Diseña 1 experimento controlado (al menos hipotético) para una de las correlaciones.
6. Comparte con un compañero. Pídele que rete tus afirmaciones.

**Entregable.**
- Reporte 1 página.
- Lista de confounders.
- Diseño experimental hipotético.
- Bitácora de retos recibidos y respuestas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Análisis estadístico | uno solo | 3-4 | 6 técnicas integradas |
| Distinción correlación-causa | confunde | menciona | profundo con confounders |
| Outliers | sin tratar | detecta | maneja con justificación |
| Comunicación | "datos crudos" | resumen | reporte ejecutivo defendible |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="Test de simetría con skew/kurtosis"}
```python
from scipy import stats

cal = df["cal_final"]
s = stats.___________(cal)
k = stats.kurtosis(cal)

print(f"Skew (asimetría): {s:.3f}")
print(f"Kurtosis (apuntamiento): {k:.3f}")

if abs(s) < 0.5:
    forma = "aproximadamente simétrica"
elif s < 0:
    forma = "sesgada a la ___________"     # cola larga a la izquierda
else:
    forma = "sesgada a la derecha"

print(f"Forma: {forma}")
```
::/act-fill

::act-order{titulo="Pasos para análisis estadístico defendible"}
[ ] Detectar outliers con IQR
[ ] Calcular percentiles clave (P10, P25, P50, P75, P90)
[ ] Reporte ejecutivo con advertencias éticas (causalidad)
[ ] Cargar dataset limpio
[ ] Tendencia central + dispersión
[ ] Matriz de correlaciones
[ ] Verificar supuestos (normalidad, simetría)
::/act-order

::act-case{titulo="Caso — el director quiere causalidad" lineas=10}
El director ve `r(asistencia, cal_final) = 0.55` y propone:
- "Hacer **obligatorio** llegar al 95% de asistencia".
- "Esto **causará** que el promedio suba 0.5 puntos".

**Pregunta.** Tu rol es asesor estadístico. Redacta una respuesta (5–8 líneas) que:
1. Reconozca la correlación (es un dato real).
2. Explique por qué la afirmación causal **NO se sigue** directamente.
3. Proponga 1 confounder plausible.
4. Sugiera **qué evidencia** convertiría la propuesta en defendible (ej. experimento).
::/act-case

::act-mindmap{titulo="Mapa mental abierto" centro="ESTADÍSTICA APLICADA" nodos_primarios=5 nodos_secundarios=10}
5 nodos sugeridos: tendencia central, dispersión, correlación, distribución, outliers. 2 ejemplos por cada uno.
::/act-mindmap

::act-mcq{titulo="Estadístico apropiado"}
1. Comparar el "centro típico" entre dos materias con outliers:
   - [ ] Media
   - [x] Mediana
   - [ ] Suma
   - [ ] Desviación estándar

2. ¿Qué test usarías para comparar promedios entre 3 grupos?
   - [ ] t de Student
   - [x] ANOVA o equivalente no paramétrico
   - [ ] Correlación
   - [ ] Chi-cuadrado
::/act-mcq

::albatros{titulo="Reto Albatros — auditor estadístico de afirmaciones" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.**
- Recibes 5 afirmaciones de un consultor sobre el rendimiento escolar.
- ¿Puedes auditar cuáles son defendibles?
- ¿Cuáles van más allá de la evidencia mostrada?

**Lo que harás.** Recibes este reporte (cópialo a tu cuaderno):

> 1. "Los alumnos de Mate tienen mediana 1.5 puntos por debajo del resto."
> 2. "Asistir más causa mejores notas."
> 3. "La correlación entre horas y nota es perfectamente lineal."
> 4. "Los 12 alumnos con cal_final < 4 son seguramente casos de bajo nivel intelectual."
> 5. "Si todos estudiaran 8 h/sem, todos aprobarían."

**Tu tarea.**
1. Para cada afirmación, decide si es **defendible**, **espuria/sin evidencia** o **falsa**.
2. Para las problemáticas, propón cómo formular la afirmación correctamente.
3. Identifica al menos 2 confounders en el dataset escolar.
4. Diseña 1 experimento controlado **factible** para validar la afirmación 2.

**Entregable.** Reporte de 1-2 páginas con tabla auditoría + propuesta experimental + bitácora de razonamiento.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Auditoría | <3 afirmaciones | 4 | 5 con justificación |
| Reformulación | sin | algunas | todas las problemáticas |
| Confounders | sin | uno | 2+ con explicación |
| Experimento | inviable | borrador | factible y ético |
::/albatros
