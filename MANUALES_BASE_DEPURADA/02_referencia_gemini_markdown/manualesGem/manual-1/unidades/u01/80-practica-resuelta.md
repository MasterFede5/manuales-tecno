---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Inventario iónico de un sorbo del bebedero

::practica{titulo="Cuántos iones de cada tipo trae un sorbo del bebedero"}
**Problema.** El reporte del laboratorio del agua del bebedero indica:

| Especie | Concentración (mg/L) |
|---|---:|
| Sodio (Na⁺) | 35 |
| Calcio (Ca²⁺) | 80 |
| Magnesio (Mg²⁺) | 24 |
| Cloruro (Cl⁻) | 50 |

Calcula cuántos iones de cada tipo bebe tu hermana en un sorbo de **50 mL** y verifica que la suma de cargas se conserve electricamente.

---

**Paso 1 — Identifica las masas molares.**

Datos de la tabla:
- M(Na) = 22.99 g/mol
- M(Ca) = 40.08 g/mol
- M(Mg) = 24.31 g/mol
- M(Cl) = 35.45 g/mol

**Paso 2 — Calcula la masa de cada ion en 50 mL.**

$$m = \text{conc} \times V$$

- Na⁺: 35 mg/L × 0.050 L = **1.75 mg**
- Ca²⁺: 80 mg/L × 0.050 L = **4.00 mg**
- Mg²⁺: 24 mg/L × 0.050 L = **1.20 mg**
- Cl⁻: 50 mg/L × 0.050 L = **2.50 mg**

**Paso 3 — Convierte a moles.**

$$n = \frac{m}{M} \times \frac{1\,\text{g}}{1000\,\text{mg}}$$

- $n(\text{Na}^+) = \dfrac{1.75 \times 10^{-3}}{22.99} = 7.6 \times 10^{-5}$ mol
- $n(\text{Ca}^{2+}) = \dfrac{4.00 \times 10^{-3}}{40.08} = 1.0 \times 10^{-4}$ mol
- $n(\text{Mg}^{2+}) = \dfrac{1.20 \times 10^{-3}}{24.31} = 4.9 \times 10^{-5}$ mol
- $n(\text{Cl}^-) = \dfrac{2.50 \times 10^{-3}}{35.45} = 7.1 \times 10^{-5}$ mol

**Paso 4 — Convierte a número de iones (multiplica por Nₐ).**

- N(Na⁺) = 7.6 × 10⁻⁵ × 6.022 × 10²³ = **4.6 × 10¹⁹ iones**
- N(Ca²⁺) = 1.0 × 10⁻⁴ × 6.022 × 10²³ = **6.0 × 10¹⁹ iones**
- N(Mg²⁺) = 4.9 × 10⁻⁵ × 6.022 × 10²³ = **3.0 × 10¹⁹ iones**
- N(Cl⁻) = 7.1 × 10⁻⁵ × 6.022 × 10²³ = **4.3 × 10¹⁹ iones**

**Paso 5 — Verifica conservación de carga.**

Carga positiva total en moles equivalentes:
$$\sum n_+ \cdot z_+ = (7.6 \times 10^{-5})(1) + (1.0 \times 10^{-4})(2) + (4.9 \times 10^{-5})(2) = 3.7 \times 10^{-4} \text{ mol-eq}$$

Carga negativa total:
$$\sum n_- \cdot z_- = (7.1 \times 10^{-5})(1) = 7.1 \times 10^{-5} \text{ mol-eq}$$

**No cuadran.** ¿Está mal el reporte?

**Paso 6 — Diagnóstico.**

No: el reporte solo enumera cuatro especies. La diferencia (3.0 × 10⁻⁴ mol-eq de carga negativa faltante) corresponde a otros aniones presentes que el laboratorio no listó pero que existen en aguas duras: principalmente **bicarbonato (HCO₃⁻)** y **sulfato (SO₄²⁻)**. Estos aparecerían en un análisis más completo y son responsables de la "dureza temporal" del agua.

**Paso 7 — Conclusión.**

> En un sorbo de 50 mL del agua del bebedero, tu hermana ingiere aproximadamente:
> - 4.6 × 10¹⁹ iones Na⁺
> - 6.0 × 10¹⁹ iones Ca²⁺
> - 3.0 × 10¹⁹ iones Mg²⁺
> - 4.3 × 10¹⁹ iones Cl⁻
>
> El balance de cargas confirma la presencia de aniones adicionales no reportados (probablemente HCO₃⁻ y SO₄²⁻) por unas 3 × 10⁻⁴ mol-eq. Para un análisis completo se solicitaría medir alcalinidad y sulfatos.
::/practica

---

::practica{titulo="ΔEN — predice el tipo de enlace para tres especies del bebedero"}
**Problema.** Las tres especies más abundantes del bebedero involucran enlaces O–H (en el agua), Na–Cl (en la sal disuelta) y Ca–O (en el carbonato de calcio que produce dureza). Predice **sin medir** qué tipo de enlace tiene cada una y verifica si esos enlaces explican por qué el agua los acoge o los rechaza.

**Paso 1 — Consigue los valores de electronegatividad (Pauling).**
- H = 2.20 · O = 3.44 · Na = 0.93 · Cl = 3.16 · Ca = 1.00.

**Paso 2 — Calcula ΔEN.**
- O–H: |3.44 − 2.20| = **1.24**
- Na–Cl: |3.16 − 0.93| = **2.23**
- Ca–O: |3.44 − 1.00| = **2.44**

**Paso 3 — Aplica el criterio.**

| ΔEN | Tipo de enlace |
|---|---|
| < 0.4 | covalente no polar |
| 0.4 – 1.7 | covalente polar |
| > 1.7 | iónico |

- O–H: covalente **polar**. Explica el dipolo del H₂O.
- Na–Cl: **iónico**. Por eso al disolverse en agua se separa en Na⁺ y Cl⁻.
- Ca–O: **iónico**. CaCO₃ se comporta como red iónica.

**Paso 4 — Conecta con el comportamiento observable.**
- El agua, por ser polar, atrae iones (interacción ion–dipolo) y los hidrata: por eso disuelve NaCl con facilidad.
- El CaCO₃ tiene enlaces iónicos pero **muy fuertes** y red cristalina compacta; el agua pura no lo disuelve bien y por eso forma sarro al evaporarse en el bebedero.

**Paso 5 — Conclusión.**
> El agua disuelve la sal (Na–Cl iónico) pero no al carbonato de calcio (Ca–O iónico) en igual medida porque la entalpía reticular del CaCO₃ supera lo que la hidratación puede liberar. Esto es lo que explica el sarro blanco que ves en el cristal del bebedero después de unos meses.
::/practica

---

::practica{titulo="Estructura de Lewis y geometría — del agua a la sal en disolución"}
**Problema.** Dibuja la estructura de Lewis del H₂O y del CO₃²⁻ (el ion carbonato responsable de la dureza temporal del bebedero). Indica geometría, ángulos aproximados y polaridad de cada uno.

**Paso 1 — Cuenta electrones de valencia.**
- H₂O: 2 × H (1) + O (6) = **8 e⁻**.
- CO₃²⁻: C (4) + 3 × O (6) + 2 (carga) = **24 e⁻**.

**Paso 2 — Esqueleto y enlaces.**
- H₂O: O en el centro, dos H en los extremos.
- CO₃²⁻: C en el centro, tres O alrededor; uno con doble enlace (resonante).

**Paso 3 — Distribuye octetos.**
- H₂O: cada H comparte 2 e⁻ con O; el O queda con 2 pares libres. Octeto del O completo, dueto del H completo.
- CO₃²⁻: el C comparte un par doble con un O y pares simples con los otros dos O (que llevan carga negativa). Estructura resonante de tres formas equivalentes.

**Paso 4 — Aplica VSEPR para predecir geometría.**
- H₂O: 2 pares enlazantes + 2 pares libres ⇒ geometría **angular**, ángulo H–O–H ≈ **104.5°**.
- CO₃²⁻: 3 zonas de densidad electrónica ⇒ geometría **trigonal plana**, ángulos O–C–O = **120°**.

**Paso 5 — Determina polaridad de cada estructura.**
- H₂O: angular + enlaces O–H polares ⇒ molécula **polar**, dipolo neto.
- CO₃²⁻: trigonal plana, simétrica ⇒ los tres dipolos C–O se cancelan ⇒ **no polar** como ion (la carga se reparte simétricamente).

**Paso 6 — Conexión con el bebedero.**
> El agua, polar, **rodea** al CO₃²⁻ orientando sus átomos H (δ⁺) hacia los oxígenos del carbonato (δ⁻ por la carga total). Esa hidratación es lo que mantiene a 60 mg/L de carbonato disueltos en lugar de precipitados. Cuando el agua se evapora en la malla del bebedero, los iones pierden su "abrigo de agua" y forman sarro: la geometría del Lewis explica el residuo blanquecino que limpias cada mes.
::/practica
