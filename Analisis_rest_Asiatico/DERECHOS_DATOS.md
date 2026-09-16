# Anexo A — Fuentes, derechos y minimización de datos

Consulta: 13/09/2026. Esta tabla documenta evidencias y límites; no sustituye una revisión de derechos de terceros.

| Fuente | Evidencia consultada | Tratamiento en esta revisión |
|---|---|---|
| TripAdvisor European Restaurants, Stefano Leone | API oficial Kaggle: CC0: Public Domain, versión 1, actualización 18/05/2021. Respuesta conservada en resultados/kaggle_metadata.json | Análisis de atributos tabulares; atribución y trazabilidad. No se redistribuyen originales en el paquete de revisión |
| Ayuntamiento de Madrid: censo y padrón | Aviso legal autoriza información municipal propia citando fuente/autor; excluye contenido multimedia y material firmado de terceros salvo indicación | Agregaciones propias con fuente, periodo y control; snapshots crudos permanecen locales |
| INE ADRH 2023 | Reutilización de información de origen INE con atribución, fecha y sin desnaturalización ni sugerencia de patrocinio | Elaboración propia de renta por distrito, sin atribuirla a barrios |
| Menús oficiales y anuncios comerciales | No se ha acreditado licencia abierta para el conjunto de sus contenidos | Referencias y hechos puntuales con URL/fecha; no copiar fotos, textos comerciales completos o bases de anuncios |

Enlaces:

- [Dataset](https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants).
- [Consulta API Kaggle](https://www.kaggle.com/api/v1/datasets/list?search=tripadvisor-european-restaurants). La evidencia es el registro cuyo ref coincide exactamente con stefanoleone992/tripadvisor-european-restaurants.
- [Aviso legal municipal](https://datos.madrid.es/pages/aviso-legal).
- [Aviso legal INE](https://www.ine.es/ss/Satellite?L=0&c=Page&cid=1254735849170&p=1254735849170&pagename=Ayuda/INELayout).
- [GDPR, artículo 4 y considerando 26](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## Alcance de CC0 y datos de origen

La licencia declarada por el publicador es evidencia más precisa que «Kaggle es público». No acredita por sí sola que el publicador controle todos los derechos de terceros ni constituye autorización de TripAdvisor para nuevas extracciones. La revisión analiza el fichero ya disponible, no realiza scraping nuevo de reseñas. No se afirma una autorización universal de reutilización de cualquier contenido de la plataforma.

## Campos y privacidad

El esquema original revisado tiene atributos de establecimientos y agregados de opiniones, no columnas específicas de nombre o identificador de reseñadores. Esto no garantiza que todos sus campos de texto libre carezcan de información personal. Por ello se excluyen nombres, enlaces, direcciones, keywords y textos libres de la matriz predictiva y de los resultados públicos de la revisión. restaurant_link sirve localmente para deduplicar; el registro de particiones conserva solo posición de fila y hash del fichero.

El padrón se usa como recuentos estadísticos agregados. No se intenta reidentificar personas, combinar celdas pequeñas ni inferir características individuales. La aplicación no recoge nombres, direcciones o contactos del usuario, no registra IPs ni guarda cuerpos de peticiones. Los contadores de sesión son agregados. El ejemplo de restaurante conserva atributos comerciales sin nombre; no debe calificarse como anonimización irreversible porque las coordenadas pueden permitir identificar el establecimiento. Los nombres comerciales pueden identificar autónomos: no se concluye automáticamente que GDPR sea inaplicable a cualquier uso futuro.

No se utilizan datos privados de empresa ni se necesita un NDA para las fuentes descritas. Incorporarlos en el futuro requeriría revisar permisos, finalidad y los plazos de la guía antes de utilizarlos.
