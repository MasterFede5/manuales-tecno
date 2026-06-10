---
unidad: 7
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Asistente Institucional Soberano operativo"}
**Objetivo.** Desplegar la **versión soberana del Asistente Institucional Albatros** en un servidor controlado por la institución, con stack 100 % local, multi-usuario con SSO, RAG sobre 5+ documentos institucionales, monitoreo, backups, y golden set comparativo contra cloud documentado.

**¿Por qué hacerla?** Es la pieza que demuestra a dirección y compliance que la institución **puede** operar IA sin lock-in con proveedor. Aunque sigan usando cloud, tener la alternativa lista es palanca de negociación y plan de contingencia.

---

### Materiales y recursos

- Hardware: PC con GPU mínima 12 GB VRAM (recomendado 24-48 GB) o Mac M2/M3 con 32+ GB RAM unificada.
- 50 GB de disco libre.
- Docker, conexión a internet (solo para descarga inicial).
- Acceso a Google Workspace para SSO (opcional pero recomendado).
- 8-12 horas distribuidas en 3-4 sesiones.

### Pasos

#### Sesión 1 — Hardware y Ollama (2 h)

1. **30 min — Verificación.** Comprobar GPU, RAM, disco, drivers actualizados.
2. **30 min — Instalación.** Ollama via script.
3. **45 min — Modelos.** Descargar Qwen 2.5 7B + 72B (si hardware lo permite) + bge-m3 + nomic-embed.
4. **15 min — Pruebas.** `ollama run qwen2.5:72b` con 3 preguntas simples.

#### Sesión 2 — Open WebUI multi-usuario (3 h)

5. **30 min — Docker.** Levantar Open WebUI.
6. **30 min — Cuenta admin.** Configurar admin, dominio, branding.
7. **45 min — SSO.** Configurar Google Workspace OAuth (o auth simple si no tienes Workspace).
8. **45 min — Modelfile institucional.** Crear `asistente.albatros` con system prompt institucional.
9. **30 min — Cuentas iniciales.** Invitar 3-5 staff piloto.

#### Sesión 3 — Knowledge bases y RAG (2-3 h)

10. **30 min — Curaduría.** Limpiar 5 PDFs institucionales.
11. **30 min — Knowledge base.** Crear "documentos-institucionales" con bge-m3.
12. **45 min — Indexación.** Subir y validar.
13. **45 min — Pruebas RAG.** Golden set 10 preguntas. Refinar chunking si necesario.

#### Sesión 4 — Operación, monitoreo, política (2 h)

14. **30 min — Backup.** Configurar backup diario del volumen Docker (a NAS local o externo).
15. **30 min — Monitoreo.** Sheet con stats semanales o Grafana/Prometheus.
16. **30 min — Documentación.** "Manual de uso" + "Manual de operación" (1 pp cada uno).
17. **30 min — Plan de contingencia.** Qué hacer si falla servidor, GPU se quema, etc.

::visual{tipo="ilustracion" descripcion="Mockup de sala de servidor pequeña institucional: workstation con GPU visible (icono RTX) etiquetada 'asistente.albatros.local'. Conectado a switch de red local. Pantalla mostrando Open WebUI con Asistente respondiendo. En el aire, escudo grande con candado etiquetado 'soberanía total: cero datos a internet'. A la derecha, lista visible de stack: Ollama, Qwen 2.5 72B, bge-m3, ChromaDB, Open WebUI. Estilo blueprint Albatros." paginas=1}

---

### Entregable

1. **Servidor desplegado** con URL accesible internamente.
2. **5+ cuentas activas** con SSO funcionando.
3. **Knowledge base institucional** con 5+ PDFs indexados.
4. **Modelfile** versionado en repo.
5. **Manual de uso** (1 pp) y **Manual de operación** (1 pp).
6. **Reporte golden set** local vs cloud (1-2 pp con cifras).
7. **Plan de contingencia** documentado.
8. **Backup automatizado** activo.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Hardware adecuado | sub-dimensionado | aceptable | optimizado para modelo |
| Stack completo | parcial | Ollama + WebUI | + RAG + auth + backup |
| Multi-usuario | uno solo | 3-5 | con SSO institucional |
| Knowledge base | sin documentos | 3 docs | 5+ con curaduría |
| Golden set | sin medir | 5 preguntas | 10+ con cloud comparativo |
| Documentación | mínima | manuales básicos | con contingencia y operación |
| Adopción | privado | piloto 5 staff | adoptado oficial con métricas |

### Hitos intermedios

| Día | Hito | Evidencia |
|---|---|---|
| Día 1 | Hardware verificado, Ollama instalado | screenshot `ollama list` |
| Día 2 | 2-3 modelos descargados | comprobación de versiones |
| Día 3 | Open WebUI en Docker | URL accesible |
| Día 5 | SSO o auth configurada | login funcional con cuenta institucional |
| Día 7 | Knowledge base con 5 PDFs | indexación verificada |
| Día 9 | Modelfile institucional + smoke test | archivo en repo |
| Día 10 | Golden 10-15 preguntas local vs cloud | reporte 1 página |
| Día 12 | Backup automático configurado | logs de backup |
| Día 14 | 3-5 cuentas piloto activas + reunión | acta + métricas |

### Reto bonus extendido (3 retos)

**Bonus 1 — Híbrido por tarea.** Aplicando la práctica resuelta, mapea las 7 tareas de tu Asistente y decide cuáles van a local con datos. Documenta la matriz y la decisión final por tarea en ADR.

**Bonus 2 — Modelo router.** Construye un workflow simple en n8n que clasifique cada pregunta entrante: si es sensible → local, si es de alta calidad → cloud, si es ambigua → local con fallback a cloud. Mide cuántas evita correctamente al cloud.

**Bonus 3 — Sandbox para investigación.** Habilita un canal en Open WebUI para que docentes prueben Qwen contra preguntas que no se atreven a hacer a ChatGPT. Mide a 30 días qué tipo de preguntas hicieron que no harían a un proveedor cloud — eso revela el valor real de la soberanía.

### Próximo paso después de esta unidad

En **U8 — MCP y Conexión de Herramientas**, el Asistente local **se integra con archivos institucionales** vía Model Context Protocol. El servidor MCP corre también local, completando el círculo de soberanía.
::/implementacion

::albatros{titulo="Reto complementario — operación a 30 días sin internet" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** ¿Tu Asistente local **realmente** funciona si cortas internet 24 horas, o depende de cosas que asumiste estaban siempre disponibles?

**Lo que harás.**
1. En tu computadora local con Ollama, **desconecta el internet** durante 30 minutos.
2. Lanza 5 preguntas a tu Asistente local. Verifica que responde.
3. Intenta acceder a Open WebUI desde otro dispositivo de la LAN. Verifica que carga.
4. Intenta cargar un PDF nuevo a knowledge base — observa qué falla y por qué.
5. Verifica que el backup automático corrió en este intervalo (debería ser local-a-local, no cloud).
6. Documenta qué funciona y qué falla en `docs/sin-internet-test-001.md`.

**Entregable.** Documento de 1 página con bitácora del test, fallos encontrados, mitigaciones a aplicar.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Test ejecutado | 5 minutos | 30 minutos | 24 horas |
| Pruebas | 2 | 5 | 5 + carga + backup + LAN |
| Fallos identificados | parche | listados | listados con plan de mitigación |
::/albatros
