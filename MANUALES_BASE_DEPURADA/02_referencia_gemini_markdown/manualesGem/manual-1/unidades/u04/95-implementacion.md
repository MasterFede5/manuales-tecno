---
unidad: 4
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — Análisis nutricional con IA + plantilla de menú escolar"}
**Objetivo.** Construir una plantilla en Google Sheets que reciba ingredientes y porciones, calcule automáticamente kcal, macronutrientes y micronutrientes, y use una IA generativa (Claude o ChatGPT) para sugerir mejoras al menú. El producto final será una herramienta operativa para que el comedor escolar diseñe menús balanceados.

**¿Por qué hacerla?** El comedor escolar no tiene presupuesto para nutricionista, pero sí necesita servir comida balanceada. Una plantilla automatizada con apoyo de IA democratiza el conocimiento nutricional y reduce la dependencia de criterio individual.

---

### Materiales

- Cuenta de Google (Sheets) o Excel.
- Cuenta de Claude (claude.ai) o ChatGPT (chat.openai.com), versión gratuita basta.
- Tabla de composición de alimentos (INSP México, USDA FoodData Central, o etiquetas de productos).
- Recetario de la cocina escolar (al menos 5 platillos).

### Pasos

**1. Crea la base de datos de ingredientes.** En la pestaña "Ingredientes":
```
| Alimento | Porción ref. (g) | kcal | CHO (g) | Lípidos (g) | Proteína (g) | Vit C (mg) | Hierro (mg) |
```
Captura al menos 30 ingredientes comunes del comedor.

**2. Hoja de "Receta".** Permite seleccionar ingredientes y porciones; calcula totales automáticamente:
```
=BUSCARV(A2, Ingredientes!A:H, 3, 0) * B2 / 100
```
para escalar al gramaje real.

**3. Hoja de "Análisis del menú".** Suma todas las recetas del día y compara contra recomendaciones diarias por edad/sexo.

**4. Integración con IA.** Crea un prompt template:
```
Estás analizando el menú diario de un comedor escolar.
Aquí los datos: [pegar tabla]
Recomendaciones para 15 años activo: 2,400 kcal, 50-60% CHO, 25-30% grasas, 15-20% proteínas.
Detecta desbalances. Sugiere 3 cambios concretos con presupuesto bajo.
Justifica cada cambio en términos químico-nutricionales.
```

Pega la tabla del menú y deja que la IA sugiera mejoras. Edita y aplica.

**5. Validación con un caso real.** Toma el menú de un día completo del comedor (desayuno + lonche + comida) y procésalo. Verifica si aporta 100 % del requerimiento diario.

**6. Documentación.** Crea una pestaña "Manual" con instrucciones de uso para el personal del comedor (sin necesidad de saber química).
::/implementacion

::visual{tipo="interfaz" descripcion="Captura del dashboard final en Google Sheets: lado izquierdo con formulario de selección de ingredientes y porciones, centro con cálculos automáticos de kcal y macronutrientes, derecha con gráfica de pastel de distribución, abajo recomendaciones de IA en formato de chat con mejoras concretas. Color Albatros." paginas="0.5" src="../manualesGem/assets/visuales/manual-1/u04/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

URL pública de la plantilla con:
1. Base de datos con ≥ 30 ingredientes.
2. Análisis de un menú real de la cocina escolar.
3. Captura de la conversación con IA mostrando análisis y recomendaciones.
4. Documento de 1-2 páginas con conclusión y plan de implementación.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Base de datos** | <15 ingredientes | 30 ingredientes | 50+ con micronutrientes |
| **Fórmulas** | manuales | escalado por gramaje | escalado + suma + verificación cruzada |
| **Integración IA** | no usa IA | usa IA con prompt simple | prompt template con instrucciones clínicas precisas |
| **Validación** | sin probar | un menú probado | comparación con recomendación oficial INSP |
| **Documentación** | sin manual | manual básico | manual + tutorial en video |

### Reto bonus (+1 punto)

Agrega una sección que **calcule el costo monetario del menú** además del nutricional, para optimizar simultáneamente nutrición y presupuesto. Ideal para escuelas con presupuesto limitado.

---

### Hitos intermedios

| Sprint | Entregable | Día |
|---|---|---|
| 1 | Pestaña "Ingredientes" con 20 alimentos cargados desde tabla del INSP | 3 |
| 2 | Hoja "Receta" con BUSCARV escalando por gramaje y dos recetas verificadas | 6 |
| 3 | Hoja "Análisis del menú" con totales y comparativa contra recomendaciones | 10 |
| 4 | Integración con IA (Claude/ChatGPT) y reporte de mejoras aplicadas | 15 |

### Reto bonus extendido (+2 puntos cada uno)

1. **Reto A:** programa una alerta automática que pinte rojo cualquier menú cuyo % de azúcares añadidos exceda el 10 % del total energético (criterio OMS) y proponga la sustitución más cercana.
2. **Reto B:** integra el costo por ingrediente para que el dashboard ofrezca dos optimizaciones: la **más nutritiva al mismo precio** y la **más barata sin sacrificar el balance** ±5 % sobre cada macronutriente.
3. **Reto C:** agrega una capa estacional que considere ingredientes de temporada local (mercado del barrio) y ajuste recomendaciones por mes con menores costos y huella ambiental.
::/implementacion
---

::albatros{titulo="Sprint corto — el desayuno deportivo del lunes" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Puedes diseñar en 30 minutos un desayuno deportivo para los lunes que cumpla con la práctica resuelta y sirva a 50 alumnos del comedor con presupuesto de \$30 por persona?

**Lo que harás.**
1. Recupera la práctica resuelta del desayuno (840 kcal, 55/25/20 distribución).
2. Diseña un menú con 5 alimentos cuyo costo total ≤ \$30 por porción y cuyo aporte cumpla la distribución.
3. Multiplica las cantidades por 50 alumnos. Calcula la lista de compra final.
4. Calcula el costo total del menú escalado.
5. Verifica: ¿alcanza con \$1500 (50 × 30)?
6. Documenta en una hoja A4 con: receta por porción, lista escalada, costo y distribución macro.

**Materiales.** Plantilla del Implementación · lista de precios local · calculadora.

**Entregable.** Hoja A4 con receta, lista de compra y verificación de presupuesto.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Distribución macro | desbalanceada | dentro de ±10 % del objetivo | dentro de ±5 % del objetivo |
| Costo | excede presupuesto | dentro del presupuesto | dentro del presupuesto con margen |
| Escalado | hecho a ojo | escalado correcto | escalado + buffer del 10 % por mermas |
::/albatros
