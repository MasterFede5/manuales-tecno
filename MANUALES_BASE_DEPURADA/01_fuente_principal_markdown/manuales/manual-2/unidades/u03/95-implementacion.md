---
unidad: 3
seccion: implementacion
paginas_objetivo: 2
---

::implementacion{titulo="Implementación Albatros — Montaña rusa virtual en Algodoo + cálculo energético"}
**Objetivo.** Diseñar una montaña rusa virtual usando el simulador gratuito **Algodoo** (o PhET *Energy Skate Park*) y validar la conservación de energía mecánica observando cómo se intercambian Ek y Ug a lo largo del recorrido. Comparar con cálculos teóricos y explicar las pérdidas reales por fricción.

**¿Por qué hacerla?** Las montañas rusas son el "laboratorio perfecto" de conservación de energía: cinética y potencial intercambian docenas de veces. Un simulador te permite ver el balance en tiempo real, modificar parámetros (fricción, altura, masa) y validar que las ecuaciones funcionan.

---

### Materiales

- Computadora con Algodoo (gratis para descarga) o navegador para PhET.
- Calculadora.
- Cuaderno para registro.

### Pasos

**1. Diseña la pista.** Crea una secuencia de subidas y bajadas de distintas alturas (~5 m). Empieza con la cima más alta.

**2. Sin fricción inicial.** Coloca un carro de masa conocida (m = 0.5 kg) en la cima. Suéltalo.

**3. Observa y registra.** Para 5-7 puntos a lo largo del recorrido:
   - Mide altura desde el punto más bajo (con regla del simulador).
   - Mide velocidad (Algodoo lo muestra).
   - Calcula $E_k = \tfrac{1}{2}mv^2$ y $U_g = mgh$.
   - Verifica que $E_k + U_g$ sea constante (dentro de error numérico).

**4. Activa fricción.** Reinicia con coeficiente de fricción de 0.05.
   - Repite las mediciones en los mismos puntos.
   - Ahora $E_k + U_g$ disminuye con la distancia recorrida.
   - Calcula el "trabajo de la fricción" como la diferencia.

**5. Cambia la masa.** Repite con m = 1 kg. Observa que la velocidad en cada punto **es la misma** (sin fricción) pero las energías son distintas.

**6. Cambia la altura inicial.** Verifica que la velocidad final escala con $\sqrt{h}$.

::visual{tipo="interfaz" descripcion="Captura de Algodoo o PhET Energy Skate Park: pista curva con subidas y bajadas, carro de juguete en una posición intermedia, panel lateral con barras dinámicas mostrando energía cinética (azul) y potencial (verde) que cambian con el tiempo, suma constante en color naranja. Color azul Albatros." paginas=0.5}

---

### Entregable

Documento de 2-3 páginas con:
1. Captura del diseño de pista.
2. Tabla con altura, velocidad, Ek, Ug, Em en 5+ puntos sin fricción.
3. Misma tabla con fricción incluida.
4. Gráfica de Em vs distancia (sin y con fricción).
5. Conclusiones sobre conservación y pérdidas.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Diseño de pista** | una sola subida | varias colinas | con loop o curvas complejas |
| **Mediciones** | <5 puntos | 5-7 puntos | sin Y con fricción comparados |
| **Cálculos** | sin teoría | Ek, Ug calculados | balance verificado con error porcentual |
| **Análisis** | descripción | identifica pérdidas | cuantifica pérdidas y explica |

### Reto bonus (+1 punto)

Diseña un loop vertical y calcula la velocidad mínima en la cima necesaria para que el carro complete el loop sin caer (cuando la fuerza centrípeta = peso). Verifica con simulación.

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Diseño | 1 | Pista virtual con 3 colinas y altura inicial fijada | captura del simulador |
| 2. Sin fricción | 2 | Tabla con 7 puntos, balance $E_k+U_g$ verificado | tabla con error <2 % |
| 3. Con fricción | 3 | Misma tabla con μ=0.05, $W_f$ calculado | comparación gráfica |
| 4. Optimización | 4 | Loop superado con altura mínima determinada empírica y teórica | reporte 3 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Eficiencia vs masa.** Repite la simulación con masas de 0.5, 1.0 y 2.0 kg manteniendo la misma fricción. Verifica que la energía perdida $W_f = \mu m g d$ escala linealmente con $m$, pero la velocidad final no depende de $m$ (sin fricción).
2. **Curva de altura mínima del loop.** Calcula y verifica numéricamente $h_\text{mín} = 2.5 R$ para tres radios distintos del loop (0.5, 1.0 y 1.5 m).
3. **Mapa de energía.** Exporta los datos del simulador y construye una gráfica $E_k(t)$ y $U_g(t)$ con sus suma. Identifica visualmente la zona donde la fricción "come" la energía.
::/implementacion

---

::albatros{titulo="Caso integrador — auditoría energética del prototipo F1" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu equipo dispone de tres datos del último prototipo: masa $m = 60$ g, velocidad pico $v_p = 18$ m/s, velocidad en meta $v_m = 14$ m/s, distancia post-empuje $d = 16$ m. ¿Adónde se fueron los joules que faltan?

**Lo que harás.**
1. Calcula $E_k$ pico y $E_k$ en meta. Reporta la diferencia $\Delta E$ en joules.
2. Asume que la fricción de rodadura aporta $W_r = \mu_r m g d$ con $\mu_r = 0.04$. Calcula $W_r$.
3. Resta: la diferencia $\Delta E - W_r$ se atribuye al arrastre aerodinámico. Despeja un valor efectivo de $C_d A$ asumiendo arrastre constante con $v_\text{prom}$.
4. Compara con valores típicos ($C_d A \sim 0.001\,\text{m}^2$ para coches escolares).
5. Recomienda **una** intervención prioritaria (rodadura vs aerodinámica) con justificación cuantitativa.

**Entregable.** Hoja con cálculos paso a paso y tabla con: $E_k$ pico, $E_k$ meta, $W_r$, $W_a$, $C_d A$ deducido, recomendación.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo $\Delta E$ y $W_r$ | parciales | completos | con unidades y cifras significativas |
| Deducción de $C_d A$ | sin valor | con valor | + comparación con valor típico |
| Recomendación | genérica | con valor numérico | con valor numérico + ruta de validación |
::/albatros
