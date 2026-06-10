---
unidad: 1
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 01

> Aquí practicas las 7 piezas de Python. No leas la clave de respuestas hasta que hayas intentado cada bloque. Si te trabas más de 5 min, pasa al siguiente y vuelve después.

### Bloque A — Variables, tipos y operadores (1.2)

::act-fill{titulo="Completa el código — operaciones aritméticas"}
Completa cada línea para que el `print` final muestre `Promedio: 7.5 · Aprueba: True`.

```python
cal_1 = 7
cal_2 = 8
promedio = (___________ + ___________) / ___________
aprueba = promedio >= ___________
print(f"Promedio: {promedio} · Aprueba: {___________}")
```
::/act-fill

::act-mcq{titulo="Predice el output"}
1. ¿Qué imprime esto?
   ```python
   print(type(7 / 2))
   print(type(7 // 2))
   ```
   - [ ] `<class 'int'>` y `<class 'int'>`
   - [x] `<class 'float'>` y `<class 'int'>`
   - [ ] `<class 'float'>` y `<class 'float'>`
   - [ ] Error de sintaxis

2. ¿Cuál es el valor final de `x`?
   ```python
   x = 5
   x += 3
   x *= 2
   x -= 1
   ```
   - [ ] 14
   - [x] 15
   - [ ] 16
   - [ ] 17

3. ¿Qué imprime `print("8" + "2")` en Python?
   - [ ] 10
   - [x] 82
   - [ ] Error
   - [ ] 8 + 2

4. ¿Cuál es booleano falso?
   - [ ] `bool([0])`
   - [x] `bool([])`
   - [ ] `bool("False")`
   - [ ] `bool(-1)`
::/act-mcq

### Bloque B — Estructuras de control (1.3)

::act-fill{titulo="Completa el if/elif para clasificar calificaciones"}
```python
def clasificar(cal):
    if cal >= 9:
        return "Excelente"
    ___________ cal >= 7:
        return "Bien"
    ___________ cal >= 6:
        return "Aprobado"
    ___________:
        return "Reprobado"

print(clasificar(8.5))   # → ___________
print(clasificar(5.9))   # → ___________
```
::/act-fill

::act-mcq{titulo="Predice el output del loop"}
1. ¿Qué imprime?
   ```python
   total = 0
   for i in range(1, 5):
       total += i
   print(total)
   ```
   - [ ] 5
   - [x] 10
   - [ ] 15
   - [ ] 4

2. ¿Cuántas iteraciones hace este `while`?
   ```python
   n = 10
   pasos = 0
   while n > 1:
       n = n // 2
       pasos += 1
   print(pasos)
   ```
   - [ ] 2
   - [ ] 3
   - [x] 4
   - [ ] Loop infinito
::/act-mcq

### Bloque C — Funciones (1.4)

::act-fill{titulo="Función que cuenta aprobados"}
```python
def contar_aprobados(calificaciones, umbral=___________):
    """Cuenta cuántas calificaciones son >= umbral."""
    aprobados = 0
    for c in ___________:
        if c >= umbral:
            aprobados ___________ 1
    return ___________

calis = [7, 5, 8, 9, 4, 6, 7]
print(contar_aprobados(calis))         # → 5
print(contar_aprobados(calis, 8))      # → 2
```
::/act-fill

::act-tf{titulo="V/F sobre funciones"}
1. Una función sin `return` siempre lanza error. ( ) ____________________
2. Los argumentos por default deben ir al final de la firma. ( ) ____________________
3. `def f(x, y=2)` permite llamar `f(5)` y `f(5, 3)`. ( ) ____________________
4. Las variables dentro de una función son visibles fuera de ella. ( ) ____________________
::/act-tf

### Bloque D — Listas, tuplas, diccionarios (1.5)

::act-mcq{titulo="¿Qué estructura usar?"}
1. Para guardar 480 estudiantes con sus 5 atributos cada uno, eliges:
   - [ ] Lista plana de strings
   - [ ] Tupla gigante
   - [x] Lista de diccionarios
   - [ ] Set de tuplas

2. Para listar las **materias únicas** que se cursan, lo ideal es:
   - [ ] Lista
   - [x] Set
   - [ ] Diccionario
   - [ ] Tupla

3. Predice el output:
   ```python
   alumno = {"id": 12, "cal": 8.5}
   alumno["asistencia"] = 0.92
   print(len(alumno))
   ```
   - [ ] 1
   - [ ] 2
   - [x] 3
   - [ ] Error
::/act-mcq

::act-fill{titulo="Construye lista de dicts a partir de listas paralelas"}
```python
ids = [1, 2, 3]
cals = [7.5, 6.0, 9.0]

estudiantes = []
for i in range(len(___________)):
    estudiantes.append({
        "id": ___________[i],
        "cal_final": ___________[i]
    })

# Otra forma con zip:
estudiantes_v2 = [
    {"id": _id, "cal_final": _cal}
    for _id, _cal in ___________(ids, cals)
]
```
::/act-fill

### Bloque E — Archivos CSV/JSON (1.6)

::act-order{titulo="Ordena los pasos para leer un CSV con DictReader"}
[ ] Iterar `for fila in reader:`
[ ] Importar el módulo `csv`
[ ] Crear `reader = csv.DictReader(f)`
[ ] Convertir cada fila string a tipos numéricos correctos
[ ] Abrir el archivo con `open(path, "r", encoding="utf-8")`
[ ] Cerrar el archivo (o usar `with`)
::/act-order

::act-mcq{titulo="JSON predice el output"}
1. ¿Qué imprime?
   ```python
   import json
   data = {"n": 3, "ok": True, "list": [1, 2]}
   s = json.dumps(data)
   print(type(s))
   ```
   - [ ] `<class 'dict'>`
   - [x] `<class 'str'>`
   - [ ] `<class 'json'>`
   - [ ] `<class 'bytes'>`
::/act-mcq

### Bloque F — Errores y excepciones (1.7)

::act-fill{titulo="try/except que protege parsing de fila"}
```python
def a_float(valor):
    try:
        return float(___________)
    except ___________:
        return None

print(a_float("8.5"))     # → 8.5
print(a_float("N/A"))     # → None
print(a_float(""))        # → ___________
```
::/act-fill

::act-tf{titulo="V/F buenas prácticas"}
1. `except:` solo (sin tipo) atrapa todo y oculta bugs reales. ( ) ____________________
2. Es buena idea envolver TODO el `main()` en un solo `try` gigante. ( ) ____________________
3. El bloque `finally` se ejecuta haya o no haya error. ( ) ____________________
4. `raise ValueError("...")` permite que tú lances tus propios errores. ( ) ____________________
::/act-tf

### Bloque G — Caso integrador

::act-table{titulo="Llena la tabla de tipos para cada columna del CSV escolar"}
| Columna | Valor crudo (string) | Tipo destino | Conversión |
|---|---|---|---|
| id | `"427"` | int |  |
| horas_estudio | `"4.5"` |  |  |
| asistencia | `"0.92"` |  |  |
| cal_anterior | `"7"` |  |  |
| cal_final | `"8.5"` |  |  |
::/act-table

::act-case{titulo="Caso — fila corrupta en la línea 47" lineas=8}
La coordinación reportó que **al cargar el CSV crashea en la línea 47**. La fila luce así:
```
427,3.5,N/A,7.0,8.5
```
Tu programa hace `float(fila["asistencia"])` y revienta. Diseña en pseudocódigo (3-5 líneas) cómo deberías modificar tu función `parsear_fila` para:
- Continuar cargando el resto del archivo.
- Registrar la línea 47 con el motivo del error.
- No propagar la excepción.
::/act-case

---

## Clave de respuestas

**Bloque A.**
- `act-fill`: `cal_1 + cal_2 / 2`, `>= 6`, `aprueba`. Output: `Promedio: 7.5 · Aprueba: True`.
- `act-mcq`: 1·B, 2·B (15: `5+3=8 → ×2=16 → −1=15`), 3·B (concatenación de strings), 4·B (lista vacía es falsy).

**Bloque B.**
- `act-fill`: `elif`, `elif`, `else`. Outputs: `Bien`, `Reprobado`.
- `act-mcq`: 1·B (1+2+3+4=10), 2·C (10→5→2→1, 4 pasos).

**Bloque C.**
- `act-fill`: `umbral=6`, `for c in calificaciones`, `aprobados += 1`, `return aprobados`.
- `act-tf`: 1·F (devuelve `None`); 2·V; 3·V; 4·F (scope local).

**Bloque D.**
- `act-mcq`: 1·C, 2·B (set evita duplicados), 3·C.
- `act-fill`: `len(ids)`, `ids[i]`, `cals[i]`, `zip`.

**Bloque E.**
- `act-order`: 2·1·5·3·4·6 (importar → abrir → reader → iterar → convertir → cerrar).
- `act-mcq`: 1·B (`json.dumps` devuelve string).

**Bloque F.**
- `act-fill`: `valor`, `ValueError`, `None` (string vacío también lanza `ValueError`).
- `act-tf`: 1·V; 2·F (granularidad por bloque); 3·V; 4·V.

**Bloque G.**
- `act-table`:

| Columna | Tipo | Conversión |
|---|---|---|
| id | int | `int(s)` |
| horas_estudio | float | `float(s)` |
| asistencia | float | `float(s)` |
| cal_anterior | float | `float(s)` |
| cal_final | float | `float(s)` |

- `act-case`: pseudocódigo modelo:
```
def parsear_fila(fila):
    try:
        return {"id": int(fila["id"]), ...}, None
    except ValueError as e:
        return None, str(e)
# en cargar_dataset, si parsear devuelve None, registra (linea, motivo) en errores
```

> **Cierre.** Si resolviste >70 % sin mirar la clave, estás listo para U2. Si <50 %, repasa el subtema correspondiente (cada bloque mapea 1-1 con un subtema 1.X).
