---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Veredicto físico-químico del bebedero

::practica{titulo="¿El agua del bebedero cumple los 5 parámetros físico-químicos básicos?"}
**Problema.** Tu equipo midió los siguientes parámetros sobre la muestra del bebedero. Determina si cumple la NOM-127-SSA1 y, si no cumple alguno, propón el tratamiento adecuado.

| Parámetro | Valor medido | Norma NOM-127 |
|---|---|---|
| pH | 7.06 ± 0.01 | 6.5 – 8.5 |
| Cloro residual | 0.40 mg/L | 0.2 – 1.5 mg/L |
| Dureza total (como CaCO₃) | 340 mg/L | ≤ 500 mg/L |
| Sólidos disueltos totales (SDT) | 720 mg/L | ≤ 1000 mg/L |
| Turbidez | 1.2 NTU | ≤ 5 NTU |

---

**Paso 1 — Comparar parámetro por parámetro contra norma.**

| Parámetro | Valor | Norma | ¿Cumple? |
|---|---:|---|:---:|
| pH | 7.06 | 6.5 – 8.5 | ✓ |
| Cloro residual | 0.40 mg/L | 0.2 – 1.5 | ✓ |
| Dureza | 340 mg/L | ≤ 500 | ✓ |
| SDT | 720 mg/L | ≤ 1000 | ✓ |
| Turbidez | 1.2 NTU | ≤ 5 | ✓ |

**Paso 2 — Calcular la concentración molar de calcio + magnesio (dureza en M).**

Si toda la dureza fuera CaCO₃:
$$[\text{CaCO}_3] = \frac{340 \text{ mg/L}}{100 \text{ g/mol} \times 1000} = 3.4 \times 10^{-3}\,\text{M} = 3.4\,\text{mM}$$

**Paso 3 — Convertir cloro residual a M.**

Asumiendo que está como HOCl (M = 52.46 g/mol):
$$[\text{HOCl}] = \frac{0.40 \text{ mg/L}}{52.46 \times 1000} = 7.6 \times 10^{-6}\,\text{M}$$

**Paso 4 — Verificar la efectividad del cloro al pH medido.**

A pH 7.06, el cloro libre se distribuye entre HOCl (forma activa, ~75%) y OCl⁻ (forma menos activa, ~25%). Como el pH está en el rango óptimo (6.5-7.5), el cloro **conserva su poder desinfectante**. Si el pH fuera ≥ 8.5, casi todo el cloro estaría como OCl⁻ y la desinfección sería ineficiente.

**Paso 5 — Calcular el Índice de Calidad del Agua (ICA) simplificado.**

Usando un esquema simple donde cada parámetro se puntúa de 0-100 según margen al límite:

| Parámetro | Margen al límite | Puntaje (0-100) |
|---|---:|---:|
| pH (rango) | bien centrado | 95 |
| Cloro | dentro de rango | 90 |
| Dureza | 32 % por debajo del límite | 85 |
| SDT | 28 % por debajo del límite | 80 |
| Turbidez | 76 % por debajo del límite | 95 |

**ICA = promedio = 89**

**Paso 6 — Veredicto y recomendación.**

> El agua del bebedero **cumple los 5 parámetros físico-químicos básicos** de la NOM-127-SSA1, con un Índice de Calidad del Agua de **89/100** (categoría: "Excelente"). Sin embargo, este análisis **no incluye los parámetros microbiológicos** (coliformes totales y fecales) ni metales pesados, que son obligatorios para una declaración formal de potabilidad.
>
> **Recomendación:** completar análisis microbiológico (≈ \$300 MXN) y metales pesados básicos (Pb, As; ≈ \$800 MXN) antes de emitir un veredicto definitivo. La calidad físico-química es excelente; el riesgo residual está en la microbiología y la presencia de contaminantes a nivel de trazas no analizados.
::/practica

---

::practica{titulo="Titulación ácido-base — calcula la concentración de ácido cítrico en un jugo escolar"}
**Problema.** En la cooperativa escolar venden jugo de limón natural. Para evaluar si el jugo agrede el esmalte dental de los alumnos, tomas una muestra de 25.0 mL y la titulas con NaOH 0.10 M usando fenolftaleína como indicador. Gastas **22.5 mL** hasta el vire rosa pálido.

Calcula la concentración de ácido cítrico ($C_6H_8O_7$, M = 192.12 g/mol) y discute el riesgo dental.

---

**Paso 1 — Reacción de titulación.**
$$C_6H_8O_7 + 3\,\text{NaOH} \rightarrow C_6H_5O_7Na_3 + 3\,H_2O$$
El ácido cítrico es **triprótico**: cada mol consume **3 moles** de NaOH.

**Paso 2 — Calcula moles de NaOH gastados.**
$$n(\text{NaOH}) = M \cdot V = 0.10 \text{ M} \times 0.0225 \text{ L} = 2.25 \times 10^{-3} \text{ mol}$$

**Paso 3 — Calcula moles de ácido cítrico.**
$$n(\text{ácido}) = \frac{n(\text{NaOH})}{3} = \frac{2.25 \times 10^{-3}}{3} = 7.50 \times 10^{-4} \text{ mol}$$

**Paso 4 — Concentración del ácido cítrico.**
$$[H_3Cit] = \frac{n}{V_{muestra}} = \frac{7.50 \times 10^{-4}}{0.0250} = 3.0 \times 10^{-2} \text{ M}$$

**Paso 5 — Convierte a g/L y a porcentaje (m/V).**
- $g/L = 0.030 \times 192.12 = 5.76 \text{ g/L}$
- $\% \text{ m/V} = 0.576 \%$

**Paso 6 — Estima el pH del jugo.**
Usando la primera disociación ($K_{a1} = 7.4 \times 10^{-4}$) como dominante:
$$[H^+] \approx \sqrt{K_{a1} \cdot C} = \sqrt{7.4 \times 10^{-4} \times 0.030} = 4.7 \times 10^{-3} \text{ M}$$
$$\text{pH} \approx -\log(4.7 \times 10^{-3}) = 2.33$$

**Paso 7 — Conclusión.**
> El jugo de la cooperativa contiene **0.030 M de ácido cítrico** (≈ 5.8 g/L) con un pH estimado de **2.3**. Este pH está **muy por debajo del umbral de desmineralización del esmalte (5.5)**, lo que justifica la recomendación de la odontóloga escolar: enjuagar con agua del bebedero después de tomarlo y no cepillarse de inmediato (el cepillado sobre esmalte ácido lo erosiona aún más). El bebedero, con pH 7.06, es **el aliado natural** para neutralizar el efecto del jugo.
::/practica

---

::practica{titulo="Dilución serial — preparar estándares para la curva de calibración del nitrato"}
**Problema.** Tu profesora te pide preparar **5 estándares** de NaNO₃ (M = 84.99 g/mol) para calibrar un fotómetro de nitrato. Las concentraciones objetivo son 50, 25, 10, 5 y 1 mg/L de NO₃⁻. Solo tienes una solución madre comercial de 1000 mg/L y matraces aforados de 100 mL. Diseña la dilución serial y verifica con cifras significativas.

---

**Paso 1 — Aplica $C_1V_1 = C_2V_2$ partiendo de la madre (1000 mg/L) a 100 mL finales.**

Para 50 mg/L: $V_1 = (50 \times 100)/1000 = 5.0$ mL → aforar a 100 mL.
Para 25 mg/L: $V_1 = 2.5$ mL → aforar a 100 mL.
Para 10 mg/L: $V_1 = 1.0$ mL → aforar a 100 mL.

Para 5 y 1 mg/L conviene **partir del estándar de 50 mg/L** ya preparado (mejor exactitud que medir 0.5 mL de la madre).

Para 5 mg/L (a partir de 50 mg/L): $V_1 = (5 \times 100)/50 = 10.0$ mL → aforar a 100 mL.
Para 1 mg/L (a partir de 10 mg/L): $V_1 = (1 \times 100)/10 = 10.0$ mL → aforar a 100 mL.

**Paso 2 — Tabla de preparación.**

| Estándar | Concentración | Origen | Vol. tomado | Aforar a |
|---|---:|---|---:|---:|
| E1 | 50 mg/L | Madre 1000 mg/L | 5.0 mL | 100 mL |
| E2 | 25 mg/L | Madre 1000 mg/L | 2.5 mL | 100 mL |
| E3 | 10 mg/L | Madre 1000 mg/L | 1.0 mL | 100 mL |
| E4 | 5 mg/L | E1 (50 mg/L) | 10.0 mL | 100 mL |
| E5 | 1 mg/L | E3 (10 mg/L) | 10.0 mL | 100 mL |

**Paso 3 — Verifica precisión instrumental.**
- Pipetar 1.0 mL con pipeta de émbolo de 1 mL: incertidumbre típica ≈ 0.01 mL (1 %).
- Aforo con matraz de 100 mL clase A: ± 0.10 mL (0.1 %).
- Incertidumbre relativa total por dilución ≈ 1 % → aceptable para una curva de calibración.

**Paso 4 — Detecta y evita el error común.**
Para 1 mg/L **no** se puede pipetar 0.1 mL de la madre con buena precisión. Por eso hicimos **dilución intermedia** desde E3. Es la regla de oro: cada paso de dilución no debe exceder un factor de 1:100 si quieres mantener la incertidumbre relativa baja.

**Paso 5 — Conclusión.**
> Los 5 estándares quedan listos con incertidumbre relativa < 2 % usando matraces aforados clase A. Las dos diluciones intermedias (50 → 5 y 10 → 1 mg/L) evitan medir volúmenes de 0.1 mL de la solución madre, que duplicarían el error. Esta serie alimentará la curva de calibración del fotómetro y permitirá medir nitratos del bebedero en la siguiente práctica.
::/practica
