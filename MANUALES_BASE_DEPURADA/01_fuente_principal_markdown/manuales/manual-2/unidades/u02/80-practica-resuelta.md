---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Análisis dinámico completo del coche F1

::practica{titulo="Calcula la fuerza, aceleración y comportamiento del coche F1"}
**Problema.** Tu coche F1 tiene:
- Masa total: 60 g.
- Cartucho de CO₂: 8 g (libera gas a 150 m/s por 0.4 s).
- Fricción de rodamiento: μₖ = 0.05.
- Pista horizontal: 20 m.

Calcula: empuje, aceleración, velocidad, momento y energía.

---

**Paso 1 — Empuje promedio (Tercera Ley + impulso).**
- Conservación de momento: $F \cdot \Delta t = m_{gas} \cdot v_{gas}$
- $F = (0.008)(150) / 0.4 = 3.0\,\text{N}$

**Paso 2 — Aceleración durante el empuje.**
- **Empuje:** 3.0 N (adelante).
- **Fricción:** $F_r = 0.05 \times (0.060)(9.8) = 0.029\,\text{N}$ (atrás).
- **Fuerza neta:** $3.0 - 0.029 = 2.97\,\text{N}$.
- **Aceleración:** $a = 2.97 / 0.060 = 49.5\,\text{m/s}^2$ (~5g).

::interioriza
Imagina que empujas un carrito de supermercado vacío con todas tus fuerzas. 
La aceleración es brutal al principio, pero si las ruedas están oxidadas (fricción), perderás algo de esa fuerza inicial.
::

**Paso 3 — Velocidad al fin del empuje (MRUA).**
- $v = at = 49.5 \times 0.4 = 19.8\,\text{m/s}$ (~71 km/h).

**Paso 4 — Verificación (Momento).**
- Momento del gas: $p_{gas} = 1.2\,\text{kg·m/s}$.
- $v_{coche} = 1.2 / 0.060 = 20\,\text{m/s}$. ✓

**Paso 5 — Energía aportada.**
- $E_{gas} = \tfrac{1}{2}(0.008)(150)^2 = 90\,\text{J}$
- $E_{coche} = \tfrac{1}{2}(0.060)(19.8)^2 = 11.8\,\text{J}$
- **Eficiencia:** 13 %. El resto escapa con el gas.

**Paso 6 a 8 — Tiempo total y mejoras.**
- Distancia en empuje: 3.96 m.
- Distancia restante: 16.04 m.
- Desaceleración: $-0.49\,\text{m/s}^2$.
- Velocidad final: 19.4 m/s.
- Tiempo total: **1.22 s**.

**Mejoras:**
1. **Reducir masa**: Bajar a 30 g sube aceleración a $100\,\text{m/s}^2$.
2. **Reducir fricción**: Rodamientos de bolas.
3. **Boquilla estrecha**: Mayor empuje.

::pausa{titulo="Aplica lo aprendido"}
¿Por qué la eficiencia de transferencia de energía es tan baja (13 %)?
*Piensa en quién se lleva la mayor parte de la energía cinética.*
::
::/practica

---

::practica{titulo="Equilibrio rotacional — chasis del F1 sobre el balance"}
**Problema.** 
- Apoyos: dos llantas separadas $L = 0.20$ m.
- Masa total: $m = 0.060$ kg.
- Centro de masa a $d = 0.07$ m de la llanta delantera.

Calcula la normal en cada eje y el riesgo de "caballito".

---

**Paso 1 a 4 — Fuerzas normales.**
- Peso $W = 0.588\,\text{N}$.
- Suma de torcas: $N_2 = (W \cdot d) / L = 0.206\,\text{N}$.
- $N_1 = 0.382\,\text{N}$.
- **Reparto:** 65 % delantera, 35 % trasera.

**Paso 5 — Centro de masa atrás ($d = 0.13$ m).**
- El reparto se invierte: 35 % delantera, 65 % trasera.

::interioriza
Es como subir una rampa en bicicleta. Si te tiras muy hacia atrás (centro de masa retrasado), 
la rueda delantera pierde agarre y puede levantarse. Si te inclinas adelante, aseguras tracción.
::

**Paso 6 y 7 — Torque máximo ("Caballito").**
- Se levanta si $N_1 = 0$.
- Ocurre cuando el empuje supera 2.55 N.
- **Riesgo:** Como el cartucho entrega 3 N, ¡hará caballito!
- **Solución:** Bajar el eje de empuje o mover el peso.

::pausa{titulo="Analiza"}
¿De qué otra forma podrías evitar el caballito sin cambiar el peso ni el motor?
*Pista: Aerodinámica.*
::
::/practica

---

::practica{titulo="Resorte y oscilación — sistema de suspensión del coche F1"}
**Problema.** 
- Resorte delantero: $k = 250\,\text{N/m}$.
- Masa por resorte: $m = 0.025$ kg.

Calcula la compresión, período y riesgo de resonancia a 12 m/s en 1.0 m.

---

**Paso 1 — Compresión estática.**
- $x = mg/k = 0.98\,\text{mm}$.

**Paso 2 y 3 — Período y Frecuencia.**
- $T = 2\pi\sqrt{m/k} = 0.0628\,\text{s}$.
- $f = 15.9\,\text{Hz}$.

**Paso 4 a 6 — Riesgo de Resonancia.**
- Tiempo en cruzar 1 m: $0.0833\,\text{s}$.
- Número de oscilaciones: $1.33$.

::interioriza
Un coche saltando en un bache es como botar una pelota de baloncesto. 
Si empujas la pelota justo cuando sube (resonancia), rebotará más alto. 
Si los baches coinciden con los 16 Hz, el coche saltará sin control.
::

**Conclusión:**
- Si hay baches cada 0.75 m a 12 m/s, el coche entrará en **resonancia**.
- **Solución:** Agregar amortiguador (fricción fluida).

::pausa{titulo="Deducción rápida"}
¿Qué pasaría con la frecuencia de salto si pones resortes más duros (mayor $k$)?
::
::/practica
