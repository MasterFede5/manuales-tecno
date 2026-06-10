---
unidad: 2
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Diseño y prueba de catapulta optimizada (CAD + ensayo)"}
**Objetivo.** Diseñar y construir una catapulta que lance una bola de 20 g a la mayor distancia posible usando un resorte calibrado. Aplicar leyes de Newton, Hooke, conservación de energía y tiro parabólico para predecir la distancia teórica antes de probar, y comparar con el resultado real.

**¿Por qué hacerla?** Esta implementación integra los 8 subtemas de la unidad: vectores, F=ma, par acción-reacción (resorte vs. brazo), torca (rotación del brazo de la catapulta), Hooke (energía del resorte), gravitación (peso de la bola). Es física aplicada en miniatura.

---

### Materiales

- Madera o cartón rígido para la base.
- Brazo de palanca: una regla o trozo de madera.
- Resorte de constante conocida ($k$ a determinar).
- Cuchara plástica o copa para alojar la bola.
- Bola pequeña (canica de 20 g, pelota de ping-pong).
- Cinta métrica.
- Cronómetro o app de cámara lenta.

### Pasos

**1. Calibra el resorte.** Mide $k$ colgando masas de 20-100 g y midiendo elongación.

**2. Diseña en papel (o CAD).** Define:
   - Longitud del brazo de palanca.
   - Punto de pivote.
   - Punto de aplicación del resorte.
   - Ángulo de lanzamiento (idealmente 45° para máximo alcance).

**3. Calcula la energía y velocidad teórica.**
   - Energía elástica: $U_e = \tfrac{1}{2}k x^2$ con la compresión esperada.
   - Suponiendo eficiencia de transferencia ~50 % (real es 30-60 %):
     $E_k = \tfrac{1}{2}m v^2 \Rightarrow v_0 = \sqrt{2 E_k / m}$.
   - Distancia teórica con tiro parabólico (ángulo 45°): $R = v_0^2/g$.

**4. Construye la catapulta.** Usa los materiales para realizar el diseño.

**5. Realiza 5 lanzamientos.** Mide la distancia de cada uno.

**6. Compara teórico vs. real.** Calcula el error porcentual e identifica fuentes (fricción del eje, resistencia del aire, ángulo no perfecto, transferencia de energía no ideal).

**7. Optimiza.** Cambia 1-2 variables (ángulo, compresión del resorte, masa de la bola) y prueba si el alcance mejora.

::visual{tipo="ilustracion" descripcion="Diagrama esquemático de la catapulta: base estable, brazo de palanca con pivote en un extremo y resorte conectado en el otro, copa para la bola en la punta del brazo. Vectores de fuerzas dibujados: tensión del resorte (en su línea de acción), peso de la bola, normal en el pivote. Anexo con trayectoria parabólica esperada y datos típicos: ángulo 45°, alcance esperado 2-5 m." paginas=0.5}

---

### Entregable

Documento de 2-4 páginas con:
1. Diseño en papel o CAD.
2. Calibración del resorte (gráfica F vs x).
3. Cálculos teóricos del alcance.
4. Datos de 5 lanzamientos.
5. Comparación teórico vs real con error porcentual.
6. 2 mejoras propuestas con justificación física.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Diseño** | esbozo simple | dibujo con dimensiones | CAD o dibujo a escala |
| **Calibración** | sin medir k | k medido | k con incertidumbre |
| **Cálculos** | sin teoría | predice alcance | considera eficiencia con justificación |
| **Lanzamientos** | <3 | 5 con distancias | 5+ con análisis estadístico |
| **Optimización** | sin probar | una variable cambiada | dos variables con análisis comparativo |

### Reto bonus (+1 punto)

Filma con cámara lenta y usa Tracker (U1) para medir la velocidad real de salida de la bola. Compara con el cálculo teórico y discute si la suposición de "50 % de eficiencia" fue realista.

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Calibración | 1 | $k$ del resorte determinado con 5 pesas y regresión | gráfica F vs x con $R^2$ |
| 2. Diseño y CAD | 2 | Dibujo a escala con cotas y diagrama de cuerpo libre | plano A4 |
| 3. Construcción y predicción | 3 | Catapulta operativa + alcance teórico calculado | foto + cálculo |
| 4. Pruebas y optimización | 4 | 5 lanzamientos, comparación, una mejora aplicada | bitácora 3 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Curva de eficiencia.** Varía la compresión del resorte en 5 valores (2, 3, 4, 5, 6 cm) y mide alcance real. Calcula la eficiencia $\eta = E_k/E_e$ para cada compresión y grafícala. ¿Es constante o cambia? Explica.
2. **Optimización del ángulo.** Construye un mecanismo que permita lanzar a 30°, 45° y 60°. Mide alcance en cada uno (con la misma compresión). Verifica si el máximo está en 45° y discute la desviación.
3. **Tres masas.** Usa proyectiles de 10 g, 20 g y 40 g. Predice y mide alcance. Verifica la tendencia $R \propto 1/m$ que predice el modelo simple de transferencia de energía.
::/implementacion

---

::albatros{titulo="Reto Albatros — diagnóstico de equilibrio del chasis" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** ¿Cómo cambia el reparto de peso entre las ruedas delanteras y traseras de tu coche F1 cuando agregas 10 g de plomo en la nariz?

**Lo que harás.**
1. Coloca el coche F1 sobre dos básculas pequeñas (una bajo cada eje) o sobre dos vasos invertidos pegados a una báscula con tara.
2. Anota $N_1$ (delantera) y $N_2$ (trasera). Verifica $N_1 + N_2 = mg$.
3. Calcula la posición del centro de masa $d$ tomando torcas: $d = (N_2 \cdot L)/(N_1+N_2)$, con $L$ = distancia entre ejes.
4. Repite tras agregar 10 g de plastilina en la nariz. Compara $d$ y reparto.
5. Predice si el coche tenderá a hacer caballito al disparar (usa el resultado del Paso 6 de la práctica resuelta de equilibrio).

**Entregable.** Tabla con cinco columnas (config., $N_1$, $N_2$, $d$, predicción caballito sí/no) para tres configuraciones de masa y discusión de media página.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Mediciones | 1 configuración | 3 configuraciones | + verificación $N_1+N_2=mg$ |
| Cálculo de $d$ | sin fórmula | con valor | + cifras significativas |
| Predicción caballito | cualitativa | cuantitativa | con valor de empuje crítico |
::/albatros
