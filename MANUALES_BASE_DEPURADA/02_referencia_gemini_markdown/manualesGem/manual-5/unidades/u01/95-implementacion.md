---
unidad: 1
seccion: implementacion
paginas_objetivo: 1
---

::implementacion{titulo="Implementación Albatros — Cargar el dataset escolar y reportarlo"}
**Objetivo.** Construir, ejecutar y compartir tu primer programa Python que carga el dataset escolar real (o simulado), genera estadísticas básicas, maneja errores con criterio, y deja el código en un repo Git público con README.

**¿Por qué hacerla?** Es el primer episodio del case study completo. Sin esta base, las siguientes 7 unidades no tienen dónde construirse.

---

### Materiales

- Cuenta Colab o Anaconda instalado.
- GitHub gratis.
- 4-5 horas (incluye debugging típico de principiante).

### Pasos

1. **Setup** del entorno (30 min).
2. **Generar CSV simulado** de 100 filas con `random` si no tienes uno real (45 min).
3. **Implementar las 4 funciones** de la práctica resuelta (90 min).
4. **Probar con casos edge** (30 min).
5. **Subir a GitHub** con README claro (45 min).
6. **Compartir** con un compañero y validar reproducibilidad (30 min).

### Entregable

1. URL del repo público.
2. Script `cargar_dataset.py` funcional.
3. CSV de prueba.
4. Reporte JSON generado.
5. README con instrucciones paso a paso.
6. Captura de pantalla del programa corriendo.

### Rúbrica

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Setup | confuso | funcional | con README |
| Funciones definidas | en main todo | algunas | parsear+cargar+stats+main |
| Manejo errores | sin try | try básico | múltiples casos |
| Estructuras | listas planas | dicts | listas de dicts con json output |
| Compartir | privado | en GitHub | con README ejecutable por terceros |

### Próximo paso

En **U2** vas a usar **NumPy y Pandas** para procesar el mismo dataset en 5 líneas en lugar de 50. Pero el mérito está en haber entendido manualmente lo que pandas hará por debajo.

### Hitos intermedios

Marca cada hito en tu repo con un commit etiquetado.

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u1-h1-setup` | Entorno corre `print("hola")` sin errores |
| H2 | `u1-h2-csv-leido` | Tu script imprime `len(estudiantes)` y muestra primera fila |
| H3 | `u1-h3-funciones` | `parsear_fila`, `cargar_dataset`, `calcular_estadisticas` separadas |
| H4 | `u1-h4-errores` | 5 filas malas reportadas con línea y motivo |
| H5 | `u1-h5-json` | `reporte.json` válido (lo abre `json.load` sin error) |
| H6 | `u1-h6-readme` | README permite a un compañero correr en <5 min |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — CLI con argumentos.** Modifica tu script para aceptar argumentos:

```bash
python cargar_dataset.py --csv dataset_escolar.csv --salida reporte.json --umbral 6.0
```

Pista: usa `argparse`. Esfuerzo: 30 min.

**Reto bonus 2 — Validador de columnas.** Agrega función `validar_schema(reader)` que verifica que el CSV tiene exactamente las columnas esperadas (`id, horas_estudio, asistencia, cal_anterior, cal_final`). Si falta o sobra alguna, devuelve mensaje claro y aborta limpio. Esfuerzo: 45 min.

**Reto bonus 3 — Modo estricto vs permisivo.** Añade un flag `--estricto` que **rechaza** todo el archivo si hay aunque sea 1 fila mala (vs el modo default que las ignora). Útil cuando coordinación necesita garantía total de integridad. Esfuerzo: 30 min.
::/implementacion

---

::albatros{titulo="Caso bonus — auditoría de un script ajeno" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Sabrías auditar el script de un compañero antes de meterlo en producción?

**Contexto.** Recibes el repo de un compañero con su script de carga del dataset escolar. La coordinación quiere que **tú avales** que el script es seguro de usar antes de procesar los 480 alumnos reales.

**Lo que harás.**
1. Lee el `README.md` del compañero. ¿Es claro? ¿Lo puedes correr en <5 min sin preguntar nada?
2. Corre el script con su CSV de prueba. ¿Funciona? ¿Hay warnings?
3. Inyecta 3 filas corruptas tú mismo y vuelve a correr. ¿Las maneja?
4. Cambia el path a uno inexistente. ¿Crashea o reporta limpio?
5. Lee el código (no solo el README): ¿hay `except:` desnudo? ¿hay `print` de debug olvidado? ¿hay rutas hardcoded?
6. Llena un checklist de auditoría con 6 ítems (sí/no + comentario).

**Entregable.** Reporte de auditoría de 1 página + checklist + 3 sugerencias concretas de mejora.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Ejecución probada | no probó | corre default | + casos edge inyectados |
| Lectura de código | no leyó | superficial | identifica anti-patrones |
| Checklist | <3 ítems | 6 ítems sí/no | con comentarios accionables |
| Tono | destructivo | técnico | constructivo + 3 mejoras concretas |
::/albatros
