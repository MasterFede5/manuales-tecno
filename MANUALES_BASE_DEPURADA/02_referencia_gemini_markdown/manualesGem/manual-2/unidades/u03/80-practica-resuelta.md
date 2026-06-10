---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Balance energético completo del coche F1

::practica{titulo="¿Cuánta energía aporta el cartucho y cuánta se pierde?"}
**Problema.** Tu coche F1 tiene:
- Masa total: 60 g (incluyendo cartucho lleno).
- Cartucho: 8 g de CO₂ que escapa a 150 m/s en 0.4 s.
- Pista: 20 m horizontal.
- Coeficiente de fricción de rodadura: 0.05.
- Coeficiente de arrastre × área: $C_d A = 0.005\,\text{m}^2$ (estimado).
- Densidad del aire: $\rho = 1.2\,\text{kg/m}^3$.

Calcula:
1. Energía cinética entregada al gas.
2. Energía cinética absorbida por el coche (al fin del empuje).
3. Eficiencia de transferencia de energía.
4. Pérdidas por fricción y resistencia del aire durante el trayecto.
5. Energía cinética del coche al llegar a la meta.

---

**Paso 1 — Energía cinética del gas (como sistema cerrado).**

$$E_{gas} = \tfrac{1}{2} m_{gas} v_{gas}^2 = \tfrac{1}{2}(0.008)(150)^2 = 90\,\text{J}$$

**Paso 2 — Energía cinética del coche al fin del empuje.**

Por conservación del momento (U3.6):
$$v_{coche} = m_{gas} v_{gas} / m_{coche\_sin\_gas} \approx 0.008(150)/0.052 = 23\,\text{m/s}$$

(O usando F=ma con fricción: ~19.8 m/s, que es lo realmente medido por la pequeña fricción durante el empuje.)

Para esta práctica, tomemos el valor más realista de 19.8 m/s (con las pérdidas):

$$E_{coche} = \tfrac{1}{2}(0.052)(19.8)^2 = 10.2\,\text{J}$$

**Paso 3 — Eficiencia.**

$$\eta = E_{coche} / E_{gas} = 10.2 / 90 = 11.3\%$$

**Solo el 11 % de la energía del cartucho se queda con el coche.** El 89 % se va con los gases.

**Esto es típico de cohetes**: la mayor parte de la energía la lleva el propelente. Por eso los cohetes son ineficientes en términos energéticos pero óptimos en términos de impulso (lo que importa para acelerar).

**Paso 4 — Pérdidas durante el trayecto (después del empuje).**

**Fricción de rodadura:**
$$W_r = \mu_r N \times d = 0.05 \times (0.052)(9.8) \times (20 - 3.96) = 0.41\,\text{J}$$

(Restamos 3.96 m porque la pista de empuje no tiene fricción significativa al estar el coche acelerando con el cartucho.)

**Resistencia del aire** (en velocidad pico de 19.8 m/s, distancia 16 m):
$$F_a = \tfrac{1}{2} C_d A \rho v^2 = \tfrac{1}{2}(0.005)(1.2)(19.8)^2 = 1.18\,\text{N}$$

(Más alta de lo que pensábamos.)

$$W_a = F_a \times 16 = 18.8\,\text{J}$$

**¡Espera!** Eso supera la energía cinética del coche (10.2 J). Eso indica que mi $C_d A$ era sobre-estimado.

**Reestimando** $C_d A$ para un F1 escolar pequeño y aerodinámico: ~0.001 m².
$$F_a = \tfrac{1}{2}(0.001)(1.2)(19.8)^2 = 0.235\,\text{N}$$
$$W_a = 0.235 \times 16 = 3.76\,\text{J}$$

Aún significativa pero realista.

**Paso 5 — Energía cinética en la meta.**

$$E_{k,meta} = E_{coche} - W_r - W_a = 10.2 - 0.41 - 3.76 = 6.03\,\text{J}$$

$$v_{meta} = \sqrt{2 E_{k,meta} / m} = \sqrt{2(6.03)/0.052} = 15.2\,\text{m/s}$$

**Conclusión:** el coche llega a la meta con velocidad de ~15 m/s (vs 19.8 m/s al fin del empuje). **Pierde 23 % de velocidad** durante el trayecto post-empuje, principalmente por **resistencia del aire** (no por fricción).

**Paso 6 — Tiempo total revisado.**

Asumiendo desaceleración aproximadamente constante:
$$\bar{v} = (19.8 + 15.2)/2 = 17.5\,\text{m/s}$$
$$t_2 = (20-3.96)/17.5 = 0.92\,\text{s}$$
$$t_{total} = 0.4 + 0.92 = 1.32\,\text{s}$$

**Paso 7 — Recomendaciones para optimizar.**

| Mejora | Energía recuperada | Velocidad mejorada |
|---|---:|---|
| Mejor aerodinámica ($C_d A$ → 0.0005) | 1.9 J | +0.5 m/s |
| Mejor rodamientos ($\mu_r$ → 0.005) | 0.37 J | +0.2 m/s |
| Reducir masa (sin cartucho 30g → 20g) | n/a | aceleración inicial mayor |
| Mejor cartucho (más CO₂, mayor v_gas) | n/a | velocidad pico mayor |

**Cálculo final del balance energético:**

```
Cartucho (química): 90 J
   ↓ (89 % perdido en gas escapado)
Coche F1 al fin del empuje: 10.2 J
   ↓ (4 % perdido en fricción)
Coche en meta: 6.0 J
```

> **Conclusión final.** El coche F1 actual es 6.7 % eficiente desde el cartucho hasta la meta. Mejoras aerodinámicas pueden subirlo a 8-10 %. Reducir la masa del cartucho descargado aumenta la velocidad pico significativamente. La aerodinámica es el cuello de botella en pistas largas.
::/practica

---

::practica{titulo="Choque inelástico — coche F1 contra barrera de espuma"}
**Problema.** Tu coche F1 ($m_1 = 0.060$ kg) llega a la meta con $v_1 = 14$ m/s y choca con un bloque de espuma ($m_2 = 0.250$ kg) que estaba en reposo. El choque es perfectamente inelástico: el coche queda incrustado. Calcula:
1. Velocidad final del conjunto coche+espuma.
2. Energía cinética antes y después del choque.
3. Porcentaje de energía cinética disipada (en deformación de la espuma, calor y sonido).
4. Si el contacto duró 0.05 s, ¿qué fuerza promedio sufrió el chasis?

---

**Paso 1 — Conservación del momento.**

$$m_1 v_1 + m_2 v_2 = (m_1 + m_2) v_f$$
$$0.060\times 14 + 0.250\times 0 = (0.310) v_f$$
$$v_f = 0.84 / 0.310 = 2.71\,\text{m/s}$$

**Paso 2 — Energías cinéticas.**

$$E_{k,0} = \tfrac{1}{2}(0.060)(14)^2 = 5.88\,\text{J}$$
$$E_{k,f} = \tfrac{1}{2}(0.310)(2.71)^2 = 1.14\,\text{J}$$

**Paso 3 — Energía disipada.**

$$\Delta E = E_{k,0} - E_{k,f} = 4.74\,\text{J}; \quad \%_\text{dis} = 4.74/5.88 = 80.6\%$$

> El choque inelástico **disipa el 80.6 %** de la energía cinética inicial. Mucho calor, deformación y sonido.

**Paso 4 — Fuerza promedio sobre el coche (impulso/tiempo).**

$$F = \frac{\Delta p}{\Delta t} = \frac{m_1 (v_f - v_1)}{\Delta t} = \frac{0.060(2.71-14)}{0.05} = -13.5\,\text{N}$$

> Magnitud 13.5 N (negativa = frenado). Eso son **23 g** de fuerza pico sobre la masa del coche. El chasis de balsa está al límite; la espuma es un buen amortiguador.

**Paso 5 — Recomendaciones.**

> Para no destrozar el coche, la barrera **debe** ser deformable: la espuma extiende $\Delta t$ y reduce $F$. Si fuera una pared rígida, $\Delta t \approx 0.005$ s y $F \approx 135$ N (~10× más): el coche se rompería.
::/practica

---

::practica{titulo="Conservación de energía — el coche F1 en una rampa con loop"}
**Problema.** En una pista con loop circular vertical (radio $R = 0.30$ m), tu coche F1 se suelta sin velocidad inicial desde una altura $h$. Se desprecia la fricción. Calcula:
1. Velocidad mínima en la cima del loop para no caer.
2. Altura mínima de soltado para que complete el loop.
3. Si lo sueltas desde $h = 1.5$ m, ¿con qué velocidad pasa por la cima del loop?

---

**Paso 1 — Velocidad mínima en la cima del loop (MCU + Newton).**

> En la cima, la fuerza centrípeta apunta hacia abajo. Si solo el peso mantiene la trayectoria circular: $mg = mv^2/R$, así
$$v_\text{cima,mín} = \sqrt{g R} = \sqrt{9.8 \times 0.30} = 1.71\,\text{m/s}$$

**Paso 2 — Altura mínima por conservación de energía.**

> Energía inicial = energía en la cima del loop (a altura $2R$):
$$mgh_\text{mín} = mg(2R) + \tfrac{1}{2} m v_\text{cima,mín}^2$$
$$h_\text{mín} = 2R + \frac{v_\text{cima,mín}^2}{2g} = 2(0.30) + \frac{(1.71)^2}{19.6} = 0.60 + 0.149 = 0.75\,\text{m}$$

> El coche debe caer al menos **0.75 m** (= 2.5 R) desde el reposo para sobrevivir el loop.

**Paso 3 — Velocidad pasando por la cima si $h = 1.5$ m.**

$$mgh = mg(2R) + \tfrac{1}{2} m v^2$$
$$v = \sqrt{2g(h - 2R)} = \sqrt{2(9.8)(1.5 - 0.60)} = \sqrt{17.64} = 4.20\,\text{m/s}$$

**Paso 4 — Verificación: ¿está por encima de $v_\text{cima,mín}$?**

> 4.20 m/s > 1.71 m/s ✓. El coche pasa el loop con holgura.

**Paso 5 — Aceleración centrípeta en la cima.**

$$a_c = v^2/R = (4.20)^2/0.30 = 58.8\,\text{m/s}^2 \approx 6\,g$$

**Paso 6 — Conclusión de diseño.**

> Diseñar la pista de soltado con $h \geq 1.0$ m garantiza un loop seguro con factor de seguridad 33 %. Pasajeros (si los hubiera) sentirían 6 g extra arriba: emoción de montaña rusa.
::/practica
