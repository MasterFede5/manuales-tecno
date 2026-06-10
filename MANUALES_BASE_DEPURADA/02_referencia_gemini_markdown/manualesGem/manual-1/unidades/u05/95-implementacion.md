---
unidad: 5
seccion: implementacion
paginas_objetivo: 6
---

::implementacion{titulo="Implementación Albatros — Diseño completo del tratamiento del bebedero (proyecto integrador)"}
**Objetivo.** Producir un **dossier técnico-económico-ambiental** completo para implementar el sistema de tratamiento del bebedero escolar. Es el proyecto integrador final del case study: combina U2 (química del agua), U3 (química del aire), U5 (estequiometría, termodinámica, cinética, química verde) en una propuesta operativa lista para presentar a la dirección.

**¿Por qué hacerla?** Llevas 5 unidades trabajando con datos del bebedero. Esta implementación es donde **todo se conecta** y produces un entregable profesional que un comité escolar podría aprobar. Es también un excelente proyecto para portafolio universitario.

---

### Estructura del dossier (15-20 páginas)

**1. Resumen ejecutivo (1 página).** Para la directora: problema, solución, costo, plazo.

**2. Diagnóstico actual (2 páginas).** Resultados de las mediciones del bebedero (pH, dureza, cloro, contaminantes microbiológicos si tienes datos). Comparación con NOM-127.

**3. Propuesta de tratamiento (3 páginas).** Justificación técnica del sistema elegido entre 3 alternativas (cloración, ozonización, UV). Tabla comparativa con costos y huella.

**4. Cálculos estequiométricos (2 páginas).** Dosificación, tiempos de contacto, balances de masa.

**5. Análisis termodinámico-cinético (2 páginas).** Espontaneidad de las reacciones, velocidades esperadas, condiciones óptimas.

**6. Análisis verde (2 páginas).** Aplicación de los 12 principios. E-factor calculado. Huella de carbono.

**7. Diseño operativo (2 páginas).** Materiales, equipos, layout, mantenimiento. Sensor IoT propuesto (de U2.7).

**8. Análisis económico (1-2 páginas).** Inversión inicial, costos operativos por L, retorno (ahorro vs comprar agua embotellada).

**9. Plan de implementación (1 página).** Cronograma a 3 meses, responsables, hitos.

**10. Conclusiones y siguientes pasos (1 página).**

**Anexos:** datos crudos, hojas de cálculo, fotos del bebedero actual.

### Materiales

- Procesador de texto (Google Docs, Word).
- Hoja de cálculo (la bitácora digital de U0 + el sensor IoT de U2 + cálculos verdes de U5).
- Acceso a precios (Mercado Libre, Home Depot, distribuidores químicos).
- Datos del bebedero (puedes usar los del manual o tomar datos reales de tu escuela).

### Pasos sugeridos

**1. Define el alcance.** ¿Es para 1 bebedero, varios, toda la escuela? Esto cambia las dimensiones.

**2. Recopila datos.** Si la escuela permite, mide pH, dureza, cloro residual durante 1 semana. Si no, usa los datos del manual.

**3. Compara 3 alternativas.** Cloración, ozonización, UV. Tabla con: costo inicial, costo operativo, energía, huella, viabilidad.

**4. Elige y justifica.** Argumento técnico con base en la comparación.

**5. Detalla el diseño.** Diagrama del sistema, dosificadores, tubería, mantenimiento.

**6. Cuantifica todo.** No dejes parámetros en "más o menos". Pesos, mL/día, kWh/mes.

**7. Anticipa objeciones.** "¿Qué si falla el sensor?", "¿qué si se acaba el cloro?". Plan B.

**8. Presenta a un panel.** Familia, docente, dirección.
::/implementacion

::visual{tipo="interfaz" descripcion="Mockup del dossier final mostrando portada con título 'Sistema de Tratamiento del Bebedero Escolar — Diseño Verde Integral', tabla de contenidos con las 10 secciones, gráficas de comparación de alternativas (cloración vs ozono vs UV) con barras de costo y huella, diagrama del sistema final con sensor IoT incluido, y pie con autor y fecha." paginas="1" src="../manualesGem/assets/visuales/manual-1/u05/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

Dossier completo (PDF o impreso) + presentación oral de 10 minutos a un panel (puede ser el grupo escolar, padres de familia, docentes).

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Diagnóstico** | datos vagos | datos del manual aplicados | datos propios + comparación con norma |
| **Justificación técnica** | una opción sin alternativas | 2 alternativas comparadas | 3+ alternativas con métricas |
| **Cálculos** | sin verificación | correctos pero limitados | completos: estequiometría + termo + cinética + verde |
| **Análisis económico** | sin números | costo operativo | inversión + operación + retorno |
| **Presentación** | lectura del documento | comunicación clara | diálogo con respuestas a Q&A |

### Reto bonus (+1 punto)

Implementa al menos **un** componente del sistema en versión prototipo: el sensor IoT (U2), el dosificador con bomba peristáltica (U5), o el dashboard de monitoreo. Documéntalo con video.

---

**Cierre.** Si llegaste hasta aquí, has hecho una verdadera **ingeniería química verde**. La directora debería estar impresionada. Más importante: **tienes evidencia de portafolio** para presentar en cualquier universidad o programa de ciencias.

---

### Hitos intermedios

| Sprint | Entregable | Día |
|---|---|---|
| 1 | Diagnóstico (sec. 1-2) con datos del bebedero recopilados o tomados del manual | 5 |
| 2 | Comparación de 3 alternativas con tabla técnica-económica (sec. 3-4) | 12 |
| 3 | Análisis termodinámico-cinético + análisis verde + diseño operativo (sec. 5-7) | 20 |
| 4 | Análisis económico, plan de implementación y presentación oral lista (sec. 8-10) | 30 |

### Reto bonus extendido (+2 puntos cada uno)

1. **Reto A:** entrega un Anexo G "Sensibilidad económica" donde modificas los costos de cloro, electricidad y agua embotellada en ±30 % y calculas cómo cambia el retorno. Útil cuando el precio de los insumos sube como en la práctica resuelta de la cal.
2. **Reto B:** integra al dossier una sección de "Estrategia de educación a la comunidad escolar" con cartelería, charla a padres y campaña en redes con base en los datos del proyecto.
3. **Reto C:** simula el sistema en un software libre (OpenLCA, EPANET o incluso una hoja con curvas de descomposición) para validar dosis y tiempos antes de la presentación al comité.
::/implementacion
---

::albatros{titulo="Sprint corto — pitch ejecutivo de 3 minutos al consejo escolar" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** Si solo tuvieras 3 minutos frente al consejo escolar para vender tu dossier, ¿qué dirías para asegurar la aprobación del proyecto?

**Lo que harás.**
1. Recupera tu dossier integrador.
2. Selecciona 3 cifras clave (costo por 1000 L, CO₂ ahorrado al año, plazo de implementación).
3. Estructura un pitch en 5 partes (problema · diagnóstico · propuesta · costo-beneficio · llamado a la acción).
4. Practícalo en voz alta, cronometrando.
5. Ensaya respuestas a 3 objeciones probables: presupuesto, mantenimiento, riesgo de fallo.
6. Graba el pitch final en video.

**Materiales.** Dossier · cronómetro · celular para grabar · espejo o compañero/a.

**Entregable.** Video de 3 minutos + guion escrito + lista de 3 objeciones con respuestas preparadas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Estructura | sin estructura | 5 partes presentes | 5 partes con tiempos cuadrados |
| Datos | 0 cifras | 1 cifra | 3 cifras clave memorables |
| Manejo de objeciones | sin preparar | 1 objeción | 3 objeciones con respuesta basada en datos |
::/albatros
