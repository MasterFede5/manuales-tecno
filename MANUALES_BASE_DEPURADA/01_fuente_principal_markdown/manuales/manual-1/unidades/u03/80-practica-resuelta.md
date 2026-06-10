---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — pH de la lluvia local con NOx atmosférico

::practica{titulo="¿Qué pH tendrá la lluvia si la zona tiene 150 µg/m³ de NO₂?"}
**Problema:**
- En una zona urbana cercana a la escuela, el monitor reporta **NO₂ = 150 µg/m³** (promedio 24h).
- Asume que **el 30 % del NO₂ se convierte en HNO₃** en la lluvia.
- Calcula el pH de la lluvia local y determina si es "lluvia natural" (pH 5.0-5.6) o ácida.

**Datos:**
- 1 m³ de aire pesa ≈ 1.2 kg a CNTP.
- Lluvia recolectada por cada m³ de aire procesado: 0.001 L.

::interioriza
Imagina que el gas NO₂ es como polvo de jugo en el aire. Solo una parte (30 %) logra atrapar la jarra de agua (la lluvia) y disolverse. Eso formará un ácido (HNO₃) que cambiará radicalmente el "sabor" (el pH) del agua que cae.
::/interioriza

::pausa{}
**Deduce antes de calcular:**
Si un gas que forma ácido fuerte se disuelve en agua pura, ¿su pH será mayor o menor que 7? ¿Qué tanto crees que baje?
::/pausa

**Paso 1 — Convierte a moles de NO₂**
- En 1 m³ de aire hay 150 µg = 1.5 × 10⁻⁴ g de NO₂.
- M(NO₂) = 46.01 g/mol.
$$n_{NO_2} = \frac{1.5 \times 10^{-4}}{46.01} = 3.26 \times 10^{-6}\,\text{mol}$$

**Paso 2 — Calcula el HNO₃ formado (30 %)**
$$n_{HNO_3} = 0.30 \times 3.26 \times 10^{-6} = 9.78 \times 10^{-7}\,\text{mol}$$
- Reacción: $\ce{2 NO2 + H2O -> HNO3 + HNO2}$
- (Asumimos que todo el NO₂ convertido es HNO₃).

**Paso 3 y 4 — Concentración de H⁺**
- Hay 0.001 L de lluvia por m³ de aire.
- $[HNO_3] = \frac{9.78 \times 10^{-7}\,\text{mol}}{0.001\,\text{L}} = 9.78 \times 10^{-4}\,\text{M}$
- Al ser ácido fuerte, $[H^+] = [HNO_3]$.

**Paso 5 y 6 — Calcula el pH y compara**
$$pH = -\log(9.78 \times 10^{-4}) = 3.01$$

| Tipo de lluvia | pH típico |
|---|---|
| Natural (con CO₂) | 5.0 – 5.6 |
| Ácida moderada | 4.0 – 5.0 |
| Ácida severa | 3.0 – 4.0 |
| **Calculada aquí** | **3.01** |

**Paso 7 — Conclusión y recomendación**
- pH ≈ 3.0: equivale a **lluvia ácida severa** (vinagre diluido).
- Al escurrir por un techo de zinc:
  - Disuelve el zinc ($\ce{Zn + 2 HNO3 -> Zn(NO3)2 + H2}$).
  - Libera iones Zn²⁺ tóxicos al agua de la cisterna.
- **Recomendación:** Verificar el pH de la cisterna tras lluvias y usar materiales inertes (PVC) en techos.
::/practica

---

::practica{titulo="Balanceo redox por ion-electrón — KMnO₄ frente a Fe²⁺ en agua de la cisterna"}
**Problema:**
- Detectaste **Fe²⁺** en el agua de la cisterna por corrosión.
- Titulas con permanganato (KMnO₄ 0.020 M) en medio ácido.
- Balancea la ecuación y calcula los mg de Fe²⁺ en 100 mL si gastaste **6.5 mL** de titulante.

::interioriza
Una titulación redox es como un trueque exacto de electrones. El KMnO₄ "compra" electrones (se reduce) y el Fe²⁺ los "vende" (se oxida) hasta que ya no queda hierro oxidable.
::/interioriza

::pausa{}
**Reflexiona:**
El permanganato es de color morado intenso. ¿Qué indicará un cambio de color permanente en el matraz?
::/pausa

**Pasos 1 a 4 — Balanceo Redox**
- **Oxidación:** $Fe^{2+} \to Fe^{3+} + e^-$ (multiplica por 5).
- **Reducción:** $MnO_4^- + 8H^+ + 5e^- \to Mn^{2+} + 4H_2O$.
- **Suma:** $5\,Fe^{2+} + MnO_4^- + 8H^+ \to 5\,Fe^{3+} + Mn^{2+} + 4H_2O$.
- Balance de carga y masa correctos (+17 en ambos lados).

**Paso 5 y 6 — Calcula Moles de Fe²⁺**
- $n(MnO_4^-) = 0.020 \times 0.0065 = 1.30 \times 10^{-4}\,\text{mol}$.
- Estequiometría (5:1): $n(Fe^{2+}) = 5 \times 1.30 \times 10^{-4} = 6.50 \times 10^{-4}\,\text{mol}$.

**Paso 7 y 8 — Convierte a concentración y concluye**
- Masa de Fe²⁺: $6.50 \times 10^{-4} \times 55.85 = 36.3$ mg (en 100 mL).
- **Concentración:** $363$ mg/L.
- **Norma:** Límite de hierro total ≤ 0.30 mg/L.
- El agua tiene **mil veces el límite** permitido.
- **Recomendación:** Clausurar bebedero y reemplazar tinaco.
::/practica

---

::practica{titulo="Estequiometría de combustión — emisiones de CO₂ del autobús escolar"}
**Problema:**
- El autobús escolar consume **30 L de diésel/día** (densidad ≈ 0.83 g/mL).
- Calcula los kg de CO₂ diarios y compáralos con la meta ONU 2050 (2 t CO₂eq/persona/año).

::interioriza
El motor es como una chimenea móvil. Toma el diésel líquido, lo oxida y lo expulsa como CO₂ gaseoso e invisible, sumando masa de oxígeno y acumulándolo en la atmósfera.
::/interioriza

::pausa{}
**Razona:**
¿Por qué el CO₂ producido por un tanque de diésel pesa más que el propio líquido combustible?
::/pausa

**Paso 1 y 2 — Combustión y masa de combustible**
- Cetano ($C_{16}H_{34}$, M = 226.45 g/mol).
- Reacción: $2\,C_{16}H_{34} + 49\,O_2 \to 32\,CO_2 + 34\,H_2O$.
- $m_{diésel} = 30\,\text{L} \times 0.83\,\text{kg/L} = 24.9\,\text{kg/día}$.

**Paso 3 y 4 — Moles producidos**
- $n_{C_{16}H_{34}} = 24\,900 / 226.45 = 110.0\,\text{mol/día}$.
- Según estequiometría: 16 moles de CO₂ por cada mol de cetano.
- $n_{CO_2} = 16 \times 110.0 = 1760\,\text{mol/día}$.

**Paso 5 y 6 — Masa diaria y anual de CO₂**
- $m_{CO_2} = 1760 \times 44.01 \approx 77\,\text{kg/día}$.
- Suponiendo 200 días lectivos: $m_{CO_2,año} \approx 77 \times 200 = 15.4\,\text{t/año}$.

**Paso 7 y 8 — Comparación y mitigación**
- Para 40 alumnos transportados: **0.39 t CO₂/alumno/año**.
- Representa el **20 % del objetivo total** per cápita 2050.
- **Acciones:**
  - Optimizar rutas ahorra ~10 % (1.5 t/año).
  - Migrar a bus eléctrico al 2030 con matriz limpia reduciría emisiones drásticamente.
::/practica
