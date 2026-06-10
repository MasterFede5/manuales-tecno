---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Veredicto físico-químico del bebedero

::practica{titulo="¿El agua del bebedero cumple los 5 parámetros físico-químicos básicos?"}
**Problema.** 
- Tu equipo midió 5 parámetros del bebedero escolar.
- ¿Cumple con la norma NOM-127-SSA1?
- De no cumplir, propón un tratamiento adecuado.

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

- A pH 7.06, el cloro libre es ~75% HOCl (activo) y ~25% OCl⁻ (menos activo).
- Está en rango óptimo (6.5-7.5), **conservando poder desinfectante**.
- A pH ≥ 8.5, predomina el OCl⁻ y la desinfección falla.

::interioriza
Imagina que el HOCl es un delantero estrella y el OCl⁻ el portero suplente. Con pH neutro, el equipo ataca bien; con pH alto, todos se vuelven porteros y el cloro no desinfecta.
::/interioriza

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

> **Veredicto:** El agua **cumple los 5 parámetros básicos** (NOM-127-SSA1).
> **ICA:** **89/100** ("Excelente").
>
> **Advertencias:** 
> - Falta análisis microbiológico (coliformes).
> - Faltan metales pesados (Pb, As).
> 
> **Recomendación:**
> - Hacer prueba microbiológica (≈ $300 MXN).
> - Medir metales básicos (≈ $800 MXN) para asegurar potabilidad.

::pausa{}
**Reflexiona:** Si el bebedero tuviera un pH de 9.0 pero el cloro residual marcara 1.0 mg/L, ¿el agua sería segura para beber? ¿Por qué?
::/pausa
::/practica

---

::practica{titulo="Titulación ácido-base — calcula la concentración de ácido cítrico en un jugo escolar"}
**Problema.** 
- La cooperativa vende jugo de limón natural.
- Quieres evaluar si daña el esmalte dental.
- Titulas **25.0 mL** de jugo con NaOH 0.10 M (indicador: fenolftaleína).
- Gastas **22.5 mL** hasta el vire rosa pálido.

Calcula la concentración de ácido cítrico ($C_6H_8O_7$, M = 192.12 g/mol) y discute su riesgo dental.

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
> **Resultados:** 
> - **Concentración:** 0.030 M (≈ 5.8 g/L).
> - **pH estimado:** ≈ 2.3.
> 
> **Riesgo dental:** 
> - El pH < 5.5 desmineraliza el esmalte.
> - **Acción:** Enjuagar con agua del bebedero (pH 7.06) para neutralizar.
> - **Ojo:** ¡No cepillar de inmediato! Frotar con ácido erosiona el esmalte.

::interioriza
El ácido ablanda el esmalte como mantequilla tibia. Si te cepillas, te lo llevas. Mejor enjuaga con agua neutra (el bebedero) para volver a "enfriar" el esmalte antes de limpiar.
::/interioriza

::pausa{}
**Reflexiona:** ¿Qué sucedería si intentamos titular este jugo con una base débil en lugar de NaOH fuerte?
::/pausa
::/practica

---

::practica{titulo="Dilución serial — preparar estándares para la curva de calibración del nitrato"}
**Problema.** 
- Debes preparar **5 estándares** de NaNO₃ (50, 25, 10, 5 y 1 mg/L de NO₃⁻).
- Propósito: Calibrar un fotómetro de nitrato.
- Material: Solución madre (1000 mg/L) y matraces aforados de 100 mL.
- Tarea: Diseñar dilución serial y verificar cifras significativas.

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
- Pipetar 0.1 mL de la madre (1000 mg/L) es muy impreciso.
- Solución: **Dilución intermedia** (desde E3).
- **Regla de oro:** Ningún paso de dilución debe exceder el factor 1:100.

**Paso 5 — Conclusión.**
> - **Precisión:** Incertidumbre < 2 % (usando matraces clase A).
> - **Método:** Las diluciones intermedias evitan medir volúmenes diminutos.
> - **Próximo paso:** Usar la curva del fotómetro para medir nitratos del bebedero.

::interioriza
Pagar una cuenta de $1 con un billete de $1000 da un cambio difícil de contar. Igual pasa al pipetar 0.1 mL de 1000 mg/L; mejor cambia billetes de $1000 por $10 primero.
::/interioriza

::pausa{}
**Reflexiona:** Si el matraz aforado tuviera gotas de agua destilada antes de añadir tu estándar, ¿afectaría la concentración final al aforar?
::/pausa
::/practica
