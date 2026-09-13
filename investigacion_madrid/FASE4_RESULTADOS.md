# Fase 4 — Renta residencial y primeras observaciones de alquiler comercial

Consulta: 12 de septiembre de 2026. Objetivo: estudiar la viabilidad de un buffet de sushi en el municipio de Madrid. No constituye una recomendación de inversión ni una selección definitiva de ubicación.

## Renta: evidencia oficial reproducible

Se extrajeron los 21 distritos municipales del servicio del INE ADRH 2023, con filtro CUMUN='28079', sin geometría. Se comprobaron año, indicador, unicidad y ausencia de truncamiento. Datos originales en `fuentes/renta_ine_2023_distritos.json`; normalización reproducible mediante `analizar_renta.py`; resultados en `renta_distritos_2023.json`.

| Distrito de contexto | Barrio estudiado previamente | Renta neta anual por persona, 2023 | Renta neta anual por hogar, 2023 |
|---|---|---:|---:|
| Chamartín | Nueva España | 32.019,21 € | 79.274,17 € |
| Moncloa-Aravaca | Argüelles | 27.768,35 € | 71.710,88 € |
| San Blas-Canillejas | Simancas | 16.769,49 € | 44.468,00 € |
| Barajas | Casco Histórico de Barajas | 22.220,26 € | 58.405,49 € |

Fuente: [servicio oficial INE, capa distritos](https://www.ine.es/servergis/rest/services/ws/ADRH_2023_Renta_media_por_hogar/MapServer/2). La [nota de publicación](https://www.ine.es/dyngs/Prensa/ADRH2023.htm) está fechada el 21/10/2025 y refiere al ejercicio 2023. Fecha de consulta no equivale a año de renta. Estos valores son de distrito: no se atribuyen al barrio de la segunda columna. La diferencia entre renta por persona y hogar depende también del tamaño y composición del hogar.

La renta describe capacidad económica residencial, pero no mide intención de consumir sushi, gasto en restauración, demanda turística ni flujo de trabajadores. No permite proyectar ventas. No se extrapola automáticamente a 2026 ni se pondera renta por hogar con habitantes de 2026 para fabricar una media de barrio.

## Alquiler: muestra exploratoria, no índice de mercado

| Identificador / zona anunciada | Alquiler mensual | Superficie anunciada | €/m²/mes calculado | Traspaso |
|---|---:|---:|---:|---:|
| 109944002 / Casco Histórico de Barajas, Plaza del Jubilado 2 | 760 € | 70 m² construidos; 61 útiles | 10,86 (construidos) | 80.000 € |
| 111165309 / Casco Histórico de Barajas, Feriantes s/n | 1.600 € | 130 m² construidos | 12,31 | 70.000 € |
| 76617-112243119 / Argüelles | 5.000 € | 400 m² anunciados | 12,50 | 120.000 € |

Fuentes individuales: [Plaza del Jubilado](https://www.idealista.com/inmueble/109944002/), [Feriantes](https://www.idealista.com/inmueble/111165309/), [Argüelles](https://www.yaencontre.com/traspaso/negocio/inmueble-76617-112243119).

Jubilado: el anunciante declara aforo 35, licencia bar-restaurante y extracción instalada; fianza anunciada de dos meses. La página abierta indica actualización «8 de septiembre», sin año explícito. Feriantes: se anuncia extracción y cocina equipada; honorarios de agencia del 15% de renta anual. Este segundo registro procede del texto indexado: disponibilidad y condiciones requieren reconfirmación. Argüelles: fianza de dos meses; dirección exacta, superficie útil y condiciones técnicas pendientes. No sumar superficies opcionales a los 400 m² publicados.

Todos son precios solicitados, no contratos cerrados. IVA, gastos repercutidos y duración contractual quedan pendientes. Las afirmaciones de licencia, aforo y extracción son del anunciante; no se han contrastado con expedientes. No se adopta su publicidad sobre afluencia o facturación como evidencia de demanda.

Los tamaños y condiciones son distintos; 70 m² no es comparable sin ajustes a 400 m². No se calcula media por barrio ni se concluye que Barajas sea más rentable. No hay todavía muestras verificadas suficientes de Nueva España o Simancas. La muestra no es aleatoria ni exhaustiva.

## Uso en el modelo de viabilidad

Separar alquiler recurrente, traspaso inicial, fianza recuperable, obras, equipamiento y capital de trabajo. El traspaso no sustituye al alquiler y tampoco equivale a inversión inicial total.

Como identidad de sensibilidad, si cada cliente aporta 10 € después de costes variables (supuesto ilustrativo, no estimación), un aumento de alquiler de 1.000 €/mes requiere 100 clientes adicionales al mes para mantener el mismo resultado operativo. Esta relación no predice que se consigan esos clientes.

La siguiente fase debe construir escenarios con ticket neto, coste de alimentos y desperdicio, personal, otros costes fijos, capacidad y días abiertos. El umbral de clientes requerido puede calcularse; la probabilidad de alcanzarlo sigue necesitando observación de demanda. No se aplica XGBoost de valoraciones para estimar rentabilidad.

## Texto propuesto para la memoria

Se incorpora información oficial de renta neta residencial por distrito (INE, ejercicio 2023) y una muestra exploratoria de ofertas de locales consultadas en septiembre de 2026. Se mantienen separados el nivel territorial, el periodo de referencia y la naturaleza de cada variable. Las rentas residenciales contextualizan el poder adquisitivo, mientras que los anuncios permiten formular escenarios de costes sujetos a validación. Ninguna de estas fuentes identifica por sí sola ventas futuras ni rentabilidad. La evidencia disponible permite estudiar condiciones necesarias de viabilidad, pero todavía no afirmar que una apertura concreta sea rentable.
