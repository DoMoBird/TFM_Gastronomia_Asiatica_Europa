# Fase 5 — Umbral de viabilidad operativa

Peng Chen · 13/09/2026

Se entrega `05_viabilidad_madrid.ipynb`, con resultados ejecutados, tabla de sensibilidad y gráfico. Los inputs editables están en `supuestos_viabilidad.json`; `modelo_viabilidad.py` genera `resultados_viabilidad.json`. Ejecutar desde la carpeta de investigación o desde TFM.

## Qué puede responder este modelo

Calcula cuántos clientes hacen falta para cubrir los costes operativos bajo supuestos explícitos. No estima demanda, probabilidad de éxito, beneficio neto, VAN ni recuperación de inversión. Ningún escenario es una estimación calibrada de un restaurante real.

## Supuestos comunes

60 asientos, dos servicios diarios, una rotación por servicio y 26 días abiertos al mes: capacidad teórica de 3.120 clientes/mes. No deriva de la superficie de los anuncios. Costes fijos de 21.000 €/mes: alquiler 3.000; coste de empresa de personal 15.000; suministros fijos 1.500; otros fijos 1.500 €. Todas estas cantidades son ilustrativas y requieren presupuestos; no son medias sectoriales. Personal debe incluir remuneración del promotor si trabaja. La parte variable de suministros debe asignarse sin duplicación al coste variable.

Ticket total con bebidas e IVA. Se aplica 10% para restauración ordinaria conforme a la [referencia AEAT](https://sede.agenciatributaria.gob.es/Sede/ayuda/25manual/IVA.html). Costes expresados sin IVA recuperable; el impuesto no recuperable deberá incorporarse al coste. No se simulan pagos fiscales. Coste variable adicional: 1 €/cliente, aparte de alimentos, bebidas y mermas.

## Resultados ilustrativos

| Escenario | Ticket total | Alimentos, bebidas y merma / ingreso neto | Ocupación supuesta | Clientes/día para equilibrio | Ocupación para equilibrio | Resultado operativo mensual |
|---|---:|---:|---:|---:|---:|---:|
| Tensión | 22 € | 46% | 40% | 82,4 | 68,7% | −8.770 € |
| Referencia | 26 € | 38% | 60% | 59,2 | 49,3% | 4.561 € |
| Favorable | 30 € | 30% | 75% | 44,6 | 37,2% | 21.333 € |

Los escenarios combinan cambios de ticket, coste y ocupación para mostrar un rango; no se asignan probabilidades. El notebook también varía únicamente ticket y ratio de alimentos para aislar su efecto sobre el umbral. «Referencia» no significa escenario más probable. No hay evidencia de que un buffet con ticket más alto alcance mayor ocupación o menor coste porcentual.

Fórmulas: ticket neto = ticket total / (1+IVA); contribución = ticket neto × (1−ratio alimentos) − variable extra; clientes de equilibrio = fijos / contribución. Si contribución no es positiva, no existe umbral finito. Si el umbral supera capacidad, se marca inviabilidad dentro de la capacidad supuesta. Se conserva el umbral continuo y se calcula también el mínimo entero mensual.

## Qué falta antes de decidir invertir

1. Local y capacidad reales; condiciones del arrendamiento y traspaso.
2. Escandallos con proveedores, gramajes, consumo buffet y desperdicio medido.
3. Plantilla y turnos con coste total de empresa; confirmar suficiencia para ambos servicios.
4. Ticket ponderado por comida/cena y laborable/festivo, bebidas, niños y descuentos.
5. Observación de demanda y ocupación por servicio. La renta de distrito no sustituye esta medición.
6. Obra, equipamiento, fianza, traspaso, financiación, calendario de desembolsos y liquidez durante arranque.

La ocupación media puede esconder saturación de fin de semana y baja demanda laboral. Los costes de plantilla y capacidad pueden cambiar por escalones; aquí permanecen fijos dentro del rango ilustrativo. Un resultado positivo antes de amortización y financiación no garantiza caja positiva ni recuperar la inversión inicial.

## Incorporación a la memoria y defensa

Conclusión defendible: «Con la evidencia disponible se puede calcular la demanda mínima exigida por distintos supuestos de operación. No se ha demostrado todavía que la demanda local alcance ese umbral. La decisión de inversión queda condicionada a validar costes, capacidad y afluencia de un emplazamiento concreto».

El antiguo modelo de valoraciones queda como análisis complementario y no alimenta las ventas del modelo económico. No se han sustituido aún la memoria ni la presentación final por estas cifras provisionales.
