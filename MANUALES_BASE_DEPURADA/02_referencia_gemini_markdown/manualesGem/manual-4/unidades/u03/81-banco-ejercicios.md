---
unidad: 3
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 03

> Trabajas con Claude.ai abierto y un editor markdown a la mano. Cada ejercicio puede pedir que **publiques un Artifact real** (gratis o demo).

### Sección A — Concepto y tipos de Artifacts (3.1)

::act-mcq{titulo="A1. ¿Artifact o no Artifact?"}
1. Necesitas que el director vea **una vez** el reporte trimestral en su iPad. Sin login.
   - [x] Artifact (link público)
   - [ ] App nativa
   - [ ] PDF en correo
   - [ ] Página web propia

2. La coordinadora necesita que **3 administrativos editen** la misma calculadora de cupos durante el día.
   - [ ] Artifact link público
   - [ ] Artifact embebido
   - [x] App con backend (no Artifact)
   - [ ] Hoja Excel compartida

3. Quieres documentar la arquitectura del Asistente con un **diagrama** que cualquiera pueda copiar.
   - [ ] React Artifact
   - [x] Mermaid Artifact
   - [ ] HTML estático
   - [ ] Imagen PNG

4. Tu novia te pide ayuda con su **playlist musical**: una mini-app que clasifica canciones por mood. Una sola vez.
   - [x] Artifact React (perfecto para prototipo)
   - [ ] App en App Store
   - [ ] Spotify clon
   - [ ] PDF
::/act-mcq

::act-tf{titulo="A2. Mitos sobre Artifacts"}
1. Un Artifact React puede llamar a APIs externas como OpenWeather sin ninguna restricción. ( ) ____________________________________________
2. Si necesitas persistencia entre sesiones de varios usuarios, Artifact sigue siendo el camino. ( ) ____________________________________________
3. Los Artifacts publicados son indexados por Google igual que cualquier web. ( ) ____________________________________________
4. Las versiones internas del proveedor (v1, v2, v3) son equivalentes a un repo Git. ( ) ____________________________________________
::/act-tf

### Sección B — Plataforma correcta (3.2 y 3.3)

::act-match{titulo="B1. Caso de uso → proveedor recomendado"}
| Caso | Proveedor recomendado |
|---|---|
| 1. Dashboard React con sliders en vivo | a) Gemini Canvas |
| 2. Documento técnico largo en español | b) Claude Artifacts |
| 3. Análisis Python con gráficos matplotlib | c) ChatGPT Canvas |
| 4. Ecosistema Workspace (Docs, Sheets) | d) ChatGPT Canvas con Code Interpreter |
::/act-match

::act-table{titulo="B2. Comparativa de proveedores en 2025"}
Completa la tabla con tu **percepción operativa actual** (no es absoluta — actualízala cuando los productos evolucionen):

| Característica | Claude Artifacts | ChatGPT Canvas | Gemini Canvas |
|---|---|---|---|
| Mejor en React |  |  |  |
| Mejor en docs largos |  |  |  |
| Mejor en código Python |  |  |  |
| Link público nativo |  |  |  |
| Mobile responsive default |  |  |  |
| Integración Workspace |  |  |  |
::/act-table

### Sección C — Primer prompt estructurado (3.4)

::act-fill{titulo="C1. Las 6 dimensiones del primer prompt"}
Un primer prompt para Artifact debe llevar:

1. _____________ — qué resuelve la mini-app y para quién.
2. _____________ — qué piezas tiene (cards, tabs, formulario, etc.).
3. _____________ de ejemplo — datos plausibles, no genéricos.
4. _____________ — paleta, fuente, mood (formal, divertido, institucional).
5. _____________ — qué hace el usuario (click, drag, input).
6. _____________ — qué NO debe hacer (no APIs externas, no persistir, etc.).
::/act-fill

::act-case{titulo="C2. Caso — escribe el primer prompt para 'calculadora de cupos'" lineas=15}
Tu institución tiene 12 grupos de bachillerato con cupos limitados. La coordinadora pierde 30 min cada mañana actualizando una hoja Excel mental. Necesitas un Artifact que: (1) muestre los 12 grupos en cards, (2) cada card con cupo total, ocupados y disponibles, (3) un botón "+1 inscrito" y "-1 baja", (4) un total general arriba, (5) alerta visual cuando un grupo queda con menos de 3 cupos. Datos del Asistente: el director firmó política de "cupos visibles a todos". Escribe el primer prompt completo (las 6 dimensiones).
::/act-case

### Sección D — Iteración y polish (3.4 cont.)

::act-order{titulo="D1. Orden de iteración recomendado"}
Tras el primer prompt, ¿en qué orden iteras?

[ ] Polish (accesibilidad ARIA, contraste, espaciado)
[ ] Mobile responsive
[ ] Datos plausibles
[ ] Layout (orden visual y jerarquía)
[ ] Microinteracciones (transiciones, feedback)
[ ] Paleta institucional
::/act-order

::act-mcq{titulo="D2. Iteración correcta"}
1. Tras 8 iteraciones tu Artifact se ve **peor** que en la 5. ¿Qué haces?
   - [ ] Sigues iterando con prompts más específicos
   - [x] Vuelves a la versión v5 desde el historial y haces nuevos prompts desde ahí
   - [ ] Empiezas desde cero
   - [ ] Pides al modelo "haz que se vea bien"

2. Tu Artifact funciona en desktop pero en móvil las cards se cortan. El prompt correcto:
   - [ ] "Hazlo responsive"
   - [x] "En pantallas <768px, las cards se apilan en columna; padding horizontal 16px; fuente cuerpo 14px"
   - [ ] "Arregla el mobile"
   - [ ] "Que se vea bien en celular"
::/act-mcq

### Sección E — Distribución y versionado (3.5 y 3.6)

::act-order{titulo="E1. Pipeline completo de release"}
[ ] Botón Publish y captura URL
[ ] Compartir URL al canal del equipo
[ ] Probar en navegador incógnito desde móvil
[ ] Descargar código (Copy)
[ ] Commit en repo + tag semver
[ ] Snapshot desktop + mobile
[ ] Actualizar CHANGELOG
::/act-order

::act-tf{titulo="E2. Versionado externo"}
1. Si publicas el link, no necesitas guardar el código en Git. ( ) ____________________________________________
2. Tomar snapshots PNG es opcional cuando ya tienes el código. ( ) ____________________________________________
3. Cambios menores (typo, paleta) merecen un nuevo tag semver. ( ) ____________________________________________
4. El CHANGELOG debe incluir tanto features como decisiones rechazadas. ( ) ____________________________________________
::/act-tf

### Sección F — Caso integrador

::act-case{titulo="F1. Caso — eliges arquitectura para el ecosistema" lineas=12}
Tu suite institucional está creciendo: dashboard, calculadora cupos, generador comunicados, simulador de horarios, quiz vocacional, pre-inscripción. Son 6 Artifacts. La coordinadora pregunta: *"¿podemos tenerlos todos en un mismo lugar para que la gente no ande perdiendo links?"*. Diseña tu solución: ¿un hub Artifact?, ¿una página Notion?, ¿una landing en Vercel?, ¿una app real? Justifica con costo (tiempo y dinero) y riesgo.
::/act-case

::act-mindmap{titulo="F2. Tu suite institucional v1" centro="SUITE ALBATROS v1.0" nodos_primarios=6 nodos_secundarios=12}
Cada rama es una mini-app. Para cada mini-app: nombre, audiencia, métrica única de uso, versión actual, último cambio, próximo issue.
::/act-mindmap

---

## Clave de respuestas

**A1.** 1-a · 2-c · 3-b · 4-a.

**A2.** 1) Falso — Artifacts tienen sandbox; las llamadas a APIs externas suelen estar restringidas o requerir CORS específico. 2) Falso — sin backend no hay persistencia compartida; migra a deploy real. 3) Falso (en general) — los links públicos pueden ser indexables o no, depende del proveedor; verifica políticas. 4) Falso — son útiles dentro de la sesión pero no sustituyen Git: el día que el proveedor cambia política o tu cuenta caduca, pierdes todo.

**B1.** 1-b · 2-c · 3-d · 4-a.

**B2.** Sugerencia (acepta variantes razonables y actualízala): Claude (mejor React, link público nativo, mobile bien); ChatGPT (mejor docs largos y Python con Code Interpreter); Gemini (mejor integración Workspace).

**C1.** Propósito · Componentes · Datos · Estilo · Interacciones · Restricciones.

**C2.** Respuesta libre. Verifica que los 6 elementos estén explícitos. Buen prompt: *"Propósito: ayudar a la coordinadora ver y actualizar cupos de 12 grupos. Componentes: 4x3 grid de cards + total arriba. Datos: 12 grupos (1A-6A, 1B-6B), cada uno con cupo total entre 25-30. Estilo: paleta azul Albatros #0E3A8A, acento naranja #F39C12 para alertas, Inter 14px. Interacciones: botón +1/-1 por card, alerta roja cuando disponibles<3. Restricciones: sin backend, sin APIs externas, datos en estado local; mobile-first; sin emojis."*

**D1.** Orden recomendado: Datos plausibles → Layout → Paleta institucional → Mobile responsive → Microinteracciones → Polish.

**D2.** 1-b · 2-b.

**E1.** Orden: Probar en incógnito → Botón Publish → Snapshot desktop+mobile → Descargar código → Commit + tag semver → Actualizar CHANGELOG → Compartir URL.

**E2.** 1) Falso — el link depende del proveedor; sin código en Git, una migración o cambio de plan te deja sin Artifact. 2) Falso — los snapshots son evidencia visual cuando el código solo no recupera el estilo del proveedor. 3) Falso — typos van a parche x.x.+1, paletas pueden ser minor x.+1.0; sigue semver. 4) Verdadero — un buen CHANGELOG documenta qué se intentó y descartó, no solo qué se lanzó.

**F1.** Respuesta libre. Buena respuesta defiende: hasta 4-5 Artifacts → hub HTML simple basta; >5 o necesidad de auth/persistencia → Notion público o landing Vercel; necesidad de control multi-usuario → app real con backend (esto cae fuera de Artifacts).

**F2.** Mapa libre. Si una rama no tiene "métrica única de uso" o "próximo issue", esa mini-app aún no es operativa.
