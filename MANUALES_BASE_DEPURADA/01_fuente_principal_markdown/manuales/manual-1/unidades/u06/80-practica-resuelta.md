---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Auditoría de seguridad del sistema del bebedero

::practica{titulo="Auditoría completa de cumplimiento legal y de seguridad del sistema"}
**Problema.** La directora pide una auditoría del cumplimiento normativo del sistema de tratamiento del bebedero. Identifica los **riesgos** principales, las **NOM** aplicables y propón un **plan de remediación** si encuentras faltantes.

**Inventario actual:**
- Bidón de hipoclorito al 5 % (50 L) en el almacén del comedor, sin pictogramas.
- FDS del cloro: no disponible.
- Bitácora de generación de residuos: no existe.
- Última análisis del agua: hace 1 año.
- Personal capacitado en manejo de químicos: ninguno.
- EPP (guantes, gafas): no hay.

---

**Paso 1 — Identificar peligros del cloro al 5 %.**

Según FDS estándar (CAS 7681-52-9):
- **C** Corrosivo: pH 11-13, daña piel y ojos.
- **T** Tóxico al ingestión.
- Si se mezcla con ácidos: libera Cl₂(g) tóxico.
- Si se mezcla con amoniaco: forma cloraminas tóxicas.

Pictogramas SGA aplicables: **GHS05** (Corrosivo), **GHS09** (Peligro ambiental).

**Paso 2 — Evaluar cumplimiento contra NOM.**

| NOM | Estado actual | Evaluación |
|---|---|:---:|
| NOM-018-STPS | Sin pictogramas, sin FDS, sin capacitación | ❌ Incumplimiento total |
| NOM-052-SEMARNAT | Sin bitácora ni gestión de lodos | ❌ Incumplimiento |
| NOM-127-SSA1 | Análisis hace 1 año (debería ser trimestral) | ⚠ Incumplimiento |
| NOM-010-STPS | TLV de cloro probablemente OK (no hay quejas de olor) | ✓ OK por ahora |

**Paso 3 — Estimar sanciones potenciales.**

- **Inspección STPS:** Detectaría incumplimiento de NOM-018 (multa típica \$50,000-\$200,000) y NOM-052 (multa típica \$100,000-\$500,000).
- **Riesgo total:** \$150,000 a \$700,000 MXN.
- **Riesgo crítico:** Accidente con cloro sin medidas preventivas implica **responsabilidad civil y penal** para el director.

::interioriza
> **Analogía:** Administrar estos químicos sin cumplir las normas es como manejar un transporte escolar sin frenos. Si algo falla, el daño no es solo la multa de tránsito, es la vida de los alumnos y tu propia libertad.
::

**Paso 4 — Plan de remediación (90 días).**

| Acción | Responsable | Plazo | Costo |
|---|---|:---:|:---:|
| Imprimir y pegar etiquetas SGA | Coordinador | 7 días | \$200 |
| Descargar e imprimir FDS del cloro | Coordinador | 7 días | \$50 |
| Comprar EPP básico (guantes, gafas, mascarilla) | Coordinador | 15 días | \$1,500 |
| Capacitación de 2 horas al personal del comedor | Externo certificado | 30 días | \$3,000 |
| Crear bitácora de residuos | Coordinador | 30 días | \$0 |
| Contratar empresa autorizada para residuos | Director | 60 días | \$1,500/año |
| Programar análisis trimestral del agua | Director | 60 días | \$8,000/año |
| Simulacro de emergencia química | Personal capacitado | 90 días | \$0 |

**Costo de remediación total año 1: \$14,250 MXN.**

**Paso 5 — Identificar incompatibilidades de almacenamiento.**

Verificar que el bidón de cloro **NO** esté almacenado junto a:
- Ácidos (libera Cl₂ tóxico).
- Amoniaco doméstico (forma cloraminas tóxicas).
- Productos de limpieza con muriático (incompatible).
- Materia orgánica (oxida y libera Cl).
- Metales reactivos (corrosión).

Distancia mínima: 2 metros, idealmente con barrera física.

**Paso 6 — Plan de emergencia.**

Si hay derrame:
1. Evacuar el área y ventilar.
2. Usar EPP completo.
3. Contener con material absorbente (arena, no sustancias orgánicas).
4. Recoger en envase resistente a la corrosión.
5. Etiquetar como residuo CT.
6. Reportar a empresa de manejo.

Si hay ingestión accidental:
1. **NO inducir vómito** (causa más daño esofágico).
2. Diluir con leche o agua si la persona está consciente.
3. Llamar al **TOXICA Tel. 800-MXN-TOXI** o servicio de emergencia.
4. Llevar la FDS al hospital.

**Paso 7 — Conclusión y entregable a la directora.**

> El sistema actual del bebedero **está fuera de norma** en al menos 3 NOM (018, 052, 127).
> 
> - **Riesgos:** Sanción de hasta \$700,000 MXN y grave peligro para la salud de los estudiantes.
> - **Solución:** Plan de remediación de 90 días con inversión de \$14,250 MXN (cumplimiento total).
> - **Beneficio:** Esta inversión equivale a solo el **2 % del riesgo de sanción mínima**. Es el costo de hacer las cosas bien.

::pausa{titulo="Active Recall: Justificación de inversión"}
1. ¿Cómo le explicarías a la directora que gastar \$14,250 MXN es en realidad un ahorro para la escuela?
2. ¿Cuál sería la NOM más crítica a resolver de forma inmediata y por qué?
::

::/practica

---

::practica{titulo="Diseño de etiqueta SGA y leyenda H/P para el bidón de cloro escolar"}
**Problema.** El bidón de hipoclorito al 5 % del comedor llegó sin etiqueta. Diseña la etiqueta SGA completa que debe portar, con pictogramas, palabra de advertencia, frases H y P, y datos del proveedor. Justifica cada elemento con base en NOM-018-STPS.

**Paso 1 — Identifica peligros.**
- pH 11–13 → corrosivo a piel y ojos (categoría 1B).
- Reacción con ácidos libera Cl₂(g) tóxico.
- Tóxico para organismos acuáticos.

**Paso 2 — Selecciona pictogramas SGA.**
- **GHS05** (corrosivo): rombo con dos tubos derramando líquido sobre superficie y mano.
- **GHS09** (peligro ambiental): rombo con árbol y pez muertos.

**Paso 3 — Determina palabra de advertencia.**
La categoría más restrictiva es 1B → palabra: **"Peligro"** (no "Atención").

**Paso 4 — Selecciona frases H (peligro).**
- H290 — Puede ser corrosivo para los metales.
- H314 — Provoca quemaduras graves en la piel y lesiones oculares graves.
- H400 — Muy tóxico para los organismos acuáticos.

**Paso 5 — Selecciona frases P (precaución).**
- P234 — Conservar únicamente en envase original.
- P260 — No respirar el polvo / humo / gas / vapores.
- P273 — Evitar liberación al medio ambiente.
- P280 — Llevar guantes, ropa y protección ocular adecuados.
- P301 + P330 + P331 — En caso de ingestión, enjuagar la boca; **no** provocar el vómito.
- P305 + P351 + P338 — En caso de contacto ocular, enjuagar con cuidado durante varios minutos. Quitar lentes de contacto.
- P310 — Llamar inmediatamente a un centro de toxicología.

**Paso 6 — Datos obligatorios del proveedor y producto.**
- Nombre comercial: Hipoclorito de sodio al 5 %.
- Identificador: CAS 7681-52-9.
- Proveedor: [nombre, dirección, teléfono y correo].
- Cantidad: 50 L · Fecha de elaboración · Lote.

**Paso 7 — Tamaño y formato.**
- Etiqueta de mínimo 100 × 75 mm (NOM-018 art. 6.5 para envases de 50 L).
- Pictogramas con borde rojo, fondo blanco, símbolo negro.
- Texto en español, legible a 1 m.
- Material resistente al agua y al cloro mismo (recomendado: vinilo laminado).

::interioriza
> **Analogía:** Una etiqueta SGA es como la "cédula de identidad y receta médica" del producto. Te dice quién es, de qué es capaz y qué hacer en caso de emergencia.
::

**Paso 8 — Conclusión.**
> La etiqueta cumple NOM-018-STPS si incluye:
> - Dos pictogramas (GHS05 y GHS09) y palabra "Peligro".
> - Tres frases H y siete frases P.
> - Datos del proveedor, lote y fecha.
>
> **Inversión:** ≈ \$30 MXN por etiqueta (despreciable frente a sanciones de \$50k–\$200k).

::pausa{titulo="Active Recall: Etiquetas y seguridad"}
1. Si un empleado no sabe leer, ¿qué elementos de la etiqueta SGA le advertirían del peligro?
2. ¿Por qué es vital incluir las frases P (precaución) además de las frases H (peligro)?
::

::/practica

---

::practica{titulo="Clasificación CRETIB de los lodos del ablandamiento del bebedero"}
**Problema.** El proceso de cal-soda para reducir dureza genera 5 kg semanales de lodos sólidos. Clasifica el residuo según CRETIB (NOM-052-SEMARNAT), determina si requiere gestión como RP y calcula el costo anual de gestión.

**Paso 1 — Caracteriza el lodo.**
Composición esperada del lodo de ablandamiento:
- 60 % CaCO₃ (sólido inerte).
- 20 % Mg(OH)₂.
- 10 % humedad.
- 10 % otros (sales, materia orgánica filtrada).
- pH del lodo: 9–10 (básico por exceso de cal).

**Paso 2 — Aplica las pruebas CRETIB.**
- **C (Corrosivo):** pH 9–10 → **NO corrosivo** (umbral CRETIB > 12.5 o < 2).
- **R (Reactivo):** ningún componente reacciona violentamente con agua o aire → **NO**.
- **E (Explosivo):** ninguno → **NO**.
- **T (Tóxico):** revisar CRT al laboratorio. En general, lodos de ablandamiento no rebasan límites de metales pesados → **NO** salvo que la cisterna haya recibido tubería de plomo.
- **I (Inflamable):** sólido no inflamable → **NO**.
- **B (Biológico-infeccioso):** no aplica → **NO**.

**Paso 3 — Resultado de clasificación.**
> El lodo **no es residuo peligroso** si la prueba T (toxicidad por lixiviado) sale negativa.
> Es un residuo de **manejo especial**, regulado por legislación estatal.

**Paso 4 — Considera el caso T positivo.**
- Si el laboratorio detecta plomo > 5 mg/L (umbral NOM-052), el lodo es **RP**.
- Esto ocurre comúnmente si la cisterna o tinaco tienen soldaduras antiguas.
- Se debe gestionar como RP-CT con NOM-052.

**Paso 5 — Costo de gestión escenario "no peligroso".**
- Generación: 5 kg/sem × 52 sem = 260 kg/año.
- Disposición (manejo especial): ≈ \$3 MXN/kg → **\$780 MXN/año**.
- **Reuso:** Mejorador de suelos ácidos en jardín escolar (costo cero y aporta al ciclo verde).

**Paso 6 — Costo de gestión escenario "peligroso".**
- Empresa autorizada NOM-052: ≈ \$25–40 MXN/kg.
- Costo total: 260 kg/año × \$30 = **\$7,800 MXN/año** (10× más caro).

::interioriza
> **Analogía:** Clasificar CRETIB es como hacer un "triage" en emergencias. Decide si el residuo requiere cuidados intensivos (confinamiento peligroso y costoso) o reposo en casa (manejo especial o reuso, económico y sustentable).
::

**Paso 7 — Recomendación.**
> 1. Realiza la prueba CRT inicial (≈ \$1,500 MXN, una sola vez).
> 2. Si es negativa: **reutiliza** los lodos en el jardín (máx. 100 g/m²/año).
> 3. Si es positiva: contrata empresa NOM-052.
> 4. Documenta todo en bitácora (fecha, peso y destino).
>
> Esto asegura el cumplimiento legal y aplica el principio 1 de química verde: **prevención de residuos**.

::pausa{titulo="Active Recall: Gestión de lodos CRETIB"}
1. ¿Por qué una soldadura antigua en un tinaco puede multiplicar por 10 el costo de gestión de los lodos?
2. Si los lodos son clasificados como "no peligrosos", ¿qué beneficios adicionales tiene reutilizarlos en los jardines de la escuela?
::

::/practica
