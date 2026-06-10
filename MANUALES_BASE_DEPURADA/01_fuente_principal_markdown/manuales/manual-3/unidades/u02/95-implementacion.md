---
unidad: 2
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Tabla comparativa pública de las 4 plataformas y elección documentada"}
**Objetivo.** Construir una tabla comparativa **propia, original y publicada** sobre ChatGPT, Claude, Gemini y Copilot, basada en tus pruebas directas (no en reseñas de terceros). El producto final será un recurso reutilizable que tú y tu comunidad pueden consultar.

**¿Por qué hacerla?** Hay miles de comparativas en internet, pero pocas en español, casi ninguna desde la perspectiva de un estudiante de bachillerato/universidad mexicano. Producir tu propia tabla te obliga a tomar postura y entregas un recurso útil para tu comunidad.

---

### Materiales y herramientas

- Cuentas gratuitas en las 4 plataformas (claude.ai, chatgpt.com, gemini.google.com, copilot.microsoft.com).
- Notion, Airtable, Google Sheets o Excel para la tabla.
- Canva o Genially para diseñar el render visual.
- 3 horas en 2 sesiones.

### Pasos

1. **Diseña 5 prompts de prueba** que cubran diversos casos de uso:
   - Uno académico (resumen de tema escolar).
   - Uno creativo (escribir un cuento corto).
   - Uno técnico (explicar Bernoulli con ejemplo numérico).
   - Uno conversacional (planeación de estudio para examen).
   - Uno multimodal o con archivo (subir un PDF y resumirlo).
2. **Aplica los 5 prompts en las 4 plataformas** (20 ejecuciones totales). Captura tiempos y respuestas.
3. **Define una rúbrica de 8 criterios** y califica cada respuesta de 1 a 5:
   - Claridad. Precisión. Tono adecuado. Estructura. Profundidad. Originalidad. Velocidad. Funciones extras usadas.
4. **Construye la tabla** comparativa en Notion/Airtable/Sheets con: criterio × plataforma × scoring × notas.
5. **Genera la versión visual** en Canva: infografía A3 con la tabla resumen + ranking final.
6. **Escribe la decisión.** 200-300 palabras explicando cuál elegiste como base de tu tutor virtual y por qué.
7. **Publica.** Sube a LinkedIn, Twitter o blog con hashtags #IA #ChatGPT #Claude #Gemini #Copilot.
8. **Recolecta retroalimentación.** Responde comentarios y agrega errata en la tabla.

::visual{tipo="ilustracion" descripcion="Captura de la tabla comparativa final del estudiante en Notion: 8 filas de criterios × 4 columnas de plataformas, con score 1-5 en cada celda, score total destacado al final, y notas cualitativas debajo. Al lado: render en Canva A3 con misma tabla en versión visual atractiva con logos de cada plataforma. En la esquina, captura del post LinkedIn donde se publicó." paginas=0.5}

---

### Entregable

1. **Link a la tabla pública** (Notion / Airtable / Google Sheets compartida en modo lectura).
2. **PDF/PNG** de la versión visual final (Canva).
3. **Captura del post** publicado en LinkedIn/Twitter con métricas a 1 semana.
4. **Decisión escrita** de 1 página: cuál elegiste, los 3 criterios decisivos, qué función vas a usar más y qué te preocupa de tu elección.
5. **Reflexión.** ¿Cambiaría tu elección si tuvieras presupuesto cero? ¿Si fuera para tu trabajo de oficina vs estudio? ¿Si tu privacidad fuera lo más importante?

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Cobertura de prompts** | 2-3 prompts | 4-5 prompts | 5+ con variedad de casos |
| **Rigor de la tabla** | scoring impresionista | rúbrica explícita | rúbrica documentada y aplicada uniformemente |
| **Diseño visual** | tabla simple | render legible | infografía atractiva compartible |
| **Decisión escrita** | "me gustó X" | argumenta 1-2 razones | argumenta con criterios + contraejemplos |
| **Publicación** | privada | enlace público | publicada con engagement |
| **Reflexión** | una sola perspectiva | considera 2 perspectivas | discute trade-offs honestamente |

### Hitos intermedios

| Sprint | Duración | Mini-entregable | Verificación |
|---|---|---|---|
| **S1 — Diseño de prompts** | 30 min | 5 prompts redactados en hoja de cálculo con criterio que prueban | Compartir con un compañero que cuestione si cubren los 5 casos |
| **S2 — Ejecución** | 60 min | 20 capturas de pantalla (5 prompts × 4 plataformas) | Al menos una captura por celda; tiempos anotados |
| **S3 — Calificación** | 30 min | Tabla con scores 1-5 en 8 criterios × 4 plataformas + notas | Auto-revisión: ¿usaste la misma rúbrica para todas? |
| **S4 — Publicación** | 30 min | Tabla pública + render visual + post LinkedIn | Link funcional + screenshot del post |

### Reto bonus extendido

1. **Reto longitudinal.** Repite el experimento **2 meses después** con los mismos prompts. ¿Cambió el ranking? Documenta cómo evolucionan las plataformas y publica un "v2" de tu tabla.
2. **Reto del prompt difícil.** Diseña **un sexto prompt diabólico** que ataque las debilidades del modelo que elegiste como base. Si tu base lo sobrevive, valida tu decisión; si no, considera replantear.
3. **Reto de costos.** Agrega una columna de **costo real por mes** considerando que vas a usar la plataforma 2 horas diarias durante un semestre. Compara con el costo de una tutoría humana equivalente. Saca conclusiones.
::/implementacion

---

::albatros{titulo="Caso real — diseña tu primera memoria persistente" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ChatGPT y Claude tienen "memoria" ahora. ¿Qué información debe **recordar** tu tutor de ti, y cuál es mejor que olvide cada chat?

**Lo que harás.**
1. **Lista 15 datos posibles** que tu tutor podría memorizar de ti (nivel, materias, gustos, errores típicos, estilo de aprendizaje, etc.).
2. **Clasifícalos en 3 columnas:** RECORDAR siempre · RECORDAR a veces · NUNCA recordar (datos sensibles, opiniones políticas, datos médicos, contraseñas).
3. **Configura la memoria** en ChatGPT (Settings → Personalization → Memory) o Claude (Settings → Profile preferences) con los 5 datos más útiles.
4. **Prueba la memoria:** abre un chat nuevo y haz una pregunta donde el modelo deba aplicar lo memorizado sin que se lo digas.
5. **Audita la memoria** después de 1 semana: ¿guardó algo que NO querías? Ve al panel de "Saved memories" y borra lo inadecuado.

**Materiales.** Acceso a ChatGPT Plus o Claude Pro con memoria activada. Cuaderno para tu lista.

**Entregable.** Tabla de 3 columnas con los 15 datos clasificados + captura del panel de memoria configurado + reflexión: ¿qué memoria te incomoda? ¿por qué?

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Clasificación | < 10 datos | 15 datos | 15 datos con criterio articulado |
| Configuración | sin memoria | 3 datos | 5 datos útiles + auditoría |
| Reflexión sobre privacidad | superficial | menciona riesgos | discute trade-offs específicos |
::/albatros
