---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Asistente semanal personal

::practica{titulo="Diseña tu rutina automatizada de 1 semana"}
**Problema:**
- Tienes una semana cargada: 3 entregas, 2 reuniones, 5 clases, gym 3x.
- También debes leer un capítulo y preparar una presentación.
- Sin IA, estimas 70 horas. ¿Podemos bajarlo a 50?
 
::interioriza
Imagina que eres un director de orquesta. No tocas todos los instrumentos, sino que coordinas a los músicos (tus IAs) para que la sinfonía (tu semana) suene perfecta sin agotarte.
::/interioriza

**Día 1: Planeación y Correo**
- **7am (Motion):** Ingresas tareas (entregas, gym, lectura). Motion agenda todo automáticamente respetando tus clases.
- **8am (Gemini):** Resumen de 30 correos. Respondes 5 urgentes con "Help me write", agendas 8 y archivas 17 de spam.

**Día 1: Clases y Tesis**
- **9am (Otter):** Graba tu clase en Zoom. Solo anotas puntos clave a mano. Otter genera resumen y subes la transcripción a NotebookLM.
- **1pm (Claude Project):** Tu knowledge base ya tiene tus fuentes. Generas borrador de ensayo en 4h (en vez de 8h).

**Días siguientes: Ejecución**
- **Martes 8am (GPT for Sheets):** Clasificas 50 papers de tesis según relevancia usando una simple fórmula.
- **Miércoles (o3):** Resuelves problemas de cálculo paso a paso usando un modelo razonador.
- **Jueves (Gamma):** Creas tu presentación pegando tu esquema en Word. Genera 12 slides en 40 minutos.

**Resultados y métricas**
- **Correo:** 2.5h (vs 7h).
- **Tesis y Reuniones:** 8.5h (vs 16h).
- **Ahorro total:** 20 horas por semana.

> **Verificación profesional:** Si tu calidad baja por usar IA, lo estás haciendo mal.
> **Trampa común evitada:** No automatices todo. Conserva espacios sin IA (lectura profunda, escritura creativa) para mantener tu mente ágil.
::/practica

::pausa{}
**Deducción:** ¿Por qué usar Motion al inicio de la semana es el paso crítico para que el resto de las herramientas funcionen sin estresarte?
::/pausa

---

## Práctica resuelta — Clasificación en Sheets

::practica{titulo="Aplica =GPT() para 200 reseñas"}
**Problema:** 
- Tu jefa pide clasificar 200 reseñas en POSITIVA/NEGATIVA/NEUTRA.
- También necesita extraer el "tema principal" en 3 palabras.
- Manualmente toma 4 horas. Con IA: 8 minutos.

**Setup y Fórmula 1**
- Instala "GPT for Sheets and Docs" y pon tu API key.
- En B2 escribe: `=GPT("Clasifica esta reseña como POSITIVA, NEGATIVA o NEUTRA. Reseña: " & A2)`
- Arrastra hasta B201. (Costo: 0.04 USD, Tiempo: 2 min).

**Fórmula 2 y Entrega**
- En C2 escribe: `=GPT("Extrae tema en 3 palabras: " & A2)`
- Audita 5 filas al azar. Si están bien, el batch tiene ~95% de precisión.
- Haz tabla dinámica y entrégala a tu jefa con hallazgos clave.

::interioriza
Igual que usar una lavadora en lugar de lavar a mano: preparas la ropa (setup), pones el detergente (prompt), y dejas que la máquina haga el trabajo pesado mientras te tomas un café.
::/interioriza

**Trade-off real:**
- Pierdes 5% de precisión pero ganas 30x tiempo y repetibilidad infinita.
- Cualquier tarea repetitiva en Sheets es candidata para `=GPT()`.
::/practica

::pausa{}
**Análisis:** Si notas que la precisión del prompt baja al 80%, ¿qué pequeño ajuste harías en la fórmula antes de descartar el uso de IA?
::/pausa

---

## Práctica resuelta — Reuniones automáticas

::practica{titulo="Pipeline Otter + ChatGPT para action items"}
**Problema:**
- Tienes reuniones semanales de 1 hora con 6-10 compromisos.
- A menudo se olvidan o las notas quedan incompletas.

**Setup y Ejecución**
- Avisa al equipo sobre el uso de Otter por privacidad.
- Otter graba en background. Participas activamente y tomas pocas notas a mano.
- Al terminar, copia la transcripción completa (Ctrl+A, Ctrl+C).

**Procesamiento**
- Pega en Claude/ChatGPT pidiendo:
  - Resumen ejecutivo (3-4 oraciones).
  - Decisiones tomadas.
  - Action items (Tarea, Responsable, Deadline).
- Pega el resultado en Slack o Notion en 5 minutos.

::interioriza
Este flujo actúa como el 'actuario' de tu equipo. Ninguna decisión se pierde en el aire; todo queda firmado, sellado y entregado automáticamente tras la reunión.
::/interioriza

**Bonus inesperado:**
- Al acumular reuniones, puedes pedirle a Claude que analice qué temas se repiten sin avanzar, diagnosticando bloqueos ocultos en el equipo.
::/practica

::pausa{}
**Evaluación:** ¿Por qué es crucial el paso de "Auditoría (2 min)" antes de enviar los compromisos al Slack del equipo?
::/pausa
