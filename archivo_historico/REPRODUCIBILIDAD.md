# Reproducibilidad

Este TFM usa **dos entornos de Python** porque TensorFlow provoca un `segmentation fault` al
importarse en el entorno base de Anaconda usado para el resto del proyecto (conflicto de versión de
`protobuf` con otros paquetes ya instalados ahí, como streamlit). Para no arriesgar la estabilidad
del entorno principal, el notebook de la red densa (Keras) se aisló en un entorno virtual propio.

## 1. Entorno principal

Usado por todos los notebooks excepto `03b_red_densa_keras.ipynb`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Entorno de TensorFlow (solo para 03b_red_densa_keras.ipynb)

```bash
python3 -m venv .venv_tf
source .venv_tf/bin/activate
pip install -r requirements-tf.txt
python3 -m ipykernel install --user --name tfm-tf --display-name "TFM (TensorFlow)"
```

Al abrir `03b_red_densa_keras.ipynb` en Jupyter, seleccionar el kernel **"TFM (TensorFlow)"**.

## 3. Credenciales de Kaggle (solo necesario para `01_carga_exploracion.ipynb`)

El dataset original se descarga automáticamente vía API de Kaggle. Requiere una cuenta de Kaggle:

```bash
kaggle auth login
# o alternativamente, generar un token en kaggle.com/settings/api
```

## 4. Orden de ejecución de los notebooks

Cada notebook genera un fichero intermedio que usa el siguiente — deben ejecutarse en este orden:

| # | Notebook | Genera |
|---|---|---|
| 1 | `01_carga_exploracion.ipynb` | `data/asian_restaurants_europe.csv` |
| 2 | `02_eda.ipynb` | figuras de `data/fig_*.png`, `data/mapa_restaurantes_asiaticos.html` |
| 2b | `02b_tendencia_buffet_asiatico.ipynb` | (análisis complementario, no genera dependencias) |
| 3 | `03_preprocesamiento_modelos.ipynb` | `data/asian_restaurants_preprocessed.csv` |
| 3b | `03b_red_densa_keras.ipynb` (kernel `tfm-tf`) | `data/dense_nn_metrics.json`, leído por el notebook 3 |
| 4 | `04_modelizacion_avanzada.ipynb` | `models/modelo_xgboost_final.joblib`, `models/feature_defaults.json` |

**Nota:** el notebook 3 carga `data/dense_nn_metrics.json` si existe (generado por el 3b). Si no
existe, avisa por consola y sigue sin la fila del modelo Keras en la tabla comparativa — no falla.

## 5. Dataset

El CSV original (~650 MB) no se incluye en este paquete por su tamaño. Ver `data/README.md` para
cómo descargarlo.
