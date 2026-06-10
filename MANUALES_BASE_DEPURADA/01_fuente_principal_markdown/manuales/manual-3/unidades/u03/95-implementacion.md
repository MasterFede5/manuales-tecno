---
unidad: 3
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Tu banco personal de 20 prompts versionados"}
**Objetivo.** Construir un **banco de prompts** propio que cubra los 20 casos de uso más recurrentes de tu vida académica/profesional. Cada prompt seguirá la anatomía R-T-C-R-F-E completa, estará versionado y será reutilizable. Es el activo más valioso que te llevas de esta unidad.

**¿Por qué hacerlo?** Después de unos meses de uso casual, descubrirás que **escribes los mismos prompts una y otra vez** —resumir un PDF, generar plan de estudio, redactar correo formal, etc. En vez de improvisarlos cada vez, tener un banco bien organizado te ahorra horas y mejora consistencia. Es el primer paso para volverte usuario potente.

---

### Materiales y herramientas

- **Notion** o **Airtable** o **Google Sheets** para almacenar prompts (gratis).
- Acceso a tu plataforma elegida (Claude/ChatGPT) para probar cada prompt.
- 4 horas en 2 sesiones.

### Pasos

1. **Identifica tus 20 casos de uso recurrentes.** Categorías sugeridas:
   - **Estudio (5 prompts):** resumen de PDF, plan de estudio, generación de quizzes, explicación de concepto, traducción técnica.
   - **Redacción (5 prompts):** correo formal, mensaje a profesor, ensayo, post LinkedIn, reseña de libro.
   - **Productividad (5 prompts):** to-do prioritizado, plan semanal, brainstorming, decisiones (pros/cons), reflexión diaria.
   - **Creativo (5 prompts):** ideas para proyecto, guion de video, dibujo conceptual, copy de marca, eslogan.
2. **Para cada prompt, escribe v1 con anatomía R-T-C-R-F-E completa.** Nombra el prompt con convención: `[Categoría] [Caso de uso] - v1`. Ejemplo: `[Estudio] Resumen PDF académico - v1`.
3. **Prueba cada uno con caso real.** Documenta tiempo de respuesta y calidad subjetiva (1-5).
4. **Itera al menos 2 veces** los prompts más críticos hasta llegar a v3.
5. **Estructura tu Notion/Airtable así:**
   - Columnas: Nombre · Categoría · Versión · Texto del prompt · Casos de prueba · Calidad (1-5) · Última iteración · Modelo recomendado.
6. **Crea atajos.** En Notion, marca tus 5 favoritos. En el celular, agrégalos al portapapeles (apps como Phrase Express o macros de iOS).
7. **Comparte con un compañero** y pídele feedback de los 5 que más usaría.

::visual{tipo="ilustracion" descripcion="Captura de Notion con base de datos de prompts: tabla con columnas Nombre/Categoría/Versión/Texto/Calidad/Modelo. 20 filas pobladas con prompts del estudiante. Filtros activos por categoría. Vista detallada de un prompt expandida mostrando las 6 capas R-T-C-R-F-E. A la derecha, app móvil con accesos directos a los 5 favoritos. Recuadro: 'banco vivo, agregas y mejoras semanalmente'." paginas=0.5}

---

### Entregable

1. **Link al banco** (Notion compartida, Airtable público o Google Sheets).
2. **PDF/PNG** con las 5 categorías y los nombres de los 20 prompts.
3. **Reporte de 1 página:**
   - ¿Cuáles 3 prompts crees que más vas a usar?
   - ¿Qué patrones aparecen en los 20 (todos requieren rol específico, todos piden formato JSON, etc.)?
   - ¿Cuál te costó más iterar y por qué?
   - ¿Compartirías tu banco públicamente o lo mantendrías privado? Razón.
4. **Captura** de tu app de prompts en uso real (un día normal).

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Cantidad de prompts** | < 12 | 15-19 | 20+ con variedad |
| **Anatomía completa** | inconsistente | mayoría con 4+ capas | 100% con 6 capas |
| **Iteración documentada** | sin versiones | 2 iteraciones promedio | 3+ iteraciones en críticos |
| **Estructura del banco** | desorganizado | categorías visibles | filtros, etiquetas, búsqueda fluida |
| **Reflexión** | superficial | identifica patrones | discute trade-offs y cómo evolucionará |
| **Compartir** | privado total | con un compañero | público con engagement |

### Hitos intermedios

| Sprint | Duración | Mini-entregable | Verificación |
|---|---|---|---|
| **S1 — Inventario** | 30 min | Lista de los 20 casos de uso recurrentes en hoja | Validar con un compañero que cubra estudio + redacción + productividad + creativo |
| **S2 — v1 de los 20** | 90 min | 20 prompts con anatomía RTCRFE en Notion/Airtable | Cada prompt tiene las 6 capas explícitas |
| **S3 — Pruebas** | 60 min | Cada prompt corrido al menos una vez con caso real + score 1-5 | Tabla con scores; identificar los 5 que requieren iteración |
| **S4 — Iteración y atajos** | 60 min | Los 5 críticos llegan a v3; 5 favoritos en atajos del celular | Probar atajos en uso real durante un día |

### Reto bonus extendido

1. **Reto del prompt insignia.** Identifica **el prompt que más usarás** y eleva su calidad a v5: agrega few-shot con 3 ejemplos, structured output completo y restricciones que descubriste por uso. Documenta cada versión.
2. **Reto de templates.** Convierte 5 de tus prompts en **templates con variables** ({{materia}}, {{nivel}}, {{contexto}}). Crea un mini-formulario en Tally o Notion que rellene los huecos automáticamente.
3. **Reto del banco compartido.** Junta tu banco con el de 3 compañeros (60 prompts en total). Curen como equipo los **mejores 30** y publiquen el "Banco Albatros v1" con créditos compartidos.
::/implementacion

---

::albatros{titulo="Caso real — diagnostica el prompt de tu compañero" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Puedes mejorar un prompt ajeno en 10 minutos sin cambiar su intención original?

**Lo que harás.**
1. **Intercambia** con un compañero su prompt más usado (uno que él ya tenga en su banco).
2. **Audita** el prompt: marca cuáles de las 6 capas R-T-C-R-F-E están y cuáles faltan o son débiles.
3. **Detecta antipatrones** (vaguedad, contradicciones, sobrecarga, suposiciones implícitas).
4. **Reescribe** una versión mejorada respetando la intención original. Documenta qué cambiaste y por qué.
5. **Devuelvan** los prompts mejorados. Cada uno corre v1 vs v_compañero con un caso real y compara con la rúbrica de 5 criterios del taller.
6. **Cierre:** anoten qué patrón de mejora se repitió en ambos prompts. Ese patrón es ahora una regla para tu banco.

**Materiales.** Acceso a su plataforma base, dos prompts reales, hoja de cálculo para comparar.

**Entregable.** a) tabla con auditoría del prompt original (6 capas + antipatrones), b) versión mejorada con cambios marcados, c) tabla comparativa v1 vs mejorada con scoring, d) reflexión sobre qué patrón de mejora se repitió.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Auditoría | identifica 1-2 huecos | identifica 4 huecos | identifica todos los huecos + antipatrones |
| Reescritura | cambios cosméticos | mejora con anatomía | mejora con anatomía + few-shot/CoT cuando aporta |
| Comparativa | impresionista | scoring de 5 criterios | scoring + análisis cualitativo |
::/albatros
