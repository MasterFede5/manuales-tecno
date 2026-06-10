# Reporte pedagógico — Manuales Albatros

Generado tras la división por semestres y la creación del front/back matter.
Contiene el plan concreto para llevar cada unidad al **60 % práctico** (objetivo
del autor), respetando el `manual-spec`.

---

## 1. Estado actual (post-división)

### 1.1 Cobertura del manual-spec

| Aspecto | Estado |
|---|---|
| §2 Tamaño carta exacto (215.9 × 279.4 mm) | ✓ los 10 PDFs cumplen |
| §3 Front matter por manual | ✓ duplicado por semestre (portada, cartas, mapa, hilo, competencias, diagnóstica) |
| §3 Back matter por manual | ✓ duplicado por semestre (cierre, material extra, glosario, bibliografía, índice analítico) |
| §4 Estructura mínima por unidad | ✓ los 12 archivos esperados en cada `uXX/` |
| §6 Catálogo de 12 tipos de actividad | ⚠ promedio 8–11/12 por unidad (mínimo §6 es 3, sobrado) |
| §7 Mini-actividades cada 4–6 pp | ✓ 3–9 pausas por unidad |
| §8 Visuales mínimos por unidad | ✓ promedio 8–13 visuales por unidad |
| §10 Bloques obligatorios por unidad | ✓ cero unidades con faltantes |
| §11.7 Descripción ≥ 50 chars en cada `::visual{}` | ✓ todos los 511 cumplen |
| §1 Rango 350–450 pp por manual | ⚠ excedido por la duplicación del front/back matter por semestre |

### 1.2 % práctico aproximado (por bytes de bloques)

| Manual | Promedio actual | Brecha al 60% |
|---:|---:|---:|
| M1 | 38.6% | 21.4 pp |
| M2 | 40.7% | 19.3 pp |
| M3 | 43.3% | 16.7 pp |
| M4 | 41.7% | 18.3 pp |
| M5 | 45.9% | 14.1 pp |

> El supervisor previo (`supervision-monitor.ps1`) mide por **páginas asignadas
> a archivos prácticos** y arroja 44–52 %. Aquí medimos por **bytes dentro de
> bloques pareados** que es más estricto y se acerca más al criterio "tiempo
> de aula que el estudiante practica".

---

## 2. Plan para subir cada unidad al 60 % práctico

### 2.1 Estimación

- Páginas promedio por unidad: ~40
- Cada punto porcentual de práctica ≈ **0.4 pp**
- Brecha promedio: 17 pp → **~7 pp prácticas extra por unidad**
- 43 unidades × 7 pp = **~300 pp prácticas nuevas a redactar**

Esto es **redacción de contenido nuevo**, no transformación mecánica. No se
puede ejecutar sin involucrar al autor.

### 2.2 Estrategia de "menor esfuerzo / mayor impacto"

Para cada unidad bajo 60 %, agregar **uno** de estos archivos (en orden de
preferencia):

1. **`81-banco-extra.md`** — 4 pp con 6–8 ejercicios adicionales del catálogo
   §6 que NO estén ya cubiertos en la unidad (cubre cobertura de catálogo
   y sube práctica).
2. **`84-mini-proyecto.md`** — 2 pp con un mini-proyecto Albatros de 30
   minutos que conecte con el case study.
3. **`86-tips-extra.md`** — 1 pp con 3–5 tips del autor en bloques
   `::interioriza::` (sube ligeramente práctica y mucho la calidad
   pedagógica).
4. **Subir el peso del taller existente** (`93-taller.md`) de 2 pp a 4 pp
   agregando un segundo bloque `::albatros::` con un subtipo distinto.

### 2.3 Plan unidad por unidad

| Manual | Unidad | %P actual | Brecha | Recomendación principal |
|---|---|---:|---:|---|
| M1 | u00 | 44.3% | 15.7 pp | `81-banco-extra.md` (6 pp) + `86-tips-extra.md` (1 pp) |
| M1 | u01 | 29.9% | 30.1 pp | `81-banco-extra.md` (8 pp) + `84-mini-proyecto.md` (4 pp) |
| M1 | u02 | 35.5% | 24.5 pp | `81-banco-extra.md` (6 pp) + ampliar taller (2 pp) |
| M1 | u03 | 38.5% | 21.5 pp | `81-banco-extra.md` (6 pp) + `86-tips-extra.md` (2 pp) |
| M1 | u04 | 42.2% | 17.8 pp | `81-banco-extra.md` (5 pp) |
| M1 | u05 | 34.8% | 25.2 pp | `81-banco-extra.md` (8 pp) + `84-mini-proyecto.md` (2 pp) |
| M1 | u06 | 45.2% | 14.8 pp | `81-banco-extra.md` (4 pp) + `86-tips-extra.md` (2 pp) |
| M2 | u01–u09 | 35–46% | 14–25 pp | misma estrategia, archivos extra por unidad |
| M3 | u01–u09 | 38–48% | 12–22 pp | misma estrategia, énfasis en mockups de interfaz |
| M4 | u01–u10 | 38–44% | 16–22 pp | misma estrategia, énfasis en dashboards y agentes |
| M5 | u01–u08 | 39–53% | 7–21 pp | misma estrategia, énfasis en notebooks Python |

Ver detalle completo unidad por unidad en
`docs/diagnostico-pedagogico.md`.

---

## 3. Cobertura del catálogo §6 — tipos por reforzar

Tipos menos usados en el conjunto (oportunidad de añadirlos en los archivos
extra):

| Tipo | Cobertura | Cuándo añadir |
|---|---|---|
| `act-puzzle` | bajo en M3-M5 | crucigrama de vocabulario al final de unidad |
| `act-mindmap` | bajo en M5 | mapa mental abierto para cerrar unidad |
| `act-label` | bajo en M2 (después de u05) | diagramas para etiquetar de la física |
| `act-order` | bajo en M5 | ordenar pasos de un pipeline ML |

---

## 4. Sugerencia de orden de ejecución

1. **Semestre 1 de M5** (ya más cerca del 60% — fácil cerrar). Empezar por u01.
2. **Semestre 2 de M5** (similar). 
3. **Manual 3** completo (43% promedio, ideal para terminar primero la rama IA).
4. **Manual 4** completo.
5. **Manual 2** completo.
6. **Manual 1** completo (mayor brecha — dejarlo para cuando el flujo esté
   afinado).

Tiempo estimado por unidad si el autor redacta 4 pp/día: **2 días de
redacción + 1 día de revisión**. Para las 43 unidades: ~130 días de trabajo
distribuido.

Alternativa: usar el script `scaffold_archivo_extra.py` (pendiente de
construir) para generar el **andamiaje** de cada archivo extra con bloques
vacíos del catálogo y dejar solo el texto al autor — reduce el tiempo a
~½ día por archivo.

---

## 5. Verificación final cuando se cierre cada unidad

Por cada unidad terminada, correr:

```
python diagnostico_pedagogico.py
```

y validar que su fila aparezca con **% práctico ≥ 60 %**. Re-correr build:

```
python build_semestres.py <N>
python print_to_pdf.py --manual <N> --all-semesters
python verify_spec.py
```

---

## 6. Lo que YA quedó hecho mecánicamente

✓ División de los 5 manuales en 10 (uno por semestre cada uno) en
  `dist/manual-N-sem-X.{html,pdf}`.

✓ Estructura `manuales/manual-N/semestre-X/` con 13 archivos por semestre
  (portada, cartas, mapa, hilo, competencias, diagnóstica, cierre, material
  extra, glosario, bibliografía, índice analítico, README).

✓ Modificación de `build/converter.py` para integrar el front/back matter
  por semestre y asignar IDs estables a cada `::visual{}`.

✓ 511 prompts visuales individuales en `assets/prompts-visuales/`, uno por
  archivo, agrupados por `manual-N/sem-X/uXX/<ID>.md`, con `inject-map.json`.

✓ Carpetas destino `assets/visuales/manual-N/uXX/` listas para recibir las
  imágenes generadas; al re-buildear se inyectan automáticamente por ID.

✓ Verificación PDF: tamaño carta exacto en los 10 PDFs.

---

## 7. Lo que requiere intervención del autor (FASE 2)

- Redactar los `81-banco-extra.md` por unidad para subir a 60 % práctico.
- Decidir si los excesos de páginas (semestres ~250-400 pp en lugar de ~200)
  son aceptables o si hay que apretar el front matter.
- Generar las 511 imágenes con los prompts y dejarlas en `assets/visuales/`
  para inyección automática.
- Revisar los 65 visuales anidados pendientes en
  `assets/prompts-visuales/anidados-pendientes.md`.
