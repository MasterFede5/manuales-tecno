---
unidad: 8
seccion: investigacion
paginas_objetivo: 1
---

::investiga{titulo="¿Cómo funciona el LIDAR de un coche autónomo y por qué reemplaza al radar?" tiempo="2 h"}
**Pregunta de investigación.** Los coches Tesla, Waymo y Zoox llevan sensores LIDAR que disparan miles de pulsos láser por segundo y miden el tiempo que tarda en regresar cada eco para construir un mapa 3D del entorno. ¿Cómo funciona exactamente? ¿Por qué la industria se está moviendo de radar (microondas) a LIDAR (luz infrarroja)? ¿Qué ventajas y desventajas tiene cada uno?

**Lo que debes encontrar.**
- Definición de **LIDAR** (Light Detection and Ranging) y la fórmula básica $d = c \cdot t/2$.
- Longitud de onda típica de un LIDAR automotriz (905 nm o 1550 nm) y por qué se elige esa banda.
- Diferencia entre **LIDAR mecánico** (rotatorio) y **LIDAR de estado sólido** (MEMS, OPA, flash).
- Por qué se prefiere LIDAR sobre radar para detectar obstáculos pequeños (una pelota, un peatón).
- Limitaciones: lluvia intensa, niebla, vidrio, espejos, polvo.
- Comparación contra cámaras estéreo (Tesla decidió no usar LIDAR; Waymo sí lo usa).
- Aplicaciones fuera del coche: drones, agricultura de precisión, arqueología, levantamiento topográfico.

**Cómo presentarlo.** Una infografía de tamaño A3 hecha en Canva o Genially con el principio de funcionamiento, comparativa LIDAR vs radar vs cámara, y un caso real (Waymo, Hesai, Velodyne, Innoviz).

**Fuentes sugeridas.**
- Documentación oficial de Velodyne, Hesai o Luminar (sus papers blancos están en PDF gratuito).
- Canal de YouTube *The Engineering Mindset* o *Real Engineering* — videos sobre LIDAR.
- Wikipedia (en inglés) → "Lidar", "Time-of-flight camera".
- Anuncios técnicos de Waymo y Tesla AI Day (transcripciones públicas).

**Criterios de evaluación.**
- **Rigor físico (35 %)** — explicas correctamente $d = c \cdot t/2$ y cómo se traduce a una nube de puntos 3D.
- **Comparativa (25 %)** — tabla LIDAR vs radar vs cámara con ventajas, desventajas y costo.
- **Aplicación local (15 %)** — relacionas con el coche F1 escolar (¿podrías hacer un mini-LIDAR con un sensor TOF como el VL53L0X?).
- **Diseño y claridad (15 %)** — la pieza es legible para alguien que no es ingeniero.
- **Citación (10 %)** — mínimo 3 fuentes verificables.
::/investiga
