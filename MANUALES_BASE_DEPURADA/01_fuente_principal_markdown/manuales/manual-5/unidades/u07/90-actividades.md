---
unidad: 7
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 07

::act-mcq{titulo="Repaso conceptual"}
1. La función ReLU es:
   - [ ] σ(x) entre 0 y 1
   - [x] max(0, x)
   - [ ] Lineal
   - [ ] Periódica

2. Sin scaling antes de NN:
   - [ ] Acelera entrenamiento
   - [x] La red entrena mucho peor o no converge
   - [ ] Es opcional
   - [ ] Solo afecta árboles

3. Para regresión, la loss típica es:
   - [ ] CrossEntropy
   - [ ] BCE
   - [x] MSE
   - [ ] Hinge

4. Para evitar sobreajuste en NN:
   - [ ] Más neuronas
   - [x] Dropout + early stopping + regularización L2
   - [ ] Más epochs
   - [ ] Sin batch
::/act-mcq

::act-match{titulo="Componente PyTorch"}
| Componente | Función |
|---|---|
| 1. Tensor | a) Algoritmo que ajusta pesos |
| 2. nn.Module | b) Array multi-dimensional con autograd |
| 3. Optimizer | c) Definición de arquitectura |
| 4. Loss | d) Mide error de predicción |
::/act-match

::interioriza{titulo="La Sinfonía de PyTorch"}
Entrenar una red en PyTorch es como dirigir una orquesta:
- Los **Tensores** son los músicos y sus instrumentos (datos).
- La **Arquitectura (nn.Module)** es la partitura musical.
- La **Loss** es el oído que detecta notas desafinadas.
- El **Optimizer** es el director que corrige a los músicos en tiempo real.
::/interioriza

::pausa{titulo="💭 Deducción Rápida"}
1. Si usamos un modelo muy grande en datos pequeños, ¿qué técnica (o "músico") es la primera que silenciarías usando Dropout para evitar memorizar la partitura?
__________________________________________________________________
::/pausa

::albatros{titulo="MLP en PyTorch para tu dataset" tipo="taller" tiempo="4 h"}
**Pregunta detonadora.** Aunque Random Forest gane, ¿qué te llevas de entrenar tu primera red neuronal?

**Lo que harás.**
- Implementar el MLP de la práctica resuelta.
- Compararlo contra el modelo baseline (Random Forest).
- Generar la curva de aprendizaje (Train vs Test Loss).
- Aplicar early stopping y Dropout.

**Entregable.** Notebook documentado con gráfica de pérdidas y conclusiones.
::/albatros

---

## Reto de Ingeniería: Empaquetado

::albatros{titulo="Reto Albatros — Empaca tu modelo" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.** Si envías tu modelo a otro equipo, ¿pueden predecir sin re-entrenarlo?

**Lo que harás.**
- Crear un artefacto que unifique: el modelo, el scaler y el esquema de variables.
- Exportarlo usando un diccionario en Python y guardarlo con Joblib.
- Escribir un script `cargar_y_predecir.py` totalmente independiente.
- Pedirle a un compañero que ejecute tu script en su computadora sin enviarle instrucciones.

**Entregable.** Repositorio Git limpio, el archivo del artefacto (`.joblib`), y el script de carga documentado.
::/albatros
