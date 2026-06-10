---
unidad: 7
seccion: caso-episodio
paginas_objetivo: 1
---

::caso{episodio=7}
**Caso Albatros — Episodio 7: Versión soberana del Asistente con Ollama y Open WebUI.**

Tu Asistente cloud funciona, pero la dirección lee los noticieros: "OpenAI sufre filtración de chats", "Anthropic cambia términos de privacidad", "Google fine-tunea modelos con datos públicos sin consentimiento explícito". El director te pregunta directo: *"¿Qué pasaría si mañana el proveedor sube precios un 300 % o cambia política sobre datos de menores? ¿Tenemos plan?"*. Tu respuesta honesta: *"sin alternativa local, no"*.

El Episodio 7 te pide construir la **versión soberana del Asistente Institucional Albatros**: un sistema corriendo localmente —en una computadora del departamento de TI o en un servidor pequeño de la institución— que **no manda datos a ningún proveedor externo**. Cubrirás el porqué, Ollama (la herramienta de facto en 2025), Open WebUI (interfaz tipo ChatGPT en localhost), alternativas LM Studio y Jan, modelos abiertos disponibles (Llama 3.1, Mistral, Qwen, DeepSeek), cuantización y hardware necesario, y conexión con bases locales. Al final, tendrás un Asistente que sigue funcionando aunque cortes internet — y que jamás filtró un dato.

> *La pregunta gancho:* ¿en qué momento el costo de mantener tu propio modelo (servidor + electricidad + tiempo) supera al costo del proveedor cloud? La respuesta depende de variables que esta unidad te ayuda a calcular. Empezamos por el **porqué**.
::/caso

