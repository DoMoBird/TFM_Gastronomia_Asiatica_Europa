# Reproducibilidad de la versión vigente

Desde la raíz del repositorio, instalar `revision_academica/requirements_revision.txt` en un entorno Python compatible. El entorno probado y las limitaciones se detallan en [revision_academica/README.md](revision_academica/README.md).

Para inferencia con los modelos ya entrenados no se necesitan los CSV:

```bash
python revision_academica/src/verificar.py
python revision_academica/src/servir.py --port 8765
```

Para reentrenar, obtener el CSV original según [data/README.md](data/README.md) y ejecutar `notebooks/01_carga_exploracion.ipynb` con el directorio de trabajo en `notebooks/`. Este genera `data/asian_restaurants_europe.csv`. El notebook requiere también sus dependencias de preparación, como Jupyter y Kaggle si se utiliza su descarga automática.

Después, desde la raíz:

```bash
python revision_academica/src/entrenar.py
python revision_academica/src/figuras.py
python revision_academica/src/verificar.py
```

La revisión no utiliza el antiguo CSV preprocesado, el modelo de `archivo_historico/models/` ni el entorno TensorFlow histórico. Los hashes y particiones del experimento publicado están en `revision_academica/resultados/`.
