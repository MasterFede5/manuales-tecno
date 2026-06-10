---
unidad: 9
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Módulo 1 del curso de orientación vocacional, producido en una sesión

> Este taller pone a tu Asistente a producir el **primer módulo completo** del curso digital de orientación vocacional del director: investigación profunda como base, secuencia didáctica de 1 sesión con rúbrica y examen, mockup de UI del módulo en herramienta UX, disclaimer legal y dataset sintético de 50 perfiles para testing. En 60 minutos sales con un módulo evaluable, navegable y verificado por humano al 20 %.

::albatros{titulo="6 productos especializados, 1 módulo completo, 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si el director te pide ahora un módulo digital de orientación vocacional con investigación, materiales pedagógicos certificables, prototipo navegable, disclaimer legal y datos para QA, ¿lo entregas hoy o lo cotizas a 6 semanas? Este taller te da la ruta de 60 minutos.

**Lo que harás (12 pasos).**

1. **Define el módulo (3 min).** Tema concreto: "Cómo elegir entre carreras del Área I (Físico-Matemáticas e Ingenierías) en bachillerato mexicano". Audiencia: 4° y 5° de bachillerato. Duración del módulo: 1 sesión de 50 min. Anota objetivo de aprendizaje (1 frase con verbo Bloom) y criterio de éxito (qué sabrá hacer el estudiante al cerrar el módulo).

2. **Deep Research base (8 min).** Lanza Deep Research (Gemini Advanced para español académico, ChatGPT DR si tu cuenta lo soporta) con la pregunta del banco bloque A: ámbito mexicano, periodo 2020-2025, fuentes preferidas (papers, SEP, OCDE, UNESCO), comparación entre bachilleratos públicos y privados, entregable de 8-15 páginas con ≥30 citas. Mientras corre, sigue al paso 3.

3. **Outline de la secuencia didáctica (4 min).** Pídele a Claude/ChatGPT que genere un outline de **una sesión de 50 min** con apertura (10 min, activación), desarrollo (30 min, contenido + actividad de pares con rúbrica visible) y cierre (10 min, metacognición + tarea). Aprendizajes alineados a Bloom (al menos 3, con verbos diferentes). Conexión con tema previo y posterior. Adaptaciones para TDAH, dislexia y talento.

4. **Rúbrica de evaluación (4 min).** Con el prompt master del subtema 9.3, genera una rúbrica de **5 criterios × 4 niveles** para el producto que entrega el estudiante (un mapa de carrera personal con 3 opciones priorizadas y argumentadas). Niveles: 1-Inicial, 2-En desarrollo, 3-Suficiente, 4-Excelente. Descriptores observables. Peso porcentual. Columna "evidencia".

5. **Examen formativo de 10 reactivos (5 min).** Distribución Bloom 40/30/20/10. Tipos: 6 opción múltiple (4 opciones, **distractores plausibles con error específico identificado**), 2 V/F justificados, 1 completar, 1 problema abierto. Pide al modelo que devuelva además: respuesta correcta + por qué cada distractor es incorrecto + nivel Bloom + tiempo estimado por reactivo.

6. **Verificación de citas del Deep Research (5 min).** Cuando vuelva el output del paso 2, abre las 5 citas que sostienen las afirmaciones más fuertes del módulo. Si alguna no se verifica, **elimínala** o reemplázala por una cita verificada. Documenta en `verificacion-citas.md` con tabla: cita / URL / verificada sí-no / acción tomada.

7. **Mockup UX del módulo (8 min).** Elige herramienta según objetivo: **Galileo AI** si solo presentarás a fundadores (mockup pulido), **v0.dev** si quieres componente React real, **Lovable** o **Bolt.new** si quieres prototipo navegable con backend ligero. Genera 3 variantes del mockup principal (pantalla con quiz vocacional + visualización de resultados + CTA "agenda sesión con tutor"). Elige 1 con tu reflexión de stakeholder. Documenta link o screenshot.

8. **Disclaimer legal del módulo (3 min).** El módulo recolecta respuestas del quiz (datos personales). Redacta con IA un **disclaimer corto** que declare: a) qué datos se recolectan, b) finalidad (orientación vocacional, no toma de decisión automatizada), c) derechos ARCO, d) contacto del responsable, e) leyenda "asistido por IA, validado por [nombre del abogado, cédula]" — pendiente de revisión legal real. Marca explícito en el repo: `[BLOQUEO: requiere validación de abogado especializado en privacidad antes de publicar]`.

9. **Dataset sintético para QA (5 min).** Genera **50 perfiles sintéticos** de estudiantes que el módulo va a recibir: nombre mexicano realista, género balanceado, promedio (distribución normal media 8.5 desv 0.8), materia favorita (variada), respuestas al quiz (3 patrones esperados: clarito hacia ingeniería, indeciso, clarito hacia ciencias básicas). Cada fila con `is_synthetic: true`. Output JSONL.

10. **Auditoría de sesgos del módulo (3 min).** Pídele al modelo: *"Critica este módulo como evaluador adversarial: ¿qué grupo, perspectiva o dato está sub-representado en lo que generaste?"*. Anota hallazgos. Aplica al menos una mitigación (diversificar ejemplos de carrera, balancear género en testimonios, incluir perfil socioeconómico variado).

11. **Validación humana 20 % (5 min).** Lista las 5 piezas que requieren ojo humano antes de publicar el módulo: a) experto pedagógico revisa secuencia + rúbrica, b) docente del área revisa examen y distractores, c) abogado revisa disclaimer, d) UX/UI ajusta accesibilidad WCAG en mockup, e) coordinador valida ejemplos institucionales. Asigna nombre y plazo a cada validación (no abstracto, persona concreta).

12. **Empaqueta y entrega (2 min).** Crea carpeta `modulo-1-orientacion-vocacional/` con todos los entregables (deep-research, secuencia, rúbrica, examen, mockup, disclaimer, dataset, auditoría, validación). Anexa `README.md` con: objetivo, duración, qué hizo IA (80 %), qué validación humana queda pendiente (20 %), responsables y plazos. Demo de 2 min navegando el mockup y mostrando los archivos.

**Materiales.**
- Cuenta de Deep Research activa (Gemini Advanced, ChatGPT Plus/Team o Perplexity Pro).
- Claude/ChatGPT para redacción de materiales y prompts master del subtema 9.3.
- Herramienta UX a elegir: Galileo AI, Uizard, v0.dev, Lovable o Bolt.new.
- Editor Markdown (VS Code) y editor JSONL ligero para el dataset.
- Plantilla institucional de aviso de privacidad (LFPDPPP) si existe.
- Lista de contactos: experto pedagógico, docente del área, abogado de privacidad, UX/UI, coordinador.

**Entregable.**
1. **`reporte-deep-research.md`** — output Deep Research con `verificacion-citas.md` adjunto (5 citas críticas verificadas, status documentado).
2. **`secuencia-didactica.md`** — sesión de 50 min con apertura/desarrollo/cierre, aprendizajes Bloom, materiales y adaptaciones para diversidad.
3. **`rubrica-mapa-carrera.md`** — 5 criterios × 4 niveles + peso porcentual + evidencia.
4. **`examen-formativo.md`** — 10 reactivos con distribución Bloom 40/30/20/10, distractores plausibles documentados.
5. **`mockup-modulo.fig` / link** — mockup UX con 3 variantes y la elegida marcada.
6. **`disclaimer-modulo.md`** — disclaimer corto con declaración LFPDPPP y bloque `[BLOQUEO: requiere validación de abogado]`.
7. **`perfiles-sinteticos.jsonl`** — 50 perfiles sintéticos con `is_synthetic: true`.
8. **`auditoria-sesgos.md`** — crítica adversarial + mitigación aplicada.
9. **`validacion-humana.md`** — tabla con 5 validaciones, responsable y plazo.
10. **`README.md`** del módulo + demo de 2 min navegando.

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Investigación profunda | sin Deep Research | DR ejecutado, citas no verificadas | DR + 5 citas críticas verificadas + tabla de status |
| Secuencia + rúbrica | una sin la otra | ambas presentes | ambas + adaptaciones de diversidad + alineadas a Bloom |
| Examen | reactivos sin distractores específicos | distractores genéricos | distractores con error específico identificado + Bloom |
| Mockup UX | imagen sin elección | 3 variantes sin elegir | 3 variantes + elegida + accesibilidad considerada |
| Disclaimer + dataset | uno de los dos | ambos | ambos + bloque de validación legal + sintético etiquetado |
| Validación humana | sin asignar | personas mencionadas | 5 validaciones con responsable y plazo concreto |
| Demo y empaque | sin demo | carpeta sin README | demo de 2 min + README claro con 80/20 IA-humano |

**Tip Albatros.** El número que debes presentar al director **no es** "el módulo está listo": es **"el módulo está al 80 % por IA y tengo plazo concreto para el 20 % humano"**. Esa transparencia es lo que convierte producción asistida en producción confiable. Las instituciones que esconden el 20 % humano fallan en producción; las que lo hacen explícito sostienen el ritmo y la calidad. Tu credibilidad escala con la disciplina, no con la velocidad.
::/albatros
