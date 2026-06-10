# Guía de Ensamblaje y Propósito de los Manuales (Estándar Albatros)

¡Bienvenido al sistema de manuales de tecnología! Este documento explica el **propósito pedagógico** de la colección y **cómo está estructurado** el repositorio para que puedas ensamblar o publicar el contenido de manera adecuada.

## 1. Propósito de la Colección

Esta colección de manuales (Manual 1 al 5) ha sido diseñada y refactorizada bajo el **Estándar Pedagógico Albatros**. Su objetivo principal es facilitar la enseñanza técnica mediante principios de ciencia cognitiva y diseño instruccional moderno:

- **Micro-Learning:** La información está fragmentada. Ningún párrafo supera las 3 líneas, privilegiando el uso de viñetas. Esto previene la sobrecarga cognitiva.
- **Baja Curva de Aprendizaje:** Antes de entrar a la teoría dura o al código, cada concepto se introduce mediante analogías de la vida real (cajas `::interioriza`).
- **Active Recall:** En lugar de pruebas de memorización, se utilizan cajas `::pausa{}` diseñadas para forzar la deducción lógica, afianzando el conocimiento.
- **Balance Práctico (60/40):** Una fuerte orientación a la resolución de casos, minimizando el tiempo de lectura (reflejado en el ajuste estricto de las `paginas_objetivo` en los metadatos de los archivos).

## 2. Arquitectura de Directorios

El repositorio está dividido en 5 manuales principales, cada uno contenido en su respectiva carpeta dentro de `/manuales/`. La estructura general de cada manual sigue esta jerarquía:

```text
📁 manuales/
├── 📁 manual-1/               # Ejemplo: Fundamentos
│   ├── 📁 unidades/
│   │   ├── 📁 u01/            # Unidad 1
│   │   │   ├── 00-portadilla.md
│   │   │   ├── 01-mapa-mental.md
│   │   │   ├── 02-caso-episodio.md
│   │   │   ├── 10-tema-1-1.md       (Lecciones teóricas)
│   │   │   ├── 10-tema-1-X.md       ...
│   │   │   ├── 80-practica-resuelta.md (Walkthrough del caso)
│   │   │   ├── 81-banco-ejercicios.md  (Ejercicios guiados)
│   │   │   ├── 90-actividades.md       (Retos, MCQs, proyectos)
│   │   │   ├── 95-implementacion.md
│   │   │   └── 99-cierre.md
│   │   └── 📁 u02/
│   └── 📄 README.md
├── 📁 manual-2/
├── 📁 manual-3/
├── 📁 manual-4/
└── 📁 manual-5/               # Machine Learning Avanzado & NLP
```

## 3. Guía de Ensamblaje

Para compilar, publicar o exportar estos manuales (ya sea usando Docusaurus, MkDocs, un generador de PDFs como Pandoc, o un LMS), debes seguir este orden lógico para ensamblar cada unidad:

1. **Apertura de la Unidad:**
   - Carga primero `00-portadilla.md` (Título y competencias).
   - Muestra el `01-mapa-mental.md` (Visión global del tema).
   - Presenta el `02-caso-episodio.md` (El caso de estudio o problema a resolver en esta unidad).

2. **Cuerpo Teórico (Lecciones):**
   - Importa en orden secuencial todos los archivos que comiencen con `10-tema-X-Y.md`. 
   - *Nota:* El motor de renderizado que utilices debe estar configurado para soportar Markdown Components (MDX) o Directivas, de manera que las cajas semánticas (`::concepto`, `::interioriza`, `::visual`, `::pausa`) se rendericen con los estilos CSS adecuados.

3. **Fase Práctica y Evaluación:**
   - Continúa con `80-practica-resuelta.md` (donde se resuelve el caso inicial).
   - Añade `81-banco-ejercicios.md` para el entrenamiento del alumno.
   - Integra `90-actividades.md` y `93-taller.md` (si existe) para evaluación o trabajo en clase.

4. **Cierre de la Unidad:**
   - Finaliza con `95-implementacion.md` (tips de implementación real/producción) y `99-cierre.md` (conclusiones y resumen).
   - Opcionalmente, puedes añadir `92-investigacion.md` y `94-fuentes.md` como anexos de lectura complementaria al final del capítulo.

## 4. Parser de Markdown (Importante para Desarrolladores)

Todos los archivos utilizan **frontmatter** (bloques `---` al inicio del archivo) de tipo YAML para metadatos (`unidad`, `titulo`, `paginas_objetivo`, `competencias`). Tu script de ensamblaje (Node.js, Python, etc.) debe usar un parser que extraiga este frontmatter para indexar correctamente los títulos y calcular los tiempos estimados de lectura, antes de procesar el resto del contenido en formato Markdown.

---
**Estado del Repositorio:** Todos los manuales (1 al 5) se encuentran 100% estandarizados y refactorizados listos para su compilación y despliegue a producción.
