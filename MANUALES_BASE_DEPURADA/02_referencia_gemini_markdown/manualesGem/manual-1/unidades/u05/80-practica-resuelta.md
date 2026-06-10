---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Diseño completo del tratamiento del bebedero

::practica{titulo="Diseño estequiométrico-energético-verde para tratar 1,000 L del bebedero"}
**Problema.** Diseña el sistema de cloración para 1,000 L diarios de agua del bebedero. Especifica:
1. Dosis de cloro (NaOCl al 5 %).
2. Tiempo mínimo de contacto.
3. Energía requerida.
4. Huella de carbono.
5. E-factor del proceso.

Datos:
- Concentración objetivo: 0.5 mg/L de cloro libre.
- Demanda de cloro del agua del bebedero: 0.3 mg/L.
- M(NaOCl) = 74.44 g/mol; M(Cl) = 35.45 g/mol.
- Constante cinética: k = 0.07 min⁻¹ a 25 °C, pH 7.
- Reducción exigida: 4 log de E. coli.
- Energía eléctrica de bombeo: 0.30 kWh/m³.
- Factor de emisión CFE: 0.42 kg CO₂eq/kWh.
- Densidad cloro al 5 %: 1.07 g/mL; M residuos sólidos: ~30 mg/L.

---

**Paso 1 — Estequiometría de la dosis.**

Cloro total requerido = residual + demanda = 0.5 + 0.3 = 0.8 mg/L.

Para 1,000 L: 0.8 g de Cl libre necesarios.

$n_{Cl} = 0.8 / 35.45 = 0.0226\,\text{mol}$
$n_{NaOCl} = 0.0226\,\text{mol}$ (relación 1:1)
$m_{NaOCl} = 0.0226 \times 74.44 = 1.68\,\text{g}$

Como cloro comercial al 5 %: $m_\text{solución} = 1.68/0.05 = 33.6\,\text{g} = 31\,\text{mL}$.

**Dosis: 31 mL de cloro al 5 % por cada 1,000 L.**

**Paso 2 — Tiempo de contacto (cinética).**

Para 4 log de reducción:
$$t = \frac{4}{k} = \frac{4}{0.07} = 57\,\text{min}\,(\text{teórico})$$

Con factor de seguridad de 1.5: **t ≈ 30 min** en práctica (asumiendo agua de calidad media). Para agua con más materia orgánica, se extiende a 60-120 min.

**Tiempo de contacto recomendado: 30 minutos.**

**Paso 3 — Energía total.**

Solo bombeo: $E = 0.30\,\text{kWh/m}^3 \times 1\,\text{m}^3 = 0.30\,\text{kWh}$ por 1,000 L.

**Energía: 0.30 kWh por 1,000 L tratados.**

**Paso 4 — Huella de carbono.**

$$\text{CO}_2 = 0.30 \times 0.42 = 0.126\,\text{kg} = 126\,\text{g CO}_2\text{eq}$$

(Más una fracción menor por producción del cloro, ~50 g extra → total ~180 g CO₂eq.)

**Huella: ~180 g CO₂eq por 1,000 L.**

**Paso 5 — E-factor.**

Producto útil = 1,000 L de agua tratada = 1,000 kg.
Residuos = 30 mg/L × 1,000 L = 30 g = 0.030 kg (lodos, exceso de cloro evaporado).

$$E\text{-factor} = \frac{0.030}{1,000} = 3 \times 10^{-5}$$

**E-factor: 3 × 10⁻⁵** (excelente, comparable a refinación de petróleo). El tratamiento de agua es de los procesos químicos más limpios.

**Paso 6 — Termodinámica (verificación de espontaneidad).**

Reacción del HOCl con materia orgánica genérica (R-H):
$$\ce{R-H + HOCl -> R-Cl + H2O}$$

ΔH ≈ -120 kJ/mol (exotérmica), ΔS ≈ +50 J/K·mol.
A 25 °C (298 K): ΔG = -120,000 - 298 × 50 = -134,900 J = -134.9 kJ/mol.

**ΔG << 0:** reacción muy espontánea, no requiere aporte energético.

**Paso 7 — Tabla resumen para la directora.**

| Parámetro | Valor |
|---|---|
| Dosis de cloro al 5 % | 31 mL por 1,000 L |
| Tiempo de contacto | 30 min |
| Energía eléctrica | 0.30 kWh por 1,000 L |
| CO₂ emitido | 180 g por 1,000 L |
| E-factor | 3 × 10⁻⁵ (limpio) |
| Costo de cloro al 5 % | ≈ \$0.50 MXN por 1,000 L |
| Costo eléctrico | ≈ \$0.90 MXN por 1,000 L |
| **Total operativo** | **≈ \$1.40 MXN por 1,000 L** |

**Paso 8 — Conclusión.**

> El tratamiento por cloración es **estequiométricamente eficiente, cinéticamente viable, termodinámicamente espontáneo y ambientalmente limpio**. Costo operativo estimado: \$1.40 MXN por 1,000 L. Para una escuela con consumo diario de 5,000 L, el costo mensual es ≈ \$210 MXN, una fracción mínima del presupuesto operativo. Se recomienda implementar con sensor IoT (U2.7) para monitoreo continuo y verificación de cloro residual cada 2 horas.
::/practica

---

::practica{titulo="Reactivo limitante y rendimiento — neutralización de la cisterna ácida"}
**Problema.** Tras un evento de lluvia ácida, la cisterna del bebedero queda con 5 m³ de agua y pH 4.0. Vas a neutralizarla con cal apagada (Ca(OH)₂) hasta pH 7.0 antes de tratarla con cloro. Calcula la masa exacta de cal, identifica si la cal disponible es limitante y obtén el rendimiento.

Datos: M(Ca(OH)₂) = 74.10 g/mol · cal disponible en bodega: 100 g · pureza comercial 90 %.

**Paso 1 — Calcula los moles de H⁺ a neutralizar.**
- pH 4.0 ⇒ [H⁺] = 1.0 × 10⁻⁴ M.
- En 5000 L: $n_{H^+} = 1.0 \times 10^{-4} \times 5000 = 0.50$ mol.

**Paso 2 — Estequiometría del proceso.**
$$Ca(OH)_2 + 2H^+ \to Ca^{2+} + 2H_2O$$
1 mol Ca(OH)₂ neutraliza 2 mol H⁺.

$$n_{Ca(OH)_2,\text{teórico}} = 0.50/2 = 0.25\,\text{mol}$$

**Paso 3 — Convierte a masa pura.**
$$m_\text{pura} = 0.25 \times 74.10 = 18.5\,\text{g}$$

**Paso 4 — Considera la pureza del 90 %.**
$$m_\text{comercial} = 18.5/0.90 = 20.6\,\text{g}$$

**Paso 5 — Verifica si la cal disponible es limitante.**
Tienes 100 g de cal al 90 %. Necesitas 20.6 g. Sobra **mucho**: la cal **NO es limitante**, lo que limita es el H⁺ del agua. Buena noticia: con un saco abierto neutralizas casi 5 cisternas.

**Paso 6 — Rendimiento esperado.**
La neutralización ácido-base es prácticamente cuantitativa (rendimiento típico > 99 %). Asumiendo 95 % por mezcla imperfecta:
$$n_{Ca(OH)_2,\text{efectivo}} = 0.25 \times 0.95 = 0.2375\,\text{mol}$$
H⁺ neutralizado = 0.475 mol; quedan 0.025 mol en 5000 L → [H⁺] residual = 5 × 10⁻⁶ M → pH ≈ 5.3.

Si quieres llegar a pH 7, agrega 5 % extra de cal: dosis recomendada 21.6 g (≈ 22 g) comerciales.

**Paso 7 — Verificación de seguridad.**
Calcio aportado: 0.25 mol × 40.08 = 10.0 g de Ca²⁺ en 5000 L = **2 mg/L**. Despreciable comparado con la dureza original del bebedero (~80 mg/L). No genera problema regulatorio.

**Paso 8 — Conclusión.**
> Para neutralizar 5 m³ del bebedero acidificado a pH 4 hasta pH neutro necesitas **≈ 22 g de cal apagada comercial** (90 % pura). El reactivo no es limitante, el rendimiento se ajusta sobre el factor de mezcla. La operación añade ≈ 2 mg/L de Ca²⁺, sin riesgo regulatorio. Esta práctica conecta directamente con la **Implementación Albatros** del dossier de tratamiento.
::/practica

---

::practica{titulo="PV = nRT y química verde — CO₂ liberado al neutralizar la dureza con cal"}
**Problema.** El proceso "cal-soda" para ablandar agua dura genera CaCO₃ que precipita pero **libera CO₂** al reaccionar con bicarbonato. Para 1 m³ de agua del bebedero con dureza temporal de 200 mg/L como CaCO₃, calcula los litros de CO₂ liberados a CNTP y evalúa si esto contradice la química verde.

**Paso 1 — Reacción simplificada del ablandamiento.**
$$Ca(HCO_3)_2 + Ca(OH)_2 \to 2\,CaCO_3 \downarrow + 2\,H_2O$$
La estequiometría no muestra CO₂ neto (queda como carbonato sólido). Pero si la dureza se neutraliza con HCl (alternativa), sí libera CO₂:
$$CaCO_3 + 2\,HCl \to CaCl_2 + H_2O + CO_2\uparrow$$

**Paso 2 — Para la ruta con HCl, calcula moles de CO₂.**
- Dureza: 200 mg/L × 1000 L = 200 g de CaCO₃ por m³.
- $n_{CaCO_3} = 200/100.09 = 2.0$ mol.
- $n_{CO_2} = 2.0$ mol (relación 1:1).

**Paso 3 — Aplica PV = nRT a CNTP (273 K, 1 atm, R = 0.0821 L·atm/(mol·K)).**
$$V = \frac{nRT}{P} = \frac{2.0 \times 0.0821 \times 273}{1} = 44.8\,\text{L de CO}_2$$

**Paso 4 — Convierte a kg de CO₂ liberado.**
$$m_{CO_2} = 2.0 \times 44.01 = 88\,\text{g} = 0.088\,\text{kg}$$

**Paso 5 — Compara las dos rutas.**

| Ruta | Reactivo | Productos | CO₂ liberado | Comentario verde |
|---|---|---|---|---|
| A — cal | Ca(OH)₂ | CaCO₃ sólido + H₂O | 0 g (neto) | atrapa el carbonato como sólido |
| B — HCl | HCl | CaCl₂ + CO₂ + H₂O | 88 g por m³ | libera CO₂ a la atmósfera |

**Paso 6 — Aplica los 12 principios verdes.**
- La ruta A respeta el principio 1 (prevención de residuos), 2 (economía atómica) y 12 (química más segura, no usa ácido fuerte).
- La ruta B viola el principio 1 (genera CO₂), aunque cumple 9 (catálisis no aplica) y 5 (disolventes seguros).

**Paso 7 — Conclusión.**
> Para ablandar 1 m³ del bebedero, la ruta con cal apagada **es ambientalmente superior** a la ruta con HCl: cero kg de CO₂ frente a 0.088 kg/m³. Para 5000 L diarios de agua escolar, eso son ~160 kg de CO₂ evitados al año solo por elegir bien la ruta. Esta decisión debe quedar registrada en el dossier de la **Implementación Albatros** con su justificación de los principios 1, 2 y 12.
::/practica
