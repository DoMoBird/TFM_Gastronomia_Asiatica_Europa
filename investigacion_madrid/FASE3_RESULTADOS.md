# Fase 3: depuración territorial, padrón y nuevo competidor

Consulta 12/09/2026. Investigación exploratoria, no censo completo ni recomendación de ubicación.

## Padrón agregado

Se descargó el CSV municipal enlazado desde https://datos.gob.es/es/catalogo/l01280796-padron-municipal1 . Datos internos: 01/08/2026; carga: 18/08/2026. 241.260 filas; 21 distritos y 131 barrios; suma de los cuatro campos de sexo/nacionalidad: 3.520.470 residentes.

Se conservaron todos los registros: no hay duplicados completos. Tres coincidencias de sección/edad corresponden a barrios distintos; eliminar por esa clave hubiera perdido población. Script analizar_padron.py, control_padron.json y agregados padron_barrios.json / padron_distritos.json permiten reproducir el cálculo.

## Direcciones de competidores contrastadas con el censo

| Marca actual en web | Barrio en registros de esa dirección | Residentes del barrio | Calidad del enlace |
|---|---|---:|---|
| Azuki, Canal de Suez 1 | Casco Histórico de Barajas (2103) | 8.838 | Nombre y dirección coinciden: id_local 210000291 |
| Sushi Ichi, Juan Ramón Jiménez 22 | Nueva España (505) | 25.502 | Dirección coincide, censo dice Restaurante Jiménez 22; identidad de local pendiente |
| Kojima, Miguel Yuste 58 | Simancas (2001) | 31.046 | Varios locales en dirección, ninguno con marca Kojima; no asignar ID aún |
| Kote, Princesa 13 | Argüelles (902) | 24.979 | Varios locales y nombres diferentes; no asignar ID aún |

Población corresponde al barrio entero, no al radio comercial de cada establecimiento. No usar estos cuatro conteos para elegir ganador: faltan trabajadores, visitantes, rentas, locales disponibles y competencia exhaustiva. Los datos administrativos no garantizan que la marca del rótulo esté actualizada.

## Kote: nuevo registro de precio y condiciones

Fuente de ubicación: https://koterestaurante.com/ (Princesa 13).
Fuente de carta y condiciones: https://koterestaurante.com/carta/ . Buffet y selección de nigiris/makis publicados.

- Comida L-V no festivos: 19,90 €.
- Otra tarifa: 26,90 €, publicada como domingo a jueves no festivos ni vísperas; el texto no especifica explícitamente noche. No asignar franja automáticamente.
- Viernes noche a domingo mediodía, festivos y vísperas: 29,90 €.
- Bebida y postre excluidos; bebida mínima obligatoria; agua 2,95 €.
- 90 minutos; hasta dos platos/persona/ronda; misma modalidad para toda la mesa; penalización publicada por desperdicio.
- Consumo publicado calculado buffet de comida + agua: 22,85 €. Para tarifa de 29,90 € + agua: 32,85 €. No es ticket medio observado, ni ingreso neto; tratamiento de IVA pendiente de confirmar.

No tomar los precios individuales de platos como coste del buffet. No extraer capacidad del tiempo máximo: 90 minutos no demuestra la rotación efectiva.

## Calidad de candidatos

El filtro amplio anterior contiene coincidencias parciales ajenas al sector (CONSUMO coincide con sumo, bancos con Pichincha coinciden con ichi). Sus 246 registros solo son una cola de revisión. Mejorar filtro con límites de palabra para marcas, conservar sushi como búsqueda amplia y mantener un registro separado de exclusiones. No eliminar silenciosamente el fichero inicial.

SUMO Fuencarral: fuente oficial https://sumorestaurante.com/restaurantes/sumo-fuencarral/ devolvió verificación anti-bot. Se mantiene candidato sin nuevo precio validado. No usar precios históricos de buscador como actuales.

## Estado y siguiente análisis

Ya hay base demográfica por barrio y tres locales con precios publicados (Ichi, Azuki, Kote). Aún falta ampliar y validar cobertura antes de construir un índice de competencia. La selección de 2-3 áreas debe apoyarse también en oferta inmobiliaria, público objetivo y costes, no solo habitantes.
