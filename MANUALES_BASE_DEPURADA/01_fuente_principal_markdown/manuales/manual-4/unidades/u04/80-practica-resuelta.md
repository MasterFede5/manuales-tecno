---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 04

::practica{titulo="Construir el 'Consultor del Reglamento' del Asistente Institucional con NotebookLM + Claude Project en 2 horas"}
**Problema:** Necesitas que el Asistente responda consultas del reglamento académico.
- Debe citar la página exacta y responder en español.
- Debe ser gratis y ofrecer audio para padres.
- Tiempo objetivo: 2 horas hasta producción.

**Paso 1 — Datos disponibles:**
- 5 PDFs (reglamento, calendario, manual docente, admisiones, ética).
- Herramientas: NotebookLM (gratis, citas, audio) y Claude Pro (razonamiento).

**Paso 2 — Estrategia:**
1. Limpiar PDFs.
2. Subir a NotebookLM y configurar guía.
3. Crear Claude Project en paralelo para casos complejos.
4. Validar con *golden set* de 8 preguntas reales.
5. Distribuir y documentar.

**Paso 3 — Limpieza (15 min):**
- Verifico texto seleccionable.
- OCRmyPDF para el reglamento escaneado.
- Renombro con convención (e.g., `reglamento_v3.pdf`).

**Paso 4 — NotebookLM (20 min):**
- Creo notebook y subo los 5 PDFs.
- Pruebo consulta y verifico cita clickable.
- Configuro instrucciones (tono, no inventar, etc.).

**Paso 5 — Claude Project (20 min):**
- Creo Project y subo los 5 PDFs.
- Configuro instrucciones y política de no-respuesta.
- Pruebo preguntas y ajusto.

**Paso 6 — Golden set (30 min):**
Pruebo 8 preguntas históricas:
- **Directas:** ✓ Ambos con cita.
- **Combinadas:** ✓ Ambos.
- **No explícitas:** NotebookLM falla, Claude ✓.
- **Fuera de docs:** Ambos dicen "no tengo info" ✓.
- **Trampa:** NotebookLM alucina, Claude maneja bien.

**Paso 7 — Análisis y decisiones:**
- Agregar sinónimos a NotebookLM.
- Enrutar casos sensibles a Claude Project.
- Costo final: $0 extra.

**Paso 8 — Distribución (15 min):**
- Link de NotebookLM a coordinación.
- Audio Overview generado para onboarding.
- Project compartido con staff.

**Respuesta:** Dos sistemas activos en 2 horas. 
NotebookLM atiende consultas rápidas, Claude atiende casos complejos.

::interioriza
**Baja la curva:** Imagina que NotebookLM es el recepcionista veloz que conoce el manual de memoria. Claude Project es el abogado del staff que conecta los puntos difíciles cuando el manual es ambiguo.
::

::pausa{}
**Deducción lógica:**
¿Por qué usar un *golden set* en lugar de preguntas sueltas?
- **Respuesta:** Porque necesitas validar los límites (preguntas fuera de contexto). Si no, descubrirás la alucinación en producción frente a un usuario real.
::
::/practica

::practica{titulo="Cómo diagnostiqué una alucinación grave del RAG y la mitigué en una tarde"}
**Problema:** Una mamá recibe respuesta de NotebookLM citando un artículo inexistente sobre reincorporación.
- La mamá ya hizo capturas.
- Tienes la tarde para diagnosticar.

**Paso 1 — Reproducir el fallo:**
- Lanzo la misma pregunta al Notebook.
- El modelo alucina de nuevo. ¡Reproducido!

**Paso 2 — Examinar el chunk:**
- Clic en la cita lleva a otro artículo irrelevante.
- El chunk recuperado no tiene la respuesta.

**Paso 3 — Hipótesis:**
- (a) Info no existe.
- (b) Mal chunking.
- (c) El modelo ignoró la instrucción.

**Paso 4 — Búsqueda manual:**
- Ctrl+F en los PDFs. 
- Conclusión: Info no existe. El modelo ignoró la regla.

**Paso 5 — Endurecer instrucciones:**
- Instrucción antigua: *"di 'no tengo información'"*.
- Instrucción nueva: *"Identifica la frase textual. Si no puedes, responde EXACTAMENTE: 'No encuentro información...'. No menciones artículos inexistentes."*

**Paso 6 y 7 — Re-test y Regression suite:**
- La pregunta original ahora arroja "no tengo info". ✓
- Variantes arrojan citas o negativas correctas. ✓

**Paso 8 — Plan preventivo:**
- La alucinación reveló una brecha institucional.
- Se levanta un ticket legal para crear el protocolo faltante.

**Respuesta:** Mitigación en 4 horas. Instrucciones mejoradas.

::interioriza
**Baja la curva:** Una alucinación no es un "virus". Es el tablero del auto encendiendo la luz de *Check Engine*. O tienes mal el aceite (instrucciones) o falta una pieza (brecha documental).
::

::pausa{}
**Deducción lógica:**
¿Qué habría pasado si solo le dijeras al modelo "no mientas" sin revisar los chunks?
- **Respuesta:** No habrías descubierto que la información realmente faltaba en el reglamento. El modelo seguiría fallando ante nuevos casos.
::
::/practica

::practica{titulo="Cómo decidí entre NotebookLM, Custom GPT y Dify para 3 casos del mismo trimestre"}
**Problema:** Necesitas 3 RAGs: 
1. (A) Chatbot web público para padres.
2. (B) Asistente interno para staff.
3. (C) Endpoint API para workflow.

**Paso 1 — Requisitos:**
- **Caso A:** Gratis, citas, no login.
- **Caso B:** Privacidad, razonamiento profundo.
- **Caso C:** API nativa, <5s de latencia.

**Paso 2 — Mapear herramientas:**
- **NotebookLM:** Citas geniales, sin API.
- **Claude Projects:** Gran razonamiento, sin API.
- **Custom GPT:** Embebible en web.
- **Dify:** API nativa, open-source.

**Paso 3 — Decisión final:**
- **Caso A:** Custom GPT embebido en iframe.
- **Caso B:** Claude Project (plan Team).
- **Caso C:** Dify self-hosted + Cohere multilingual.

**Paso 4 y 5 — Setup paralelo:**
- Configuración y despliegue rápido.
- Validación con stakeholders.

**Paso 6 — Golden cruzado:**
- 12 preguntas en los 3 sistemas.
- Dify domina latencia, Claude domina complejidad.

**Respuesta:** 3 sistemas RAG operativos en 3 días.
Costo: ~$150 mensual total.

::interioriza
**Baja la curva:** Buscar "el mejor RAG" es como buscar "el mejor zapato". Si vas a correr, usas tenis (Dify); si vas a la nieve, botas (Claude); si estás en casa, pantuflas (NotebookLM).
::

::pausa{}
**Deducción lógica:**
¿Por qué se eligió Cohere multilingual para Dify en lugar de OpenAI?
- **Respuesta:** Porque los documentos contenían frases en lenguas locales (náhuatl) y español. Los embeddings de OpenAI degradan su calidad en búsquedas multilingües.
::
::/practica
