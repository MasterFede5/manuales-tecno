---
unidad: 7
seccion: taller
paginas_objetivo: 2
---

## Taller — Instalas Ollama y benchmarkeas vs la nube en 60 minutos

::albatros{titulo="Instalas Ollama, sirves un modelo y lo benchmarkeas vs Claude/ChatGPT en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si pudieras correr "tu propio ChatGPT" en tu laptop sin pagar nunca y sin que nada saliera a internet, ¿qué pondrías en él que hoy no pones por miedo?

**Lo que harás.** Vas a instalar **Ollama** en tu computadora, descargar un modelo abierto, hacerle 7 preguntas reales, lanzarle las **mismas 7** a Claude o ChatGPT en paralelo, y comparar los resultados con criterios objetivos. Al cerrar el cronómetro tendrás: tu primer modelo local corriendo, una tabla comparativa local vs nube, y una decisión documentada de qué casos llevar a local y cuáles dejar en cloud.

**Materiales reales.**
- Computadora con mínimo 16 GB RAM (GPU recomendada, integrada también funciona).
- 5 GB libres en disco.
- Cuenta Claude o ChatGPT abierta para comparar.
- 60 min sin notificaciones.

**Pasos (10).**

1. **Min 0–5 — Instalación de Ollama.** En Mac/Linux ejecuta: `curl -fsSL https://ollama.ai/install.sh | sh`. En Windows: descarga el instalador de ollama.com. Verifica con `ollama --version`.

2. **Min 5–15 — Descarga de modelo.** Decide según tu hardware:
   - 16 GB RAM sin GPU dedicada → `ollama pull qwen2.5:7b` (~4.5 GB, lento pero funciona).
   - 24 GB RAM o GPU 8-12 GB → `ollama pull qwen2.5:14b` (~9 GB, mejor calidad).
   - 32 GB+ RAM o GPU 16+ GB → `ollama pull qwen2.5:32b` (~20 GB, muy buena calidad).
   La descarga tarda 3-15 min según conexión. Mientras descarga, sigue al paso 3.

3. **Min 15–18 — Diseña 7 preguntas de benchmark.** En tu editor:
   - 3 preguntas factuales en español sobre tu institución o materia (sin RAG).
   - 1 pregunta de razonamiento (matemática, lógica, planificación).
   - 1 pregunta creativa (redactar, resumir, traducir).
   - 1 pregunta sensible (deberías querer mantenerla local: dato de menor, info financiera, mensaje íntimo).
   - 1 pregunta de "no sé" (algo que el modelo no debería saber con certeza).

4. **Min 18–20 — Smoke test local.** En terminal: `ollama run qwen2.5:7b` (o el que descargaste). Lanza una pregunta simple para verificar que funciona. Sale con `/bye`.

5. **Min 20–25 — Construye system prompt.** Crea archivo `Modelfile.albatros`:
   ```
   FROM qwen2.5:7b
   SYSTEM """
   Eres un asistente útil en español mexicano profesional y cálido.
   Si no tienes información, responde 'no tengo información sobre eso'.
   Sé breve y directo.
   """
   PARAMETER temperature 0.3
   ```
   Ejecuta: `ollama create albatros-local -f Modelfile.albatros`.

6. **Min 25–40 — Lanza las 7 preguntas a local.** `ollama run albatros-local`. Pega las 7 preguntas. Para cada respuesta apunta:
   - Tiempo de respuesta visual (estimado).
   - Calidad subjetiva 1-5.
   - ¿Citó fuente o lo inventó?
   - Notas.

7. **Min 40–50 — Lanza las 7 preguntas a cloud.** En Claude o ChatGPT, lanza las mismas 7 preguntas. Mismo registro: tiempo, calidad, fuentes, notas.

8. **Min 50–55 — Tabla comparativa.** En tu editor, construye:

   | # | Pregunta | Local: tiempo | Local: calidad | Cloud: tiempo | Cloud: calidad | Decisión |
   |---|---|---|---|---|---|---|

   En la columna "Decisión" para cada pregunta escribe: *local OK*, *cloud necesario*, o *cualquiera*.

9. **Min 55–58 — TCO mental rápido.** Estima:
   - Volumen mensual de las preguntas que decidiste "local OK".
   - Costo cloud equivalente: volumen × $0.002 (estimado promedio).
   - Costo local: tu electricidad mensual añadida (estimado $5-30).
   - Decisión: ¿migrar esa porción a local vale la pena?

10. **Min 58–60 — Documentación y compartir.** Pega resultados en `local-ai-benchmark.md` en tu repo. Comparte el archivo con un compañero y pídele que añada 2 preguntas suyas para el siguiente benchmark.

**Entregable.**
- Ollama corriendo con modelo elegido.
- Modelfile customizado (`Modelfile.albatros`) en tu repo.
- `local-ai-benchmark.md` con 7 preguntas, 7×2 respuestas, tabla comparativa, TCO mental, decisión.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Setup local | parcial | Ollama + 1 modelo | Ollama + Modelfile customizado |
| Benchmark | <3 preguntas | 7 preguntas | 7 incluyendo sensible y "no sé" |
| Comparativa | informal | tabla con tiempo y calidad | tabla + decisión por pregunta |
| TCO | ausente | mental | con números aproximados |
| Decisión | "depende" | qué migrar | qué migrar + cuándo + criterio de revisión |
| Compartir | privado | enviado | compañero añadió preguntas |
::/albatros
