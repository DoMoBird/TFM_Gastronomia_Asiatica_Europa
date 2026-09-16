# Reproducibilidad de la versión vigente

Desde la raíz del repositorio, instalar `Analisis_rest_Asiatico/requirements_revision.txt` en un entorno Python compatible. El entorno probado y las limitaciones se detallan en [Analisis_rest_Asiatico/README.md](Analisis_rest_Asiatico/README.md).

Para inferencia con los modelos ya entrenados no se necesitan los CSV:

```bash
python Analisis_rest_Asiatico/src/verificar.py
python Analisis_rest_Asiatico/src/servir.py --port 8765
```

Para reentrenar, obtener el CSV original según [data/README.md](data/README.md) y ejecutar `notebooks/01_carga_exploracion.ipynb` con el directorio de trabajo en `notebooks/`. Este genera `data/asian_restaurants_europe.csv`. El notebook requiere también sus dependencias de preparación, como Jupyter y Kaggle si se utiliza su descarga automática.

Después, desde la raíz:

```bash
python Analisis_rest_Asiatico/src/entrenar.py
python Analisis_rest_Asiatico/src/figuras.py
python Analisis_rest_Asiatico/src/verificar.py
```

Los hashes y particiones del experimento publicado están en `Analisis_rest_Asiatico/resultados/`.
