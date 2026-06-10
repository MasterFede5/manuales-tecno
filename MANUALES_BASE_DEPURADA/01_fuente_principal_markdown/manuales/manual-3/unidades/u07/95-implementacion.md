---
unidad: 7
seccion: implementacion
paginas_objetivo: 5
---

::implementacion{titulo="Implementación Albatros — TU GPT/Gem/Project publicado con feedback de comunidad"}
**Objetivo.** Construir, publicar y operar **TU primer asistente IA propio** durante 4 semanas, recolectar feedback de mínimo 10 usuarios reales y publicar caso de estudio en redes profesionales.

**¿Por qué hacerla?** Es el momento donde dejas de "consumir IA" y la **produces**. Ese cambio de identidad —de usuario a creador— es lo que distingue al estudiante promedio del que va a destacar profesionalmente en la era IA.

---

### Materiales y herramientas

- ChatGPT Plus ($20/mes) **o** Claude Pro ($20/mes) **o** Gemini Advanced ($20/mes).
- 8-15 archivos de knowledge ya organizados.
- 1 mes de operación + 2 horas iniciales de construcción.

### Plan de 4 semanas

#### Semana 1 — Construcción (4 horas)
- Día 1: investigación de GPT Store / casos similares (1 h).
- Día 2: redactar instructions con anatomía completa (1 h).
- Día 3: organizar y subir knowledge (1 h).
- Día 4: pruebas con 10+ prompts y 2 iteraciones (1 h).
- Día 5: publicar y compartir.

#### Semana 2 — Adopción inicial
- Comparte link en WhatsApp grupos clase, LinkedIn, Twitter.
- Recolecta feedback inicial.
- 1-2 iteraciones rápidas (semana 2 día 4).

#### Semana 3 — Refinamiento
- Identifica casos edge no manejados.
- Agrega knowledge faltante.
- Refina conversation starters según uso real.

#### Semana 4 — Análisis y publicación
- Métricas: usuarios únicos, mensajes totales, feedback cualitativo.
- Reporte público en LinkedIn/blog.
- Plan v2 documentado.

::visual{tipo="ilustracion" descripcion="Dashboard del proyecto del estudiante: 1) Captura de su GPT/Project publicado con avatar y descripción. 2) Métricas a 4 semanas: 47 usuarios únicos, 230 mensajes totales, 12 feedbacks recibidos. 3) Top 3 conversation starters más usados con porcentajes. 4) Heat map de horas de uso (sábado domingo más alto). 5) Captura de post LinkedIn anunciando el GPT con 50+ likes y 8 comentarios. 6) Plan v2 con 5 mejoras a aplicar." paginas=1}

---

### Entregable

1. **Link** al GPT/Project publicado y accesible.
2. **Carta de identidad** del asistente (1-2 pp): caso, audiencia, instructions completas, knowledge, capabilities, distribución.
3. **Reporte de operación** (3 pp):
   - Métricas a 4 semanas (usuarios, mensajes, feedback).
   - Top 5 prompts más comunes.
   - 3 casos edge encontrados y cómo los resolviste.
   - Plan v2 con 5 mejoras priorizadas.
4. **Post público** en LinkedIn anunciando el GPT con resultados.
5. **Reflexión personal** (1 pp):
   - ¿Cómo cambió tu visión de la IA al construir vs solo usarla?
   - ¿Qué harías distinto la próxima vez?
   - ¿Construirías otro GPT en próximos 6 meses? ¿Cuál?

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Construcción** | < 100 palabras instructions | 200-500 palabras | 500+ con casos edge cubiertos |
| **Knowledge** | 1-3 archivos | 5-10 archivos | 10-20 organizados |
| **Pruebas iniciales** | 1-2 prompts | 5-7 | 10+ con verificación sistemática |
| **Distribución** | privado | link compartido | público con difusión activa |
| **Adopción** | < 5 usuarios | 5-15 usuarios | 20+ con engagement real |
| **Iteración** | sin iterar | 1-2 iteraciones | v2 documentada con changelog |
| **Reporte público** | sin publicar | post simple | artículo con métricas |
| **Reflexión** | superficial | identifica aprendizajes | discute identidad de creador |

### Hitos intermedios

| Sprint | Duración | Mini-entregable | Verificación |
|---|---|---|---|
| **S1 — Diseño** | 2 h | Carta de identidad + 8-15 archivos de knowledge organizados | Caso, audiencia y diferenciación clara |
| **S2 — Construcción** | 2 h | GPT/Project configurado y probado con 10 prompts | Pasa pruebas técnicas y casos edge |
| **S3 — Lanzamiento** | 4 h | Publicado + 5+ usuarios reales + post LinkedIn | Tiene engagement real |
| **S4 — Iteración v2** | 4 h | v2 con 5 mejoras priorizadas + changelog público | Métricas demostran mejora |

### Reto bonus extendido

1. **Reto del segundo GPT.** Construye un **segundo asistente** complementario al primero (ej. tutor de la materia más fácil). ¿El segundo es más rápido de construir gracias a las plantillas que dejaste?
2. **Reto cross-plataforma.** Replica tu GPT en Gemini Gem y Claude Project. Compara adopción real: ¿cuál tuvo más uso de tu audiencia?
3. **Reto de monetización piloto.** Diseña un plan para cobrar 50 pesos/mes a 10 usuarios. Calcula viabilidad y considera implicaciones éticas.
::/implementacion

---

::albatros{titulo="Caso real — el GPT que se desactivó por uso inapropiado" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Qué haces cuando descubres que alguien está usando TU GPT para algo que no era tu intención?

**Lo que harás.**
1. **Lee** la "Política de uso" oficial de OpenAI/Anthropic/Google sobre GPTs y asistentes públicos.
2. **Imagina 3 escenarios de uso indebido**: a) un compañero usa tu tutor para hacer trampa en examen; b) un desconocido usa tu GPT educativo para sacar contenido y revenderlo; c) tu knowledge incluye un dato que no debías compartir y alguien lo extrae con un prompt curioso.
3. **Diseña un protocolo de respuesta** para cada escenario: ¿qué cambias en instructions? ¿qué removes de knowledge? ¿despublicas?
4. **Implementa** una "política de uso" en las propias instructions: agrega una sección al inicio que define usos prohibidos.
5. **Documenta** el caso en un archivo `politica-de-uso.md` para tu portafolio de creador IA.

**Materiales.** Acceso a tu GPT del taller, políticas oficiales de OpenAI/Anthropic.

**Entregable.** a) Protocolo escrito de respuesta a 3 escenarios; b) sección "política de uso" agregada a tus instructions; c) reflexión: ¿quién es responsable de los usos indebidos, tú o el usuario?

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura de escenarios | 1 | 2-3 | 3+ con familia distinta |
| Protocolo | "lo bajo y ya" | con pasos | con pasos + comunicación + lecciones |
| Reflexión sobre responsabilidad | "es del usuario" | matiza | discute responsabilidad compartida |
::/albatros
