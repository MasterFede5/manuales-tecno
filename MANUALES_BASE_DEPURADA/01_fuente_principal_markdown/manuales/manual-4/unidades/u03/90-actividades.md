---
unidad: 3
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 03

::interioriza
Imagina que Artifacts es como una cocina rápida donde puedes armar platillos digitales al instante. No necesitas ser ingeniero para cocinar algo útil, solo saber dar la receta correcta.
::/interioriza

::pausa{}
**Reflexiona:** ¿Qué platillo digital (mini-app) le falta a tu equipo hoy para no pasar hambre de automatización?
::/pausa

::act-mcq{titulo="Repaso conceptual"}
1. Un Artifact NO es la mejor opción para:
   - [x] Conversación exploratoria sin entregable
   - [ ] Dashboard React interactivo
   - [ ] Documento >800 palabras editable
   - [ ] Diagrama Mermaid

2. Para una mini-app interactiva con sliders y gráficas en tiempo real, el proveedor más sólido en 2025 es:
   - [x] Claude Artifacts
   - [ ] ChatGPT Canvas
   - [ ] Gemini Canvas
   - [ ] Notion AI

3. La mejor vía para distribuir un dashboard a stakeholders externos sin login durante una demo es:
   - [ ] Deploy real en Vercel
   - [x] Link público (publish)
   - [ ] Embed iframe
   - [ ] Download HTML

4. Tu mini-app necesita persistir datos entre sesiones de varios usuarios. ¿Sigue siendo Artifact?
   - [ ] Sí, con localStorage
   - [x] No, migra a deploy real con BD
   - [ ] Sí, con cookies
   - [ ] No, descarta el proyecto

5. Versionar **solo** con las versiones internas del proveedor es:
   - [ ] Suficiente
   - [x] Frágil porque dependes del proveedor
   - [ ] Equivalente a Git
   - [ ] Imposible de hacer
::/act-mcq

::act-table{titulo="Completa la tabla — proveedor por caso de uso"}
| Caso del Asistente | Proveedor recomendado | Por qué |
|---|---|---|
| Dashboard React interactivo |  |  |
| Documento técnico largo en español |  |  |
| Reporte de investigación con citas |  |  |
| Diagrama de arquitectura Mermaid |  |  |
| Análisis Python con gráficas |  |  |
| Mockup HTML estático |  |  |
::/act-table

::act-match{titulo="Relaciona la vía de distribución con su contexto ideal"}
| Vía | Contexto ideal |
|---|---|
| 1. Link público | a) Dashboard interno embebido en Notion del equipo |
| 2. Embed iframe | b) Demo rápida en una junta sin instalación |
| 3. Download HTML | c) Producción con login institucional y datos sensibles |
| 4. Deploy real (Vercel) | d) Backup propio independiente del proveedor |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Un Artifact puede llamar a APIs externas como OpenWeather sin restricciones. ( ) ____________________________________________

2. Si tu Artifact tiene 8 versiones, las versiones 1-5 se pueden recuperar siempre. ( ) ____________________________________________

3. Gemini Canvas es la mejor opción para mini-apps React altamente interactivas. ( ) ____________________________________________

4. Es buena práctica descargar el código incluso si publicas link público. ( ) ____________________________________________

5. Un Artifact con datos personales debe publicarse solo si lo proteges con contraseña. ( ) ____________________________________________
::/act-tf

::act-order{titulo="Ordena los pasos para construir y distribuir un Artifact profesional"}
[ ] Tag semver y push del repo
[ ] Compartir URL al equipo
[ ] Primer prompt estructurado
[ ] Iteraciones pequeñas con polish final
[ ] Datos de ejemplo plausibles
[ ] Botón Publish y verificar URL
[ ] Descargar código y commit en Git
[ ] Definir tipo (React / HTML / Mermaid / etc.)
::/act-order

::albatros{titulo="Construir y publicar tu propio mini-app Artifact con versionado completo" tipo="taller" tiempo="120 min"}
**Pregunta detonadora.** 
- Si tu equipo tuviera un dashboard celular, ¿qué decisiones tomaría más rápido?

**Lo que harás.**
1. Define una mini-app real para tu institución.
   - Ejemplos: calculadora de cupos, simulador de horarios.
2. Estructura el primer prompt (subtema 3.4).
   - Propósito, componentes, datos de ejemplo, estilo.
3. Construye la mini-app en Claude Artifacts o similar.
4. Itera al menos 5 veces.
   - Mejora datos, layout, versión mobile y polish.
5. Publica como link público.
6. Descarga código y haz commit en Git.
   - Usa tag `v1.0.0` y `CHANGELOG.md`.
7. Captura snapshot desktop + mobile.
8. Recolecta feedback de 3 personas.

**Materiales.** 
- Cuenta de LLM, repo Git (GitHub gratis), 2 horas.

**Entregable.**
- URL pública del Artifact.
- Carpeta `tools/<nombre>/v1.0.0/` con código.
- Reporte de feedback (1 pp).

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Primer prompt | improvisado | estructurado | con todas las dimensiones |
| Iteraciones | 1-2 cambios | 3-4 ajustes | 5+ con polish y mobile |
| Datos | placeholders | parciales | plausibles y consistentes |
| Versionado externo | sin commit | commit | tag semver + CHANGELOG + snapshots |
| Distribución | privado | URL compartida | URL + feedback recolectado |
| Reflexión | mínima | identifica mejoras | propone v1.1.0 con criterios |
::/albatros

::act-fill{titulo="Completa el primer prompt patrón"}
Toda mini-app Artifact arranca con las 6 dimensiones del subtema 3.4:

1. _____________ — qué resuelve y para quién.
2. _____________ — piezas (cards, tabs, formularios).
3. _____________ — valores plausibles, no genéricos.
4. _____________ — paleta institucional, fuente, mood.
5. _____________ — qué hace el usuario (click, input).
6. _____________ — qué NO debe hacer (sin APIs, sin persistencia).
::/act-fill

::act-mindmap{titulo="Mapa mental de tu suite institucional" centro="SUITE ARTIFACTS ALBATROS" nodos_primarios=6 nodos_secundarios=12}
Una rama por mini-app de tu institución (real o planeada). En cada secundario: audiencia, métrica única de uso, versión actual, próximo issue, dueño funcional.
::/act-mindmap

::act-label{titulo="Etiqueta el ciclo de release de un Artifact"}
::visual{tipo="diagrama-flujo" descripcion="Diagrama de flujo del ciclo de release de un Artifact con 9 estaciones numeradas: idea, wireframe, primer prompt, iteraciones, datos plausibles, mobile, polish, publish, versionado externo. Espacio para que el alumno escriba la salida esperada de cada estación y el modo de falla más común." paginas=0.5}
> Marca: a) la estación que más estudiantes saltan y luego pagan caro · b) la estación con mayor tentación de "saltarse" cuando hay prisa · c) la estación que protege de la dependencia del proveedor · d) la estación donde aterriza por primera vez la opinión externa.
::/act-label

::act-case{titulo="Caso de diseño — eliges proveedor con números" lineas=12}
La coordinadora pide 3 piezas en una semana: 
- (1) Dashboard del Asistente.
- (2) Generador de cartas formales en español.
- (3) Análisis Python con histograma.

Tienes Claude Pro y ChatGPT Plus. 
Decide qué proveedor usar para cada pieza y justifica.
Considera: calidad, tiempo, mobile, embeddability.
::/act-case

::albatros{titulo="Reto — auditas un dashboard heredado y propones v2" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** 
- Tu institución tiene dashboards viejos (Power BI, Excel). 
- ¿Siguen contestando las preguntas de dirección hoy?

**Lo que harás.**
1. Pide acceso al dashboard ejecutivo más usado.
2. Lista 3 preguntas semanales de dirección.
3. Verifica si el dashboard las responde en <10s.
4. Identifica las 3 brechas más graves.
5. Esboza un Artifact v2 para cerrarlas.
6. Construye un prototipo v2 en Claude.
7. Comparte ambos con un stakeholder para que elija.

**Entregable.** 
- Lista de 3 preguntas + tabla de brechas.
- URL del prototipo + decisión del stakeholder.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Diagnóstico | informal | con 3 preguntas | con 3 preguntas y % de respuesta |
| Brechas | genéricas | concretas | con dato observable |
| Prototipo v2 | sketch | funcional básico | publicado y mobile |
| Decisión del stakeholder | informal | dato cualitativo | preferencia con razón explicada |
::/albatros
