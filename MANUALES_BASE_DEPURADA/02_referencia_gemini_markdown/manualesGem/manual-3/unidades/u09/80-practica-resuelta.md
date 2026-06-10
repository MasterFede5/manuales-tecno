---
unidad: 9
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 09

::practica{titulo="Auditar un examen de práctica generado por tu tutor IA"}
**Problema.** Le pediste a tu tutor que generara un examen de 10 reactivos de Historia para tus compañeras y compañeros del salón. El examen quedó listo en 40 segundos. Antes de compartirlo, decides auditarlo bajo los seis criterios de la Unidad 9. **¿Está listo para circular o necesita ajustes?**

**Paso 1 — Datos.**
- 10 reactivos opción múltiple sobre "Revolución Mexicana".
- 4 personajes mencionados: Madero, Villa, Zapata, Carranza.
- 0 mujeres mencionadas. 0 personajes indígenas referidos por nombre propio.
- 1 reactivo afirma "Madero fue asesinado por Huerta en 1913" (verificable, correcto).
- 1 reactivo afirma "Villa nació en 1878" (verificable, fecha exacta es 1878 — correcto).
- El examen pide al final el correo del estudiante "para enviar resultado".

**Paso 2 — Estrategia.** Aplicar los seis filtros de la unidad en orden. Para cada uno, decidir: pasa / requiere ajuste / no pasa.

**Paso 3 — Auditoría.**

| Filtro | Hallazgo | Decisión |
|---|---|---|
| 9.1 Sesgos | 0 mujeres en 4 personajes; sub-representación clara | Ajuste — agregar Adelitas, Hermila Galindo, Carmen Serdán; balance |
| 9.2 Privacidad | Pide correo personal sin política | No pasa — eliminar el correo o sustituir por entrega anónima |
| 9.3 Derechos de autor | Reactivos parafraseados; ningún texto literal de libro | Pasa — pero declarar "examen asistido por IA" |
| 9.4 Deepfakes | No aplica (texto, no imagen ni voz) | Pasa |
| 9.5 Impacto educativo | Es práctica voluntaria, no calificación oficial | Pasa con declaración de uso |
| 9.6 Marco legal | Procesa correos = LFPDPPP. Lo evita el ajuste de 9.2 | Pasa con ajuste |

**Paso 4 — Razonamiento.**
- Dos hallazgos exigen cambios obligatorios (sesgo de selección + privacidad de correos).
- Cuatro hallazgos pasan con la condición de **declarar el uso de IA** y **aplicar entrega anónima**.
- El tiempo total de auditoría: ~10 minutos. El costo de no hacerla: una compañera puede sentirse no representada (sesgo) o un correo personal puede terminar en logs de un proveedor sin consentimiento (privacidad).

**Paso 5 — Respuesta.** El examen **no está listo** en su versión original. Aplicas dos ajustes:
1. **Re-prompt al tutor:** *"Reescribe el examen incluyendo al menos 3 personajes femeninas o indígenas, mantén dificultad equivalente."*
2. **Sustituye el campo "correo"** por un código aleatorio que cada estudiante anota en su libreta.
3. **Agregas el pie:** *"Examen asistido por IA · revisado y editado por [tu nombre] · sin recolección de datos personales."*

**Paso 6 — Verificación.** Vuelves a correr la tabla con la nueva versión. Los 6 filtros pasan. Compartes el examen al grupo de WhatsApp del salón.

**Lección.** Una auditoría ética de IA no toma horas: toma 10 minutos disciplinados con una checklist como esta. La diferencia entre "creador responsable" y "creador descuidado" es **hacerla siempre**, no solo cuando se acuerda.
::/practica
