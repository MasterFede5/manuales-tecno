---
unidad: 3
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 03

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
**Pregunta detonadora.** Si tu equipo tuviera un dashboard que cualquiera pudiera abrir desde su celular, ¿qué decisiones tomaría más rápido cada semana?

**Lo que harás.**
1. Define una mini-app real útil para tu institución (no genérica). Ejemplos: calculadora de cupos, simulador de horarios, generador de comunicados, quiz orientación vocacional, dashboard departamental.
2. Estructura el primer prompt con propósito, componentes, datos de ejemplo, estilo, interacciones, restricciones (subtema 3.4).
3. Construye la mini-app en Claude Artifacts (recomendado) o tu proveedor preferido.
4. Itera al menos 5 veces (datos, layout, mobile, polish, accesibilidad).
5. Publica como link público.
6. Descarga código y commitea en repo Git con tag `v1.0.0` y `CHANGELOG.md`.
7. Captura snapshot desktop + mobile.
8. Comparte el link con al menos 3 personas y recolecta feedback.

**Materiales.** Cuenta gratis o Pro de un LLM, repo Git (GitHub gratis), 2 horas.

**Entregable.**
- URL pública del Artifact.
- Carpeta `tools/<nombre>/v1.0.0/` con código + snapshots + CHANGELOG.
- Reporte de feedback (1 pp): qué dijo cada persona, qué incorporarías en v1.1.0.

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
> Marca: a) la estación que más estudiantes saltan y luego pagan caro · b) la estación con mayor tentación de "saltarse" cuando hay prisa · c) la estación que protege de la dependencia del proveedor · d) la estación donde aterriza por primera vez la opinión externa.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama de flujo del ciclo de release de un Artifact con 9 estaciones numeradas: idea, wireframe, primer prompt, iteraciones, datos plausibles, mobile, polish, publish, versionado externo. Espacio para que el alumno escriba la salida esperada de cada estación y el modo de falla más común." paginas="0.5" src="../manualesGem/assets/visuales/manual-4/u03/90-actividades-v01.svg"}
::act-case{titulo="Caso de diseño — eliges proveedor con números" lineas=12}
La coordinadora pide 3 piezas en una semana: (1) dashboard del Asistente, (2) generador de cartas formales en español neutral, (3) análisis Python de las solicitudes del último trimestre con histograma. Tienes Claude Pro y ChatGPT Plus, no Gemini Advanced. Decide qué pieza construyes en qué proveedor y justifica con tradeoffs concretos (calidad esperada, tiempo estimado, mobile, embeddability, costo de migrar después).
::/act-case

::albatros{titulo="Reto — auditas un dashboard heredado y propones v2" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Tu institución probablemente tiene un dashboard ejecutivo viejo (Power BI, Excel, Google Data Studio). ¿Sigue contestando las preguntas que dirección hace hoy?

**Lo que harás.**
1. Pide acceso al dashboard ejecutivo más usado de tu institución.
2. Lista las 3 preguntas que dirección hace cada semana.
3. Para cada pregunta, anota si el dashboard la responde en <10 s.
4. Identifica las 3 brechas más graves.
5. Esboza un Artifact v2 que las cierre.
6. Construye el v2 en Claude (no perfecto, prototipo).
7. Comparte ambos a un stakeholder y pide que elija.

**Entregable.** Lista de 3 preguntas + tabla de brechas + URL del prototipo + decisión del stakeholder.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Diagnóstico | informal | con 3 preguntas | con 3 preguntas y % de respuesta |
| Brechas | genéricas | concretas | con dato observable |
| Prototipo v2 | sketch | funcional básico | publicado y mobile |
| Decisión del stakeholder | informal | dato cualitativo | preferencia con razón explicada |
::/albatros
