---
unidad: 2
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Mide la fuerza de empuje del cartucho de CO₂

Un taller de 60 minutos donde tu equipo F1 Albatros instrumenta un banco de pruebas para medir directamente el empuje (fuerza) del cartucho de CO₂ y el coeficiente de fricción de rodamiento del coche. Aplica los subtemas 2.3 (F = ma), 2.4 (3ª Ley) y 2.6 (Hooke).

::albatros{titulo="Taller — Banco de empuje y fricción del coche F1" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** ¿De qué tamaño es realmente el empuje del cartucho de CO₂ y cuánta fuerza pierdes por la fricción de las llantas? ¿Cómo lo medirías sin un dinamómetro de laboratorio?

**Lo que harás.** Construirás un dinamómetro casero con un resorte calibrado, montarás el coche en un riel inclinable y medirás: 1) coeficiente de fricción de rodamiento $\mu_r$, 2) empuje promedio del cartucho $F_{\text{CO}_2}$, 3) verificación de la 3ª ley.

**Materiales.**
- Coche F1 escolar (puede ser un modelo de prueba sin cartucho real, simulando con bandas elásticas).
- Resorte de constante k conocida (ver 2.6) o tres bandas elásticas calibradas.
- Regla, cinta métrica, hilo resistente.
- Riel o tabla larga (mínimo 1 m) que pueda inclinarse.
- Transportador o app de inclinómetro del celular.
- Cronómetro y báscula de cocina (precisión 1 g).
- 3 cartuchos de CO₂ idénticos (o 3 sets de bandas elásticas con la misma tensión inicial).

**Pasos.**

1. **Pesa todo.** Mide masa del coche con cartucho ($m_1$) y sin cartucho descargado ($m_2$). Anota $\Delta m = m_1 - m_2$ (masa del gas expulsado).

2. **Calibra el resorte.** Cuelga 5 masas distintas (50, 100, 150, 200, 250 g), mide la elongación con regla y construye la gráfica F vs x. Calcula $k$ por regresión lineal.

3. **Mide $\mu_r$ por inclinación.** Coloca el coche en el riel y aumenta gradualmente el ángulo. Justo antes de que se mueva por sí solo, anota el ángulo $\theta_c$. Calcula $\mu_s \approx \tan\theta_c$. Después déjalo rodar y mide la aceleración midiendo tiempo en recorrer 0.8 m: $a = 2x/t^2$. De $a = g(\sin\theta - \mu_r\cos\theta)$ despeja $\mu_r$.

4. **Mide $\mu_r$ por método de tirón.** Ahora horizontal: ata un hilo del coche al resorte. Tira del resorte horizontal y registra la elongación cuando el coche se mueve a velocidad constante. $F_\text{tirón} = k \cdot x = \mu_r \cdot m_1 \cdot g$.

5. **Compara los dos $\mu_r$.** Calcula promedio y desviación.

6. **Empuje del cartucho — método A: anclaje.** Ata el coche al resorte por un hilo (el coche queda inmóvil), dispara el CO₂. Mide la elongación máxima del resorte. $F_\text{máx} = k \cdot x_\text{máx}$. Aproxima el empuje promedio como $F_\text{prom}\approx F_\text{máx}/2$ (modelo triangular).

7. **Empuje del cartucho — método B: 2ª ley.** Suelta el coche libre, mide tiempo en recorrer los primeros 2 m. Calcula $a = 2x/t^2$, después $F_\text{neta} = m_1 \cdot a$ y suma fricción: $F_\text{empuje} = F_\text{neta} + \mu_r m_1 g$.

8. **Empuje del cartucho — método C: impulso.** Pesa la masa expulsada y estima velocidad del gas (≈ 150 m/s estándar). $F\cdot \Delta t = \Delta m \cdot v_\text{gas}$.

9. **Tabla comparativa.** Crea una tabla con los tres métodos:

   | Método | $F_\text{empuje}$ medido (N) | Hipótesis principal |
   |---|---|---|
   | A — anclaje | | resorte ideal, modelo triangular |
   | B — 2ª ley | | aceleración constante en 2 m |
   | C — impulso | | $v_\text{gas}=150$ m/s |

10. **Verificación 3ª ley.** Con la masa de gas expulsado y la velocidad final del coche, calcula $\Delta p_\text{gas}$ y $\Delta p_\text{coche}$. Deberían ser similares (con signo opuesto).

11. **Discute fuentes de error.** Lista al menos 3 (resorte no ideal, fricción del riel, $v_\text{gas}$ asumida).

12. **Cierre.** Cada equipo recomienda **una** modificación específica al coche para reducir $\mu_r$ con justificación numérica.

**Entregable.** Bitácora de 1.5 páginas con: gráfica F vs x del resorte, valor de $k$, dos valores de $\mu_r$ con discusión, tres valores de $F_\text{empuje}$ con tabla comparativa, verificación de la 3ª ley, propuesta de mejora.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Calibración del resorte | sin gráfica | gráfica con 5 puntos | + regresión lineal y $R^2$ |
| Medición de $\mu_r$ | un método | dos métodos | dos métodos comparados con error |
| Empuje del CO₂ | un método | dos métodos | tres métodos con discusión |
| Verificación 3ª ley | sin verificar | $\Delta p$ similares | + análisis de discrepancia |
::/albatros
