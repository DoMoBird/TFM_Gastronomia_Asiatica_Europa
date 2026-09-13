# Guion revisado del vídeo

Peng Chen · 10 diapositivas · objetivo: menos de 5 minutos.
Ensayar y medir la duración real; no basta con estimarla por palabras.

## 1. Gastronomía asiática en Europa

Hola, soy Peng Chen. Mi trabajo analiza restaurantes asiáticos en Europa, con especial foco en España. Combina análisis exploratorio, predicción de valoración y una aplicación local. Mi interés inicial por abrir un buffet de sushi en Madrid sirve como motivación, pero distingo esa decisión de lo que realmente permite demostrar el dataset.

## 2. Datos y adecuación al problema

Parto de TripAdvisor European Restaurants, publicado en 2021. El filtro asiático contiene 86.306 restaurantes, y 81.315 tienen valoración válida. Verifiqué la licencia CC0 declarada en la API de Kaggle. La muestra es histórica y depende de la cobertura de la plataforma. Por eso no la trato como un censo actual ni como una base de beneficios empresariales.

## 3. Comparación europea y foco en España

England, France, Germany y Spain concentran una parte importante de los registros. España aporta 8.295 restaurantes. Conservo las etiquetas originales: England no equivale a todo el Reino Unido. Además, la ciudad está incompleta en muchos registros españoles, por lo que no afirmo que Madrid sea el mayor mercado. Las diferencias geográficas describen la muestra, no oportunidades de inversión demostradas.

## 4. Predicción y disponibilidad de información

Comparo dos variantes. La primera utiliza ubicación, horarios, precio, dietas y cocinas. La segunda añade comida, servicio, valor, ambiente y número de reseñas. Estas opiniones ya existentes están estrechamente relacionadas con el rating objetivo. La comparación permite comprobar cuánto depende el resultado de información reputacional. Ninguna variante se ha validado como predicción de una nueva apertura.

## 5. Selección de modelos en validación

Separé entrenamiento, validación y test, estratificando por territorio. La imputación y codificación se ajustan dentro del pipeline. Comparé una referencia de media, regresión lineal, Random Forest y XGBoost. Seleccioné el algoritmo por validación y reservé el test para evaluación final. La diferencia entre los dos conjuntos de árboles sin reputación es pequeña; no la presento como una superioridad general de Random Forest.

## 6. Error de predicción en test: RMSE

En las mismas 16.263 observaciones de test, la referencia tiene un RMSE de 0,695. Sin reputación, Random Forest baja a 0,625 y su error absoluto medio es de 0,462 puntos. Con reputación, XGBoost alcanza 0,542 de RMSE y 0,361 de error absoluto medio. La mejora es real en esta muestra, pero no demuestra capacidad para predecir rentabilidad ni generalización a datos actuales.

## 7. Interpretabilidad y límites

Recalculé la importancia mediante permutación sobre una muestra de validación. Sin reputación destacan algunas etiquetas y horarios; con reputación destacan comida y servicio. El gráfico muestra cuánto empeora el error al desordenar una variable. Esto explica dependencia del modelo, no el efecto causal de cambiar el negocio. Las variables correlacionadas y la falta de información pueden influir en ese orden.

## 8. Productivización del modelo

El modelo sin reputación se integra en una aplicación local. El usuario introduce características y recibe una estimación identificada por versión. El sistema comprueba tipos, rangos y correspondencia entre país y región; informa de los valores imputados. Probé que la API coincide con el pipeline y rechaza entradas inválidas. Hay contadores básicos de uso y ausencias, aunque todavía no es un servicio empresarial desplegado.

## 9. Madrid como aplicación complementaria

Para Madrid incorporé censo de locales, padrón, renta del INE y ofertas de restaurantes. Estas fuentes mejoran el contexto y la discusión de actualidad, pero no aportan directamente ventas futuras. No interpreto unos pocos buffets etiquetados como el total de competidores. Los escenarios de equilibrio permanecen como anexo: calculan condiciones bajo supuestos, sin demostrar que una inversión concreta sea rentable.

## 10. Conclusiones y siguientes mejoras

La conclusión principal es que puedo estimar valoraciones históricas con una mejora moderada sobre una referencia sencilla, explicar parte del comportamiento del modelo y demostrar una aplicación reproducible. La lección es elegir variables según su disponibilidad y no confundir rating con éxito económico. La siguiente mejora sería validar con una captura independiente y actual, y medir la utilidad real de la herramienta. Gracias.

## Grabación

Usar presentacion_revisada_v2.pptx. Voz del alumno obligatoria; cámara opcional. Entregar MP4 de hasta 5 minutos y procurar no superar 50 MB. Esta revisión no incluye un vídeo grabado.
