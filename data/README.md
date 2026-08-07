# Datos

## Dataset original (no incluido en el paquete de entrega)

**`tripadvisor_european_restaurants.csv`** (~650 MB) no se incluye en este paquete por su tamaño.
Es un dataset público que puede descargarse directamente:

- **Fuente:** https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants
- **Licencia:** CC0 (dominio público)
- **Descarga vía Kaggle API** (requiere `kaggle auth login`, ver `../REPRODUCIBILIDAD.md`):

```bash
kaggle datasets download -d stefanoleone992/tripadvisor-european-restaurants --unzip -p .
```

El notebook `../notebooks/01_carga_exploracion.ipynb` asume que este fichero está en esta carpeta
y genera a partir de él los ficheros derivados (más pequeños) que sí forman parte del proyecto:

## Ficheros derivados (generados por los notebooks, incluidos en el proyecto)

| Fichero | Tamaño aprox. | Generado por |
|---|---|---|
| `asian_restaurants_europe.csv` | 55 MB | `01_carga_exploracion.ipynb` |
| `asian_restaurants_preprocessed.csv` | 17 MB | `03_preprocesamiento_modelos.ipynb` |
| `dense_nn_metrics.json` | <1 KB | `03b_red_densa_keras.ipynb` |
| `fig_*.png` | ~1 MB en total | notebooks 02, 03, 04 |
| `mapa_restaurantes_asiaticos.html` | 8,6 MB | `02_eda.ipynb` |

Si se necesita reconstruir todo desde cero, basta con descargar el dataset original a esta carpeta
y ejecutar los notebooks en el orden indicado en `../REPRODUCIBILIDAD.md`.
