# Fase 2: precios publicados y candidatos del censo

Consulta: 12/09/2026. Resultados provisionales, no recomendación de inversión.

## Precios adultos publicados

| Local | Comida laborable | Cena laborable | Otras franjas | Condiciones |
|---|---|---|---|---|
| Sushi Ichi, Juan Ramón Jiménez 22 | 18,80 € L-V no festivos | 26,80 € L-J no festivos ni vísperas | 28,80 €: viernes noche, domingos, festivos y vísperas según texto del PDF; sábado no aparece explícito, consultar | IVA incluido; mínimo una bebida por persona; bebida y postre excluidos; 3 € por plato no consumido; no compartir ni llevar |
| Azuki, Canal de Suez 1, Barajas | Desde 16,50 € L-V no festivos | 22,50 € L-J | 25,50 € viernes noche, fines de semana y festivos | Bebidas y postres excluidos; IVA y obligatoriedad de bebida no confirmados en página consultada |

Fuentes primarias:
- Ichi: https://www.sushiichimadrid.com/_files/ugd/4b1306_dd3b7aacfaec4be2adf91a6d6cbcdc39.pdf — leído visualmente, copia local fuentes/ichi_menu.pdf. No consta fecha de vigencia. El menú de 17,50 € es de cuatro platos, NO buffet; no incluirlo como precio buffet. Horario de PDF y web difiere: no usar sin confirmar.
- Azuki: https://www.azukisushimadrid.com/buffet-sushi-madrid-barajas — precios en texto oficial, consultados hoy; no es cotización garantizada ni precio medio de mercado.

No se calcula media de mercado con dos establecimientos. El precio base del buffet no equivale al ticket total ni al ingreso neto. Para comparación homogénea falta el coste de bebida y confirmar impuestos/condiciones.

## Censo municipal descargado

Fuente: https://datos.madrid.es/dataset/200085-0-censo-locales/resource/200085-1-censo-locales/download/200085_20260731_053218.csv

- 203.637 filas, 203.637 identificadores de local únicos, 46 columnas.
- Campo fx_carga: 11/09/2026 en todas las filas. El nombre de URL contiene julio: conservar snapshot y hash, no inferir fecha de observación por nombre.
- Delimitador real: punto y coma; texto con espacios finales. Se eliminaron espacios para comparar.
- 246 candidatos por rotulo que contiene sushi/kojima/ginza/azuki/sumo/ichi (sin distinguir mayúsculas).
- Estados registrados: 220 Abierto, 20 Cerrado, 6 Baja Reunificación.
- Candidatos y metadatos: candidatos_censo.json y control_censo.json.

Estos candidatos NO equivalen a establecimientos de sushi, mucho menos buffet: la búsqueda puede producir falsos positivos (por ejemplo coincidencias parciales con ichi), además de omitir nombres sin palabras clave. El estado Abierto es administrativo, no verificación presencial. Coordenadas son proyectadas; no tratarlas como latitud/longitud sin verificar CRS.

## Exclusiones registradas

Qing Tian Ramen Sushi: https://www.qingtianramenshushi.es/ — página oficial lo sitúa en Murcia. Excluido aunque apareció en búsqueda de Madrid; su precio no entra en la comparación local.

## Próximo trabajo concreto

1. Cruzar direcciones oficiales de competidores con id_local y distrito/barrio del censo; validar manualmente ambigüedades.
2. Revisar los 220 candidatos abiertos y descubrir locales adicionales por búsqueda territorial, registrando no-buffet, cerrado, dudoso y confirmado.
3. Ampliar precios comparables y bebida mínima. No deducir sábado de franjas incompletas.
4. Descargar padrón e indicadores y cruzar por códigos territoriales; solo entonces seleccionar 2-3 áreas para comparar demanda y alquileres. La cantidad de candidatos por distrito no mide atractivo inversor.
5. Recoger cotizaciones y observaciones para escenarios, sin reemplazar datos desconocidos por cifras inventadas.

Los archivos brutos se conservan localmente. No se han subido a GitHub ni modificado los entregables previos.
