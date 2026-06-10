---
unidad: 1
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 01

::act-mcq{titulo="Repaso conceptual"}
1. ¿Cuál entorno es preferible para principiante con laptop modesta?
   - [ ] VS Code
   - [x] Google Colab
   - [ ] Anaconda Navigator
   - [ ] PyCharm

2. La diferencia entre `8 / 3` y `8 // 3` en Python es:
   - [ ] `/` solo funciona con int, `//` con float
   - [x] `/` devuelve float (2.666), `//` devuelve int (2, división entera)
   - [ ] No hay diferencia
   - [ ] `//` es más rápida

3. Para guardar 480 estudiantes con sus datos, la estructura ideal es:
   - [ ] Lista de tuplas
   - [ ] Diccionario único con claves "alumno1, alumno2..."
   - [x] Lista de diccionarios
   - [ ] Set de strings

4. ¿Cuál es la forma correcta de manejar errores al convertir string a float?
   - [ ] Verificar tipo antes con `if isinstance`
   - [x] try/except ValueError
   - [ ] No hay problema, Python lo maneja solo
   - [ ] Usar `int()` en su lugar

5. Para leer CSV con headers en Python sin pandas, lo más limpio es:
   - [ ] `open()` y dividir por comas manualmente
   - [x] `csv.DictReader`
   - [ ] `read_csv()` (es de pandas)
   - [ ] `json.load()`
::/act-mcq

::interioriza
Imagina que las estructuras de datos son cajas organizadoras:
- Una **lista** es una hilera de cajas numeradas (1, 2, 3...).
- Un **diccionario** es un estante con etiquetas personalizadas ("nombre", "edad").
- Una **lista de diccionarios** es como un archivero: cada cajón (lista) tiene carpetas etiquetadas (diccionario). ¡Perfecto para alumnos!
::/interioriza

::pausa{}
**Reflexión rápida:**
- ¿Por qué no usaríamos una sola lista larga con todos los datos mezclados (ej. `[nombre1, edad1, nombre2, edad2...]`)?
- ¿Qué problema causaría si nos piden buscar la edad del alumno número 300?
::/pausa

::act-table{titulo="Completa la tabla — qué estructura para qué dato"}
| Dato | Estructura | Justificación |
|---|---|---|
| Calificaciones de un alumno (lista ordenada) |  |  |
| Datos de un alumno (id, nombre, edad) |  |  |
| Coordenadas (x, y) de un punto |  |  |
| Materias únicas que cursa el bachillerato |  |  |
| 480 estudiantes con sus 5 columnas |  |  |
::/act-table

::act-match{titulo="Relaciona excepción con caso"}
| Excepción | Caso típico |
|---|---|
| 1. FileNotFoundError | a) `float("ABC")` |
| 2. ValueError | b) `lista[100]` con lista de 5 |
| 3. KeyError | c) `open("noexiste.csv")` |
| 4. IndexError | d) `dict["clave_no_existe"]` |
| 5. TypeError | e) `5 + "hola"` |
| 6. ZeroDivisionError | f) `5 / 0` |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. En Python, las llaves `{}` se usan solo para diccionarios. ( ) ____________________________________________

2. `try/except` debe ser lo primero al escribir cualquier programa nuevo. ( ) ____________________________________________

3. Una función sin `return` devuelve `None` por defecto. ( ) ____________________________________________

4. Las tuplas son más rápidas que las listas para acceso por índice. ( ) ____________________________________________

5. `csv.DictReader` convierte automáticamente los valores a tipos correctos. ( ) ____________________________________________
::/act-tf

::act-order{titulo="Ordena los pasos del script de carga del CSV escolar"}
[ ] Reportar errores y guardar JSON
[ ] Definir función `parsear_fila` con try/except
[ ] Calcular estadísticas
[ ] Importar csv y json
[ ] Iterar líneas del CSV con DictReader
[ ] Definir función `cargar_dataset(path)`
[ ] Llamar `main()` desde `if __name__ == "__main__"`
[ ] Definir función `calcular_estadisticas`
::/act-order

::albatros{titulo="Tu primer programa Python que carga CSV escolar y produce reporte" tipo="taller" tiempo="3 h"}
**Pregunta detonadora.**
- Si nunca habías programado antes, ¿qué se siente ver tu primer script Python ejecutándose y dando resultados sobre datos reales?

**Lo que harás.**
- Configura tu entorno (Colab recomendado para empezar).
- Crea CSV simulado de 50 estudiantes con columnas: id, horas_estudio, asistencia, cal_anterior, cal_final.
- Implementa el script de la práctica resuelta paso a paso.
- Prueba con casos edge (archivo no existe, valores inválidos, columna faltante).
- Agrega una función propia: `top_5_estudiantes(estudiantes)` que devuelve los 5 mejores.
- Guarda código en repo Git (GitHub gratis).
- Documenta en README cómo correr el script.
- Pasa tu código a un compañero para que lo corra y reporta su experiencia.

**Materiales.**
- Cuenta Colab o Anaconda.
- Repositorio GitHub.
- 3 horas estimadas.

**Entregable.**
- Script Python funcional.
- CSV de prueba.
- README con instrucciones.
- Reporte JSON generado.
- Captura de pantalla del programa corriendo.


**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Setup | un solo intento | funcional | con README |
| Lectura CSV | sin error | con DictReader | con manejo de errores |
| Estructuras | uso pobre | listas y dicts | con funciones reusables |
| Manejo errores | sin try | try básico | múltiples casos manejados |
| Código limpio | spaghetti | funciones | bien nombrado y documentado |
| Compartir | privado | en GitHub | con README claro y reproducible |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="Completa el script — bucle que clasifica 5 alumnos"}
Tu script debe imprimir `Aprobados: 3 · Reprobados: 2` cuando recibe la lista.

```python
calificaciones = [7.5, 5.0, 8.0, 4.5, 9.0]
aprobados = ___________
reprobados = 0

for cal in ___________:
    if ___________ >= 6:
        aprobados ___________ 1
    else:
        reprobados += 1

print(f"Aprobados: {aprobados} · Reprobados: {___________}")
```
::/act-fill

::act-order{titulo="Ordena los pasos para crear y publicar un repo Git con tu script"}
[ ] `git push -u origin main`
[ ] Crear repo en GitHub (botón "New")
[ ] `git init` en la carpeta local
[ ] Escribir el script `cargar_dataset.py`
[ ] `git remote add origin URL`
[ ] `git commit -m "first commit"`
[ ] `git add cargar_dataset.py README.md`
[ ] Redactar el `README.md` con instrucciones
::/act-order

::act-case{titulo="Caso — el CSV viene con encabezados raros" lineas=10}
Coordinación te entrega un CSV con fallas:
- El encabezado es **`Id;Horas;Asis;CalAnt;CalFin`**.
- Presenta mayúsculas inconsistentes.
- Usa separador `;` en vez de `,`.
- Tu script falla porque `fila["id"]` no existe (la clave real es `"Id"`).

Diseña en pseudocódigo (5–8 líneas) cómo deberías:
- Detectar el separador real.
- Normalizar los nombres de columna a minúsculas y sin espacios.
- Mapear los nombres normalizados a los esperados por tu pipeline.
::/act-case

::act-table{titulo="Errores comunes en U1 y cómo manejarlos"}
| Síntoma observado | Excepción Python | Causa raíz | Cómo manejar |
|---|---|---|---|
| `[Errno 2] No such file or directory` |  |  |  |
| `could not convert string to float: 'N/A'` |  |  |  |
| `KeyError: 'cal_final'` |  |  |  |
| `IndexError: list index out of range` |  |  |  |
| `TypeError: unsupported operand type(s) for +: 'int' and 'str'` |  |  |  |
::/act-table

::act-mindmap{titulo="Mapa mental abierto" centro="MI PRIMER SCRIPT PYTHON" nodos_primarios=6 nodos_secundarios=12}
Llena las burbujas:
- 6 nodos primarios (entorno, datos, control, funciones, archivos, errores).
- Por cada uno, 2 ejemplos concretos de tu script.
::/act-mindmap

::albatros{titulo="Reto Albatros — debug del script roto" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.**
- ¿Puedes encontrar 5 bugs en código ajeno que **parece** funcionar pero produce resultados erróneos?

**Lo que harás.**
Recibes este script (cópialo tal cual a un archivo `roto.py`):

```python
import csv

def cargar(path):
    estudiantes = []
    f = open(path)
    reader = csv.DictReader(f)
    for fila in reader:
        estudiantes.append({
            "id": fila["id"],
            "cal": fila["cal_final"]
        })
    return estudiantes

def promedio(estudiantes):
    suma = 0
    for e in estudiantes:
        suma += e["cal"]
    return suma / len(estudiantes)

estudiantes = cargar("dataset_escolar.csv")
print(promedio(estudiantes))
```

**Bugs a encontrar.**
Identifica al menos 5 problemas (hay 6 reales). Para cada uno:
- Línea donde ocurre.
- Descripción del problema.
- Fix propuesto.

**Pistas (lee solo si te trabas).**
- ¿Qué pasa si el CSV no existe?
- ¿`f` se cierra alguna vez?
- ¿`fila["cal_final"]` viene como número o string?
- ¿Qué tipo es `e["cal"]` cuando se suma?
- ¿Qué pasa si la lista está vacía y se divide entre cero?
- ¿Qué pasa si una fila tiene `cal_final` igual a `"N/A"`?

**Entregable.**
- Archivo `roto_arreglado.py`.
- Comentarios `# BUG N: descripción + fix` por cada uno.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Bugs detectados | <2 | 3-4 | 5-6 con fix correcto |
| Comentarios | sin documentar | una línea | descripción + por qué |
| Script final | crashea aún | corre pero no robusto | corre + maneja edge cases |
::/albatros
