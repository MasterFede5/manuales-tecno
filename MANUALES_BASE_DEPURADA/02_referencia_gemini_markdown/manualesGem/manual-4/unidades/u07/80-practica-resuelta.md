---
unidad: 7
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 07

::practica{titulo="Desplegar el Asistente Institucional 100 % local con Ollama + Open WebUI + RAG en una tarde"}
**Problema.** Construir la versión soberana del Asistente: Ollama con Qwen 2.5 72B Q4 + Open WebUI multi-user con SSO institucional + knowledge base con reglamento + golden test contra versión cloud. Hardware: workstation con RTX A6000 48 GB VRAM. Tiempo objetivo: 4 horas (1 tarde).

**Paso 1 — Datos / hardware.**
- Workstation: Ubuntu 22.04, RTX A6000 (48 GB VRAM), 64 GB RAM, 2 TB SSD, Docker instalado, IP fija en LAN institucional.
- Reglamento académico v3.0 (35 pp), manual del docente v2.1 (60 pp), código de ética v1.0 (8 pp).
- Cuentas Google Workspace para SSO.
- Dominio interno `asistente.albatros.local` con DNS resuelto.

**Paso 2 — Estrategia.**
1. Instalar Ollama y descargar modelos.
2. Instalar Open WebUI vía Docker.
3. Configurar SSO con Google Workspace.
4. Crear knowledge base "reglamento" y subir docs.
5. Configurar embedder bge-m3.
6. Crear cuentas a 5 staff piloto.
7. Golden set comparativo local vs cloud.

**Paso 3 — Instalación Ollama (15 min).**
```bash
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar modelos (toma ~30 min total con buena conexión)
ollama pull qwen2.5:72b      # principal razonamiento
ollama pull qwen2.5:7b       # rápido para clasificación
ollama pull bge-m3           # embeddings
ollama pull nomic-embed-text # backup embedder

# Verificar
ollama list
```

**Paso 4 — Open WebUI (10 min).**
```bash
docker run -d \
  -p 3000:8080 \
  --gpus all \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Abro `http://asistente.albatros.local:3000`, creo cuenta admin con mi correo institucional.

**Paso 5 — SSO Google Workspace (20 min).**
- Open WebUI Settings → Auth → OAuth.
- Configurar Client ID + Client Secret de Google Cloud Console.
- Restringir a dominio `albatros.edu.mx`.
- Probar login con otra cuenta institucional.

**Paso 6 — Knowledge base (30 min).**
- Workspace → Knowledge → "+ New" → "reglamento".
- Settings: embedder `bge-m3`, chunk size 500, overlap 50.
- Upload: 3 PDFs (reglamento, manual docente, ética).
- Indexación tarda ~3 minutos en GPU.
- Verificar: ChromaDB indexó 412 chunks.

**Paso 7 — Configuración del modelo principal (15 min).**

Modelfile custom:
```
FROM qwen2.5:72b
SYSTEM """
Eres el Asistente Institucional Albatros. Respondes en español mexicano
profesional y cálido. Cuando uses información de #reglamento o documentos,
cita el archivo y página entre [corchetes]. Si no encuentras la respuesta
en los documentos, di explícitamente "no tengo información sobre eso en
mis fuentes institucionales".
"""
PARAMETER temperature 0.3
PARAMETER num_ctx 8192
```

`ollama create asistente -f Modelfile.asistente`

Configurar este modelo como default en Open WebUI.

**Paso 8 — Golden set local vs cloud (60 min).**

Lanzo las mismas 15 preguntas (las del golden de U4) en:
- Versión cloud actual (Claude Sonnet + RAG en Claude Project).
- Versión local nueva (Qwen 2.5 72B + RAG en Open WebUI).

| # | Pregunta | Cloud | Local |
|---|---|---|---|
| 1 | Plazo apelación | ✓ | ✓ |
| 2 | Inasistencias | ✓ | ✓ |
| 3 | Reincorporación tras 3 faltas | ✓ | ✓ con cita levemente menos precisa |
| 4 | Becas hermanos | ✓ | ✓ |
| 5 | Calendario exámenes | ✓ | ✓ |
| 6 | Director (NO está) | "no info" ✓ | "no info" ✓ |
| 7 | Dispraxia (NO está) | "no info" ✓ | "no info" ✓ |
| 8 | Tono molesto | excelente | bueno (4/5 vs 5/5) |
| 9-15 | varios | 14/15 | 13/15 |

Resumen: **local 13/15 vs cloud 14/15**. Latencia local 12s vs cloud 3s. Local **suficiente para producción** con stakeholders no-críticos.

**Paso 9 — Cuentas piloto y socialización (30 min).**
- 5 staff piloto invitados por correo (link público de registro restringido a dominio).
- Reunión de 30 min mostrando uso, knowledge base, cuándo escalar a cloud.
- Documento "Cómo usar el Asistente Local" (1 pp).

**Paso 10 — Monitoreo (15 min).**
- Configurar Prometheus + Grafana opcional para métricas.
- Por ahora: Sheet con logs manuales semanales (uso, errores).
- Backup automatizado del volumen Docker (diario).

**Respuesta.** Asistente Institucional v1.0 local desplegado. Acceso: `https://asistente.albatros.local:3000` con SSO Google. 5 cuentas piloto. Knowledge base con 3 documentos institucionales. Golden 13/15. Latencia 12s mediana. Costo recurrente $0 (electricidad ~$80/mes).

**Verificación final.** A 1 semana: 5 staff usaron 47 conversaciones. 0 incidentes. 2 tickets reportando lentitud (mitigado: configurar router para preferir Qwen 7B en preguntas simples). Coordinadora reporta: "se siente igual que ChatGPT pero sin temor de filtrar datos".

**Lección.** Las 7 técnicas de la unidad encajan: **por qué local** (privacidad de menores) → **Ollama** (instalación trivial) → **Open WebUI** (UI institucional) → **Qwen 2.5 72B** (mejor español abierto) → **Q4_K_M** (cabe en GPU) → **bge-m3 + ChromaDB** (RAG soberano). El stack local 2025 está maduro para producción institucional educativa con datos sensibles.
::/practica

::practica{titulo="Cómo benchmarkeé 3 tamaños de Qwen y elegí el menor que basta"}
**Problema.** El proveedor de hardware ofrece 3 opciones para la workstation del Asistente local: GPU 24 GB ($2 000), 48 GB ($3 500), 96 GB ($7 200). Cada GPU encaja con un tamaño máximo de Qwen 2.5: 14B, 32B o 72B respectivamente. Necesito saber qué tamaño basta para nuestros casos antes de comprometer presupuesto.

**Paso 1 — Definir criterios de "suficiente".**
- Calidad: golden set RAGAS del Asistente con score ≥ 4.0/5 promedio.
- Latencia: respuesta < 15 s en 90 % de las preguntas.
- Sin alucinaciones graves (cita inventada o fact incorrecto verificable).

**Paso 2 — Setup de prueba.**
Pido al proveedor demos remotas de 1 hora con cada GPU. Llevo USB con:
- 5 PDFs institucionales para indexar.
- 20 preguntas del golden RAG.
- Modelfile con system prompt institucional.

**Paso 3 — Ronda 1: Qwen 2.5 14B Q4 en GPU 24 GB.**
- Tiempo de carga: 8 segundos.
- Latencia mediana: 6 s. P95: 11 s.
- Calidad sobre 20: 14/20 correctas, 4 con detalle menor faltante, 2 alucinaciones (citó artículo equivocado pero textualmente del documento). Score promedio: 3.8/5.
- **Veredicto: marginal**. Buen rendimiento, calidad cercana al umbral.

**Paso 4 — Ronda 2: Qwen 2.5 32B Q4 en GPU 48 GB.**
- Tiempo de carga: 14 s.
- Latencia mediana: 9 s. P95: 16 s.
- Calidad: 17/20 correctas, 3 parciales, 0 alucinaciones graves. Score promedio: 4.3/5.
- **Veredicto: pasa el umbral con margen**.

**Paso 5 — Ronda 3: Qwen 2.5 72B Q4 en GPU 96 GB.**
- Tiempo de carga: 22 s.
- Latencia mediana: 12 s. P95: 21 s — **excede el umbral del 90 %**.
- Calidad: 18/20 correctas, 2 parciales, 0 alucinaciones graves. Score promedio: 4.5/5.
- **Veredicto: sube +0.2 de calidad pero excede latencia y cuesta 2x más**.

**Paso 6 — Decisión basada en datos.**

| Métrica | 14B (24 GB) | 32B (48 GB) | 72B (96 GB) |
|---|---|---|---|
| Calidad ≥ 4.0 | 3.8 ✗ | 4.3 ✓ | 4.5 ✓ |
| Latencia P95 < 15 s | 11 ✓ | 16 — | 21 ✗ |
| Sin alucinaciones graves | ✗ | ✓ | ✓ |
| Costo GPU | $2 000 | $3 500 | $7 200 |
| Calidad/$ | mejor pero falla calidad | mejor balance | sobre-dimensionado |

**Elijo Qwen 2.5 32B en GPU 48 GB**. Pasa el umbral de calidad con margen, latencia justa pero aceptable (P95 16 s, mediana 9 s), sin alucinaciones graves, costo $3 500.

**Paso 7 — Plan de revisión.**
ADR-018: *"32B Q4 en GPU 48 GB. Re-evaluar a 12 meses si: (a) volumen >500 consultas/día y latencia se vuelve cuello, o (b) llega Qwen 3.0 que cabe en 24 GB con calidad equivalente"*.

**Paso 8 — Comunicación al patronato.**
Reporte de 1 página con tabla, costo total a 36 meses (HW + electricidad + mantenimiento ≈ $9 800), comparativa contra cloud ($12 600 a 36 meses), no-monetarias (privacidad). Patronato aprueba $3 500 + presupuesto operativo.

**Respuesta.** Compra autorizada de workstation con GPU 48 GB. Decisión basada en 60 datos medidos en 3 horas, no en intuición o catálogo del proveedor.

**Verificación.** A 6 meses, el Asistente 32B atiende 4 200 consultas/mes con 4.2/5 satisfacción y latencia mediana 9 s. Volumen estable. Decisión validada.

**Lección.** "El modelo más grande es el mejor" es **mantra falso**. La pregunta correcta no es *"¿cuál es el más capaz?"* sino *"¿cuál es el más pequeño que basta?"*. Pagar 2x por +0.2 puntos de calidad y latencia peor es derroche. La regla operativa: **mide tu caso real con golden, define umbrales antes de probar, elige el menor modelo que los pase**.
::/practica

::practica{titulo="Cómo decidí qué workflows migrar a local y cuáles dejar en cloud sin pelearme con dirección"}
**Problema.** Tienes el Asistente local operativo (32B) y el cloud operativo (Sonnet). Dirección pregunta: *"¿migramos todo a local? Sale más barato"*. Tú sabes que no es tan simple. Necesito una matriz de decisión defendible.

**Paso 1 — Inventariar tareas del Asistente.**

| Tarea | Volumen/mes | Sensibilidad de datos | Calidad requerida | Latencia tolerada |
|---|---|---|---|---|
| Clasificar solicitudes | 4 200 | media | media | <2 s |
| Redactar comunicados | 800 | baja | alta | <30 s |
| Resumen de juntas | 60 | media | alta | <60 s |
| Consulta reglamento (RAG) | 1 200 | baja | alta | <10 s |
| Caso emocional (crisis) | 12 | crítica | crítica | <30 s |
| Generación de contenido educativo | 30 | baja | alta | <120 s |
| Análisis de datos calificaciones | 80 | crítica | media | <60 s |

**Paso 2 — Criterio de migración.**
Una tarea va a local si cumple **al menos 2** de:
- Sensibilidad de datos alta o crítica (privacidad de menores).
- Volumen alto que hace cloud caro (> 1 000 llamadas/mes).
- Calidad puede ser **media** (32B local cumple).
- No requiere capacidades específicas de Sonnet/Opus (razonamiento extremo, contexto >100k).

**Paso 3 — Mapear cada tarea.**

| Tarea | ¿Local? | Razón |
|---|---|---|
| Clasificar solicitudes | **sí** | Volumen alto + calidad media basta |
| Redactar comunicados | no | Calidad alta requerida y volumen bajo |
| Resumen de juntas | **sí** | Sensibilidad media + volumen bajo + acepta latencia |
| Consulta reglamento (RAG) | **sí** | Volumen alto + calidad alta pero 32B + RAG la cumple |
| Caso emocional (crisis) | **sí** | Sensibilidad crítica — no debe salir |
| Generación de contenido educativo | no | Calidad alta requerida; el 32B se queda corto |
| Análisis de datos calificaciones | **sí** | Sensibilidad crítica |

Resultado: **5 de 7 tareas a local, 2 quedan en cloud**.

**Paso 4 — Estimar ahorro.**
- Volumen total a cloud antes: 7 380 llamadas/mes × $0.005 promedio = ~$37/mes.
- Volumen tras migración: 830 llamadas/mes × $0.008 (más caras porque son las "alta calidad") = ~$7/mes.
- Ahorro de cloud: ~$30/mes ($360/año).
- Costo de local ya provisionado.
- **Ahorro real**: ~$360/año.

Si solo es por costo, no vale la pena pelear. La ganancia es **soberanía + plan B + reducción de superficie regulatoria**.

**Paso 5 — Pruebas A/B en producción.**
Para cada tarea decidida "local": canary 10 % al modelo local y 90 % al cloud durante 2 semanas. Medir:
- Calidad subjetiva (rúbrica humana sobre 30 ejemplos).
- Latencia.
- Errores.

Para 5 tareas con canary: 4 pasan, 1 falla (clasificar solicitudes — 32B falla 8 % vs Sonnet 3 %; mantener cloud).

**Paso 6 — Decisión final.**

| Tarea | Decisión final |
|---|---|
| Clasificar solicitudes | cloud (calidad cae demasiado) |
| Redactar comunicados | cloud |
| Resumen de juntas | local |
| Consulta reglamento (RAG) | local con fallback a cloud si no encuentra |
| Caso emocional (crisis) | local con review humano siempre |
| Generación contenido educativo | cloud |
| Análisis datos calificaciones | local |

4 de 7 a local. Las 3 en cloud por razones documentadas.

**Paso 7 — ADR y comunicación.**
ADR-019: *"Migración parcial a local. 4 tareas con sensibilidad o volumen alto a local; 3 tareas con calidad crítica permanecen en cloud. Revisión a 6 meses cuando llegue Qwen 3 o equivalente."*

Reporte a dirección de 1 página con tabla, ahorro real (~$360/año), y argumento principal: *"el valor no es ahorrar — es controlar dónde viven los datos sensibles"*.

**Respuesta.** Migración parcial ejecutada. 4 tareas locales, 3 cloud, criterios documentados. Dirección entiende que "todo a local" era equivocado y agradece el análisis.

**Verificación.** A 90 días: cero incidentes de calidad en producción, cero leak de datos sensibles. Patronato satisfecho con la postura.

**Lección.** "Cloud o local" es **falsa dicotomía**. La realidad operativa es **híbrido por tarea**: cada uso tiene perfil de sensibilidad/calidad/volumen distinto. La sabiduría es **mapear y decidir por tarea**, no por dogma. El día que dirección te pida "todo a uno o todo al otro", lleva la matriz.
::/practica
