---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — pH de la lluvia local con NOx atmosférico

::practica{titulo="¿Qué pH tendrá la lluvia si la zona tiene 150 µg/m³ de NO₂?"}
**Problema.** En una zona urbana cercana a la escuela, el monitor SIMAT reporta una concentración promedio de **NO₂ = 150 µg/m³** durante 24 horas. Asumiendo que **el 30 % del NO₂ se convierte en HNO₃** y se incorpora a la lluvia, calcula el pH de la lluvia local. ¿Cumple el rango de "lluvia natural" (pH 5.0-5.6) o es lluvia ácida?

Datos: 1 m³ de aire pesa ≈ 1.2 kg a CNTP; volumen de lluvia recolectada por cada m³ de aire procesado: 0.001 L (asume).

---

**Paso 1 — Convierte la concentración a moles de NO₂.**

En 1 m³ de aire hay 150 µg = 1.5 × 10⁻⁴ g de NO₂.
M(NO₂) = 14.01 + 2 × 16.00 = 46.01 g/mol.

$$n_{NO_2} = \frac{1.5 \times 10^{-4}}{46.01} = 3.26 \times 10^{-6}\,\text{mol}$$

**Paso 2 — Calcula el HNO₃ formado (30 %).**

$$n_{HNO_3} = 0.30 \times 3.26 \times 10^{-6} = 9.78 \times 10^{-7}\,\text{mol}$$

Reacción simplificada:
$$\ce{2 NO2 + H2O -> HNO3 + HNO2}$$

(Para fines de pH, asumimos que todo el NO₂ convertido se vuelve HNO₃ por simplicidad.)

**Paso 3 — Asume volumen de lluvia recolectada.**

Por cada m³ de aire procesado, asumimos 1 mL = 0.001 L de lluvia. Entonces:

$$[HNO_3] = \frac{9.78 \times 10^{-7}\,\text{mol}}{0.001\,\text{L}} = 9.78 \times 10^{-4}\,\text{M}$$

**Paso 4 — Como HNO₃ es ácido fuerte, [H⁺] = [HNO₃].**

$$[H^+] = 9.78 \times 10^{-4}\,\text{M}$$

**Paso 5 — Calcula el pH.**

$$pH = -\log(9.78 \times 10^{-4}) = 3.01$$

**Paso 6 — Compara contra referencias.**

| Tipo de lluvia | pH típico |
|---|---|
| Pura (agua destilada) | 7.0 |
| Natural (con CO₂) | 5.0 – 5.6 |
| Ácida moderada | 4.0 – 5.0 |
| Ácida severa | 3.0 – 4.0 |
| Calculada en este ejercicio | **3.01** |

**Paso 7 — Conclusión y recomendación.**

> Una lluvia local en estas condiciones tendría un pH de aproximadamente **3.0**, equivalente a vinagre diluido. Es **lluvia ácida severa**. Si esta lluvia escurriera por un techo de zinc o lámina galvanizada y entrara a la cisterna del bebedero, en poco tiempo se observaría:
> - Disolución del zinc (Zn + 2 HNO₃ → Zn(NO₃)₂ + H₂).
> - Liberación de iones Zn²⁺ al agua almacenada (riesgo a la salud).
> - Acidificación del agua almacenada.
>
> **Recomendación:** verificar pH del agua de la cisterna después de eventos lluviosos prolongados; aislar el sistema de captación de pluviales contaminados; considerar materiales de techo inertes (como lámina de PVC) en zonas con NOx alto.
::/practica

---

::practica{titulo="Balanceo redox por ion-electrón — KMnO₄ frente a Fe²⁺ en agua de la cisterna"}
**Problema.** El laboratorio detectó **hierro ferroso** (Fe²⁺) en el agua de la cisterna por corrosión del tinaco. Decides cuantificarlo titulando con permanganato (KMnO₄ 0.020 M) en medio ácido. Balancea la ecuación redox completa y calcula cuántos mg de Fe²⁺ había en 100 mL de muestra si gastaste **6.5 mL** de titulante.

**Paso 1 — Identifica las semirreacciones en medio ácido.**
- Oxidación: $Fe^{2+} \to Fe^{3+} + e^-$
- Reducción: $MnO_4^- + 8H^+ + 5e^- \to Mn^{2+} + 4H_2O$

**Paso 2 — Iguala electrones.** Multiplica la oxidación por 5:
$$5\,Fe^{2+} \to 5\,Fe^{3+} + 5e^-$$

**Paso 3 — Suma semirreacciones.**
$$5\,Fe^{2+} + MnO_4^- + 8H^+ \to 5\,Fe^{3+} + Mn^{2+} + 4H_2O$$

**Paso 4 — Verifica balance de masa y carga.**
- Masa: 5 Fe, 1 Mn, 4 O, 8 H ✓ ambos lados.
- Carga: izquierda = +10 + (−1) + (+8) = +17; derecha = +15 + (+2) + 0 = +17 ✓.

**Paso 5 — Calcula moles de KMnO₄ gastados.**
$$n(MnO_4^-) = 0.020 \times 0.0065 = 1.30 \times 10^{-4}\,\text{mol}$$

**Paso 6 — Aplica la estequiometría 5:1.**
$$n(Fe^{2+}) = 5 \times 1.30 \times 10^{-4} = 6.50 \times 10^{-4}\,\text{mol}$$

**Paso 7 — Convierte a masa y a concentración.**
- m = $6.50 \times 10^{-4} \times 55.85 = 3.63 \times 10^{-2}$ g = **36.3 mg** de Fe²⁺ en 100 mL.
- $[Fe^{2+}] = 36.3$ mg/100 mL = **363 mg/L**.

**Paso 8 — Compara con norma.**
NOM-127-SSA1: hierro total ≤ **0.30 mg/L**.

> El agua de la cisterna tiene **363 mg/L de Fe²⁺**, **mil veces el límite de la norma**. Recomendación inmediata: clausurar el bebedero y reemplazar el tinaco corroído. La técnica permanganométrica detectó el problema en menos de 10 mL de titulante.
::/practica

---

::practica{titulo="Estequiometría de combustión — emisiones de CO₂ del autobús escolar"}
**Problema.** El autobús escolar consume **30 L de diésel/día** (densidad ≈ 0.83 g/mL). Calcula los kg de CO₂ que emite al día y compáralos con la huella per cápita objetivo (2 t CO₂eq/persona/año, ONU 2050).

**Paso 1 — Reacción de combustión completa del diésel.**
Usa el cetano ($C_{16}H_{34}$, M = 226.45 g/mol) como representativo:
$$2\,C_{16}H_{34} + 49\,O_2 \to 32\,CO_2 + 34\,H_2O$$

**Paso 2 — Masa de combustible diaria.**
$$m_{diésel} = 30\,\text{L} \times 0.83\,\text{kg/L} = 24.9\,\text{kg/día}$$

**Paso 3 — Moles de cetano.**
$$n_{C_{16}H_{34}} = \frac{24\,900\,\text{g}}{226.45} = 110.0\,\text{mol/día}$$

**Paso 4 — Moles de CO₂.**
La estequiometría 2 mol cetano → 32 mol CO₂ ⇒ por cada mol de cetano salen **16 mol de CO₂**.
$$n_{CO_2} = 16 \times 110.0 = 1760\,\text{mol/día}$$

**Paso 5 — Masa de CO₂.**
$$m_{CO_2} = 1760 \times 44.01 = 77\,458\,\text{g/día} \approx 77\,\text{kg/día}$$

**Paso 6 — Conversión anual.**
Suponiendo 200 días lectivos/año:
$$m_{CO_2,año} \approx 77 \times 200 = 15\,400\,\text{kg/año} = 15.4\,\text{t/año}$$

**Paso 7 — Compara con metas y huella per cápita.**
- Si en el autobús viajan 40 alumnos: **0.39 t CO₂/alumno/año** solo por el bus escolar.
- Eso equivale a **20 % del objetivo total** per cápita 2050.

**Paso 8 — Conclusión y propuesta.**
> El autobús escolar emite ≈ **15.4 t de CO₂/año** y aporta 0.39 t por alumno transportado. Para mitigar, dos vías concretas: rutas optimizadas (ahorrarían ~10 % combustible ⇒ 1.5 t/año) y, en horizonte 2030, migración a unidad eléctrica con CFE mix (factor 0.42 kg/kWh) que reduciría las emisiones a un tercio. Este cálculo alimenta directamente la calculadora de huella de la **Implementación Albatros**.
::/practica
