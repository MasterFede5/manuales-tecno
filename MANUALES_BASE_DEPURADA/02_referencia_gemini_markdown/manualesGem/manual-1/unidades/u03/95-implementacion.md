---
unidad: 3
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — Calculadora de huella de carbono familiar"}
**Objetivo.** Construir una herramienta digital (en Google Sheets o como página web simple en HTML/JavaScript) que calcule la huella de carbono anual de una familia mexicana y proponga un plan personalizado de reducción de emisiones.

**¿Por qué hacerla?** Saber que el CO₂ es un gas de efecto invernadero es un dato. Calcular **cuánto produces tú y tu familia** lo convierte en algo accionable. La herramienta también te enseña dónde están los mayores aportes y dónde puedes hacer la mayor diferencia con el menor esfuerzo.

---

### Materiales

- Cuenta de Google (Sheets) o computadora con editor de texto.
- Datos de consumo familiar: recibos de luz CFE, recibos de gas, kilómetros recorridos en auto, hábitos alimenticios, frecuencia de vuelos.
- Tabla de factores de emisión (ver siguiente sección).

### Categorías y factores de emisión típicos para México

| Categoría | Factor | Unidad |
|---|---|---|
| Electricidad CFE (mix) | 0.42 | kg CO₂eq/kWh |
| Gas LP doméstico | 2.95 | kg CO₂eq/L |
| Gas natural | 2.0 | kg CO₂eq/m³ |
| Gasolina (auto) | 2.31 | kg CO₂eq/L |
| Diésel | 2.68 | kg CO₂eq/L |
| Vuelo doméstico | 0.21 | kg CO₂eq/km/persona |
| Vuelo internacional | 0.25 | kg CO₂eq/km/persona |
| Carne de res | 27 | kg CO₂eq/kg |
| Pollo | 6.9 | kg CO₂eq/kg |
| Lácteos | 3.2 | kg CO₂eq/kg |
| Arroz | 2.7 | kg CO₂eq/kg |
| Frutas y verduras | 0.5-1.5 | kg CO₂eq/kg |
| Residuos a relleno sanitario | 0.5 | kg CO₂eq/kg |

### Pasos

**1. Diseña la estructura de la hoja.** Crea pestañas:
- **Datos** — entradas del usuario por mes.
- **Factores** — tabla de factores (la de arriba).
- **Cálculos** — suma de cada categoría.
- **Dashboard** — gráfica de pastel + total + comparativa contra promedio nacional (3.6 t CO₂eq/persona/año).

**2. Fórmulas clave.**
```
Emisiones electricidad = SUMA(kWh) × 0.42
Emisiones transporte = SUMA(L combustible) × factor
Emisiones alimentación = SUMA(kg por categoría × factor)
TOTAL = suma de categorías
```

**3. Sistema de recomendaciones.**
- Si transporte > 30 % → sugerir transporte público, bicicleta, carpooling.
- Si alimentación animal > 30 % → sugerir un día vegetariano/semana.
- Si electricidad > 25 % → sugerir LEDs, electrodomésticos eficientes.

**4. Comparativa con promedios.**
| Nivel | t CO₂eq/persona/año |
|---|---:|
| Promedio mundial sostenible (objetivo 2050) | 2.0 |
| Promedio México 2023 | 3.6 |
| Promedio Estados Unidos 2023 | 16.5 |
| Tu familia | (calculado) |
::/implementacion

::visual{tipo="interfaz" descripcion="Captura del dashboard final de la calculadora: lado izquierdo con formulario de entrada de datos por categoría, centro con gráfica de pastel mostrando distribución de emisiones por sector (electricidad, transporte, alimentación, residuos), derecha con total anual en grandes números y comparativa contra el promedio mexicano. Recomendaciones personalizadas en lista al pie." paginas="0.5" src="../manualesGem/assets/visuales/manual-1/u03/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

URL pública de la calculadora con datos de tu propia familia capturados. Reporte de 1-2 páginas con:
1. Total de emisiones anuales.
2. Sector con mayor contribución.
3. Tres acciones concretas de reducción con su impacto esperado en kg CO₂eq.
4. Compromiso firmado por la familia.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Datos completos** | menos de 3 categorías | 5-6 categorías | todas las categorías + meses representativos |
| **Fórmulas funcionales** | errores frecuentes | cálculos correctos | con validación de entrada |
| **Visualización** | tabla simple | gráfica básica | dashboard interactivo con filtros |
| **Recomendaciones** | genéricas | personalizadas | con cuantificación de impacto |

### Reto bonus (+1 punto)

Agrega una sección que **proyecte** las emisiones de tu familia para los próximos 5 años bajo dos escenarios: "sin cambios" vs "con plan de reducción". Calcula cuántas toneladas evitarías acumulativamente.

---

### Hitos intermedios

| Sprint | Entregable | Día |
|---|---|---|
| 1 | Recolección de recibos (luz, gas, gasolina) y captura en hoja datos | 3 |
| 2 | Tabla de factores cargada y fórmulas verificadas con un mes ejemplo | 6 |
| 3 | Dashboard con gráfica de pastel y total anual estimado | 10 |
| 4 | Sistema de recomendaciones + plan firmado por la familia | 14 |

### Reto bonus extendido (+2 puntos cada uno)

1. **Reto A:** agrega una pestaña "transporte escolar" que reciba los kilómetros del autobús y calcule la huella por alumno transportado, aprovechando la práctica resuelta de la combustión del diésel.
2. **Reto B:** integra una API o link al SIMAT para que el dashboard muestre la calidad del aire local **al lado** de tu huella, contextualizando el aporte de tu familia.
3. **Reto C:** habilita un modo "comparativo familiar": cada miembro de la familia ingresa sus datos de transporte y alimentación; la app reparte la huella y muestra quién contribuye más, con metas individuales sugeridas.
::/implementacion
---

::albatros{titulo="Sprint corto — auditoría de huella del autobús escolar" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Cuál es la huella de carbono del autobús escolar de tu plantel y cómo se compara con la huella per cápita de un alumno?

**Lo que harás.**
1. Entrevista al chofer o administrador para obtener: consumo de diésel diario o semanal, número de alumnos transportados, kilometraje de ruta.
2. Aplica el factor de emisión del diésel (2.68 kg CO₂eq/L) y calcula emisiones diarias y anuales (200 días lectivos).
3. Divide entre el número de alumnos transportados para obtener la huella per cápita por transporte escolar.
4. Compara con la huella mexicana promedio (3.6 t CO₂eq/persona/año).
5. Propón **una** mejora factible (ruta optimizada, carpooling, llantas adecuadas) y estima el ahorro en kg CO₂eq/año.

**Materiales.** Cuaderno · calculadora · datos del autobús · factores de emisión.

**Entregable.** Ficha de 1 página con: datos recolectados, cálculo, comparativo y propuesta de mejora con su impacto estimado.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Recolección de datos | datos incompletos | consumo y alumnos | consumo, ruta y kilometraje verificados |
| Cálculo | error en factor | factor correcto | factor + cifras significativas + per cápita |
| Propuesta | sin estimar impacto | impacto cualitativo | impacto cuantificado en kg CO₂eq/año |
::/albatros
