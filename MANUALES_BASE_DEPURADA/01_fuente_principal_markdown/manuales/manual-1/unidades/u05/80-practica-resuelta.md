---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Diseño completo del tratamiento del bebedero

::practica{titulo="Diseño estequiométrico-energético-verde para tratar 1,000 L del bebedero"}
**Problema.** 
Diseña el sistema de cloración para 1,000 L diarios de agua del bebedero. 

Especifica:
- Dosis de cloro (NaOCl al 5 %).
- Tiempo mínimo de contacto.
- Energía requerida y huella de carbono.
- E-factor del proceso.

**Datos clave:**
- Concentración objetivo: 0.5 mg/L de cloro libre.
- Demanda de cloro del bebedero: 0.3 mg/L.
- Constante cinética: k = 0.07 min⁻¹ a 25 °C.

---

**Paso 1 — Estequiometría de la dosis.**

- Cloro total requerido = residual + demanda = 0.8 mg/L.
- Para 1,000 L: 0.8 g de Cl libre necesarios.
- $n_{Cl} = 0.0226\,\text{mol}$
- $m_{NaOCl} = 1.68\,\text{g}$

**Dosis final:** 31 mL de cloro al 5 % por cada 1,000 L.

::interioriza
**La regla de la sopa salada:**
Añadir cloro al agua es como echar sal a una sopa. 
La "demanda" es la cantidad de sal que absorben los ingredientes (las bacterias). 
El "residual" es el sabor salado que queda en el caldo para protegerlo de echarse a perder.
::

**Paso 2 — Tiempo de contacto.**

- Para 4 log de reducción: $t = 57\,\text{min}$ (teórico).
- **Tiempo recomendado:** 30 min (con factor de seguridad).

**Paso 3 y 4 — Energía y Huella de carbono.**

- Energía de bombeo: 0.30 kWh por 1,000 L.
- $\text{CO}_2 = 0.30 \times 0.42 = 126\,\text{g CO}_2\text{eq}$.
- **Huella total:** ~180 g CO₂eq por 1,000 L.

**Paso 5 — E-factor.**

- Residuos = 30 g.
- Producto útil = 1,000 kg.
- **E-factor:** $3 \times 10^{-5}$ (muy limpio).

**Conclusión.**
> El tratamiento es eficiente, espontáneo y limpio. 
> Costo estimado: $1.40 MXN por 1,000 L.
::/practica

::pausa{}
**Deduce:**
Si el agua del bebedero estuviera más turbia (mayor demanda), ¿cómo afectaría a la "sopa salada" y a la cantidad de ml de cloro requeridos?
::

---

::practica{titulo="Reactivo limitante y rendimiento — neutralización de la cisterna ácida"}
**Problema.** 
La cisterna (5 m³) tiene pH 4.0 por lluvia ácida. 
Neutraliza con cal apagada (Ca(OH)₂) hasta pH 7.0. 
Halla la masa exacta de cal y evalúa si 100 g de cal comercial (90 %) son suficientes.

**Paso 1 — Moles de H⁺ a neutralizar.**
- pH 4.0 ⇒ [H⁺] = $1.0 \times 10^{-4}$ M.
- En 5000 L: $n_{H^+} = 0.50$ mol.

**Paso 2 — Estequiometría y pureza.**
- 1 mol Ca(OH)₂ neutraliza 2 mol H⁺.
- $n_{Ca(OH)_2,\text{teórico}} = 0.25\,\text{mol}$.
- Masa pura = 18.5 g.
- **Masa comercial (90 %):** 20.6 g.

::interioriza
**El extintor de incendios:**
El ácido (H⁺) es el fuego y la cal es el extintor. 
Tienes un extintor enorme (100 g), pero solo necesitas un chorrito (20.6 g) para apagar la "acidez". 
¡El fuego (H⁺) es el limitante, no tu extintor!
::

**Paso 3 — Reactivo limitante.**
- Tienes 100 g. Necesitas 20.6 g. 
- La cal **NO es limitante**. ¡Sobra para casi 5 cisternas!

**Conclusión.**
> Necesitas **≈ 22 g de cal comercial**. 
> Añade ≈ 2 mg/L de Ca²⁺, lo cual no es riesgo regulatorio.
::/practica

::pausa{}
**Piénsalo:**
Si la cal comercial tuviera solo 50 % de pureza, ¿serían suficientes los 100 g disponibles en bodega para neutralizar la cisterna?
::

---

::practica{titulo="PV = nRT y química verde — CO₂ liberado al neutralizar la dureza"}
**Problema.** 
El proceso "cal-soda" abate dureza. 
Calcula los litros de CO₂ a CNTP liberados por la ruta con HCl vs. la ruta con cal. 
Evalúa según química verde.

**Paso 1 — Cálculo con HCl.**
- Dureza: 200 g CaCO₃ por m³.
- $n_{CaCO_3} = 2.0$ mol.
- **CO₂ liberado:** 2.0 mol.

**Paso 2 — Volumen (PV = nRT).**
- $V = \frac{2.0 \times 0.0821 \times 273}{1} = 44.8\,\text{L de CO}_2$.
- Masa = 88 g (0.088 kg) de CO₂.

::interioriza
**La botella de refresco agitada:**
Usar HCl es como abrir un refresco agitado; liberas gas (CO₂) al aire al instante. 
Usar cal es como congelar el refresco; atrapas las burbujas dentro de la botella (como sólido).
::

**Paso 3 — Comparación y 12 principios.**
- **Ruta cal:** Cero emisiones. Previene residuos (P1) y es segura (P12).
- **Ruta HCl:** Libera 88 g de CO₂ por m³.

**Conclusión.**
> La ruta con cal es **ambientalmente superior**. 
> Evitas ~160 kg de CO₂ al año en una escuela.
::/practica

::pausa{}
**Active recall:**
¿Qué principio de la química verde viola directamente la ruta de neutralización con ácido clorhídrico (HCl)?
::
