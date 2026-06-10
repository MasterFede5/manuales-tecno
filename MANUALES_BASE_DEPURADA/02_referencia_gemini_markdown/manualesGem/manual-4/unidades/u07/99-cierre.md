---
unidad: 7
seccion: cierre
paginas_objetivo: 2
---

## Cierre y autoevaluación — Unidad 07

Cerraste la unidad de IA Local y Open Source. Ahora puedes:

1. **Evaluar** cuándo migrar a IA local según privacidad, costo, control y volumen.
2. **Operar Ollama** para descargar y ejecutar modelos abiertos.
3. **Desplegar Open WebUI** como ChatGPT institucional con multi-usuario y SSO.
4. **Comparar** Ollama, LM Studio y Jan según contexto.
5. **Elegir modelos abiertos** (Llama, Mistral, Qwen, DeepSeek) según idioma y caso.
6. **Aplicar cuantización** (Q4_K_M sweet spot) según hardware disponible.
7. **Construir RAG 100 % local** con embedder + vector store + modelo, sin que un byte salga.

> **Frase puente.** Tu Asistente vive soberano. Le falta una capacidad: **conectarse a archivos institucionales y herramientas externas** sin abandonar el modelo. La Unidad 8 te lleva a **MCP (Model Context Protocol)**, el estándar 2025 que permite que cualquier modelo (Claude, ChatGPT, local) se conecte a archivos, GitHub, Slack, Notion vía servidores MCP — incluyendo servidores que tú mismo levantas en tu institución.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **Por qué local** | desconozco | sé las razones | distingo cuándo aplica | matriz de decisión | ROI calculado |
| **Ollama** | nunca abrí | instalado | modelos descargados | API + Modelfile custom | producción multi-modelo |
| **Open WebUI** | desconozco | instalado | uso individual | multi-user + KB | con SSO + plugins |
| **LM Studio / Jan** | desconozco | conozco uno | uso ocasional | criterio de elección | matriz comparativa |
| **Modelos abiertos** | uno solo | conozco 3-4 familias | elijo según caso | benchmark personal | stack mixto cloud+local |
| **Cuantización y hardware** | sin entender | conozco Q4 | elijo nivel adecuado | mido latencia y calidad | optimización fina |
| **RAG local** | sin construir | piezas separadas | stack 100 % local | con observabilidad | con re-indexación automatizada |

### Pregunta de cierre

> Tu Asistente local está corriendo desde hace 3 meses con 30 cuentas institucionales, sin incidentes. La GPU principal se quema un viernes en la noche. El lunes hay actividades académicas que dependen del Asistente. **Diseña** tu plan en 5 actos: (1) cómo lo detectaste, (2) plan inmediato (lunes 8:00), (3) reparación a corto plazo (semana), (4) mejora estructural (mes), (5) qué documento de contingencia debió evitarte el susto.

### Conexión con la siguiente unidad

En **U8 — MCP y Conexión de Herramientas**, llevas contigo el Asistente local de esta unidad y lo extiendes con servidores MCP locales que le permiten **leer y escribir** en archivos de la institución, GitHub interno, calendar, sin pasar por proveedores externos. La soberanía completa.
