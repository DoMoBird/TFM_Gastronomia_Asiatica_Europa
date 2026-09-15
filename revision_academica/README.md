# Revisión académica — Peng Chen

Esta es la versión de trabajo alineada con la propuesta aprobada: **EDA europeo de restaurantes asiáticos, foco en España, predicción de rating, evaluación, interpretación y productivización**. Madrid es una aplicación complementaria. Los ficheros anteriores se conservan en `../archivo_historico/`; sus conclusiones de inversión y métricas no deben mezclarse con esta revisión.

## Lectura

- `entrega/memoria_revisada.pdf`: portada e índice propios, cuerpo de 10 páginas; párrafos justificados.
- `entrega/presentacion_revisada_v4.pptx`: presentación vigente. Los guiones de grabación son material personal local y no se distribuyen.
- `ALINEACION_REQUISITOS.md`: propuesta, guía y correo docente cotejados.
- `DERECHOS_DATOS.md`: evidencia de uso y privacidad.
- `entrega/anexo_modelizacion.ipynb` y `.html`: resultados ejecutados y ruta para reentrenar.

## Anexo B — reproducibilidad

Entorno de cálculo probado: Python 3.13.5, numpy 2.1.3, pandas 2.2.3, scikit-learn 1.6.1, xgboost 3.4.0, joblib 1.4.2. Consultar `requirements_revision.txt`. La creación de PDF usa reportlab en el runtime de documentos; no es necesario para inferencia o entrenamiento.

Desde la raíz de TFM:

```bash
python revision_academica/src/entrenar.py
python revision_academica/src/figuras.py
python revision_academica/src/verificar.py
python revision_academica/src/servir.py --port 8765
```

Abrir `http://127.0.0.1:8765`, cargar el ejemplo y estimar. Mantener abierto el proceso del servidor mientras se utiliza la aplicación. Abrir directamente `src/interfaz.html` con `file://` no ejecuta el modelo; la página muestra instrucciones para acceder al servicio local. Si el puerto está ocupado, elegir otro con `--port`. El servidor no se expone a la red.

Entrada de entrenamiento: `data/asian_restaurants_europe.csv`, cuyo SHA-256 se conserva en `resultados/evaluacion.json`. Se obtiene ejecutando el notebook original `notebooks/01_carga_exploracion.ipynb` sobre el fichero descargado de Kaggle. La revisión no necesita el CSV preprocesado antiguo. Los datos crudos no están en el paquete revisado; conservar la estructura TFM/data y TFM/revision_academica al reproducir.

Se seleccionan algoritmos en validación con parámetros prefijados. El test se evalúa una vez por conjunto tras reajustar en el 80%. No se fusionan métricas anteriores de SVR/Keras ni la búsqueda antigua. El dataset completo ya se exploró: se declara esta limitación, aunque el nuevo test esté separado del ajuste actual.

`resultados/particiones.json` contiene los índices del dataframe con objetivo válido y su uso. `evaluacion.json` conserva hashes, versiones, métricas por país, bootstrap e importancia. El bootstrap no incluye incertidumbre por deriva, selección o cadenas.

## Anexo C — producto y operación

Implementado: validación de campos, categorías, finitud, rangos observados, coherencia país/región; ausencia explícita e imputación en pipeline; rechazo de exceso de nulos; hash al cargar modelo; salud y métricas. La concordancia de coordenadas con polígonos no está validada: es un límite adicional, no asumir que país/región consistentes garantizan la latitud correcta.

Las métricas viven en memoria y se reinician al reiniciar el proceso. `/metrics` ofrece conteos, latencia total, suma de predicciones, resultados fuera de escala, tasas de ausencia y una alerta heurística desde 20 respuestas. No hay ratings posteriores para medir error real en producción. El servicio no tiene autenticación, persistencia ni escalabilidad empresarial; por ello escucha solo en localhost.

Promoción de versión: conservar hashes y artefacto anterior, repetir evaluación independiente y contrato, verificar metadatos, sustituir el par modelo/informe, reiniciar y comprobar `/health`. Reversión: restaurar el par anterior. No cargar joblib de terceros no confiables. No realizar reentrenamiento automático a partir de peticiones del usuario.

Pruebas: paridad API/pipeline, valores fuera de rango, NaN, categoría inexistente, cocina fraccionaria, campo extra, ausencia de país, estructura incorrecta y pareja país/región inválida. Se comprobaron además HTTP 200/400 y flujo real de ejemplo en navegador.

## Anexo D — Madrid

Los informes y código están en `../investigacion_madrid/`. Población, renta, precios y alquiler aportan contexto; los escenarios económicos son ilustrativos y no sustituyen la predicción de rating. Las afirmaciones de «un solo buffet», «hueco de mercado demostrado» y «techo de rating» quedan retiradas de la versión revisada.

## Pendiente de entrega por el alumno

Ensayar y grabar vídeo con voz propia (≤5 minutos), revisar fecha vigente de entrega y comprobar permisos de los enlaces al publicar. El correo docente no contiene una fecha concreta; la fecha 2025 del plan histórico no se usa como plazo vigente. El historial Git identifica la revisión publicada. No se ha enviado el trabajo a los tutores.

## Regeneración de documentos

El cálculo y servicio funcionan con Python y las dependencias anteriores. El PDF requiere adicionalmente reportlab y las fuentes Arial del sistema macOS usadas en esta entrega; ajustar las rutas de fuentes en src/memoria.py en otro sistema. El PPT es editable directamente. Su generador src/presentacion.mjs requiere el runtime de artefactos de Codex (@oai/artifact-tool) y las variables PRESENTATIONS_SKILL_DIR, RUNTIME_PYTHON y RUNTIME_NODE_MODULES. No es una dependencia del entrenamiento. Al regenerar el PPT, usar un nombre de salida nuevo, porque el validador conserva las versiones previas.

La presentación vigente es la v4, revisada página a página con captura real del demostrador. La v2 se conserva como base editable del script `src/revisar_presentacion_v3.mjs`; no utilizarla para grabar el vídeo actual. El script restaura los libros de datos de los gráficos con `src/restaurar_libros_graficos.py` (lxml y openpyxl). Los guiones personales no se incluyen en las notas del PPT vigente.
