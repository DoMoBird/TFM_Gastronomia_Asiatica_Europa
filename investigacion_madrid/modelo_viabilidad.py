"""Escenarios ilustrativos, no previsión de demanda ni beneficio neto."""
import json, math
from pathlib import Path
BASE = Path(__file__).resolve().parent

def evaluar(p):
    for k in ('ticket_bruto', 'dias', 'asientos', 'servicios', 'rotaciones'):
        if p[k] <= 0: raise ValueError(k)
    if not 0 <= p['ocupacion'] <= 1 or not 0 <= p['ratio_alimentos'] < 1: raise ValueError('ratio')
    if p['iva'] < 0 or p['variable_extra'] < 0 or any(v < 0 for v in p['fijos'].values()): raise ValueError('coste')
    neto = p['ticket_bruto'] / (1 + p['iva'])
    margen = neto * (1-p['ratio_alimentos']) - p['variable_extra']
    fijos = sum(p['fijos'].values())
    capacidad = p['dias'] * p['asientos'] * p['servicios'] * p['rotaciones']
    clientes = capacidad * p['ocupacion']
    umbral = fijos / margen if margen > 0 else None
    return dict(ticket_neto=neto, margen_cliente=margen, fijos_mes=fijos,
        capacidad_clientes_mes=capacidad, clientes_mes=clientes,
        ingresos_netos_mes=clientes*neto, resultado_operativo_mes=clientes*margen-fijos,
        umbral_clientes_mes=umbral, clientes_enteros_minimos=math.ceil(umbral) if umbral is not None else None,
        umbral_clientes_dia=umbral/p['dias'] if umbral is not None else None,
        ocupacion_equilibrio=umbral/capacidad if umbral is not None else None,
        equilibrio_dentro_capacidad=umbral is not None and umbral <= capacidad)

def generar():
    config=json.loads((BASE/'supuestos_viabilidad.json').read_text())
    resultados={k:evaluar(v) for k,v in config['escenarios'].items()}
    base=config['escenarios']['referencia']
    sensibilidad=[]
    for ticket in (22,26,30):
        for ratio in (.30,.38,.46):
            p={**base,'ticket_bruto':ticket,'ratio_alimentos':ratio}
            sensibilidad.append({'ticket_bruto':ticket,'ratio_alimentos':ratio,**evaluar(p)})
    out={'advertencia':config['advertencia'],'escenarios':resultados,'sensibilidad':sensibilidad}
    (BASE/'resultados_viabilidad.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    return out

if __name__ == '__main__':
    for nombre,r in generar()['escenarios'].items():
        print(nombre, 'clientes/día:',round(r['umbral_clientes_dia'],1), 'ocupación:',round(r['ocupacion_equilibrio']*100,1),'resultado:',round(r['resultado_operativo_mes']))
