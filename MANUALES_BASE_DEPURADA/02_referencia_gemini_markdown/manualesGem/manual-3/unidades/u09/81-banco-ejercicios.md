---
unidad: 9
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 09

> Banco de práctica para ética y uso responsable de IA: detección de sesgos, palancas de privacidad, atribución de outputs, identificación de deepfakes, decisiones de carrera y aterrizaje regulatorio. Privilegia ejercicios de **juicio**, **redacción de criterios** y **toma de postura**. Resuelve antes de mirar la clave.

---

### Bloque A — Sesgos en datos y resultados (9.1)

::act-mcq{titulo="Tipología de sesgos"}
1. Le pides al tutor "5 ingenieros importantes" y devuelve 5 hombres europeos del siglo XX. El sesgo dominante es:
   - [ ] Confirmación
   - [x] Selección (corpus inclinado hacia hombres europeos)
   - [ ] Despliegue
   - [ ] Agregación

2. Aceptas la corrección del autocompletado aunque sabías que tenías razón. Eso ilustra:
   - [ ] Sesgo histórico
   - [ ] Sesgo de selección
   - [x] Sesgo de automatización
   - [ ] Sesgo de agregación

3. Un modelo entrenado para "estudiantes de bachillerato" rinde mal con estudiantes de educación técnica. Es:
   - [ ] Sesgo de confirmación
   - [x] Sesgo de agregación (el promedio falla en sub-grupos)
   - [ ] Sesgo histórico
   - [ ] Sesgo de selección
::/act-mcq

::act-fill{titulo="Tres tácticas de mitigación"}
Para reducir sesgo en lo que tu tutor produce, hay tres tácticas que sí funcionan:

1. **Diversifica fuentes en el prompt.** En vez de "dame ejemplos de X", pide ejemplos representando al menos _____________ continentes y un balance de _____________.
2. **Pide _____________ en lugar de promedios.** "Salario promedio" oculta sesgo regional; "salario mínimo, mediano y máximo en CDMX, NY y Bangalore" revela el rango real.
3. **Cierra con auditoría.** Antes de publicar, pídele al modelo: *"¿Qué _____________, perspectiva o dato puede estar _____________ en lo que acabas de generar?"*.

Los tres orígenes de un sesgo en IA son: _____________ (corpus inclinado), _____________ (la arquitectura optimiza una métrica) y _____________ (uso del sistema en contexto distinto al diseñado).
::/act-fill

::act-case{titulo="Auditoría en 10 minutos a tu tutor" lineas=10}
Diseña una auditoría de sesgo de 10 minutos para tu tutor IA. Define: a) dos prompts distintos para detectar el sesgo (uno de variación demográfica, otro de contraste de roles), b) qué métrica vas a contar (proporción de mujeres, no occidentales, etc.), c) el umbral en el cual declaras que hay sesgo, d) qué harás si lo detectas (no usar el output, ajustar prompt, cambiar de modelo).
::/act-case

---

### Bloque B — Privacidad y datos personales (9.2)

::act-tf{titulo="V/F sobre privacidad en chats IA"}
1. Si activas el "modo temporal" de ChatGPT, tu prompt nunca toca los servidores del proveedor. ( ) ____________
2. Por defecto, los datos enviados vía API de OpenAI o Anthropic NO se usan para entrenar el modelo. ( ) ____________
3. Pegar el RFC de un compañero en un chat público sin su consentimiento puede violar la LFPDPPP. ( ) ____________
4. Borrar una conversación en la interfaz elimina los logs internos del proveedor. ( ) ____________
5. La voz de tu podcast subido a Spotify puede clonarse con 30 segundos de muestra. ( ) ____________
::/act-tf

::act-match{titulo="Palanca de privacidad → qué hace"}
| Palanca | Efecto |
|---|---|
| 1. No usar para entrenamiento | a) Sustituye nombres y lugares antes de pegar |
| 2. Modo temporal / efímero | b) El historial no se guarda en tu cuenta |
| 3. Anonimización manual | c) Tu prompt no alimenta futuras versiones del modelo |
| 4. Uso vía API | d) Por defecto los datos no entrenan el modelo |
| 5. Derechos ARCO | e) Pides Acceso, Rectificación, Cancelación u Oposición a la empresa |
::/act-match

::act-fill{titulo="Lo que NUNCA debes pegar"}
Tres categorías de información que **NUNCA** debes pegar en un chat público:

1. **PII de _____________ sin consentimiento** — el correo de una compañera, el RFC de un familiar, la dirección de tu tía. Si no es tuyo, no es tuyo para compartirlo.
2. **_____________** — contraseñas, tokens de API, llaves SSH, números de tarjeta. Aunque pidas "explica este error", no incluyas la línea con la _____________ key.
3. **Información sujeta a _____________ o contrato laboral** — código fuente confidencial, lista de clientes, estrategia. La ley puede caer encima incluso si la intención era buena.

En México los datos sensibles (salud, religión, ideología, orientación sexual, datos genéticos) están protegidos por la _____________; en la UE por el _____________; los derechos ARCO se ejercen ante el _____________ si la empresa te ignora.
::/act-fill

---

### Bloque C — Derechos de autor (9.3)

::act-mcq{titulo="Autoría y atribución"}
1. Tu tutor genera un texto 100 % automático sin edición tuya. En EE. UU. (US Copyright Office, 2023):
   - [ ] Tienes copyright pleno
   - [ ] El proveedor del modelo tiene copyright
   - [x] No es protegible por copyright (no hubo autoría humana suficiente)
   - [ ] Es del dominio público obligatorio en México

2. Le pides "haz una caricatura mía estilo Studio Ghibli" y la publicas. Riesgo principal:
   - [ ] Sesgo de selección
   - [x] Plagio efectivo + uso de marca de un tercero
   - [ ] Privacidad
   - [ ] Sesgo histórico

3. La licencia más recomendada para publicar tu material editado por IA y mantenerte protegido:
   - [ ] Copyright tradicional reservado
   - [x] Creative Commons BY 4.0
   - [ ] CC BY-NC-ND
   - [ ] Sin licencia
::/act-mcq

::act-table{titulo="Riesgo por tipo de output"}
| Tipo de output | Riesgo (alto/medio/bajo) | Práctica recomendada |
|---|---|---|
| Texto largo (>300 palabras) | | |
| Código fuente | | |
| Imagen "estilo Studio Ghibli" | | |
| Voz clonada de famoso | | |
| Música generada (Suno, Udio) | | |
::/act-table

::act-tf{titulo="V/F sobre derecho de autor en IA"}
1. Tu prompt cuenta como obra protegible bajo la LFDA mexicana. ( ) ____________
2. El test de "similitud sustancial" es el que decide si hubo plagio efectivo. ( ) ____________
3. Si tu output reproduce literalmente un fragmento de un libro con copyright, tú eres responsable aunque el modelo lo "memorizara". ( ) ____________
4. La duración del derecho de autor en México es vida del autor + 100 años. ( ) ____________
5. Decir "asistido por IA" al pie de un texto te exime de cualquier responsabilidad por el contenido. ( ) ____________
::/act-tf

---

### Bloque D — Deepfakes y desinformación (9.4)

::act-order{titulo="Pipeline de un deepfake — ordena las etapas"}
[ ] Distribución en TikTok / WhatsApp / X
[ ] Recolección de datos públicos del objetivo (30 s audio + 5 fotos)
[ ] Generación del video o audio falso
[ ] Entrenamiento o fine-tune del modelo
::/act-order

::act-mcq{titulo="Detección rápida de deepfakes"}
1. De los 7 indicadores rápidos, el que MÁS rápido delata un deepfake de imagen es:
   - [ ] El tono de voz
   - [x] Las manos y los dedos (anatomía aún falla)
   - [ ] El logo del canal
   - [ ] El color de fondo

2. C2PA (Coalition for Content Provenance and Authenticity) sirve para:
   - [ ] Generar deepfakes
   - [x] Firmar criptográficamente la procedencia y el historial de un archivo
   - [ ] Borrar metadatos de fotos
   - [ ] Detectar virus

3. Recibes un audio de tu mejor amiga insultándote. Antes de responder, deberías:
   - [ ] Reenviarlo a tu grupo de amigos para que opinen
   - [x] Llamarla por teléfono o pedir prueba de vida (palabra clave previa)
   - [ ] Bloquearla
   - [ ] Compartirlo en tu story
::/act-mcq

::act-case{titulo="Tu protocolo anti-deepfake personal" lineas=8}
Diseña tu **protocolo anti-deepfake personal** en 5 puntos: a) qué fotos y audios públicos vas a limitar a partir de hoy, b) cuál será tu palabra clave de prueba de vida con familia cercana, c) qué marca de agua llevarán tus outputs IA, d) a qué autoridad reportarás un deepfake recibido (incluye correo o sitio), e) cómo verificarás un archivo sospechoso (mencionar contentcredentials.org).
::/act-case

---

### Bloque E — Impacto laboral y educativo (9.5)

::act-table{titulo="Mapa de tu carrera frente a la IA"}
| Carrera | Exposición a IA (alta/media/baja) | Tarea que se automatiza primero | Habilidad humana que SUBE de valor |
|---|---|---|---|
| Medicina general | | | |
| Diseño gráfico | | | |
| Derecho corporativo | | | |
| Psicología clínica | | | |
| Ingeniería de software | | | |
::/act-table

::act-tf{titulo="V/F sobre el impacto laboral y educativo"}
1. Casi ningún trabajo se automatiza al 100 %; casi todos se aumentan. ( ) ____________
2. Pedirle al tutor que resuelva tu examen el día del examen es uso responsable si lo declaras. ( ) ____________
3. Generar 30 preguntas de práctica con tu tutor para estudiar el examen es uso legítimo. ( ) ____________
4. La IA hace la empatía y el contacto presencial mejor que un humano en consulta clínica. ( ) ____________
5. Declarar uso de IA en cada entrega académica protege tu honestidad y te cubre legalmente. ( ) ____________
::/act-tf

::act-case{titulo="Política personal de uso académico de IA" lineas=8}
Redacta tu **política personal** en 5 reglas para usar IA en tu vida académica. Cada regla debe distinguir un uso que SÍ delegas (resumir, generar prácticas, corregir ortografía, lluvia de ideas, traducir) de uno que NO (resolver examen, escribir ensayo final sin declarar). Cierra con la frase modelo de declaración que vas a anexar al pie de tus entregas.
::/act-case

---

### Bloque F — Ley de IA en México y UE (9.6)

::act-match{titulo="Pirámide de riesgo del AI Act"}
| Nivel | Ejemplo |
|---|---|
| 1. Riesgo inaceptable (prohibido) | a) Filtros de spam, asistentes de productividad |
| 2. Alto riesgo (estrictamente regulado) | b) Chatbots, deepfakes, reconocimiento de emociones |
| 3. Riesgo limitado (transparencia) | c) IA que decide admisión escolar o filtra CVs |
| 4. Riesgo mínimo (libre uso) | d) *Social scoring* gubernamental, manipulación subliminal |
::/act-match

::act-mcq{titulo="Marco legal en México y UE"}
1. En abril de 2026, en México:
   - [ ] Existe una Ley Federal de IA aprobada y vigente
   - [x] No hay ley específica de IA; aplican LFPDPPP, LFDA y otras leyes generales
   - [ ] El AI Act europeo aplica directamente sin adaptación
   - [ ] Está prohibido el uso de IA en educación

2. El AI Act de la UE impone multas de hasta:
   - [ ] 100 000 €
   - [ ] 1 M €
   - [ ] 10 M €
   - [x] 35 M € o 7 % de facturación global

3. Si tu tutor califica o filtra estudiantes para una beca, el AI Act lo clasifica como:
   - [ ] Riesgo mínimo
   - [ ] Riesgo limitado
   - [x] Alto riesgo (educación que decide admisión o calificación)
   - [ ] Riesgo inaceptable
::/act-mcq

::act-fill{titulo="Tres reglas operativas que ya puedes adoptar"}
Tres reglas que puedes adoptar **ya** como si fueran ley:

1. **Etiqueta visible.** Toda pieza producida o asistida sustancialmente por IA lleva la nota _____________ o _____________.
2. **Registro de uso.** Lleva una bitácora simple con: _____________, _____________, _____________ y la decisión humana posterior. Si te auditan o demandan, esa bitácora es tu defensa.
3. **Supervisión humana en decisiones que importan.** Cualquier output que afecte a _____________ (calificación, recomendación de salud, contratación) pasa por _____________ antes de salir. No automatices la _____________.
::/act-fill

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-c · 3-b. **Fill:** 3 continentes · género · rangos · grupo · sub-representado · datos · algoritmo · despliegue. **Caso (ejemplo):** a) prompt 1 "lista 5 referentes históricos en X" repetido 3 veces / prompt 2 "describe a un X exitoso vs una X exitosa"; b) proporción de mujeres y de no occidentales; c) umbral <20 %; d) ajustar prompt + diversificar + auditoría explícita.

**Bloque B — V/F:** 1-F (sí toca servidores; solo no se guarda en tu historial) · 2-V · 3-V · 4-F (solo del historial visible, no necesariamente de logs internos) · 5-V. **Match:** 1-c · 2-b · 3-a · 4-d · 5-e. **Fill:** terceros · credenciales · secret · NDA · LFPDPPP · GDPR/RGPD · INAI.

**Bloque C — MCQ:** 1-c · 2-b · 3-b. **Tabla:** texto largo = medio/editar 30 % · código = alto/CopyriskBot, snippets propios · imagen estilo Ghibli = alto/cambiar a "ilustración acuarela suave" sin marca · voz clonada de famoso = muy alto/solo con autorización escrita · música generada = medio/uso personal, no comercial sin verificar. **V/F:** 1-F (la LFDA reconoce solo a personas físicas como autores; el prompt no es obra) · 2-V · 3-V · 4-V · 5-F (declarar es necesario pero no exime de responsabilidad por contenido).

**Bloque D — Order:** recolección → entrenamiento → generación → distribución. **MCQ:** 1-b · 2-b · 3-b. **Caso (ejemplo):** a) reducir audios públicos a clips < 30 s con marca de agua y limitar fotos de alta resolución; b) palabra clave única acordada con familia cercana, jamás compartida en redes; c) marca discreta "Generado con IA · @usuario" en esquina inferior; d) Policía Cibernética (cibernetica@ssp.cdmx.gob.mx) o reporte directo a la plataforma; e) verificar en contentcredentials.org/verify.

**Bloque E — Tabla:** medicina = media / lectura imágenes rutina / comunicación con paciente y manualidad clínica · diseño gráfico = muy alta / maquetas y banco imágenes / dirección de arte y branding profundo · derecho corporativo = alta / revisión contratos y búsqueda jurisprudencial / estrategia, negociación y juicio ético · psicología clínica = baja / triaje y screening / vínculo terapéutico y juicio clínico complejo · ingeniería de software = alta / 30–50 % código de pega / arquitectura, debugging crítico y comunicación con cliente. **V/F:** 1-V · 2-F (es trampa académica; declarar no la legitima) · 3-V · 4-F (la IA simula por chat pero pierde en cuerpo y presencia) · 5-V.

**Bloque F — Match:** 1-d · 2-c · 3-b · 4-a. **MCQ:** 1-b · 2-d · 3-c. **Fill:** "asistido por IA" · "generado con IA" · fecha · herramienta · prompt · otra persona · tus ojos · responsabilidad.
