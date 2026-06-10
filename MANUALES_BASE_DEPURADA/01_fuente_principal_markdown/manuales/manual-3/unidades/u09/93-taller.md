---
unidad: 9
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Auditoría ética y código de conducta de tu tutor IA

> Este taller convierte las 6 dimensiones éticas de la unidad en **un protocolo ejecutable de 60 minutos**. Sales con tu tutor auditado, configurado y firmado: una auditoría de sesgo real, las palancas de privacidad activadas, marcas de procedencia en outputs, política de uso académico y un **Código Ético público** firmado y publicable.

::albatros{titulo="60 minutos para blindar y certificar éticamente tu tutor IA" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si mañana publicaras una pieza con tu tutor y un periodista te preguntara "¿con qué sesgos opera tu modelo, dónde van los datos de quienes te escriben y quién es dueño de lo que produces?", ¿podrías responder en 30 segundos por cada pregunta? Este taller te da las respuestas y la firma pública.

**Lo que harás (12 pasos).**

1. **Audita sesgo (5 min).** Ejecuta el prompt-1 de variación demográfica (5 referentes de una profesión, repite 3 veces con sinónimos: líderes / pioneros / referentes) y el prompt-2 de contraste de roles ("describe a un X exitoso" vs. "describe a una X exitosa"). Cuenta proporción de mujeres y no occidentales en prompt-1; lista adjetivos diferentes en prompt-2. Anota en `auditoria-sesgo.md`.

2. **Define umbral y mitigación (3 min).** Si proporción <20 % en cualquier dimensión sensible, declara sesgo de selección. Reescribe el prompt original agregando "representando al menos 3 continentes y un balance de género". Vuelve a ejecutarlo. Documenta cuánto bajó el sesgo.

3. **Configura privacidad (5 min).** Entra a la cuenta del modelo que más uses (ChatGPT / Claude / Gemini) y activa: a) "no usar para entrenamiento", b) "modo temporal" como default, c) revisa retención de logs. Si tienes acceso a API, marca preferirla para tareas con datos sensibles. Captura la pantalla de las palancas activadas.

4. **Lista anti-pegado (2 min).** Redacta tu lista personal de "3 cosas que NUNCA pego en chat público": PII de terceros, credenciales (passwords, API keys), información bajo NDA. Pégala como nota fija en tu navegador o en un sticky.

5. **Atribución y licencia (5 min).** Elige una pieza ya publicada del U08 (post, carrusel o video). Edítale al pie: a) declaración de uso de IA explícita ("Borrador inicial: GPT-4 · Edición y argumentos: 100 % míos"), b) licencia CC BY 4.0 con tu nombre, c) lista de fuentes que el modelo citó (verificadas; los modelos alucinan citas).

6. **Marca de procedencia (5 min).** En tus próximos outputs visuales agrega una marca discreta "Generado con IA · @usuario" en esquina inferior derecha. Si trabajas con Adobe o cámara compatible, activa C2PA / Content Credentials. Verifica una pieza en contentcredentials.org/verify y captura el reporte.

7. **Banco de prueba de vida (3 min).** Acuerda con un familiar cercano una **palabra clave** de prueba de vida que jamás circule en redes. Si reciben un audio "tuyo" pidiendo dinero o algo urgente, te llaman para verificar. Apunta el acuerdo en una nota privada (no en el chat IA).

8. **Política de uso académico (5 min).** Redacta tu política personal en 5 reglas distinguiendo qué SÍ delegas (resumir, generar prácticas, corregir ortografía, lluvia de ideas) y qué NO (resolver examen, escribir ensayo final sin declarar). Cierra con la **frase modelo** que vas a anexar al pie de cada entrega.

9. **Mapa regulatorio (3 min).** En una hoja, ubica tu tutor en la pirámide del AI Act. ¿Riesgo mínimo, limitado o alto? Argumenta con el caso de uso real (¿califica o filtra estudiantes? ¿genera contenido sintético? ¿ofrece servicios a terceros?). Anota la categoría y las obligaciones que te corresponden.

10. **Bitácora de uso (2 min).** Crea una hoja de cálculo simple con columnas: fecha · herramienta · prompt resumido · output · revisión humana realizada. Esa bitácora es tu defensa si alguien audita o demanda. Compromete a llenarla en tus próximos 10 usos sustantivos del tutor.

11. **Redacta tu Código Ético (15 min).** Documento de **una página** con 7 secciones obligatorias: a) **qué SÍ hace** tu tutor, b) **qué NO hace** (líneas rojas), c) **datos** que guarda y por cuánto tiempo, d) **fuentes** que acredita, e) **errores** que asume y cómo los corrige, f) **cómo contactarte** para reclamar / corregir / pedir borrado, g) **firma con fecha**. Usa el Markdown del repositorio; nómbralo `codigo-etico-tutor.md`.

12. **Publica y socializa (2 min).** Sube tu Código Ético a tu sitio o como pin en tu perfil principal. Anuncia el lanzamiento con un post breve: "Mi tutor IA opera bajo este código. Estas son sus líneas rojas". Invita a 3 personas a leerlo y darte feedback. Documenta sus comentarios en `codigo-etico-tutor.md` como historial v1 → v1.1.

**Materiales.**
- Cuenta del modelo IA principal (ChatGPT / Claude / Gemini) con configuración accesible.
- Editor Markdown (VS Code, Obsidian, Notion).
- Hoja de cálculo simple (Google Sheets, Excel) para la bitácora.
- Acceso a contentcredentials.org/verify (verificación C2PA).
- Repositorio personal o sitio público (GitHub Pages, Notion público, blog) para alojar el código ético.
- Familiar o amigo cercano para acordar palabra clave de prueba de vida.

**Entregable.**
1. **`auditoria-sesgo.md`** — registro de los 2 prompts ejecutados, proporciones, umbral aplicado y prompt mitigado.
2. **Captura de pantalla** de las 3 palancas de privacidad activadas (no entrenamiento, modo temporal, retención).
3. **Pieza del U08 reeditada** con declaración de uso de IA, licencia CC BY 4.0 y fuentes verificadas.
4. **`codigo-etico-tutor.md`** — código ético firmado de una página con las 7 secciones obligatorias, publicado y con link.
5. **`bitacora-uso.xlsx`** o equivalente — plantilla creada y compromiso firmado de llenarla en próximos 10 usos.
6. **Reflexión escrita (200 palabras)** — qué descubriste sobre tu tutor que no sabías y qué cambiará en tu operación a partir de hoy.

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Auditoría de sesgo | declarativa | 1 prompt ejecutado | 2 prompts + métrica + mitigación verificada |
| Palancas de privacidad | ninguna activada | 1–2 activadas | 3 activadas + bitácora iniciada |
| Atribución y licencia | sin declaración | declaración genérica | CC BY 4.0 + fuentes verificadas + uso explícito |
| Detección y prevención de deepfakes | sin protocolo | marca de agua | marca + C2PA + palabra clave de prueba de vida |
| Código ético | borrador parcial | 1 pp con 4–5 secciones | 1 pp con las 7 secciones, firmado y publicado |
| Aterrizaje regulatorio | sin clasificar | clasificado en pirámide | clasificado + obligaciones documentadas |
| Reflexión final | superficial | menciona aprendizajes | identifica cambios concretos y plan a 30 días |

**Tip Albatros.** El Código Ético que firmas hoy no es burocracia: es **publicidad inversa**. Cuando alguien dude de tu tutor (y va a pasar), apuntas al documento y se acaba la conversación. Las personas que operan con código ético público son las que la audiencia escoge cuando todas las demás empiezan a verse iguales. Tu firma vale más cuando va respaldada.
::/albatros
