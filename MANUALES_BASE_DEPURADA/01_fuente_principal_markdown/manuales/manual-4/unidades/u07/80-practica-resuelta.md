---
unidad: 7
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 07

::practica{titulo="Desplegar el Asistente Institucional 100 % local con Ollama + Open WebUI + RAG en una tarde"}
**Problema.** 
- Construir la versión soberana del Asistente en 4 horas.
- Usar Ollama (Qwen 2.5 72B Q4), Open WebUI y RAG.
- Implementar SSO institucional y evaluar contra versión cloud. 

**Paso 1 — Datos y hardware.**
- Servidor: Ubuntu 22.04, RTX A6000 (48 GB), IP fija y Docker.
- Base documental: Reglamento, manual docente y ética (103 páginas).
- Acceso Google Workspace y dominio `asistente.albatros.local`.

**Paso 2 — Estrategia.**
1. Instalar Ollama y descargar modelos.
2. Levantar Open WebUI con Docker.
3. Configurar Single Sign-On (SSO).
4. Subir la knowledge base.
5. Indexar y configurar modelo principal.
6. Habilitar usuarios y realizar pruebas (Golden set).

**Paso 3 — Instalación Ollama (15 min).**
- Ejecuta `curl -fsSL https://ollama.ai/install.sh | sh`.
- Descarga los modelos base:
```bash
ollama pull qwen2.5:72b
ollama pull qwen2.5:7b
ollama pull bge-m3
```

**Paso 4 — Open WebUI (10 min).**
- Lanza el contenedor con soporte para GPU:
```bash
docker run -d -p 3000:8080 --gpus all \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main
```

**Paso 5 — SSO Google Workspace (20 min).**
- Configura OAuth en Open WebUI con credenciales de Google Cloud.
- Restringe el acceso al dominio institucional.

**Paso 6 — Knowledge base (30 min).**
- Sube los PDFs desde la sección Knowledge de Open WebUI.
- Usa el embedder `bge-m3` y verifica la indexación en ChromaDB.

**Paso 7 — Configuración del modelo (15 min).**
- Crea un `Modelfile.asistente` con el system prompt:
```
FROM qwen2.5:72b
SYSTEM """Eres el Asistente Albatros. Responde usando #reglamento."""
PARAMETER temperature 0.3
```
- Compílalo: `ollama create asistente -f Modelfile.asistente`.

::interioriza
Imagina que construyes un búnker de alta tecnología en un fin de semana. No necesitas fabricar los ladrillos (modelos) ni las puertas (interfaz); solo ensamblas piezas prefabricadas robustas (Ollama y Docker) en un terreno propio (servidor local).
::/interioriza

**Paso 8 — Golden set local vs cloud (60 min).**
- Ejecuta 15 pruebas estandarizadas.
- La versión local acierta 13/15, comparada con 14/15 en la nube.
- La latencia es de 12s frente a 3s en cloud. Suficiente para producción.

**Paso 9 — Monitoreo y despliegue.**
- Invita a 5 usuarios piloto.
- Programa backups automáticos del volumen Docker.

::pausa{}
**Deduce:** Si la latencia es de 12 segundos, ¿por qué los usuarios podrían preferir esta versión local sobre una versión en la nube que responde en 3 segundos? Piensa en el caso de uso principal.
::/pausa

**Resumen.** 
- Despliegue exitoso en una tarde. 
- La arquitectura local es madura y segura para datos sensibles.
::/practica

::practica{titulo="Cómo benchmarkeé 3 tamaños de Qwen y elegí el menor que basta"}
**Problema.** 
- Hay 3 GPUs posibles: 24 GB, 48 GB, 96 GB.
- Necesitamos evaluar si basta Qwen 14B, 32B o 72B para nuestro colegio.
- No queremos sobredimensionar el presupuesto sin justificación.

**Paso 1 — Criterios de éxito.**
- Calidad: RAGAS score ≥ 4.0/5.
- Latencia: 90 % de respuestas en < 15 segundos.
- Seguridad: Cero alucinaciones graves demostrables.

**Paso 2 — Evaluación progresiva.**
- **14B (24 GB):** Rápido (11s), pero falla calidad (3.8) y tiene alucinaciones.
- **32B (48 GB):** Excelente balance. Calidad 4.3, latencia 16s, sin alucinaciones graves.
- **72B (96 GB):** Calidad superior (4.5), pero lento (21s) y cuesta el doble.

::interioriza
Comprar el modelo de 72B es como rentar un autobús escolar para llevar a tres alumnos. El 32B es la van perfecta: cumple la función, cuesta la mitad y se estaciona (latencia) más rápido.
::/interioriza

**Paso 3 — Decisión fundamentada.**
- Elegimos Qwen 2.5 32B en la GPU de 48 GB.
- Pasa los umbrales de calidad sin comprometer críticamente la latencia.
- Se documenta con un ADR-018.

**Resumen.** 
- El proveedor intentará vender el equipo más grande.
- La métrica real debe ser: "¿cuál es el menor modelo que resuelve el problema?".

::pausa{}
**Deduce:** ¿Por qué es vital definir los umbrales de éxito (Paso 1) antes de empezar a hacer pruebas con los modelos?
::/pausa
::/practica

::practica{titulo="Cómo decidí qué workflows migrar a local y cuáles dejar en cloud"}
**Problema.** 
- La dirección sugiere migrar *todo* a local por ahorro de costos.
- Necesitas demostrar que algunas tareas son mejores en la nube.
- Requieres una matriz de decisión objetiva.

**Paso 1 — Criterios de migración.**
- Envía a local si hay: alta sensibilidad de datos o alto volumen de uso.
- Mantén en cloud si: requiere razonamiento extremo o genera bajo costo.

**Paso 2 — Mapeo de tareas.**
- **A local (5 tareas):** RAG interno, resúmenes, crisis, datos académicos.
- **A cloud (2 tareas):** Redacción compleja y contenido educativo.

::interioriza
Piensa en el Asistente como un equipo de especialistas. Las consultas médicas (datos sensibles) las atiendes en tu propia clínica a puerta cerrada. El diseño gráfico (redacción compleja), lo tercerizas a una agencia porque es más capaz y ocasional.
::/interioriza

**Paso 3 — Prueba A/B (Canary).**
- Desvía el 10% del tráfico al modelo local.
- Descubrimos que el local falla en clasificar solicitudes (8% de error vs 3%).
- Revertimos esa tarea específica a cloud.

**Paso 4 — Decisión final.**
- 4 tareas quedan en local y 3 en cloud.
- El ahorro real es poco (~$360/año).
- El valor real de la migración es la privacidad y soberanía de los datos.

::pausa{}
**Deduce:** Si el ahorro anual es mínimo, ¿cómo convencerías a la dirección de mantener esta arquitectura híbrida en lugar de volver 100% a la nube?
::/pausa

**Lección.** 
- No existe una solución única de "todo local" o "todo cloud".
- La arquitectura moderna asume un enrutamiento inteligente según el caso.
::/practica
