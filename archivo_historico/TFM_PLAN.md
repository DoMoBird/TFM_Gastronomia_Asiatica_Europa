# TFM - Máster Big Data, Data Science e Inteligencia Artificial (UCM Online)

> **Plan histórico. Revisión vigente: 13/09/2026.** Consultar [revision_academica/README.md](revision_academica/README.md) y [correspondencia con los requisitos](revision_academica/ALINEACION_REQUISITOS.md). Se conserva el núcleo aprobado: EDA europeo, foco en España y predicción de rating. Madrid es una aplicación complementaria. Las fechas de 2025, las afirmaciones de éxito de nuevas aperturas y los estados de tareas de este documento no describen la revisión vigente.

## 📋 INFORMACIÓN GENERAL

- **Alumno:** (Peng Chen)
- **Máster:** Big Data, Data Science e Inteligencia Artificial - UCM Online
- **Tutores:** Carlos Ortega y Santiago Mota
- **Fecha de entrega:** 17 de septiembre de 2025
- **Modalidad:** Individual
- **Opción elegida:** Opción 1 — Análisis de un dataset (orientación Data Scientist)

---

## 🎯 TEMA DEL TFM

**Análisis de la gastronomía asiática en Europa con foco en España**

A partir del dataset público **"TripAdvisor European Restaurants"** disponible en Kaggle, se filtra únicamente los restaurantes de cocina asiática para analizar su presencia, distribución y factores de éxito en Europa.

### Dataset
- **Fuente:** Kaggle — `https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants`
- **Tamaño original:** +1.000.000 de restaurantes europeos, 42 atributos
- **Subconjunto de trabajo:** Solo restaurantes asiáticos (filtrado por tipo de cocina)
- **Licencia:** Pública (scraping TripAdvisor)

### Tipos de cocina asiática a filtrar
```python
asian_cuisines = ['Chinese', 'Japanese', 'Thai', 'Korean',
                  'Vietnamese', 'Indian', 'Asian', 'Sushi',
                  'Dim Sum', 'Ramen', 'Noodles']
```

---

## 📝 ÍNDICE DEL TFM

1. Introducción y motivación
2. Descripción del dataset y fuentes de datos
3. Análisis Exploratorio de Datos (EDA)
   - 3.1 Distribución geográfica de restaurantes asiáticos en Europa
   - 3.2 Tipos de cocina asiática predominantes por país
   - 3.3 Análisis de valoraciones y reseñas
4. Preprocesamiento y transformación de datos
5. Modelización
   - 5.1 Predicción de valoración de restaurantes
   - 5.2 Comparativa de modelos (Random Forest, XGBoost, Regresión)
   - 5.3 Interpretabilidad del modelo (SHAP)
6. Productivización del modelo (API/aplicación)
7. Conclusiones y líneas futuras
8. Bibliografía

---

## 🔬 DESCRIPCIÓN DEL PROYECTO

El presente TFM analiza la presencia y el éxito de la gastronomía asiática en Europa, con especial foco en España, a partir del dataset público "TripAdvisor European Restaurants" disponible en Kaggle (+1M de registros, 42 atributos).

Tras filtrar los restaurantes de cocina asiática (china, japonesa, tailandesa, coreana, vietnamita, entre otras), se realizará un análisis exploratorio completo para identificar patrones geográficos, tipos de cocina predominantes y factores que influyen en la valoración de los usuarios.

Posteriormente se desarrollarán modelos de Machine Learning en Python para predecir la valoración de un restaurante asiático en función de sus características, comparando diferentes técnicas y evaluando su interpretabilidad. Como valor añadido, se plantea la productivización del modelo mediante una aplicación sencilla que permita estimar el éxito potencial de un nuevo restaurante asiático en una ciudad europea.

---

## 🛠️ TECNOLOGÍAS Y LIBRERÍAS

- **Lenguaje:** Python 3
- **Entorno:** Jupyter Notebook (exportar a HTML al finalizar)
- **Librerías principales:**
  - `pandas` — manipulación de datos
  - `numpy` — operaciones numéricas
  - `matplotlib` / `seaborn` — visualización
  - `plotly` — gráficos interactivos (mapas geográficos)
  - `scikit-learn` — modelos ML y preprocesamiento
  - `xgboost` — modelo XGBoost
  - `shap` — interpretabilidad del modelo
  - `fastapi` o `streamlit` — productivización (opcional)

---

## 📅 PLANNING SEMANAL

### Semana 1 — 7 al 13 agosto · ARRANQUE
- [ ] Descargar el dataset de Kaggle
- [ ] Cargar el dataset con pandas
- [ ] Filtrar restaurantes asiáticos
- [ ] Primera exploración: shape, columnas, tipos de datos, nulos
- [ ] Instalar todas las librerías necesarias

### Semana 2 — 14 al 20 agosto · EDA
- [ ] Análisis exploratorio completo
- [ ] Gráficos de distribución por país, ciudad, tipo de cocina
- [ ] Mapa geográfico de restaurantes asiáticos en Europa
- [ ] Análisis de valoraciones (ratings) y número de reseñas
- [ ] Identificar variables más relevantes para el modelo

### Semana 3 — 21 al 27 agosto · PREPROCESAMIENTO Y PRIMEROS MODELOS
- [ ] Limpieza de datos (nulos, outliers, encoding)
- [ ] Transformación de variables (feature engineering)
- [ ] Dividir en train/test
- [ ] Entrenar modelos iniciales: Regresión Lineal, Random Forest, XGBoost
- [ ] Comparativa de métricas (RMSE, MAE, R²)

### Semana 4 — 28 agosto al 3 septiembre · MODELIZACIÓN AVANZADA
- [ ] Ajuste de hiperparámetros (GridSearchCV / RandomizedSearchCV)
- [ ] Interpretabilidad con SHAP (gráficos de importancia de variables)
- [ ] Productivización: función o app sencilla que reciba inputs y devuelva predicción de rating
- [ ] Validación cruzada

### Semana 5 — 4 al 10 septiembre · DOCUMENTACIÓN
- [ ] Redactar la memoria (máx. 20 páginas, fuente Verdana/Arial 10-11)
- [ ] Preparar anexos con el código completo
- [ ] Exportar el notebook a HTML
- [ ] Revisar que el informe sea comprensible para perfil de negocio

### Semana 6 — 11 al 17 septiembre · CIERRE Y ENTREGA
- [ ] Grabar el vídeo (máx. 5 minutos, formato MP4, máx. 50MB)
- [ ] Revisión final con el checklist de la guía
- [ ] Subir todo a la plataforma
- [ ] **ENTREGA: 17 de septiembre**

---

## ✅ CHECKLIST FINAL (según guía UCM)

- [ ] ¿Has visto los derechos de uso de los datos? (Kaggle - público ✅)
- [ ] ¿Tienes el código compartido en GitHub o Drive/Dropbox?
- [ ] ¿Es accesible desde el link?
- [ ] ¿Santiago Mota y Carlos Ortega tienen permisos de acceso?
- [ ] ¿La memoria ocupa máximo 20 hojas?
- [ ] ¿Tienes el código en los Anexos?
- [ ] ¿El proyecto es reproducible?
- [ ] ¿Has incluido un apartado de conclusiones?
- [ ] ¿Has incluido el vídeo de máximo 5 minutos?
- [ ] ¿El vídeo describe el proyecto (no es un elevator pitch)?
- [ ] ¿Has incluido bibliografía (máx. media página)?

---

## 📁 ESTRUCTURA DE ENTREGABLES

```
NombreApellido1Apellido2_Gastronomia_Asiatica_Europa.zip
│
├── memoria.html          # Jupyter Notebook exportado a HTML (máx. 20 páginas)
├── video.mp4             # Vídeo presentación (máx. 5 min / 50MB)
└── anexos/
    └── notebook.ipynb    # Código completo con EDA, modelos, etc.
```

---

## 🔑 NOTAS IMPORTANTES

- El trabajo es **individual**
- No se admiten cambios de tema a **menos de 15 días** de la entrega (límite: ~2 septiembre)
- Las dudas a tutores deben enviarse **por escrito** (correo o foro), nunca por llamada
- Los errores de instalación de librerías hay que resolverlos de forma **autónoma**
- No presentar en PowerPoint — usar memoria técnica redactada
- No presentar como artículo científico
- El vídeo no requiere aparecer en cámara, pero sí voz en off
- La portada, contraportada e índice **no cuentan** para las 20 páginas
