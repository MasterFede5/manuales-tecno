---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Análisis nutricional del lonche escolar

::practica{titulo="¿Cumple el lonche escolar las recomendaciones de macronutrientes para un adolescente?"}
**Problema:**
- El comedor sirvió un lonche: 100 g pollo asado, 80 g arroz, 1 tortilla (30 g), 50 g ensalada, 1 manzana (180 g) y 250 mL agua.
- **Objetivo:** Calcular aporte calórico y distribución de macronutrientes.
- **Comparación:** Adolescente activo de 15 años (2,400 kcal/día, 50-60 % CHO, 25-30 % grasas, 15-20 % proteínas).

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
- 1 g de CHO = 4 kcal
- 1 g de proteína = 4 kcal
- 1 g de lípido = 9 kcal

| Macro | Gramos | kcal |
|---|---:|---:|
| CHO | 62.8 | 251 |
| Proteína | 35.8 | 143 |
| Lípido | 4.9 | 44 |
| **Suma** | — | **438** |

(La pequeña discrepancia con el paso 1 viene de redondeos en las tablas.)

**Paso 4 — Distribución porcentual.**
- $\%\,CHO = \frac{251}{438} \times 100 = 57\%$
- $\%\,Proteína = \frac{143}{438} \times 100 = 33\%$
- $\%\,Lípidos = \frac{44}{438} \times 100 = 10\%$

**Paso 5 — Comparar contra recomendaciones.**

| Macro | Recomendación | Lonche actual | Veredicto |
|---|---|---:|:---:|
| CHO | 50-60 % | 57 % | ✓ |
| Proteínas | 15-20 % | 33 % | ⚠ alto |
| Lípidos | 25-30 % | 10 % | ⚠ bajo |

**Paso 6 — Aporte energético total.**
- El lonche aporta 438 kcal de las 2,400 kcal diarias necesarias.
- Esto equivale a un **18 % del requerimiento**.
- Debería aportar 25-30 % (~600-720 kcal). Es **insuficiente energéticamente**.

::interioriza
**Analogía:** Imagina que el metabolismo del alumno es como el presupuesto del comedor:
- Los **carbohidratos** son el dinero para gastos diarios.
- Los **lípidos** son la cuenta de ahorros para imprevistos.
- La **proteína** es el fondo de mantenimiento de las instalaciones.
Este menú gasta mucho en mantenimiento, pero ahorra muy poco.
::/interioriza

**Paso 7 — Conclusión y recomendación.**
- El lonche cumple en carbohidratos pero está **desbalanceado**.
- Tiene exceso de proteína y déficit de lípidos saludables.
- Es bajo en kcal totales para un adolescente activo.

**Recomendaciones operativas:**
- **Aceite:** Agregar 1 cucharada de aceite de oliva al arroz (+120 kcal).
- **Pollo:** Bajar a 70 g (reduce proteína a ~25 %, más balanceado).
- **Extras:** Incluir 30 g de aguacate o 15 g de almendras (+50 kcal).
- **Cereales:** Aumentar arroz a 120 g o sumar 1 tortilla más.
::/practica

---

::practica{titulo="Conservación por refrigeración — cuántas horas dura el pollo a distintas temperaturas"}
**Problema:** 
- Reciben 30 kg de pollo crudo a las 7 a.m. 
- **Objetivo:** Saber cuánto tiempo dura en cada ambiente antes de cocinarlo.
- **Opciones:** Refri A (4 °C), Refri B (12 °C averiado), Mesón (22 °C).
- **Dato clave:** La velocidad de descomposición se duplica cada 10 °C (Q₁₀ ≈ 2). A 4 °C dura 24 h.

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
- A 4 °C la carga se duplica en 24 h.
- A 22 °C habrá **3.5 duplicaciones** en el mismo periodo.
- ¡Habrá 11 veces más bacterias para el mismo tiempo!

**Paso 5 — Consideración de zona de peligro.**
- La FDA define la "zona de peligro" entre **4 y 60 °C**. 
- El refri B y el mesón están dentro de esta zona crítica.

::interioriza
**Analogía:** Las bacterias son como estudiantes al escuchar el timbre del recreo.
- A 4°C, están dormidos en clase (multiplicación lenta).
- A 22°C (mesón), acaban de salir al patio corriendo (se multiplican exponencialmente).
¡No los dejes demasiado tiempo en el patio sin supervisión!
::/interioriza

**Paso 6 — Conclusión y plan operativo.**
- El pollo debe cocinarse **el mismo día** si toca el mesón antes de las 2 p.m.
- La regla para la cocinera: "Mesón = 6 horas máximo; Refri tibio = cerrar el día cocinando".
- **Acción:** Reparar Refri B urgentemente y poner termómetro.
::/practica

---

::practica{titulo="Equilibrio energético — diseña el desayuno de un alumno deportista"}
**Problema:**
- Alumno: 16 años, 65 kg, entrena fútbol. Necesita 2,800 kcal/día. 
- **Meta del desayuno:** 30 % del total.
- **Distribución:** 55 % CHO, 25 % lípidos, 20 % proteína.

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
- **kcal reales:** 87.1×4 + 35.4×9 + 41.3×4 = 832 kcal.
- **% CHO:** 348/832 = **42 %** (objetivo 55 %).
- **% lípidos:** 319/832 = **38 %** (objetivo 25 %).
- **% proteína:** 165/832 = **20 %** (objetivo 20 %, ✓).

**Paso 5 — Ajusta la receta.**
- El desayuno actual está muy alto en lípidos (almendras/huevo).
- **Ajuste 1:** Reduce a 1 huevo (elimina 78 kcal y 5.5 g lípidos).
- **Ajuste 2:** Agrega 1 tortilla de maíz (suma 64 kcal y 13 g CHO).
- **Nuevo perfil:** ~801 kcal, CHO 50 %, lípidos 33 %, proteína 17 %.

**Paso 6 — Conclusión.**
- La distribución de 50/33/17 se acerca al objetivo 55/25/20.
- Es excelente para el alumno deportista, y lograble en el comedor.
- Iterar más afinaría los números (**Implementación Albatros**).
::/practica

::pausa
**Active Recall:**
1. ¿Qué macronutriente aporta más calorías por gramo y cuánto?
2. Según la regla Q₁₀, si la temperatura baja de 24°C a 14°C, ¿qué le ocurre al tiempo de conservación seguro del alimento?
3. ¿Por qué el lonche de la práctica 1 no es suficiente a pesar de tener mucha proteína?
::/pausa
