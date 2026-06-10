---
unidad: 9
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Microrred renovable escolar para la flota F1"}
**Objetivo.** Construir y caracterizar una microrred solar autónoma a pequeña escala que pueda recargar las baterías de toda una flota de coches F1 escolares y, opcionalmente, alimentar la iluminación y sonido de la pista durante una jornada de carreras. Esta es la **implementación final** de tu manual de Física Albatros.

**¿Por qué hacerla?** Es la integración de **toda la unidad** en un proyecto real. Aplicas estructura atómica (efecto fotoeléctrico del panel), física nuclear (la energía del Sol como fuente última) y energías renovables (balance, almacenamiento, conversión). Y es replicable: tu escuela puede instalar el sistema permanentemente.

---

### Materiales

- 1-2 paneles solares de 100-200 W (LG, Jinko, Trina; ≈ 1 500 MXN c/u).
- 1 controlador de carga MPPT 30 A (Victron BlueSolar o equivalente; ≈ 2 500 MXN).
- 1 batería LiFePO4 12 V / 100 Ah (≈ 8 000 MXN; o gel deep-cycle más barata).
- 1 inversor 12 V → 110 V AC, 500 W (≈ 1 500 MXN, opcional).
- 1 cargador USB DC-DC 12 V → 5 V con 4 puertos (≈ 200 MXN).
- Cable solar #10 AWG (≈ 200 MXN).
- Estructura de soporte (madera, PVC o aluminio).
- Multímetro digital con función amperaje DC.
- Coches F1 escolares con baterías 3.7 V LiPo (al menos 5).

### Pasos

1. **Cálculo previo.** Aplica la práctica resuelta de la unidad para tu escuela. Documenta paneles necesarios, batería, jornada de uso esperada.
2. **Instalación física.** Monta los paneles con orientación sur (en hemisferio norte) e inclinación = latitud local (≈ 19° en CDMX). Conecta a controlador MPPT, batería, inversor.
3. **Caracterización del panel.** Mide $V_{oc}$, $I_{sc}$, $P_{max}$ a diferentes horas del día y días con/sin nubes. Construye la curva I-V.
4. **Carga de coches F1.** Mide cuánto demora cargar una batería 3.7 V / 1000 mAh desde el banco solar. Repite con varias en paralelo.
5. **Auditoría energética.** Durante una jornada real de carreras, registra cada hora: irradiancia (lux), V batería, A consumida. Construye gráfica de día completo.
6. **Comparación con red.** Con la energía suministrada por la microrred, calcula el costo equivalente si lo hubieras tomado de CFE (3-5 MXN/kWh) y el CO₂ evitado.
7. **Documentación de instalación.** Diagrama eléctrico, manual de operación, plan de mantenimiento (limpieza paneles cada 6 meses, revisión batería anual, reemplazo en 8-10 años).

::visual{tipo="ilustracion" descripcion="Microrred completa instalada en escuela: panel solar inclinado en techo orientado al sur conectado por cable solar a controlador MPPT en pared interior. MPPT conectado a batería LiFePO4 12V. Batería con 3 salidas: 1) cargador USB con 4 puertos cargando coches F1 escolares en una mesa. 2) Inversor 110V con luminarias LED iluminando la pista. 3) Toma para laptop y proyector de la presentación. Multímetro midiendo voltaje en la batería. Plano de la pista con coches estacionados cargándose visible." paginas=1}

---

### Entregable final

Reporte ejecutivo de 5-8 páginas con:
1. **Cálculos de diseño** — práctica resuelta aplicada a tu escuela.
2. **Diagrama eléctrico** — esquema completo con conexiones, fusibles, calibres de cable.
3. **Caracterización del panel** — curva I-V medida + comparación con datasheet.
4. **Auditoría de jornada** — gráficas de irradiancia, V batería y consumo durante una jornada de carreras real.
5. **Análisis económico** — costo total de instalación, ahorro anual, retorno de inversión.
6. **Análisis ambiental** — CO₂ evitado en 25 años de vida útil.
7. **Reflexión integradora** — ¿qué unidad del manual te resultó más útil para este proyecto? ¿Qué ampliarías para una escuela completa? ¿Qué pasaría si quisieras hacerlo 100 % autónomo (con electrolizador y celda de combustible para días nublados)?

### Rúbrica de evaluación final

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Cálculos de diseño** | inconsistentes | aplica fórmulas | dimensiona y justifica con margen de seguridad |
| **Instalación física** | no funciona | funciona, falta orden | instalación profesional documentada con fotos |
| **Caracterización** | sin medir | un solo punto | curva I-V completa con análisis de eficiencia |
| **Auditoría jornada** | sin datos | tabla básica | gráfica horaria con discusión de picos |
| **Análisis económico** | sin números | costo total | ROI calculado y comparado con red |
| **Análisis ambiental** | sin números | CO₂ anual | CO₂ ciclo de vida + equivalencias |
| **Reflexión** | sin reflexión | menciona conceptos | integra estructura atómica + nuclear + renovables |
::/implementacion
