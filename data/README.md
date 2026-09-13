# Datos para la revisión vigente

Los CSV grandes están excluidos de Git. No se han sustituido por datos de restaurantes de 2026: el entrenamiento sigue utilizando TripAdvisor European Restaurants, versión publicada en 2021.

Fuente: [Kaggle — TripAdvisor European Restaurants](https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants). La evidencia de licencia CC0 y sus límites se documentan en [DERECHOS_DATOS.md](../revision_academica/DERECHOS_DATOS.md).

Descargar y extraer `tripadvisor_european_restaurants.csv` en esta carpeta. Ejecutar `../notebooks/01_carga_exploracion.ipynb` desde `notebooks/` para generar `asian_restaurants_europe.csv`, la entrada del entrenamiento revisado. Ambos CSV permanecen locales y no se incluyen en Git ni en el paquete de entrega.

El antiguo `asian_restaurants_preprocessed.csv` no es necesario para la revisión. Las figuras, métricas y mapas antiguos se han trasladado a `../archivo_historico/data/`. Los resultados vigentes están en `../revision_academica/resultados/`.

Consultar [REPRODUCIBILIDAD.md](../REPRODUCIBILIDAD.md) para el orden de ejecución.
