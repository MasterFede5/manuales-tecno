---
name: manual-architecture-builder
description: "Replica, crea o audita la arquitectura de construccion de manuales Albatros basada en MANUALES_BASE_DEPURADA. Use cuando se deba crear una carpeta base fiel para nuevos manuales, ordenar fuentes Markdown, referencias, diseno, assets visuales, prompts, motor de compilacion, documentacion pedagogica y fuentes externas sin mezclar contenido ni perder imagenes."
---

# Manual Architecture Builder

## Proposito
Usar esta skill para construir o auditar la distribucion de carpetas de los manuales Albatros. Esta skill no redacta sesiones completas; controla la arquitectura: donde van fuentes, referencias, diseno, imagenes, prompts, scripts de compilacion, reportes y fuentes externas.

Para redaccion pedagogica usar las skills `manual-session-orchestrator`, `manual-session-writer`, `manual-ficha-tecnica`, `manual-code-practice` y `manual-session-validator`.

## Flujo obligatorio
1. Ubicar la raiz del proyecto y, si existe, tomar `MANUALES_BASE_DEPURADA` como referencia primaria.
2. Antes de crear o mover estructura, leer `references/distribucion.md`.
3. Si el trabajo toca imagenes, prompts o iconografia, leer `references/visuales-assets.md`.
4. Si el trabajo toca HTML, PDF, DOCX o scripts de build, leer `references/pipeline.md`.
5. Si el usuario pide iterar una unidad como patron maestro, leer `references/unidad-html-iterativa.md` y trabajar sobre un solo HTML.
6. Mantener separadas las fuentes canonicas, referencias historicas, diseno, assets y salidas compiladas.
7. No borrar imagenes ni PDFs de referencia. Si hay depuracion, copiar primero a una carpeta de recuperacion o preservacion.
8. Reportar conteos concretos: carpetas creadas, imagenes preservadas, prompts, manuales y archivos aun pendientes.

## Estructura raiz esperada
La raiz depurada debe conservar estos bloques numerados:

```text
00_temario_estructura/
01_fuente_principal_markdown/
02_referencia_gemini_markdown/
03_referencias_quimica/
04_referencia_diseno/
05_assets_visuales_iconos/
06_motor_compilacion_minimo/
07_docs_pedagogicos/
08_fuentes_externas/
```

No renombrar estos bloques salvo que el usuario lo pida explicitamente. Los numeros expresan flujo de trabajo: temario, fuente, referencias, diseno, assets, motor, validacion y fuentes externas.

## Reglas de separacion
- `01_fuente_principal_markdown` es el codigo fuente canonico de nuevos manuales.
- `02_referencia_gemini_markdown`, `03_referencias_quimica` y `04_referencia_diseno` son referencias, no origen canonico.
- `05_assets_visuales_iconos` guarda iconos, prompts visuales, imagenes generadas y recursos de marca.
- `06_motor_compilacion_minimo` guarda scripts y plantillas de conversion.
- `07_docs_pedagogicos` guarda diagnosticos, arquitectura y verificacion.
- `08_fuentes_externas` guarda materiales externos y PDFs fuente.

## Crear una base nueva
Cuando el usuario pida crear una copia estructural, usar el script:

```powershell
powershell -ExecutionPolicy Bypass -File codex-skills/manual-architecture-builder/scripts/scaffold-manual-architecture.ps1 -TargetRoot MANUALES_BASE_NUEVA
```

Despues de ejecutar el script, revisar manualmente que:
- existan los 9 bloques numerados, de `00` a `08`;
- existan `manual-1` a `manual-5`;
- cada manual tenga `manifest.md`, `semestre-1`, `semestre-2` y `unidades`;
- existan carpetas para `iconos`, `prompts-visuales` y `visuales`;
- el motor tenga carpeta `build`.

## Auditoria minima
Para auditar una base:
1. Listar los 9 bloques raiz y detectar faltantes.
2. Contar manuales en `01_fuente_principal_markdown/manuales`.
3. Revisar estructura de cada `manual-N`.
4. Verificar convenciones de unidades y semestres.
5. Contar imagenes en `05_assets_visuales_iconos/visuales`.
6. Contar prompts en `05_assets_visuales_iconos/prompts-visuales`.
7. Revisar scripts en `06_motor_compilacion_minimo`.
8. Entregar un reporte breve con faltantes, riesgos y acciones sugeridas.
