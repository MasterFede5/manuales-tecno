---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Balance energético completo del coche F1

::practica{titulo="¿Cuánta energía aporta el cartucho y cuánta se pierde?"}
**Problema.** Analizamos un coche F1 con:
- **Masa total:** 60 g (incluyendo cartucho lleno).
- **Cartucho:** 8 g de CO₂ expulsado a 150 m/s en 0.4 s.
- **Pista:** 20 m horizontal.
- **Fricción:** $\mu_r = 0.05$. Aerodinámica: $C_d A = 0.005\,\text{m}^2$ (estimación). Aire: $\rho = 1.2\,\text{kg/m}^3$.

**Objetivos:**
1. Calcular la energía cinética del gas y absorbida por el coche.
2. Evaluar eficiencia y pérdidas por fricción/aerodinámica.
3. Determinar la velocidad de meta.

---

**Paso 1 — Energía del gas (sistema cerrado)**
- El gas es nuestra fuente principal de energía.
- $E_{gas} = \tfrac{1}{2} m_{gas} v_{gas}^2 = \tfrac{1}{2}(0.008)(150)^2 = 90\,\text{J}$

**Paso 2 — Energía del coche al finalizar el empuje**
- Conservación de momento: $v_{coche} \approx 23\,\text{m/s}$.
- Ajustando por fricción durante el disparo: **19.8 m/s**.
- $E_{coche} = \tfrac{1}{2}(0.052)(19.8)^2 = 10.2\,\text{J}$

**Paso 3 — Eficiencia del cohete**
- $\eta = E_{coche} / E_{gas} = 10.2 / 90 = 11.3\%$
- ¡Solo el 11 %! El 89 % de la energía se escapa con el gas.

::interioriza
- Imagina empujar un bote lanzando pelotas de boliche hacia atrás.
- Tu energía se va volando con la pelota; el bote apenas recibe una fracción.
::

**Paso 4 — Pérdidas durante el rodaje**
- **Rodadura:** $W_r = 0.05 \times (0.052)(9.8) \times 16.04 = 0.41\,\text{J}$
- **Corrección aerodinámica (perfil menor de balsa):** $C_d A \approx 0.001\,\text{m}^2$.
- $F_a = \tfrac{1}{2}(0.001)(1.2)(19.8)^2 = 0.235\,\text{N} \implies W_a = 0.235 \times 16 = 3.76\,\text{J}$

**Paso 5 — Meta**
- $E_{k,meta} = E_{coche} - W_r - W_a = 10.2 - 0.41 - 3.76 = 6.03\,\text{J}$
- $v_{meta} = \sqrt{2(6.03)/0.052} = 15.2\,\text{m/s}$ (Pierde 23% de velocidad).

**Paso 6 — Recomendaciones**
- **Flujo:** Bajar $C_d A$ a 0.0005 otorga **1.9 J** extra.
- **Ruedas:** Mejorar rodamientos a $\mu_r = 0.005$ da **0.37 J**.
- **Resumen:** Eficiencia global del 6.7%. ¡La aerodinámica manda!
::/practica

::pausa{tipo="resolucion"}
¿Por qué reducir el peso del coche NO mejora su eficiencia energética final respecto a la resistencia aerodinámica? (Pista: inercia).
::/pausa

---

::practica{titulo="Choque inelástico — F1 vs. Espuma"}
**Problema.** 
- Coche ($m_1 = 0.060$ kg) choca a $v_1 = 14$ m/s.
- Espuma ($m_2 = 0.250$ kg) en reposo. Choque perfectamente inelástico.

**Objetivos:**
1. Velocidad final combinada y energía disipada.
2. Fuerza sobre el chasis (impacto de 0.05 s).

---

**Paso 1 — Conservación del momento**
- $m_1 v_1 + m_2 v_2 = (m_1 + m_2) v_f$
- $0.060\times 14 = (0.310) v_f \implies v_f = 2.71\,\text{m/s}$

**Paso 2 — Energías y Disipación**
- Antes: $E_{k,0} = 5.88\,\text{J}$. Después: $E_{k,f} = 1.14\,\text{J}$.
- Pérdida: **4.74 J** (¡Se disipa el **80.6 %**!).

::interioriza
- Un choque inelástico es como saltar en un charco de lodo.
- La energía se pierde deformando el lodo; la espuma hace lo mismo para proteger la madera.
::

**Paso 3 — Fuerza de impacto**
- $F = \frac{\Delta p}{\Delta t} = \frac{0.060(2.71-14)}{0.05} = -13.5\,\text{N}$
- Equivale a **23 g** de fuerza. Contra concreto sufriría 135 N.
- **Conclusión:** La deformación salva al coche.
::/practica

::pausa{tipo="resolucion"}
¿Qué ocurriría con el coche F1 si el bloque de espuma estuviera empotrado a una pared?
::/pausa

---

::practica{titulo="Rampa con Loop — Desafío G-Force"}
**Problema.** 
- Loop de radio $R = 0.30$ m. Coche se suelta desde altura $h$ sin fricción.

**Objetivos:**
1. Velocidad mínima en la cima y altura de soltado.
2. Fuerzas si $h = 1.5$ m.

---

**Paso 1 — Límite de la cima**
- $mg = mv^2/R \implies v_\text{cima} = \sqrt{g R} = 1.71\,\text{m/s}$

**Paso 2 — Conservación para hallar altura mínima**
- $mgh_\text{mín} = mg(2R) + \tfrac{1}{2} m v_\text{cima}^2$
- $h_\text{mín} = 0.75\,\text{m}$. Debe caer desde al menos **2.5 veces el radio**.

::interioriza
- Funciona como un balde con agua girando.
- La inercia debe vencer a la gravedad, de lo contrario te mojas.
::

**Paso 3 — Análisis con holgura ($h = 1.5$ m)**
- Velocidad: $v = \sqrt{2g(h - 2R)} = 4.20\,\text{m/s}$ (sobrevive).
- Fuerza (aceleración): $a_c = v^2/R = 58.8\,\text{m/s}^2 \approx 6\,g$.
- ¡Sentir 6 G extra es intenso!
::/practica

::pausa{tipo="resolucion"}
Si añadieras fricción de rodadura real a la pista, ¿cómo ajustarías $h$?
::/pausa
