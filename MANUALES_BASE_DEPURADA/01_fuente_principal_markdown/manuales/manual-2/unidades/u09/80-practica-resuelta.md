---
unidad: 9
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Energía renovable para la flota F1 escolar

::practica{titulo="Diseña la microrred solar de tu pista F1 escolar"}
**Problema.** Tu escuela quiere instalar un sistema solar para alimentar una jornada completa de carreras F1 in Schools. Datos:

- Radiación solar promedio en CDMX: 5.4 kWh/m²·día.
- Panel disponible: 400 W pico, área 1.96 m², eficiencia 20.4 %, vida útil 25 años.
- Consumo de la jornada: 8 cargas por coche × 30 coches × 3.7 Wh por carga = 888 Wh.
- Iluminación de la pista: 5 luminarias LED × 30 W × 4 h = 600 Wh.
- Sonido de la presentación: 200 W × 3 h = 600 Wh.
- Laptop y proyector: 150 W × 4 h = 600 Wh.
- Eficiencia total del sistema (MPPT + inversor + batería + cargador): 70 %.

Calcula:

1. Consumo total de la jornada en Wh.
2. Energía solar diaria que produce un panel.
3. Número mínimo de paneles para cubrir la jornada.
4. Capacidad de batería necesaria si quieres reserva para 1 día sin sol.
5. Ahorro de CO₂ anual asumiendo que reemplazas 200 kWh de la red eléctrica nacional (CFE: 450 g CO₂/kWh).

---

**Paso 1 — Consumo total.**

$$E_{jornada} = 888 + 600 + 600 + 600 = 2\,688\,\text{Wh} \approx 2.7\,\text{kWh}$$

**Paso 2 — Producción solar por panel.**

$$E_{panel} = 5.4\,\text{kWh/m}^2 \cdot 1.96\,\text{m}^2 \cdot 0.204 = 2.16\,\text{kWh/día}$$

(Equivale a 400 W × 5.4 h pico ≈ 2 160 Wh, mismo resultado por otra vía.)

**Paso 3 — Número de paneles.**

Con eficiencia del sistema $\eta_{sis} = 0.70$:

$$E_{útil/panel} = 2.16 \times 0.70 = 1.51\,\text{kWh/día}$$

$$N_{paneles} = \lceil 2.7 / 1.51 \rceil = \lceil 1.79 \rceil = 2\,\text{paneles}$$

> **Conclusión.** Bastan 2 paneles de 400 W para cubrir una jornada completa de F1 escolar.

**Paso 4 — Capacidad de batería con 1 día de reserva.**

Si quieres operar 1 día sin sol con respaldo total:

$$E_{batería} = 2 \times 2.7 = 5.4\,\text{kWh}$$

A 12 V eso son $5400/12 = 450\,\text{Ah}$. Pero las baterías LiFePO4 no se descargan al 100 % (típicamente al 80 % máximo para preservar vida útil):

$$C_{nominal} = 450/0.80 = 562\,\text{Ah}$$

> **Solución comercial.** Banco de 6 baterías LiFePO4 de 100 Ah / 12 V (≈ $30 000-40 000 MXN total).

**Paso 5 — Ahorro de CO₂.**

200 kWh anuales × 0.45 kg CO₂/kWh = **90 kg CO₂/año** evitados.

En 25 años de vida útil: **2.25 toneladas** de CO₂ evitadas. Equivale a las emisiones de un coche compacto manejando 12 000 km, o a plantar ≈ 100 árboles maduros.

> **Conclusión integral.**
> Con $\sim 30 000$ MXN en paneles + baterías + electrónica, tu escuela cubre una flota completa de F1 escolar usando energía 100 % limpia, ahorra dinero a la red, evita 2.25 t de CO₂ y tiene un proyecto educativo permanente. El retorno de inversión típico en México es de 6-8 años, después de los cuales la energía es **prácticamente gratuita** durante 17-19 años más.

> **Verificación de orden de magnitud.** Un kWh de solar PV en México cuesta ≈ 1 MXN producir; comprado a CFE cuesta 3-5 MXN. La diferencia justifica la inversión inicial.
::/practica

---

::practica{titulo="Datación radiocarbónica — antigüedad de un fósil de la pista F1"}
**Problema.** Encuentras un trozo de carbón fosilizado bajo la pista escolar y quieres saber cuántos años tiene. Una muestra se analiza y resulta tener una actividad de C-14 igual al 6.25 % de la actividad de un trozo de madera moderno. La vida media del C-14 es $T_{1/2} = 5\,730$ años. Calcula:
1. Número de vidas medias transcurridas.
2. Edad estimada del fósil.
3. Si la incertidumbre en la actividad es ±10 %, ¿cuál es la incertidumbre de la edad?

---

**Paso 1 — Número de vidas medias.**

> $0.0625 = (1/2)^n$. Tomando logaritmo:
$$n = \log(0.0625)/\log(0.5) = -1.204/-0.301 = 4$$

> Han pasado **4 vidas medias** del C-14.

**Paso 2 — Edad.**

$$t = n \cdot T_{1/2} = 4\times 5\,730 = 22\,920\,\text{años}$$

**Paso 3 — Incertidumbre.**

> Si la actividad medida es $A = 0.0625\pm 0.00625$ (es decir 6.25 % ±10 %): el rango es 0.0563 a 0.0688. Para cada límite calculamos $n$:
> - $n_+ = \log(0.0688)/\log(0.5) = 3.86$
> - $n_- = \log(0.0563)/\log(0.5) = 4.15$

> Edades extremas: 22 100 años y 23 800 años. **Incertidumbre ±~850 años** alrededor de 22 920 años.

**Paso 4 — Conclusión.**

> El fósil bajo la pista tiene **22 900 ± 900 años**: de la última glaciación (Pleistoceno tardío). Antes de tu coche F1 había mamuts caminando por ahí. La datación por C-14 es útil hasta ~50 000 años; para edades mayores se usan otros isótopos (K-40, U-238).
::/practica

---

::practica{titulo="Aerogenerador escolar — potencia para iluminar la pista F1"}
**Problema.** Tu escuela analiza instalar un mini-aerogenerador de $D = 1.5$ m de diámetro de palas en el techo. La velocidad media del viento en el sitio es $\bar v = 5.5$ m/s. La densidad del aire es 1.20 kg/m³ y el coeficiente de potencia $C_p$ del aerogenerador es 0.35. Calcula:
1. Área barrida por las palas.
2. Potencia eólica disponible.
3. Potencia eléctrica entregada.
4. Energía generada en 24 h y comparación con el consumo de la jornada F1 (2.7 kWh).
5. Si $\bar v$ aumenta a 7.5 m/s, ¿cuánto crece la producción?

---

**Paso 1 — Área barrida.**

$$A = \pi r^2 = \pi (0.75)^2 = 1.767\,\text{m}^2$$

**Paso 2 — Potencia eólica disponible.**

$$P_\text{disp} = \tfrac{1}{2} \rho A v^3 = 0.5\times 1.20\times 1.767\times 5.5^3 = 176.4\,\text{W}$$

**Paso 3 — Potencia eléctrica.**

$$P_\text{eléc} = C_p P_\text{disp} = 0.35\times 176.4 = 61.7\,\text{W}$$

**Paso 4 — Energía en 24 h.**

> Asumiendo viento estable (idealización; en la realidad varía mucho):
$$E_\text{día} = 61.7\,\text{W}\times 24\,\text{h} = 1\,481\,\text{Wh} = 1.48\,\text{kWh}$$

> Es **55 %** del consumo de la jornada F1. Combinado con paneles solares completaría el 100 %.

**Paso 5 — A 7.5 m/s.**

> $P \propto v^3$, factor $(7.5/5.5)^3 = 2.54$.

$$P_\text{eléc, 7.5} = 61.7\times 2.54 = 156.8\,\text{W}$$

> A 7.5 m/s un solo aerogenerador cubriría toda la jornada con margen. Por eso la **velocidad del viento es CRÍTICA**: pequeñas mejoras en ubicación (techo más alto, sin obstáculos) compensan inversiones grandes en hardware.

**Paso 6 — Recomendación.**

> Antes de comprar el aerogenerador, hacer una campaña de medición de viento de 1 mes con anemómetro local para verificar la velocidad media real. Sitios con $\bar v < 4.5$ m/s no son viables económicamente; sitios con $\bar v > 6$ m/s tienen ROI < 5 años.
::/practica
