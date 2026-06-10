---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 03

::practica{titulo="Construir y publicar el Dashboard v1.0 del Asistente Institucional Albatros como Artifact en 90 minutos"}
**Problema.** Tras aprobar el PRD en U2, dirección pide ver "cómo va el Asistente" cada lunes. Tu meta: producir un Artifact React publicado, con métricas, módulos, ADRs y riesgos, distribuido al equipo y respaldado en Git. Tiempo total: 90 minutos.

**Paso 1 — Datos disponibles.**
- 4 métricas iniciales: solicitudes resueltas (24), tasa de escalación (12 %), latencia mediana (1.4 s), costo del mes ($46).
- 3 módulos en operación: clasificador-solicitudes v1.2, redactor-comunicado v1.0, resumen-juntas v1.0.
- 3 ADRs documentados: modelo híbrido, no-objetivo psicopedagogía, retención logs 30 días.
- 2 riesgos activos: dependencia única proveedor, cambio precios LLM.

**Paso 2 — Estrategia.**
1. Decidir tipo: Artifact React (interactividad) en Claude (mejor en React).
2. Primer prompt completo y estructurado.
3. Iterar 4-5 veces para datos, layout, mobile, polish.
4. Publicar en `claude.site`.
5. Descargar código y commitear como v1.0.0 en repo.
6. Compartir URL y captura al equipo.

**Paso 3 — Primer prompt (10 min).**
Compongo el prompt con la estructura del subtema 3.4: propósito, componentes, datos, estilo, interacciones, restricciones. Lo pego en Claude Pro (mejor render React). Recibo v1 funcional en 35 segundos.

**Paso 4 — Iteraciones (45 min).**
- *"Cambia paleta a azul Albatros #0E3A8A y acento naranja #F39C12"* → v2.
- *"Agrega tab 'Decisiones' con cards expandibles para los 3 ADRs"* → v3.
- *"En métricas, agrega sparkline mini con datos simulados de 12 puntos"* → v4.
- *"Mobile-first: en pantallas <768px las 4 cards se apilan en columna"* → v5.
- *"Polish: revisa accesibilidad ARIA, contraste, espaciado, errores en consola"* → v6.

Cada iteración entre 30 y 90 segundos. Tras v5 doy una vuelta visual a navegación entre tabs (transición sutil con framer-motion).

**Paso 5 — Datos plausibles (10 min).**
En v7 sustituyo placeholders por valores realistas del proyecto. Hago un mini chequeo de consistencia: si latencia es 1.4s y costo $46, ¿coherente con 24 solicitudes resueltas? Sí (margen razonable). Tab Riesgos: redacto en lenguaje accesible para director sin perder precisión.

**Paso 6 — Publicación (5 min).**
Botón Publish en Claude. URL `claude.site/abc123`. Pruebo en navegador incógnito desde mi celular: carga en 1.2 s, mobile responsive funciona, todas las tabs cambian sin recarga.

**Paso 7 — Versionado externo (10 min).**
- Botón Code → Copy en Claude.
- Pego en `tools/dashboard/v1.0.0/App.jsx` del repo.
- Capturo dos snapshots: `snapshot-desktop.png` y `snapshot-mobile.png`.
- Escribo entrada en CHANGELOG: "v1.0.0 dashboard inicial con 4 métricas, 3 módulos, 3 ADRs, 2 riesgos. Stack React + Tailwind + recharts."
- `git commit -m "feat(dashboard): release v1.0.0 con 4 secciones"` y `git tag v1.0.0`.

**Paso 8 — Distribución (5 min).**
- Pego URL en canal Slack #albatros-asistente.
- Edito mensaje fijo del canal: "Dashboard semanal · v1.0.0 · actualizado lunes".
- Aviso al director con captura adjunta.

**Paso 9 — Verificación (5 min).**
- 3 personas distintas abren el link desde dispositivos distintos: 2 desktop, 1 mobile. Todas reportan que cargan correctamente.
- La coordinadora académica encuentra que el ADR-002 tiene un error de fecha. Lo corrijo en v1.0.1 (5 minutos), republico, actualizo URL si cambió.

**Respuesta.** Dashboard v1.0.0 (luego v1.0.1) publicado en `claude.site/abc123`, respaldado en Git con tag, distribuido al equipo y validado por tres personas. Tiempo total: 90 min, dentro del objetivo. La dirección lo abrió desde su iPad y dijo "esto sí responde mi pregunta".

**Verificación final.** Una semana después, actualizo datos (lunes 8:00 ritual). Tiempo: 8 minutos. Versión v1.1.0. Confirma que el flujo es sostenible.

**Lección.** Las 6 técnicas no se aplican secuencialmente como receta: se interconectan. **Concepto** te dice qué tipo elegir; **plataforma** te dice dónde construir; **mini-app** te da el patrón concreto; **compartir** convierte el artifact en valor; **versionado** lo hace duradero. Saltarse versionado es la grieta más cara de cerrar después.
::/practica

::practica{titulo="Cómo construí la calculadora de cupos y la conecté con el dashboard sin romper nada"}
**Problema.** El dashboard v1.1.0 ya está en uso. La coordinadora pide ahora una **calculadora de cupos** independiente —que abra en su celular durante las inscripciones presenciales— y que el dashboard refleje los cupos en tiempo real. Tienes 2 horas. Sin backend.

**Paso 1 — Decidir alcance honesto.**
"Tiempo real" sin backend es imposible. Lo redefino con la coordinadora: la calculadora **muestra cupos al momento de abrirse**, los cambios viven en su sesión, y al final del día ella **exporta JSON** que se pega en el dashboard manualmente. Acepta. Documento esta limitación en el ADR-008.

**Paso 2 — Diseño de la calculadora.**
Wireframe a mano: header con total general, grid 4×3 con 12 cards (1A-6A, 1B-6B), cada card con nombre, cupo total, ocupados, disponibles, botones +1/-1, alerta visual si <3.

**Paso 3 — Primer prompt en Claude.**
Las 6 dimensiones explícitas. Datos plausibles: cada grupo con cupo total entre 25-30 y ocupados aleatorios entre 18-28. Restricciones: sin APIs, datos en estado local React, mobile-first, exportable como JSON con botón "descargar estado".

Recibo v1 funcional en 40 segundos.

**Paso 4 — Iteraciones (45 min).**
- v2 — paleta azul Albatros + naranja para alertas.
- v3 — fix: las cards en mobile se cortaban. Pidió ajustar a `grid-cols-1 md:grid-cols-3 gap-4`.
- v4 — botón "Exportar estado" arriba, descarga `cupos-YYYY-MM-DD-HHMM.json`.
- v5 — botón "Importar estado" para que la coordinadora pueda cargar el archivo del día anterior.
- v6 — alerta visual: card rojo cuando <3 disponibles, ámbar cuando <5, badge con número.
- v7 — accesibilidad: ARIA labels en botones, contraste WCAG AA, keyboard navigation.

**Paso 5 — Verificación cruzada de dispositivo.**
Publish → URL. Pruebo en mi laptop, mi celular y le paso a una compañera el link (su Android viejo). En el Android se rompió la fuente. Itero v8: web-safe fallback `Inter, system-ui, sans-serif`. Funciona.

**Paso 6 — Versionado externo.**
- `tools/calculadora-cupos/v1.0.0/App.jsx` en repo.
- `snapshot-desktop.png` y `snapshot-mobile.png`.
- `CHANGELOG.md` con: *"v1.0.0 — 12 grupos, +/-, exportar/importar JSON, alertas, mobile responsive, ARIA"*.
- `git tag v1.0.0`.

**Paso 7 — Conexión con el dashboard.**
En el dashboard v1.1.0, agrego un nuevo botón en la sección "Cupos": *"Cargar estado del día"*. El usuario carga el JSON exportado de la calculadora. El dashboard muestra los 12 cupos de manera read-only.

Itero el dashboard a v1.2.0 con la nueva sección. Versionado: `tools/dashboard/v1.2.0/`.

**Paso 8 — Documentación y entrega a coordinadora.**
1 página en `docs/uso-calculadora-cupos.md` con: cómo abrir, cómo usar +/-, cómo exportar al final del día, cómo cargar en dashboard. Le dejo hipervínculo de la calculadora fijo en su WhatsApp Web.

**Paso 9 — Smoke test con la coordinadora.**
La acompaño 15 min en su sesión real de inscripciones. Captura 12 alumnos nuevos en 18 minutos. Exporta JSON. Carga en dashboard sin mi ayuda. **Funciona.**

**Respuesta.** Calculadora v1.0.0 publicada y conectada al dashboard v1.2.0 vía export JSON. Tiempo total: 1 h 50 min, dentro del objetivo. La coordinadora ahora actualiza cupos en su celular y el dashboard refleja al final del día.

**Verificación.** A los 5 días, la coordinadora reporta que ahorró 4 horas de la semana en la actualización mental de cupos. El dashboard tiene datos reales por primera vez.

**Lección.** "Tiempo real" sin backend es discusión técnica que casi siempre se puede **redefinir como "fin del día"**. Cuando el caso de uso lo permite, evitas semanas de migración a app real. Lo difícil no fue construir la calculadora — fue **negociar el alcance honesto** y luego protegerlo en el ADR.
::/practica

::practica{titulo="Cómo decidí entre Claude Artifact y deploy real para el quiz vocacional"}
**Problema.** El departamento de orientación pide un **quiz vocacional** con 30 preguntas, resultado final con tipo de carrera sugerido, y una **base de datos** de respuestas para análisis posterior. ¿Artifact o app real?

**Paso 1 — Mapear los requisitos.**
- Frontend: 30 preguntas, navegación, resultado.
- Persistencia: respuestas de **todos** los estudiantes guardadas para análisis.
- Acceso: estudiantes lo abren desde su celular o computadora del laboratorio.
- Anonimato: la institución pidió que no se guarden nombres, solo grupo y carrera tentativa.
- Volumen esperado: 240 estudiantes en 1 semana.

**Paso 2 — Probar la hipótesis Artifact.**
Construyo en Claude un prototipo en 30 min. Las 30 preguntas como cards, resultado con explicación, paleta institucional. Funciona localmente. **Pero al cerrar el navegador, las respuestas se pierden** — el Artifact no tiene backend.

Workaround posible: cada estudiante "exporta JSON al final" y un coordinador los junta. Calculo: 240 archivos JSON × juntar a mano = 6 horas. **Inviable.**

**Paso 3 — Estimar el deploy real.**
Frontend: el código React del Artifact es reutilizable. Hosting en Vercel: gratis. Base de datos: Supabase free tier (hasta 500 MB). Endpoint de POST: una función serverless de 20 líneas. Total estimado: 4 horas para tener algo profesional con persistencia.

**Paso 4 — Comparativa formal.**

| Criterio | Artifact + export | Deploy Vercel + Supabase |
|---|---|---|
| Tiempo de construcción | 30 min | 4 horas |
| Costo de operación | $0 | $0 (free tier) |
| Persistencia compartida | no | sí |
| Acceso estudiantes | link | link |
| Análisis posterior | 6 h juntar JSONs | query SQL en 5 min |
| Mantenibilidad | yo cada vez que cambia | repo + deploy automático |
| Riesgo de pérdida de datos | alto | bajo |

**Paso 5 — Decisión documentada en ADR.**
ADR-009: *"quiz vocacional sale en deploy real (Vercel + Supabase) en lugar de Artifact, por requisito duro de persistencia centralizada para análisis posterior. El código del prototipo Artifact se reutiliza como base"*.

**Paso 6 — Build híbrido.**
- Reutilizo el código React del Artifact como base (sí estaba bueno).
- Agrego un cliente Supabase de 15 líneas.
- Función serverless `/api/submit-quiz` que recibe `{ grupo, carrera_tentativa, respuestas }` y guarda anónimo.
- Deploy a Vercel en 8 minutos.
- URL `quiz-albatros.vercel.app`.

**Paso 7 — Smoke test con 5 estudiantes.**
5 estudiantes voluntarios completan el quiz. Reviso Supabase: las 5 respuestas están guardadas anónimamente. Acceso público al quiz, acceso restringido (rol service) a la base de datos.

**Paso 8 — Documentación y traspaso.**
Repo en GitHub. README con cómo desplegar, cómo cambiar las preguntas, cómo exportar resultados a CSV. Reúno al departamento de orientación y les muestro el flujo completo.

**Respuesta.** Quiz vocacional en producción real, 240 estudiantes en 5 días, todas las respuestas en Supabase listas para análisis. **No es Artifact**, y eso es bueno: el problema requería persistencia compartida.

**Verificación.** El departamento de orientación corre su análisis con 240 respuestas reales. Genera reporte de tendencias. Imposible con Artifacts.

**Lección.** Artifacts son **excelentes** para casos sin persistencia compartida (dashboards, calculadoras de sesión, prototipos). Cuando el caso pide guardar datos de muchos usuarios, fuérzate a hacer deploy real desde el principio — el Artifact es buen prototipo pero **mal producto** ahí. La señal es siempre la misma: si necesitas analizar datos de varios, sales del Artifact.
::/practica
