---
unidad: 8
seccion: implementacion
paginas_objetivo: 5
---

::implementacion{titulo="Implementación Albatros — Predictor Albatros desplegado y validado"}
**Objetivo.** Construir, desplegar y validar la **app final del Asistente Predictor Albatros**: integra ML clásico + IA generativa + RAG institucional + Streamlit + buenas prácticas, lista para uso real por coordinación académica.

Esta es la implementación culminante del Manual 5. Cierra el case study completo.

---

### Materiales

- Modelo entrenado U5 (joblib).
- 3 PDFs institucionales (reglamento, manual docente, política).
- Anthropic API key + OpenAI API key.
- GitHub + Streamlit Community Cloud.
- 8-10 horas distribuidas en 4 sesiones.

### Pasos

#### Sesión 1 — Setup y RAG (2-3 h)

1. Instalar dependencias: `streamlit`, `anthropic`, `openai`, `joblib`, `numpy`, `pandas`.
2. Pre-computar embeddings de chunks de los 3 PDFs → `indice_rag.json`.
3. Test búsqueda semántica con 10 queries.

#### Sesión 2 — App básica (2 h)

4. Crear `app.py` con UI de inputs + predicción + explicación.
5. Test local con `streamlit run app.py`.
6. Iterar diseño UX.

#### Sesión 3 — Buenas prácticas (2 h)

7. Aplicar caching (`cache_resource` para modelo, `cache_data` para queries).
8. Manejo de errores con try/except + retry + fallback.
9. Logging básico.
10. Validación de inputs.
11. Secrets configurados.

#### Sesión 4 — Despliegue + validación (2-3 h)

12. Subir a GitHub (sin secrets).
13. Deploy en Streamlit Cloud.
14. Configurar secrets.
15. Test con 5 personas reales (coordinación, dirección, docente, padre, alumno mayor).
16. Documentar feedback y ajustes.
17. Reporte final.
::/implementacion

::visual{tipo="ilustracion" descripcion="Mockup app desplegada a tamaño página: header institucional Albatros, sidebar con configuración, área principal con sliders + botón + métricas + análisis IA + caja expandible con fuentes RAG. URL streamlit.app visible. Estilo screenshot real Albatros." paginas="1" src="../manualesGem/assets/visuales/manual-5/u08/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

1. **URL pública** de app desplegada.
2. **Repo GitHub** con código + README + estructura clara.
3. **Reporte de testeo** (2 pp): casos probados, feedback, ajustes.
4. **Documento de arquitectura** (1 pp): cómo encajan ML + RAG + LLM + Streamlit.
5. **Captura de pantalla** de app funcionando con caso real.

### Rúbrica

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| App funcional | local solo | desplegada | + multi-user |
| Integración ML + IA | predictor solo | + Claude | + RAG institucional |
| UX | crudo | título + inputs | + tabs + sidebar + métricas |
| Buenas prácticas | none | 2-3 | las 5 con evidencia |
| Validación usuarios | privado | 1 persona | 5+ con feedback escrito |
| Documentación | mínima | README | + arquitectura + diagrama |

### Cierre del Manual 5

Esta es la implementación final del manual. Tu app combina:
- **U1**: Python básico para todo el código.
- **U2**: pandas para manejo de datos.
- **U3**: visualizaciones opcionales en Streamlit.
- **U4**: estadística para validar predicciones.
- **U5**: modelo ML que predice.
- **U6**: clusters opcionales para segmentar usuarios.
- **U7**: red neuronal opcional alternativa.
- **U8**: APIs de IA generativa para explicar.

**De cero programación a app desplegada.** Ese fue el viaje de 8 unidades.

### Próximo paso después del manual

Si quieres profundizar:
- Cursos de Andrew Ng (DeepLearning.AI).
- Practicar en Kaggle competitions.
- Construir 3-5 proyectos con datos reales propios.
- Contribuir a proyectos open source en GitHub.
- Aplicar ML a problemas que te apasionen.

La carrera técnica en IA es un camino de **construcción continua**. Este manual te dio el primer kilómetro.
::/implementacion