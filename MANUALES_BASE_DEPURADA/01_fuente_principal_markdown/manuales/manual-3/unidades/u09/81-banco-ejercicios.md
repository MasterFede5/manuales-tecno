---
unidad: 9
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 09

> **Banco de práctica:** Ética y uso responsable de IA.
> - Detección de sesgos y palancas de privacidad.
> - Atribución, deepfakes y regulación.
> - Privilegia el **juicio**, **redacción de criterios** y **toma de postura**.
> 
> *Resuelve todo antes de mirar la clave al final.*

::interioriza
**El simulador de vuelo:** 
Este banco de ejercicios es tu simulador. 
Es mejor equivocarte aquí ajustando un prompt, que filtrar datos reales de tu empresa o sesgar una decisión importante.
::/interioriza

::pausa{}
¿Estás listo para cuestionar tus propios sesgos antes de auditar a la IA?
::/pausa

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
Para reducir sesgo en lo que tu tutor produce, aplica estas tres tácticas:

- **Diversifica fuentes en el prompt:** 
  Pide ejemplos representando al menos _____________ continentes y un balance de _____________.
- **Pide _____________ en lugar de promedios:** 
  "Salario mínimo, mediano y máximo en CDMX, NY y Bangalore" revela el rango real.
- **Cierra con auditoría:** 
  Pregunta: *"¿Qué _____________, perspectiva o dato puede estar _____________ en lo que acabas de generar?"*.

Los tres orígenes de un sesgo en IA son: 
- _____________ (corpus inclinado).
- _____________ (la arquitectura optimiza una métrica). 
- _____________ (uso del sistema en contexto distinto al diseñado).
::/act-fill

::act-case{titulo="Auditoría en 10 minutos a tu tutor" lineas=10}
Diseña una auditoría de sesgo de 10 minutos para tu tutor IA. Define: 
- a) Dos prompts distintos (variación demográfica y contraste de roles).
- b) Qué métrica vas a contar (proporción de mujeres, no occidentales, etc.).
- c) El umbral en el cual declaras que hay sesgo.
- d) Qué harás si lo detectas (no usar output, ajustar prompt, etc.).
::/act-case

---

### Bloque B — Privacidad y datos personales (9.2)

::act-tf{titulo="V/F sobre privacidad en chats IA"}
1. Si activas el "modo temporal" de ChatGPT, tu prompt nunca toca los servidores del proveedor. ( ) ____________
2. Por defecto, los datos enviados vía API de OpenAI o Anthropic NO se usan para entrenar el modelo. ( ) ____________
3. Pegar el RFC de un compañero en un chat público sin consentimiento puede violar la LFPDPPP. ( ) ____________
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
| 5. Derechos ARCO | e) Pides Acceso, Rectificación, Cancelación u Oposición |
::/act-match

::act-fill{titulo="Lo que NUNCA debes pegar"}
Tres categorías de información **prohibidas** en un chat público:

- **PII de _____________ sin consentimiento:** 
  Correo, RFC o dirección ajenos. Si no es tuyo, no lo compartas.
- **_____________:** 
  Contraseñas, tokens de API, llaves SSH. No incluyas la línea con la _____________ key.
- **Información sujeta a _____________ o contrato laboral:** 
  Código fuente confidencial o lista de clientes.

En México los datos sensibles están protegidos por la _____________.
En la UE por el _____________.
Los derechos ARCO se ejercen ante el _____________ si la empresa te ignora.
::/act-fill

---

### Bloque C — Derechos de autor (9.3)

::act-mcq{titulo="Autoría y atribución"}
1. Tu tutor genera un texto 100 % automático sin edición tuya. En EE. UU.:
   - [ ] Tienes copyright pleno
   - [ ] El proveedor del modelo tiene copyright
   - [x] No es protegible por copyright (falta autoría humana)
   - [ ] Es del dominio público obligatorio en México

2. Le pides "haz una caricatura mía estilo Studio Ghibli" y la publicas. Riesgo:
   - [ ] Sesgo de selección
   - [x] Plagio efectivo + uso de marca de un tercero
   - [ ] Privacidad
   - [ ] Sesgo histórico

3. La licencia recomendada para material editado por IA y mantenerte protegido:
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
2. El test de "similitud sustancial" decide si hubo plagio efectivo. ( ) ____________
3. Si tu output reproduce un libro con copyright, eres responsable aunque el modelo lo memorizara. ( ) ____________
4. La duración del derecho de autor en México es vida del autor + 100 años. ( ) ____________
5. Decir "asistido por IA" te exime de cualquier responsabilidad por el contenido. ( ) ____________
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
   - [x] Firmar criptográficamente la procedencia y el historial
   - [ ] Borrar metadatos de fotos
   - [ ] Detectar virus

3. Recibes un audio de tu mejor amiga insultándote. Antes de responder, deberías:
   - [ ] Reenviarlo a tu grupo de amigos para que opinen
   - [x] Llamarla por teléfono o pedir prueba de vida (palabra clave)
   - [ ] Bloquearla
   - [ ] Compartirlo en tu story
::/act-mcq

::act-case{titulo="Tu protocolo anti-deepfake personal" lineas=8}
Diseña tu **protocolo anti-deepfake personal** en 5 puntos: 
- a) Qué fotos/audios vas a limitar a partir de hoy.
- b) Cuál será tu palabra clave de prueba de vida con familia.
- c) Qué marca de agua llevarán tus outputs IA.
- d) A qué autoridad reportarás un deepfake (incluye correo).
- e) Cómo verificarás un archivo sospechoso.
::/act-case

---

### Bloque E — Impacto laboral y educativo (9.5)

::act-table{titulo="Mapa de tu carrera frente a la IA"}
| Carrera | Exposición a IA (alta/media/baja) | Tarea automatizada primero | Habilidad humana al alza |
|---|---|---|---|
| Medicina general | | | |
| Diseño gráfico | | | |
| Derecho corporativo | | | |
| Psicología clínica | | | |
| Ingeniería de software | | | |
::/act-table

::act-tf{titulo="V/F sobre el impacto laboral y educativo"}
1. Casi ningún trabajo se automatiza al 100 %; casi todos se aumentan. ( ) ____________
2. Pedirle al tutor que resuelva tu examen en tiempo real es uso responsable si lo declaras. ( ) ____________
3. Generar 30 preguntas de práctica con tu tutor para estudiar es uso legítimo. ( ) ____________
4. La IA hace la empatía y contacto presencial mejor que un humano en clínica. ( ) ____________
5. Declarar uso de IA en cada entrega protege tu honestidad y te cubre legalmente. ( ) ____________
::/act-tf

::act-case{titulo="Política personal de uso académico de IA" lineas=8}
Redacta tu **política personal** en 5 reglas para usar IA:
- Distingue un uso que SÍ delegas (resumir, generar prácticas, corregir).
- Distingue un uso que NO (resolver examen, escribir ensayo final sin declarar). 
- Cierra con la frase modelo de declaración que anexarás a tus entregas.
::/act-case

---

### Bloque F — Ley de IA en México y UE (9.6)

::act-match{titulo="Pirámide de riesgo del AI Act"}
| Nivel | Ejemplo |
|---|---|
| 1. Riesgo inaceptable | a) Filtros de spam, asistentes de productividad |
| 2. Alto riesgo | b) Chatbots, deepfakes, reconocimiento de emociones |
| 3. Riesgo limitado | c) IA que decide admisión escolar o filtra CVs |
| 4. Riesgo mínimo | d) *Social scoring*, manipulación subliminal |
::/act-match

::act-mcq{titulo="Marco legal en México y UE"}
1. En abril de 2026, en México:
   - [ ] Existe una Ley Federal de IA aprobada y vigente
   - [x] No hay ley de IA; aplican LFPDPPP, LFDA y generales
   - [ ] El AI Act europeo aplica directamente sin adaptación
   - [ ] Está prohibido el uso de IA en educación

2. El AI Act de la UE impone multas de hasta:
   - [ ] 100 000 €
   - [ ] 1 M €
   - [ ] 10 M €
   - [x] 35 M € o 7 % de facturación global

3. Si tu tutor califica estudiantes para una beca, el AI Act lo clasifica como:
   - [ ] Riesgo mínimo
   - [ ] Riesgo limitado
   - [x] Alto riesgo (educación que decide admisión)
   - [ ] Riesgo inaceptable
::/act-mcq

::act-fill{titulo="Tres reglas operativas que ya puedes adoptar"}
Tres reglas que puedes adoptar **ya** como si fueran ley:

- **Etiqueta visible:** 
  Toda pieza producida o asistida por IA lleva la nota _____________ o _____________.
- **Registro de uso:** 
  Lleva una bitácora con: _____________, _____________, _____________ y la decisión humana. 
- **Supervisión humana:** 
  Cualquier output que afecte a _____________ (calificación, salud) pasa por _____________ antes de salir. No automatices la _____________.
::/act-fill

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-c · 3-b. 
**Fill:** 3 continentes · género · rangos · grupo · sub-representado · datos · algoritmo · despliegue. 
**Caso:** a) prompt 1 "lista 5 referentes" repetido / prompt 2 "describe un X vs una X"; b) proporción de mujeres/no occidentales; c) umbral <20 %; d) ajustar prompt + auditoría.

**Bloque B — V/F:** 1-F (toca servidores, solo no guarda historial) · 2-V · 3-V · 4-F (solo borra historial visible) · 5-V. 
**Match:** 1-c · 2-b · 3-a · 4-d · 5-e. 
**Fill:** terceros · credenciales · secret · NDA · LFPDPPP · GDPR/RGPD · INAI.

**Bloque C — MCQ:** 1-c · 2-b · 3-b. 
**Tabla:** texto largo = medio/editar 30 % · código = alto/CopyriskBot · imagen Ghibli = alto/cambiar a "ilustración acuarela" · voz clonada = muy alto/solo autorización escrita · música generada = medio/uso personal. 
**V/F:** 1-F (el prompt no es obra) · 2-V · 3-V · 4-V · 5-F (declarar no exime de responsabilidad).

**Bloque D — Order:** recolección → entrenamiento → generación → distribución. 
**MCQ:** 1-b · 2-b · 3-b. 
**Caso:** a) reducir audios públicos < 30 s con marca; b) palabra clave única; c) marca discreta en esquina; d) Policía Cibernética (cibernetica@ssp.cdmx.gob.mx); e) verificar en contentcredentials.org/verify.

**Bloque E — Tabla:** medicina = media / lectura imágenes / comunicación paciente · diseño gráfico = muy alta / maquetas / dirección de arte · derecho corporativo = alta / revisión contratos / estrategia y ética · psicología clínica = baja / triaje / vínculo terapéutico · ingeniería de software = alta / 30–50 % código de pega / arquitectura y debugging. 
**V/F:** 1-V · 2-F (trampa académica) · 3-V · 4-F (IA pierde en presencia) · 5-V.

**Bloque F — Match:** 1-d · 2-c · 3-b · 4-a. 
**MCQ:** 1-b · 2-d · 3-c. 
**Fill:** "asistido por IA" · "generado con IA" · fecha · herramienta · prompt · otra persona · tus ojos · responsabilidad.
