# Anexo A — Correspondencia con la propuesta y las instrucciones docentes

Revisión: 13/09/2026. Autor: Peng Chen.

## Propuesta enviada (aportada por el alumno)

Modalidad: **1) Análisis de un dataset**.

Índice: Introducción · EDA de restaurantes asiáticos en Europa · Preprocesamiento · Modelización (predicción de rating) · Evaluación de modelos · Conclusiones · Bibliografía.

Descripción: «Análisis de la gastronomía asiática en Europa a partir del dataset de TripAdvisor European Restaurants (+1M registros). Se realizará un EDA centrado en restaurantes de cocina asiática, seguido de modelos de predicción de valoración y análisis comparativo por países, con especial foco en España».

## Fuentes de requisitos

Guía original: `01_Guía para el Trabajo Fin de Master - UCM - Online - BigData, Data Science  Inteligencia Artificial.pdf` (12 páginas), localizada en Downloads. SHA-256: 2db23bdfac90d8dcefd4b98494daea954645830f7782225a268ae4e6512f9a6c.

Correo de Carlos y Santiago aportado por el alumno en esta conversación: aprobación general de propuestas salvo incidencias expresas; derechos de datos; GDPR cuando proceda; adecuación, representatividad y actualidad de fuentes; conexión de asignaturas; modificaciones leves permitidas si se mantiene la esencia; énfasis en interpretabilidad y productivización. La fecha del correo y una fecha vigente de entrega no se aportaron. No se inventa una confirmación individual del tutor.

| Requisito | Evidencia de la revisión | Límite / pendiente |
|---|---|---|
| EDA europeo y España | Memoria §§3–4; eda_paises.json; notebook revisado | Muestra histórica, cobertura no censal |
| Transformación de datos | Pipeline de imputación, indicadores, escalado y one-hot | No demuestra ausencia de sesgo de selección |
| Diferentes modelos y evaluación | Media, Lineal, RF, XGB; validación separada; test común | Hiperparámetros prefijados; futura validación externa |
| Interpretabilidad | Permutación recalculada y ablación de reputación | No causal; variables correlacionadas |
| Productivización | Web/API local, esquema, versión, hash y métricas básicas | No despliegue empresarial público |
| Conexión entre asignaturas | Python, estadística, ML, software y fuentes territoriales | Se prioriza pertinencia sobre cantidad de modelos |
| Derechos / privacidad | DERECHOS_DATOS.md y metadatos Kaggle | No confundir declaración CC0 con derechos de terceros |
| Memoria ≤20 caras | 10 páginas de cuerpo, portada e índice independientes | Verificar cualquier edición posterior |
| Vídeo ≤5 min, voz propia | Guion y PPT revisados | Grabación y cronometraje pendientes del alumno |
| Anexos y reproducibilidad | Código, notebook/HTML, artefactos y registro de partición | Descarga del dataset original por quien reproduzca |
| Madrid | Sección de aplicación y anexos | No reemplaza rating por rentabilidad |

La inferencia de alineación se basa en conservar datos, objeto y objetivo de modelización de la propuesta, añadiendo las fases explicitadas por el correo. No constituye una garantía de calificación. No se solicita cambio de tema ni se envía correo automáticamente.
