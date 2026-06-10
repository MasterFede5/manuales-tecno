---
unidad: 0
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Caracteriza la muestra del bebedero

::practica{titulo="¿El pH del bebedero está dentro de norma?"}
**Problema.** Tu equipo midió el pH de la muestra del bebedero **5 veces seguidas** con un potenciómetro digital de resolución 0.01 unidades. La NOM-127-SSA1 (calidad del agua para consumo humano) exige pH entre **6.5 y 8.5**. Las lecturas obtenidas fueron:

| Medición | pH |
|---|---|
| 1 | 7.06 |
| 2 | 7.04 |
| 3 | 7.10 |
| 4 | 7.03 |
| 5 | 7.07 |

Reporta el resultado correctamente y concluye si la muestra cumple la norma.

---

**Paso 1 — Aplica el método.** La pregunta es verificable contra un valor de referencia (NOM-127). Tienes datos experimentales repetidos. Toca analizar.

**Paso 2 — Calcula la media aritmética.**
$$\bar{x} = \frac{7.06 + 7.04 + 7.10 + 7.03 + 7.07}{5} = \frac{35.30}{5} = 7.060$$

**Paso 3 — Calcula la desviación estándar.**
Diferencias respecto a la media: $0.000, -0.020, +0.040, -0.030, +0.010$.
Cuadrados: $0, 0.0004, 0.0016, 0.0009, 0.0001$. Suma: $0.0030$.

$$s = \sqrt{\frac{0.0030}{n-1}} = \sqrt{\frac{0.0030}{4}} = \sqrt{0.00075} \approx 0.027$$

**Paso 4 — Incertidumbres tipo A y B.**
- $u_A = \dfrac{s}{\sqrt{n}} = \dfrac{0.027}{\sqrt{5}} = 0.012$
- $u_B = \dfrac{\text{resolución}}{2} = \dfrac{0.01}{2} = 0.005$

**Paso 5 — Incertidumbre combinada.**
$$u_c = \sqrt{u_A^2 + u_B^2} = \sqrt{0.012^2 + 0.005^2} = \sqrt{0.000169} \approx 0.013$$

**Paso 6 — Reporte con cifras significativas correctas.**
La incertidumbre tiene 1–2 cs; el valor se redondea al mismo decimal:

$$\boxed{\text{pH} = 7.06 \pm 0.01}$$

**Paso 7 — Conversión a [H⁺] en mol/L (notación científica).**
Por definición, $[H^+] = 10^{-pH} = 10^{-7.06} = 8.7 \times 10^{-8}$ mol/L.

**Paso 8 — Compara contra la norma.**
Norma NOM-127: $6.5 \le \text{pH} \le 8.5$. Tu intervalo de confianza:
$$7.06 - 0.01 = 7.05 \quad \text{a} \quad 7.06 + 0.01 = 7.07$$
**Está completamente dentro de norma.**

**Paso 9 — Conclusión profesional.**
> El pH de la muestra del bebedero del patio es **7.06 ± 0.01**, equivalente a una concentración de protones de **8.7 × 10⁻⁸ mol/L**. El intervalo está contenido en el rango permitido por la NOM-127-SSA1 (6.5–8.5), por lo que **el agua cumple el parámetro de pH**.

> *Nota:* este reporte solo cubre pH. Antes de declarar el agua segura para consumo, deben analizarse otros parámetros: dureza, cloro residual, coliformes totales y fecales (siguientes unidades).
::/practica

---

::practica{titulo="Conversión SI con cifras significativas — masa del salinómetro escolar"}
**Problema.** El laboratorio recibió un salinómetro portátil con un certificado que dice: *"masa neta del kit: 1 lb 4 oz, longitud de la sonda: 12 pulgadas, autonomía: 6 horas con pilas AA"*. Tu profesora pide que cargues el dato al inventario en **unidades del SI con cifras significativas adecuadas**.

**Paso 1 — Identifica los factores de conversión exactos.**
- 1 lb = 0.45359237 kg (factor exacto, sin incertidumbre)
- 1 oz = 28.349523 g (factor exacto)
- 1 in = 2.54 cm (factor exacto)

**Paso 2 — Suma masa.** 1 lb + 4 oz = 1 × 0.45359237 kg + 4 × 0.028349523 kg = 0.45359237 + 0.11339809 = 0.56699046 kg.

**Paso 3 — Determina cs del dato original.** "1 lb 4 oz" aporta **1 cs en la libra y 1 cs en las onzas** (números reportados sin decimales). Por la regla de la suma, el resultado se redondea al decimal menos preciso: a 0.1 kg.

**Paso 4 — Reporta masa.** $m = 0.6$ kg, equivalente a $6 \times 10^{-1}$ kg en notación científica.

**Paso 5 — Convierte la longitud.** 12 in × 2.54 cm/in = 30.48 cm = 0.3048 m. Como "12" tiene **2 cs**, redondeas a $0.30$ m = $3.0 \times 10^{-1}$ m.

**Paso 6 — Convierte la autonomía.** 6 h × 3600 s/h = 21 600 s. Con 1 cs en el dato original ⇒ $2 \times 10^4$ s.

**Paso 7 — Cuadro final para el inventario.**

| Parámetro | Valor original | Valor SI |
|---|---|---|
| Masa | 1 lb 4 oz | $0.6$ kg |
| Longitud sonda | 12 in | $0.30$ m |
| Autonomía | 6 h | $2 \times 10^4$ s |

**Paso 8 — Conclusión profesional.**
> El kit pesa aproximadamente **0.6 kg**, su sonda mide **0.30 m** y su autonomía nominal es de **$2 \times 10^4$ s** (~6 h). Las cifras significativas reflejan la precisión del certificado de fábrica, no la del cálculo: agregar más decimales daría una falsa sensación de exactitud que no respalda la fuente original.
::/practica

---

::practica{titulo="Decidir con datos — ¿el bebedero está más caliente que el del laboratorio?"}
**Problema.** Mediste la temperatura de **dos bebederos distintos** (patio y laboratorio) con el mismo termómetro digital de resolución 0.1 °C. Los datos:

| n | Patio (°C) | Laboratorio (°C) |
|---|---|---|
| 1 | 22.4 | 21.7 |
| 2 | 22.6 | 21.8 |
| 3 | 22.5 | 21.9 |
| 4 | 22.7 | 21.6 |
| 5 | 22.3 | 21.8 |

¿Está el del patio significativamente más caliente o la diferencia es solo ruido de medición?

**Paso 1 — Calcula media y dispersión por bebedero.**
- Patio: $\bar{x}_P = 22.50$ °C · diferencias: $-0.10, +0.10, 0.00, +0.20, -0.20$ · cuadrados: $0.01, 0.01, 0, 0.04, 0.04 = 0.10$ · $s_P = \sqrt{0.10/4} = 0.158$ ≈ 0.16 °C.
- Laboratorio: $\bar{x}_L = 21.76$ °C · diferencias: $-0.06, +0.04, +0.14, -0.16, +0.04$ · cuadrados: $0.0036, 0.0016, 0.0196, 0.0256, 0.0016 = 0.052$ · $s_L = \sqrt{0.052/4} \approx 0.114$.

**Paso 2 — Incertidumbre combinada por bebedero.**
- $u_{A,P} = 0.16/\sqrt{5} = 0.072$ · $u_B = 0.05$ · $u_{c,P} = \sqrt{0.072^2 + 0.05^2} \approx 0.088$.
- $u_{A,L} = 0.114/\sqrt{5} = 0.051$ · $u_{c,L} = \sqrt{0.051^2 + 0.05^2} \approx 0.071$.

**Paso 3 — Reportes individuales.**
- Patio: $T_P = 22.5 \pm 0.1$ °C
- Laboratorio: $T_L = 21.8 \pm 0.1$ °C

**Paso 4 — Diferencia y su incertidumbre.**
$$\Delta T = T_P - T_L = 22.50 - 21.76 = 0.74 \text{ °C}$$
$$u_{\Delta} = \sqrt{u_{c,P}^2 + u_{c,L}^2} = \sqrt{0.088^2 + 0.071^2} \approx 0.11 \text{ °C}$$

**Paso 5 — Criterio de significancia.** Una diferencia es **significativa** si $|\Delta T| > 2 \cdot u_{\Delta}$. Aquí $2 \cdot u_{\Delta} = 0.22$ °C y $|\Delta T| = 0.74$ °C. Como $0.74 > 0.22$, la diferencia es real, no atribuible a ruido.

**Paso 6 — Conclusión profesional.**
> El bebedero del patio está, en promedio, **0.7 ± 0.1 °C** más caliente que el del laboratorio. La diferencia supera tres veces la incertidumbre, por lo que el efecto **es estadísticamente significativo**. Posibles explicaciones a investigar: exposición solar de la tubería del patio o la sombra del laboratorio. Próximo paso: medir a distintas horas para descartar el efecto solar.
::/practica
