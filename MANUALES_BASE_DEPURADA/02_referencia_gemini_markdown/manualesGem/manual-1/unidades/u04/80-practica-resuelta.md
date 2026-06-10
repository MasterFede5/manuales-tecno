---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Análisis nutricional del lonche escolar

::practica{titulo="¿Cumple el lonche escolar las recomendaciones de macronutrientes para un adolescente?"}
**Problema.** El comedor sirvió hoy un lonche con: 100 g de pollo asado, 80 g de arroz cocido, 1 tortilla (30 g), 50 g de ensalada (jitomate, lechuga), 1 manzana (180 g) y 250 mL de agua. Calcula su aporte calórico, distribución de macronutrientes y compara con las recomendaciones para un adolescente activo de 15 años (necesidad: 2,400 kcal/día con 50-60 % carbohidratos, 25-30 % grasas, 15-20 % proteínas).

Datos nutricionales aproximados:

| Alimento | Porción | kcal | CHO (g) | Lípidos (g) | Proteína (g) |
|---|---:|---:|---:|---:|---:|
| Pollo asado | 100 g | 165 | 0 | 3.6 | 31 |
| Arroz cocido | 80 g | 104 | 23 | 0.2 | 2.2 |
| Tortilla maíz | 30 g | 64 | 13 | 0.7 | 1.6 |
| Jitomate + lechuga | 50 g | 9 | 1.8 | 0.1 | 0.5 |
| Manzana | 180 g | 94 | 25 | 0.3 | 0.5 |

---

**Paso 1 — Suma de calorías.**
$$165 + 104 + 64 + 9 + 94 = 436\,\text{kcal}$$

**Paso 2 — Suma de macronutrientes.**

| Macro | Total (g) |
|---|---:|
| Carbohidratos | 0 + 23 + 13 + 1.8 + 25 = **62.8** |
| Lípidos | 3.6 + 0.2 + 0.7 + 0.1 + 0.3 = **4.9** |
| Proteínas | 31 + 2.2 + 1.6 + 0.5 + 0.5 = **35.8** |

**Paso 3 — Calorías por macronutriente.**

Recordatorio: 1 g de CHO = 4 kcal · 1 g de proteína = 4 kcal · 1 g de lípido = 9 kcal.

| Macro | Gramos | kcal |
|---|---:|---:|
| CHO | 62.8 | 251 |
| Proteína | 35.8 | 143 |
| Lípido | 4.9 | 44 |
| **Suma** | — | **438** |

(La pequeña discrepancia con el paso 1 viene de redondeos en las tablas.)

**Paso 4 — Distribución porcentual.**

$$\%\,CHO = \frac{251}{438} \times 100 = 57\%$$
$$\%\,Proteína = \frac{143}{438} \times 100 = 33\%$$
$$\%\,Lípidos = \frac{44}{438} \times 100 = 10\%$$

**Paso 5 — Comparar contra recomendaciones.**

| Macro | Recomendación | Lonche actual | Veredicto |
|---|---|---:|:---:|
| CHO | 50-60 % | 57 % | ✓ |
| Proteínas | 15-20 % | 33 % | ⚠ alto |
| Lípidos | 25-30 % | 10 % | ⚠ bajo |

**Paso 6 — Aporte energético total.**
El lonche aporta 438 kcal de las 2,400 kcal diarias necesarias = **18 % del requerimiento**.

Para un alumno con 3 comidas al día más colaciones, el lonche debería aportar 25-30 % (~600-720 kcal). Este lonche es **insuficiente energéticamente** para un adolescente activo.

**Paso 7 — Conclusión y recomendación.**

> El lonche cumple en distribución de carbohidratos pero está **desbalanceado**: tiene exceso de proteína (33 % vs 15-20 %) y déficit de lípidos saludables (10 % vs 25-30 %). Además, es bajo en kcal totales para un adolescente activo.
>
> **Recomendaciones operativas:**
> - Agregar 1 cucharada de aceite de oliva al arroz (+120 kcal, 14 g lípidos saludables).
> - Cambiar a una porción de pollo de 70 g (reduce proteína a ~25 %, más balanceado).
> - Incluir 30 g de aguacate o 15 g de almendras (+50 kcal de grasa saludable).
> - Aumentar el arroz a 120 g o agregar 1 tortilla más (+100 kcal de CHO complejos).
::/practica

---

::practica{titulo="Conservación por refrigeración — cuántas horas dura el pollo a distintas temperaturas"}
**Problema.** El comedor recibe 30 kg de pollo crudo a las 7 a.m. La cocinera quiere saber cuánto tiempo puede tener el pollo en cada refrigerador antes de cocinarlo, sin riesgo microbiológico. Datos:
- Refri A: 4 °C (correctamente operado).
- Refri B: 12 °C (semi-frío, con falla).
- Mesón: 22 °C (cocina ambiental).

Se sabe (regla empírica) que la velocidad de descomposición microbiana **aproximadamente se duplica** por cada **10 °C** de aumento (regla Q₁₀ ≈ 2). El pollo "dura" 24 h a 4 °C.

**Paso 1 — Aplica la regla Q₁₀.**
$$t = t_0 \cdot 2^{-(T-T_0)/10}$$
con $t_0$ = 24 h, $T_0$ = 4 °C.

**Paso 2 — Calcula tiempos seguros.**
- A 4 °C: $t = 24 \cdot 2^{0} = $ **24 h**.
- A 12 °C: $t = 24 \cdot 2^{-(12-4)/10} = 24 \cdot 2^{-0.8} \approx 24 \cdot 0.574 \approx$ **13.8 h**.
- A 22 °C: $t = 24 \cdot 2^{-(22-4)/10} = 24 \cdot 2^{-1.8} \approx 24 \cdot 0.287 \approx$ **6.9 h**.

**Paso 3 — Convierte a horario operativo.**
- Refri A (entró 7 a.m.): cocinar antes de las **7 a.m. del día siguiente**.
- Refri B (entró 7 a.m.): cocinar antes de las **9 p.m. del mismo día**.
- Mesón (entró 7 a.m.): cocinar antes de la **2 p.m. del mismo día**.

**Paso 4 — Estimación de carga microbiana relativa.**
Si a 4 °C la carga inicial $N_0$ se duplica en 24 h (cinética típica), a 22 °C habrá **3.5 duplicaciones** en el mismo periodo: $N/N_0 \approx 2^{3.5} \approx 11$ veces más bacterias para el mismo tiempo.

**Paso 5 — Consideración de zona de peligro.**
La FDA define la "zona de peligro" entre **4 y 60 °C**. El refri B y el mesón están dentro. Cualquier pollo en esos rangos debe consumirse pronto.

**Paso 6 — Conclusión y plan operativo.**
> El pollo debe cocinarse **el mismo día** si toca el mesón antes de las 2 p.m. y en menos de 14 h si está en el refri averiado. La cocinera del comedor recibe la regla simple: "si lo dejas en mesón, máximo 6 horas; si refri funciona bien, hasta 24 h; si refri tibio, antes del cierre del día". Para una decisión profesional, agregar termómetro permanente al refri B y verificar funcionamiento.
::/practica

---

::practica{titulo="Equilibrio energético — diseña el desayuno de un alumno deportista"}
**Problema.** Un alumno de 16 años, 65 kg, entrena fútbol 5 veces por semana. Su requerimiento energético es 2,800 kcal/día. El desayuno debe aportar **30 %** del total con la siguiente distribución de macronutrientes: 55 % CHO, 25 % lípidos, 20 % proteína. Diseña el desayuno con alimentos disponibles en el comedor.

**Paso 1 — Calcula kcal totales del desayuno.**
$$E_{des} = 0.30 \times 2800 = 840\,\text{kcal}$$

**Paso 2 — Calcula gramos de cada macronutriente.**
- CHO: $0.55 \times 840 / 4 = 462/4 = 115.5$ g.
- Lípidos: $0.25 \times 840 / 9 = 210/9 = 23.3$ g.
- Proteína: $0.20 \times 840 / 4 = 168/4 = 42.0$ g.

**Paso 3 — Construye el desayuno con la base de datos del comedor.**

| Alimento | Porción | kcal | CHO | Lípidos | Proteína |
|---|---:|---:|---:|---:|---:|
| Avena cocida | 80 g secos | 305 | 54 | 5 | 11 |
| Plátano | 120 g | 107 | 27 | 0.4 | 1.3 |
| Huevo entero | 2 unidades (100 g) | 155 | 1.1 | 11 | 13 |
| Queso panela | 60 g | 132 | 1 | 9 | 12 |
| Almendras | 20 g | 116 | 4 | 10 | 4 |
| Agua del bebedero | 250 mL | 0 | 0 | 0 | 0 |
| **Suma** | | **815** | **87.1** | **35.4** | **41.3** |

**Paso 4 — Verifica los porcentajes.**
- kcal verificadas: 87.1×4 + 35.4×9 + 41.3×4 = 348.4 + 318.6 + 165.2 = 832 kcal (consistente con tabla).
- % CHO = 348/832 = **42 %** (objetivo 55 %).
- % lípidos = 319/832 = **38 %** (objetivo 25 %).
- % proteína = 165/832 = **20 %** (objetivo 20 %, ✓).

**Paso 5 — Ajusta la receta.**
El desayuno está alto en lípidos (almendras y huevo) y bajo en CHO. Para acercarlo al objetivo, ajusta:
- Reduce a **1** huevo (no 2): elimina 78 kcal y 5.5 g de lípidos.
- Agrega **1 tortilla de maíz** (30 g, 64 kcal, 13 g CHO).
- Resultado nuevo: ~801 kcal, CHO 100 g (50 %), lípidos 30 g (33 %), proteína 35 g (17 %). Más cerca, ajustar siguiendo la misma lógica si quieres exactitud.

**Paso 6 — Conclusión.**
> El desayuno deportivo del alumno alcanza ~840 kcal con 1 huevo, avena, plátano, queso panela, almendras, una tortilla y agua del bebedero. La distribución 50/33/17 se aproxima al objetivo 55/25/20 sin perjuicio nutricional. Iterar dos veces más permitiría afinar al 1 % de cada porcentaje. Esta lógica alimenta la **Implementación Albatros** del menú escolar con IA.
::/practica
