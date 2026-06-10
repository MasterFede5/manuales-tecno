---
manual: 5
titulo: "Inteligencia Artificial con Programación"
subtitulo: "De Python al primer modelo de Machine Learning y APIs de IA"
publico: "Estudiantes con curiosidad técnica · sin experiencia previa de programación"
unidades: 8
paginas_total_objetivo: 372
paginas_min: 350
paginas_max: 450
prerrequisitos: "Manual 4 (IA Avanzada) recomendado · álgebra básica"
politica_simplificacion: |
  Versión simplificada respecto al borrador anterior:
  - Sale MLOps avanzado (Docker, CI/CD)
  - Sale Computer Vision profunda (YOLO, SAM, Detectron) → glosario
  - Sale fine-tuning de Transformers, NER → glosario
  - Sale LangGraph/CrewAI (mover al Manual 4 §6 Agentes)
  - El núcleo: Python → datos → ML clásico → red neuronal básica → API → proyecto
  - Sin matemáticas pesadas; intuición + recetario + caso continuo
case_study:
  nombre: "Predictor de rendimiento escolar"
  premisa: |
    La coordinación académica te entrega un dataset anonimizado con horas
    de estudio, asistencia, calificaciones previas y resultado final.
    Tu misión: construir paso a paso un sistema que prediga el rendimiento
    de un estudiante y lo explique en lenguaje natural. Cada unidad agrega
    una pieza al sistema.
  episodios:
    U1: "Cargar la lista de calificaciones desde un CSV con Python"
    U2: "Limpiar el dataset con NumPy y Pandas"
    U3: "Visualizar la distribución de calificaciones por materia"
    U4: "¿Correlacionan horas de estudio y calificación final?"
    U5: "Tu primer modelo predictor con scikit-learn"
    U6: "Segmentar estudiantes en perfiles con K-Means"
    U7: "Mejorar el predictor con una red neuronal en PyTorch"
    U8: "Tu predictor explica resultados con la API de Claude"
---

# Manifest — Manual 5: IA con Programación (simplificado)

## Asignación de páginas (suma = 372 pp)

| Sección | pp | acumulado |
|---|---:|---:|
| Front matter (10) + diagnóstica (4) | 14 | 14 |
| **U1 — Tu Primer Python para IA** | 35 | 49 |
| **U2 — Datos con NumPy y Pandas** | 40 | 89 |
| **U3 — Visualización de Datos** | 35 | 124 |
| **U4 — Estadística para entender datos** | 35 | 159 |
| **U5 — Tu Primer Modelo de Machine Learning** | 50 | 209 |
| **U6 — Aprendizaje No Supervisado** | 40 | 249 |
| **U7 — Redes Neuronales (introducción)** | 45 | 294 |
| **U8 — Programar con APIs de IA Generativa** | 50 | 344 |
| Examen integrador + glosario + biblio + índice | 28 | **372** |

---

## U1 — Tu Primer Python para IA (35 pp)

**Caso E1:** Cargar la lista de calificaciones desde un CSV.

| Subtema | pp |
|---|---:|
| 1.1 Configuración: Anaconda, VS Code, Colab | 4 |
| 1.2 Variables, tipos, operadores | 5 |
| 1.3 Estructuras de control: if, for, while | 5 |
| 1.4 Funciones y argumentos | 4 |
| 1.5 Listas, tuplas, diccionarios | 5 |
| 1.6 Lectura y escritura de archivos (CSV, JSON) | 4 |
| 1.7 Errores y excepciones básicas | 3 |
| Práctica resuelta + Actividades | 4 |
| Implementación Albatros: cargar el CSV escolar | 1 |

**Sin OOP avanzada · sin decoradores · sin entornos virtuales en U1 (mover a U2).**

**Visuales:** infografía instalación · diagrama flujo de control · cuadro estructuras.

---

## U2 — Datos con NumPy y Pandas (40 pp)

**Caso E2:** Limpiar el dataset escolar (nulos, duplicados, tipos).

| Subtema | pp |
|---|---:|
| 2.1 NumPy: arrays y operaciones básicas | 6 |
| 2.2 Pandas: Series y DataFrame | 6 |
| 2.3 Lectura: CSV, Excel, JSON | 4 |
| 2.4 Limpieza: nulos, duplicados, tipos | 6 |
| 2.5 Filtrado y selección | 5 |
| 2.6 Agrupación (groupby) y agregaciones | 5 |
| Práctica resuelta + Actividades | 5 |
| Implementación Albatros: dataset escolar limpio | 3 |

**Sin merge complejo · sin pivot · sin series temporales** (mover a glosario).

**Visuales:** diagrama Series vs DataFrame · cuadro métodos · ejemplo antes/después limpieza.

---

## U3 — Visualización de Datos (35 pp)

**Caso E3:** Visualizar distribución de calificaciones por materia.

| Subtema | pp |
|---|---:|
| 3.1 Matplotlib esencial: línea, barras, dispersión | 6 |
| 3.2 Histogramas y boxplots | 5 |
| 3.3 Seaborn para gráficos rápidos y bonitos | 5 |
| 3.4 Personalización: títulos, ejes, paleta | 4 |
| 3.5 Interpretación visual: ¿qué muestra el gráfico? | 5 |
| 3.6 Storytelling con datos (3 reglas básicas) | 4 |
| Práctica resuelta + Actividades | 4 |
| Implementación Albatros: visualización del dataset escolar | 2 |

**Sin Plotly · sin Streamlit en U3** (Streamlit aparece en U8).

**Visuales:** galería de gráficos · cuadro qué tipo de gráfico para qué dato.

---

## U4 — Estadística para entender datos (35 pp)

**Caso E4:** ¿Correlacionan horas de estudio y calificación?

| Subtema | pp |
|---|---:|
| 4.1 Media, mediana, varianza, desviación estándar | 6 |
| 4.2 Distribución normal y curva de campana | 5 |
| 4.3 Percentiles y cuartiles | 4 |
| 4.4 Correlación (Pearson) — sin matemáticas duras | 6 |
| 4.5 Correlación vs causalidad | 4 |
| 4.6 Detección de outliers | 4 |
| Práctica resuelta + Actividades | 4 |
| Implementación Albatros: correlación del dataset | 2 |

**Sin pruebas de hipótesis t-test/chi² formales** → glosario "Para profundizar".

**Visuales:** infografía distribución normal · cuadro correlación interpretada · ejemplos outliers.

---

## U5 — Tu Primer Modelo de Machine Learning (50 pp)

**Caso E5:** Tu primer predictor de calificaciones con scikit-learn.

| Subtema | pp |
|---|---:|
| 5.1 ¿Qué es ML? Supervisado vs no supervisado | 4 |
| 5.2 Pipeline: datos → features → modelo → evaluación | 5 |
| 5.3 Train/test split y validación cruzada | 5 |
| 5.4 Métricas: accuracy, precision, recall, F1, RMSE | 6 |
| 5.5 Regresión lineal | 6 |
| 5.6 Regresión logística (clasificación) | 6 |
| 5.7 Árboles de decisión | 5 |
| 5.8 Sobreajuste, sesgo-varianza, regularización (intuitivo) | 5 |
| Práctica resuelta + Actividades | 5 |
| Implementación Albatros: predictor con scikit-learn | 3 |

**Sin XGBoost/LightGBM, SVM, Naïve Bayes detallados** → tabla comparativa con 1 párrafo cada uno y glosario.

**Visuales:** pipeline ML · diagrama train/test · árbol de decisión · matriz de confusión.

---

## U6 — Aprendizaje No Supervisado (40 pp)

**Caso E6:** Segmentar perfiles de estudiantes.

| Subtema | pp |
|---|---:|
| 6.1 Concepto de clustering | 4 |
| 6.2 K-Means paso a paso | 8 |
| 6.3 Cómo elegir K (codo, silueta) | 5 |
| 6.4 PCA básico (intuición + uso) | 6 |
| 6.5 Detección de anomalías simple | 5 |
| Práctica resuelta + Actividades | 6 |
| Implementación Albatros: segmentación del dataset | 6 |

**Sin DBSCAN, t-SNE, UMAP detallados** → glosario.

**Visuales:** infografía clustering · ejemplo PCA antes/después.

---

## U7 — Redes Neuronales: introducción (45 pp)

**Caso E7:** Mejorar el predictor con una red neuronal en PyTorch.

| Subtema | pp |
|---|---:|
| 7.1 Neurona artificial e intuición | 5 |
| 7.2 Capas, activaciones (ReLU, Softmax) | 6 |
| 7.3 Forward pass y backpropagation (intuitivo, sin derivadas) | 6 |
| 7.4 PyTorch: estilo recetario (tensors, nn.Module, optimizer) | 8 |
| 7.5 Tu primer MLP entrenado en Colab | 8 |
| 7.6 Diagnóstico: curva de aprendizaje | 4 |
| Práctica resuelta + Actividades | 5 |
| Implementación Albatros: red neuronal sobre el dataset | 3 |

**Sin TensorFlow paralelo, sin GPU avanzada, sin CNNs/RNNs/Transformers** → glosario.

**Visuales:** diagrama neurona · arquitectura MLP · curva de aprendizaje.

---

## U8 — Programar con APIs de IA Generativa (50 pp)

**Caso E8:** Tu predictor explica resultados con IA generativa.

| Subtema | pp |
|---|---:|
| 8.1 Configurar API de Claude / OpenAI | 5 |
| 8.2 Tu primer chatbot en 30 líneas | 5 |
| 8.3 Streaming y tool use (introducción) | 5 |
| 8.4 Embeddings y búsqueda semántica básica | 6 |
| 8.5 Mini-RAG sobre 3 documentos | 8 |
| 8.6 Despliegue con Streamlit | 6 |
| 8.7 Buenas prácticas: costo, manejo de errores, caching | 5 |
| Práctica resuelta + Actividades | 5 |
| Implementación Albatros: predictor + explicador en Streamlit | 5 |

**Sin LangChain/LlamaIndex/LangGraph completos** → mostrar 1 ejemplo y glosario.

**Visuales:** diagrama API · captura Streamlit · diagrama RAG mínimo.
