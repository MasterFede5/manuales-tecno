---
unidad: 7
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 07

> Trabajas con tu computadora (Linux, Mac o Windows con WSL). Tienes Ollama instalado y al menos 16 GB de RAM. Si no tienes GPU, igual puedes hacer la mayoría de los ejercicios con modelos pequeños (Qwen 2.5 7B, Phi-3).

### Sección A — Por qué y cuándo (7.1)

::act-mcq{titulo="A1. Razones para migrar a IA local"}
1. La razón **principal** para que una institución educativa migre a IA local es:
   - [ ] Costo
   - [x] Soberanía de datos sensibles (menores, calificaciones, salud)
   - [ ] Velocidad
   - [ ] Calidad del modelo

2. Para una startup pequeña con 3 desarrolladores y volumen bajo, el ahorro mensual de migrar a Ollama suele ser:
   - [ ] Alto, vale la pena
   - [x] Marginal, no compensa el esfuerzo de mantenimiento
   - [ ] Negativo siempre
   - [ ] Imposible de calcular

3. ¿En qué momento el costo total (servidor + electricidad + tiempo) supera al cloud?
   - [ ] A 100 llamadas/mes
   - [ ] A 1 000 llamadas/mes
   - [x] Depende del volumen, modelo y tarifa eléctrica — calcular caso por caso
   - [ ] A 10 000 llamadas/mes
::/act-mcq

::act-tf{titulo="A2. Mitos sobre IA local"}
1. IA local es siempre más barata que cloud. ( ) ____________________________________________
2. Con Ollama no hace falta seguir comprando GPU; el CPU basta. ( ) ____________________________________________
3. Migrar a local elimina el riesgo de leak de datos. ( ) ____________________________________________
4. La calidad de Qwen 2.5 72B es comparable a Claude Sonnet en español. ( ) ____________________________________________
::/act-tf

### Sección B — Ollama, Open WebUI, LM Studio, Jan (7.2, 7.3, 7.4)

::act-match{titulo="B1. Componente → rol"}
| Componente | Rol |
|---|---|
| 1. Ollama | a) UI multi-usuario tipo ChatGPT |
| 2. Open WebUI | b) Runtime CLI/API de modelos abiertos |
| 3. LM Studio | c) UI individual para Mac/Windows |
| 4. Jan | d) UI individual open source multiplataforma |
::/act-match

::act-order{titulo="B2. Orden de despliegue de un Asistente local multi-usuario"}
[ ] Configurar SSO o auth simple
[ ] Instalar Ollama
[ ] Descargar modelos principales y embedder
[ ] Levantar Open WebUI con Docker
[ ] Crear Modelfile customizado con system prompt institucional
[ ] Crear knowledge base con embedder local
[ ] Configurar backup automático del volumen
[ ] Probar con golden set vs cloud
::/act-order

::act-fill{titulo="B3. Comando esencial de Ollama"}
Para descargar e iniciar Qwen 2.5 7B en tu máquina, los comandos son:

```bash
ollama _____________ qwen2.5:7b
ollama _____________
ollama _____________ qwen2.5:7b
```

Para crear un modelo customizado a partir de un Modelfile, el comando es:

```bash
ollama _____________ asistente -f Modelfile.asistente
```

Y para servir el modelo en HTTP localhost:11434, Ollama lo hace _____________ tras instalación.
::/act-fill

### Sección C — Modelos abiertos (7.5)

::act-table{titulo="C1. Modelo recomendado por hardware y caso"}
| Hardware | Modelo recomendado | Caso del Asistente |
|---|---|---|
| Laptop 16 GB RAM, GPU integrada |  |  |
| PC RTX 3060 12 GB VRAM |  |  |
| Workstation A6000 48 GB VRAM |  |  |
| Mac M3 Max 128 GB RAM unificada |  |  |
| Servidor multi-GPU enterprise |  |  |
::/act-table

::act-mcq{titulo="C2. Elegir familia de modelos"}
1. Para una institución hispanohablante mexicana, la familia abierta más recomendable en 2025 es:
   - [ ] Llama 3.1
   - [ ] Mistral
   - [x] Qwen 2.5
   - [ ] Phi-3

2. Para reasoning puro y matemáticas:
   - [ ] Llama 3.1 8B
   - [x] DeepSeek R1 o Qwen 2.5 Coder/Math
   - [ ] Phi-3 mini
   - [ ] Mistral 7B

3. Para edge / móvil con muy poco RAM:
   - [ ] Qwen 2.5 72B
   - [ ] Llama 3.1 70B
   - [x] Phi-3 mini o Gemma 2B
   - [ ] DeepSeek 67B
::/act-mcq

### Sección D — Cuantización y hardware (7.6)

::act-fill{titulo="D1. Decodifica nombres de cuantización"}
Q4_K_M significa modelo cuantizado a _____________ bits con _____________ calidad ~98 %, _____________ memoria. Q8 mantiene calidad casi sin pérdida pero usa _____________ memoria que Q4. Q2 es la **menor** memoria pero pierde mucha _____________. El "sweet spot" calidad/tamaño suele ser _____________.
::/act-fill

::act-mcq{titulo="D2. Cabe o no cabe"}
1. Llama 3.1 70B Q4_K_M (~40 GB) en una GPU de 24 GB VRAM (RTX 3090):
   - [ ] Cabe perfecto
   - [x] No cabe (necesita offload a RAM, será lento)
   - [ ] Cabe en Q2
   - [ ] Imposible de saber

2. Qwen 2.5 7B Q4 (~4.5 GB) en una laptop con GPU integrada y 16 GB RAM:
   - [x] Cabe en RAM con CPU inference, ~5-10 tok/s
   - [ ] Imposible
   - [ ] Solo en GPU
   - [ ] Solo en Mac

3. Mac Studio M2 Ultra 192 GB unificada puede correr:
   - [ ] Solo modelos pequeños
   - [x] Modelos grandes (70B+ Q8) gracias a memoria unificada
   - [ ] Solo Apple ML
   - [ ] Solo en frío
::/act-mcq

### Sección E — RAG local y caso integrador (7.7)

::act-tf{titulo="E1. Soberanía total"}
1. RAG con embedder cloud y modelo local mantiene la soberanía. ( ) ____________________________________________
2. Si tu vector store es ChromaDB local pero el embedder es OpenAI, los datos sensibles **siguen** saliendo a internet. ( ) ____________________________________________
3. Para soberanía total: modelo + embedder + vector store + UI deben ser locales. ( ) ____________________________________________
::/act-tf

::act-case{titulo="E2. Caso — calculas TCO local vs cloud" lineas=14}
Tu institución gastará $4 200/año en cloud (Claude Sonnet). Para migrar a local, propones: workstation $3 500 (one-time), electricidad $80/mes, mantenimiento 4 h/mes a $25/h. Calcula TCO a 12, 24 y 36 meses comparando ambos. ¿En qué momento local "paga"? ¿Qué consideraciones no-monetarias importan más que el costo? Mínimo 10 líneas con números.
::/act-case

::act-mindmap{titulo="E3. Tu stack soberano v1.0" centro="ASISTENTE LOCAL ALBATROS" nodos_primarios=7 nodos_secundarios=14}
Las 7 ramas: (1) hardware, (2) Ollama + modelos descargados, (3) Open WebUI configurado, (4) embedder + vector store local, (5) auth/SSO, (6) backup y monitoreo, (7) golden set comparativo cloud. Datos concretos.
::/act-mindmap

---

## Clave de respuestas

**A1.** 1-b · 2-b · 3-c.

**A2.** 1) Falso — local tiene costo de hardware, electricidad, mantenimiento; cloud puede ser más barato a volúmenes bajos. 2) Falso — CPU corre modelos pero a 10x menor tokens/s; para producción se recomienda GPU o Apple Silicon. 3) Falso — local mitiga riesgo de leak con proveedor pero introduce riesgos de fuga interna; sin política de acceso, los datos siguen vulnerables. 4) Generalmente cierto — Qwen 2.5 72B compite cerca de Sonnet en español; valida con tu golden set.

**B1.** 1-b · 2-a · 3-c · 4-d.

**B2.** Orden: instalar Ollama → descargar modelos + embedder → levantar Open WebUI → configurar SSO/auth → Modelfile customizado → knowledge base → backup automático → golden vs cloud.

**B3.** `pull` · `list` · `run` · `create` · automáticamente.

**C1.** Sugerencia (acepta variantes razonables): laptop 16 GB → Qwen 2.5 7B Q4 (CPU inference) para personal/dev. RTX 3060 12 GB → Qwen 2.5 14B Q4 o Llama 3.1 8B Q8 para single user. A6000 48 GB → Qwen 2.5 72B Q4_K_M para multi-usuario institucional. Mac M3 Max 128 GB → Llama 3.1 70B Q8 o Qwen 2.5 72B Q8 con buen rendimiento. Servidor multi-GPU → modelos 100B+ o múltiples instancias balanceadas.

**C2.** 1-c · 2-b · 3-c.

**D1.** 4 · ~98 % · menor (~30 % menos que Q8) · más · calidad · Q4_K_M.

**D2.** 1-b · 2-a · 3-b.

**E1.** 1) Falso — el embedder cloud envía cada chunk a OpenAI; los datos salen. 2) Verdadero. 3) Verdadero.

**E2.** Sugerencia de cálculo:
- Cloud: $4 200 × 1, 2, 3 = $4 200 / $8 400 / $12 600.
- Local: $3 500 + ($80 + $100) × 12 × 1, 2, 3 = $5 660 / $7 820 / $9 980.
- Break-even: ~entre 24 y 36 meses si cloud = $4 200/año.
- No-monetarias: privacidad de menores, control sobre el modelo (no actualización forzada), independencia de proveedor (B-007 del PRD), capacidad de operar offline.

**E3.** Mapa libre. Si una rama tiene <2 datos concretos, esa pieza aún no está madura.
