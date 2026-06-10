---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 03

::practica{titulo="Construir y publicar el Dashboard v1.0 del Asistente Institucional Albatros como Artifact en 90 minutos"}
**Problema.**
- Dirección pide ver "cómo va el Asistente" cada lunes. 
- Meta: producir un Artifact React publicado y respaldado en Git.
- Tiempo límite: 90 minutos.

**Paso 1 — Datos disponibles.**
- **4 métricas:** 24 resueltas, 12% escalación, latencia 1.4s, costo $46.
- **3 módulos:** clasificador, redactor, resumen.
- **3 ADRs:** modelo híbrido, no psicopedagogía, logs 30 días.
- **2 riesgos:** dependencia proveedor, cambio precios.

**Paso 2 — Estrategia.**
- Elegir Artifact React en Claude.
- Prompt estructurado y 4-5 iteraciones rápidas.
- Publicar en `claude.site`.
- Versionar código en repositorio (`v1.0.0`).
- Distribuir URL en Slack.

::interioriza
> Piensa en construir este Artifact como montar un mueble de IKEA.
> No fabricas la madera (eso es el React base).
> Solo juntas las piezas (datos y módulos) y lo atornillas (versionado).
::

**Paso 3 — Primer prompt (10 min).**
- Aplico estructura del subtema 3.4.
- Uso Claude Pro para mejor render de React.
- Resultado: versión 1 funcional en 35 segundos.

**Paso 4 — Iteraciones (45 min).**
- v2: *"Aplica azul Albatros #0E3A8A y naranja #F39C12"*.
- v3: *"Agrega tab Decisiones con los 3 ADRs"*.
- v4: *"Sparklines en métricas"*.
- v5: *"Mobile-first: apilar en pantallas <768px"*.
- v6: *"Polish: ARIA, contraste, espaciado"*.

**Paso 5 — Datos y Publicación (15 min).**
- Inserto datos plausibles y valido consistencia.
- Lenguaje accesible en Riesgos para la dirección.
- Clic en Publish. Pruebo desde móvil en incógnito (carga en 1.2s).

**Paso 6 — Versionado (10 min).**
- Copio código a `tools/dashboard/v1.0.0/App.jsx`.
- Tomo capturas de pantalla (desktop y móvil).
- Hago commit y tag en Git: `git tag v1.0.0`.

**Paso 7 — Distribución y Verificación (10 min).**
- Enlace enviado al canal Slack #albatros-asistente.
- 3 usuarios validan la carga correcta en distintos dispositivos.
- Corrección ágil (v1.0.1) tras feedback en 5 minutos.

::pausa{titulo="Deducción rápida"}
¿Por qué versionar el código localmente si ya está publicado en claude.site?
- Para mantener un histórico inmutable y evitar perder el Artifact si expira la URL.
- Para facilitar futuras iteraciones en local o por otros desarrolladores.
::

**Respuesta y Lección.** 
- Logrado en 90 min. Validado por dirección.
- Mantenimiento semanal: solo 8 minutos (confirmando sostenibilidad).
- **No te saltes el versionado:** es la grieta más costosa de reparar a futuro.
::/practica

::practica{titulo="Cómo construí la calculadora de cupos y la conecté con el dashboard sin romper nada"}
**Problema.** 
- Coordinadora necesita calculadora de cupos móvil durante inscripciones.
- Debe actualizar el dashboard en tiempo real (pero no hay backend).
- Límite de tiempo: 2 horas.

**Paso 1 — Decidir alcance honesto.**
- "Tiempo real" sin backend es inviable.
- **Redefinición:** Calcula localmente y exporta JSON al final del día.
- Se documenta esta restricción en el ADR-008.

**Paso 2 — Diseño y Primer Prompt.**
- Wireframe: 12 cards, cupos, botones +1/-1, alertas visuales.
- Prompt en Claude con restricciones claras y estado local React.
- Obtenida primera versión en 40 segundos.

**Paso 3 — Iteraciones (45 min).**
- v2-v3: Paleta Albatros y arreglos mobile (grid).
- v4-v5: Botones para "Exportar" e "Importar" JSON.
- v6-v7: Alertas visuales (<3 cupos = rojo) y accesibilidad ARIA.

**Paso 4 — Despliegue y Versionado.**
- Prueba cruzada en varios dispositivos (fix fuente fallback a Inter).
- Guardado en `tools/calculadora-cupos/v1.0.0/App.jsx`.
- Nuevo tag de Git: `v1.0.0`.

::interioriza
> Redefinir el "tiempo real" a un "cierre de caja diario" es vital.
> Como en un comercio: anotas las ventas locales todo el día.
> Al cerrar, envías el resumen al contador (el dashboard).
::

**Paso 5 — Conexión con Dashboard.**
- Se agrega botón "Cargar estado del día" al dashboard (versión 1.2.0).
- El dashboard procesa el JSON para mostrar lectura de cupos.
- Documentación en `docs/uso-calculadora-cupos.md`.

**Paso 6 — Entrega.**
- Acompañamiento a la coordinadora durante 15 minutos reales.
- Exporta JSON al final y carga en dashboard sin fricción.
- Ahorra 4 horas semanales de reportes manuales.

::pausa{titulo="Evaluación de Alcance"}
¿Por qué aceptar un JSON manual en lugar de exigir un backend?
- Cumple el objetivo de negocio dentro del tiempo disponible (2 horas).
- Valida el flujo antes de invertir tiempo en infraestructura compleja.
::
::/practica

::practica{titulo="Cómo decidí entre Claude Artifact y deploy real para el quiz vocacional"}
**Problema.** 
- Se requiere quiz de 30 preguntas para 240 estudiantes.
- **Dato clave:** Necesidad estricta de guardar datos para análisis.
- ¿Uso Artifact o hago un deploy real?

**Paso 1 — Hipótesis Artifact.**
- Prototipo en 30 minutos: rápido y funcional localmente.
- **Bloqueador:** Al cerrar pestaña, los datos se pierden.
- Juntar 240 archivos JSON a mano tomaría más de 6 horas. Inviable.

**Paso 2 — Deploy Real (4 horas).**
- Reutilizo el frontend del prototipo Artifact.
- Uso Vercel (hosting gratis) y Supabase (BD gratis).
- Añado una función serverless de 20 líneas para el POST.

**Paso 3 — Comparativa.**
- Artifact: 30 min, 0 persistencia colectiva, 6 h de consolidación.
- Deploy: 4 h, SQL integrado, automatizado y seguro.
- **Decisión (ADR-009):** Despliegue real (Vercel + Supabase).

::interioriza
> El Artifact es como un cuaderno borrador.
> Sirve perfecto para ideas y uso personal.
> Pero si necesitas recoger firmas de 240 personas, ocupas un buzón oficial (Deploy Real).
::

**Paso 4 — Ejecución y Validación.**
- Código React integrado con cliente Supabase (15 líneas).
- Deploy en Vercel logrado en 8 minutos.
- Smoke test exitoso con 5 voluntarios, guardando datos anónimos.

**Lección Final.**
- Los Artifacts brillan para prototipos o apps sin persistencia compartida.
- Si requieres analizar datos de múltiples usuarios de forma centralizada:
- ¡Debes usar un deploy real! El Artifact es mal producto para eso.

::pausa{titulo="Identificando Límites"}
¿Cuál es la señal indiscutible de que un Artifact ya no sirve?
- Cuando la aplicación requiere recolectar y agregar datos de varios usuarios de forma persistente.
::
::/practica
