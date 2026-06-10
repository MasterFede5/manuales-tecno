---
unidad: 3
seccion: taller
paginas_objetivo: 2
---

## Taller — Construir un dashboard funcional en 60 minutos

::albatros{titulo="Construyes un dashboard publicado y compartido en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si dirección te pidiera **mañana** ver el avance del Asistente, ¿podrías mandar un link en un mensaje de WhatsApp que abra y se entienda en 30 segundos?

**Lo que harás.** Vas a construir un **dashboard funcional** del Asistente Institucional como Artifact React. Métricas, módulos, ADRs y riesgos. Publicado, versionado y enviado a una persona externa que lo abre en su celular antes de que termine la hora.

**Materiales reales.**
- Cuenta Claude (Free sirve, Pro mejor para iteraciones más rápidas).
- Repo Git existente del proyecto.
- 4 métricas reales de tu institución (puede ser conteo de solicitudes, % escalación, latencia, costo).
- 3 módulos del Asistente o de cualquier proyecto IA en curso.
- 2-3 ADRs documentados (puede ser de U2).
- 1 persona externa al equipo accesible por WhatsApp.

**Pasos (10).**

1. **Min 0–5 — Wireframe a mano.** En papel, dibuja 4 secciones del dashboard: header con número grande (KPI principal), 4 cards de métricas, lista de módulos con badge de estado, sección de ADRs y riesgos al pie. **No pases al teclado** hasta tener wireframe.

2. **Min 5–15 — Primer prompt estructurado.** En Claude, redacta el prompt con las 6 dimensiones (propósito, componentes, datos, estilo, interacciones, restricciones). Mínimo 15 líneas. Ejecuta. Recibes v1 funcional.

3. **Min 15–25 — Iteración paleta y datos.** *"Cambia paleta a azul #0E3A8A y acento #F39C12. Sustituye datos placeholder por: solicitudes=24, escalación=12 %, latencia=1.4s, costo=$46."* → v2.

4. **Min 25–35 — Iteración layout y módulos.** *"Agrega tab 'Módulos' con cards expandibles para 3 módulos: clasificador v1.2, redactor v1.0, resumen v1.0. Cada card con estado (verde/ámbar/rojo) y last update."* → v3.

5. **Min 35–40 — Tab decisiones y riesgos.** *"Agrega tab 'Decisiones' con cards para 2-3 ADRs (título, fecha, decisión, alternativa). Tab 'Riesgos' con tabla simple."* → v4.

6. **Min 40–45 — Mobile y polish.** *"Mobile-first: en <768px, cards apiladas, fuente cuerpo 14px, padding 16px. Polish: ARIA labels, contraste WCAG AA, sparklines mini con datos simulados de 12 puntos en cada métrica."* → v5.

7. **Min 45–48 — Verificación en mobile.** Botón Publish. Copia el link. Ábrelo desde **tu propio celular** en navegador incógnito. Si algo se rompe, regresa al chat: *"corrige Y en mobile"* → v5.1. Si todo funciona, sigue.

8. **Min 48–53 — Versionado.** Botón Code → Copy. Crea `tools/dashboard/v1.0.0/App.jsx` en tu repo. Toma `snapshot-desktop.png` y `snapshot-mobile.png`. Escribe `CHANGELOG.md` con 1 línea. Commit con mensaje `feat(dashboard): release v1.0.0`. Si tienes acceso, `git tag v1.0.0`.

9. **Min 53–58 — Distribución externa.** Manda WhatsApp a tu persona externa: *"hola, ¿puedes abrir este link en 30 segundos y decirme qué entendiste?"*. Pega el URL del Artifact.

10. **Min 58–60 — Captura feedback.** Anota qué dijo la persona en `tools/dashboard/feedback-v1.0.0.md`. Si entendió las 4 métricas y el estado de los módulos, **el dashboard funciona**. Si no, anota qué le confundió: ese es tu primer issue para v1.1.0.

**Entregable.**
- URL pública del Artifact (en repo y en WhatsApp del compañero).
- Carpeta `tools/dashboard/v1.0.0/` con `App.jsx` + 2 snapshots + CHANGELOG.
- `feedback-v1.0.0.md` con la respuesta de la persona externa.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Wireframe previo | sin papel | mental | dibujado y respetado |
| Primer prompt | improvisado | con 4 dimensiones | con las 6 |
| Iteraciones | 1-2 | 3-4 | 5+ con polish |
| Mobile | no funciona | aceptable | impecable |
| Versionado externo | sin commit | commit | tag semver + CHANGELOG + 2 snapshots |
| Validación social | no se hizo | persona miró | persona explicó qué entendió y qué confundió |
::/albatros
