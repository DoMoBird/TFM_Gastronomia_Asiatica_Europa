# Madrid: estudio de mercado y viabilidad económica

> **Actualización de alcance, 13/09/2026:** esta investigación se conserva como aplicación complementaria y anexo. El núcleo del TFM vuelve a la propuesta aprobada: análisis europeo y predicción de rating. Véase [revisión académica](../revision_academica/README.md). La pregunta económica que sigue documenta esta línea exploratoria; no sustituye la pregunta principal del TFM.

Fecha de consulta: 12/09/2026. Autor del TFM: Peng Chen.

## Pregunta de investigación
¿Bajo qué condiciones de ubicación, precio, demanda y costes sería económicamente viable abrir un restaurante de sushi tipo buffet libre en el municipio de Madrid?

Alcance: municipio de Madrid, no toda la Comunidad. Unidad de competencia: establecimiento físico, no marca. La base inicial es una muestra de descubrimiento no exhaustiva. Una web accesible prueba la oferta publicada, no una inspección presencial ni la apertura efectiva a fecha de consulta.

## Evidencia inicial de competencia

| Establecimiento | Dirección publicada | Formato publicado | Fuente primaria | Estado |
|---|---|---|---|---|
| Kojima Sushi | C. de Miguel Yuste, 58, 28037 Madrid | Buffet libre con sushi; web lo sitúa en San Blas-Canillejas | https://www.kojimasushi.es/ | Dirección y formato leídos en web; precios pendientes |
| Sushi Ichi | C/Juan Ramón Jiménez, 22, 28036 Madrid | Buffet a la carta de sushi | https://www.sushiichimadrid.com/ | Dirección y formato leídos; menú PDF enlazado, precio no transcrito |
| Ginza Asian Food Hall | Plaza de las Cortes, 3, 28014 Madrid | Buffet libre asiático | https://ginzafoodhall.com/ | Dirección y formato en resultado indexado oficial; apertura directa falló; reconfirmar contenido y sushi en buffet |
| Sol Sushi | Pendiente de lectura verificable | Running sushi buffet libre | https://www.solsushi.es/ | Formato leído; dirección pendiente, no contar aún en censo municipal validado |
| Umi Sushi Buffet | Pendiente | Buffet asiático con sushi | https://umisushibuffet.com/ | Candidato en buscador; web no se pudo abrir, pendiente |

Menú de Sushi Ichi enlazado por su web: https://www.sushiichimadrid.com/_files/ugd/4b1306_dd3b7aacfaec4be2adf91a6d6cbcdc39.pdf
Menú de Ginza localizado: https://ginzafoodhall.com/wp-content/uploads/2024/01/Buffet-libre-GINZA.pdf (lector web rechazó el tamaño; no se extrajeron precios).

Estos registros NO son el total de competidores. No se calcula densidad ni cuota de mercado con esta muestra.

## Fuentes para el análisis territorial

1. Censo de locales y actividades del Ayuntamiento. Fuente: https://datos.gob.es/es/catalogo/l01280796-censo-de-locales-sus-actividades-y-terrazas-de-hosteleria-y-restauracion
   Uso: direcciones, identificadores, estado registrado y actividades. Un local puede tener varias actividades; deduplicar por id_local antes de contar. No identifica necesariamente sushi ni buffet; cruzar con investigación comercial. No confundir actividad registrada con licencia autorizada.
2. Padrón municipal: https://datos.gob.es/es/catalogo/l01280796-padron-municipal1
   Uso: población residente por distrito/barrio/sección, edad y sexo. Residentes no equivalen a clientes ni a flujo peatonal.
3. Panel de indicadores: https://datos.gob.es/es/catalogo/l01280796-panel-de-indicadores-de-distritos-y-barrios-de-madrid-estudio-sociodemografico1
   Uso: contexto territorial socioeconómico. Comprobar año de cada variable antes de comparar; publicación reciente no garantiza observaciones recientes.
4. Indicadores demográficos a 1/1/2025: https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/dataset.iam?id=14a90c28-23f3-11eb-b20f-98e7f4edb47e
   Uso: cartografía demográfica y límites para comparación territorial, no estimación directa de demanda de sushi.

Se han localizado las fuentes, pero todavía NO se han descargado ni analizado sus microdatos. No se ha seleccionado un barrio ganador.

## Protocolo de recogida

Buscar por distrito combinando sushi/buffet libre/buffet a la carta/running sushi/all you can eat. Registrar también consultas sin resultados. Deduplicar nombre y dirección, verificar municipio, conservar URL y fecha por campo. Separar confirmados, candidatos, cerrados y excluidos. No interpretar ausencia de etiqueta como ausencia de formato.

Campos necesarios por local: nombre, marca, dirección, municipio, distrito/barrio oficiales, coordenadas con procedencia, formato, precio adulto comida laborable, cena laborable y fin de semana, bebida obligatoria e importe, postre incluido, límites de tiempo/platos, fecha del menú, fecha de consulta, fuente y grado de verificación. Precios desconocidos quedan nulos. No combinar precio de menú del día convencional con buffet.

Para ocupación: observación repetida entre semana y fin de semana, comida y cena, indicando fecha/hora, capacidad observable y limitaciones. No deducir ventas del número de reseñas.

## Modelo económico a construir

Inputs pendientes de evidencia: presupuesto inicial, alquiler de locales concretos, adecuación/obra, equipamiento, fianza, personal y costes de empresa, suministros, seguros, coste de ingredientes, mermas, comisiones, días abiertos, asientos y rotación por servicio. Usar presupuestos con fecha; mantener supuestos separados de datos observados.

Trabajar con ingresos y costes sobre una base fiscal consistente; no comparar ticket con impuestos incluidos con ingresos netos. Definir si el resultado es operativo, antes de amortizaciones, financiación e impuestos, o flujo de caja.

- Clientes mensuales = suma por servicio de asientos × rotaciones × ocupación × días correspondientes.
- Ingreso neto mensual = suma de clientes por servicio × ticket neto por servicio.
- Margen de contribución por cliente = ticket neto − coste variable por cliente (incluye merma atribuible).
- Umbral de clientes = costes fijos / margen de contribución positivo.
- Resultado operativo simplificado = ingreso neto − costes variables − costes fijos.
- Liquidez: inversión inicial + déficit acumulado durante arranque + reserva; incluir calendario de pagos.

Evaluar escenarios y sensibilidad en ocupación, ticket, alquiler, plantilla y materia prima. No introducir cifras como si fueran estimaciones de Madrid hasta disponer de fuentes. No afirmar rentabilidad aún.

## Integración académica

Conservar análisis europeo y comparación de modelos como contexto/apéndice. El predictor actual describe valoración condicionada a subpuntuaciones; no demuestra demanda, causalidad, rentabilidad ni éxito antes de apertura.

Nueva estructura: resumen; pregunta y alcance; fuentes y calidad; competencia; comparación territorial; metodología económica; escenarios; discusión y límites; conclusiones; bibliografía y anexos reproducibles.

La nueva pregunta y el peso del componente económico deben contrastarse con la guía y tutores antes de dar la memoria por definitiva. No se han modificado ni publicado los entregables anteriores en esta fase.

## Actualización de fase 2

Ver FASE2_RESULTADOS.md: censo descargado y auditado, candidatos generados y dos menús contrastados. Sustituye el estado anterior «microdatos aún no descargados» para el censo; padrón e indicadores siguen pendientes.

## Actualización de fase 3

Ver FASE3_RESULTADOS.md: padrón descargado/agregado, direcciones cotejadas y Kote añadido. El padrón ya no está pendiente; indicadores de renta y validación exhaustiva de competidores sí.

### Fase 4: renta y locales

Véase [FASE4_RESULTADOS.md](FASE4_RESULTADOS.md): extracción validada de los 21 distritos del INE ADRH 2023, tres primeras observaciones de locales con alquiler y traspaso separados, y limitaciones de comparabilidad. `analizar_renta.py` reproduce la normalización del snapshot oficial conservado; `renta_distritos_2023.json` contiene los resultados. Pendiente ampliar la muestra de locales y construir escenarios operativos.

### Fase 5: modelo de escenarios operativos (13/09/2026)

[FASE5_RESULTADOS.md](FASE5_RESULTADOS.md) documenta supuestos y límites. Notebook: `05_viabilidad_madrid.ipynb`; parámetros: `supuestos_viabilidad.json`; cálculo: `modelo_viabilidad.py`. Los parámetros comerciales son ilustrativos, no una previsión calibrada. Se calcula equilibrio operativo; inversión inicial y demanda real siguen pendientes.
