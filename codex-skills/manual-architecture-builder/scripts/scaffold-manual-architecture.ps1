param(
  [string]$TargetRoot = "MANUALES_BASE_NUEVA",
  [switch]$Force
)

$ErrorActionPreference = "Stop"

function New-Dir($Path) {
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
  }
}

function New-TextFile($Path, $Content) {
  if ((Test-Path -LiteralPath $Path) -and -not $Force) {
    return
  }
  $parent = Split-Path -Parent $Path
  New-Dir $parent
  Set-Content -LiteralPath $Path -Value $Content -Encoding UTF8
}

$root = Join-Path (Get-Location) $TargetRoot

$topDirs = @(
  "00_temario_estructura\manifiestos_5_manuales",
  "01_fuente_principal_markdown\manuales",
  "02_referencia_gemini_markdown\manualesGem",
  "03_referencias_quimica",
  "04_referencia_diseno",
  "05_assets_visuales_iconos\iconos",
  "05_assets_visuales_iconos\prompts-visuales",
  "05_assets_visuales_iconos\visuales",
  "06_motor_compilacion_minimo\build\example",
  "07_docs_pedagogicos",
  "08_fuentes_externas"
)

foreach ($dir in $topDirs) {
  New-Dir (Join-Path $root $dir)
}

$semesterFiles = @(
  "00-portada.md",
  "01-carta-estudiante.md",
  "02-carta-docente.md",
  "03-mapa-contenidos.md",
  "04-hilo-conductor.md",
  "05-competencias.md",
  "06-diagnostica.md",
  "90-cierre-semestre.md",
  "91-material-extra.md",
  "92-glosario-semestre.md",
  "93-bibliografia-semestre.md",
  "94-indice-analitico.md"
)

$unitFiles = @(
  "README.md",
  "00-portadilla.md",
  "01-mapa-mental.md",
  "02-caso-episodio.md",
  "10-tema-1-1.md",
  "10-tema-1-2.md",
  "80-practica-resuelta.md",
  "81-banco-ejercicios.md",
  "90-actividades.md",
  "92-investigacion.md",
  "93-taller.md",
  "94-fuentes.md",
  "95-implementacion.md",
  "99-cierre.md"
)

$manualUnits = @{
  1 = @("u00","u01","u02","u03","u04","u05","u06")
  2 = @("u01","u02","u03","u04","u05","u06","u07","u08","u09")
  3 = @("u01","u02","u03","u04","u05","u06","u07","u08","u09")
  4 = @("u01","u02","u03","u04","u05","u06","u07","u08","u09","u10")
  5 = @("u01","u02","u03","u04","u05","u06","u07","u08")
}

foreach ($manual in 1..5) {
  $manualRoot = Join-Path $root "01_fuente_principal_markdown\manuales\manual-$manual"
  New-Dir $manualRoot
  New-TextFile (Join-Path $manualRoot "manifest.md") @"
---
manual: $manual
titulo: "Manual $manual"
estado: borrador
---
"@

  foreach ($semester in @("semestre-1", "semestre-2")) {
    $semesterRoot = Join-Path $manualRoot $semester
    New-Dir $semesterRoot
    foreach ($file in $semesterFiles) {
      New-TextFile (Join-Path $semesterRoot $file) "---`ntitulo: `"`"`n---`n"
    }
  }

  $unitsRoot = Join-Path $manualRoot "unidades"
  New-Dir $unitsRoot
  foreach ($unit in $manualUnits[$manual]) {
    $unitRoot = Join-Path $unitsRoot $unit
    New-Dir $unitRoot
    foreach ($file in $unitFiles) {
      New-TextFile (Join-Path $unitRoot $file) "---`nmanual: $manual`nunidad: $unit`ntitulo: `"`"`n---`n"
    }
  }

  foreach ($bucket in @("sem1", "sem2")) {
    New-Dir (Join-Path $root "05_assets_visuales_iconos\visuales\manual-$manual\$bucket")
  }
  foreach ($unit in $manualUnits[$manual]) {
    New-Dir (Join-Path $root "05_assets_visuales_iconos\visuales\manual-$manual\$unit")
    New-Dir (Join-Path $root "05_assets_visuales_iconos\prompts-visuales\manual-$manual\$unit")
  }
}

New-TextFile (Join-Path $root "00_temario_estructura\ARQUITECTURA.md") "# Arquitectura de manuales`n"
New-TextFile (Join-Path $root "07_docs_pedagogicos\verificacion-spec.md") "# Verificacion de especificacion`n"

Write-Output "manual_architecture_created=$root"

