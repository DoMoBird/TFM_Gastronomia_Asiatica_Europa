"""Normaliza el snapshot INE ADRH 2023; no imputa renta de distrito a barrios."""
import json
from pathlib import Path
BASE = Path(__file__).resolve().parent
SOURCE = 'https://www.ine.es/servergis/rest/services/ws/ADRH_2023_Renta_media_por_hogar/MapServer/2/query'
QUERY = {'f': 'json', 'where': "CUMUN = '28079'", 'outFields': '*', 'returnGeometry': 'false'}
raw = json.loads((BASE/'fuentes/renta_ine_2023_distritos.json').read_text())
assert not raw.get('exceededTransferLimit') and 'error' not in raw
names = {int(r['COD_DISTRITO']): r['DESC_DISTRITO'] for r in json.loads((BASE/'padron_distritos.json').read_text())}
rows = []
for feature in raw['features']:
    a = feature['attributes']
    assert a['CUMUN'] == '28079' and a['anyo'] == '2023'
    assert a['indicador1'] == 'Renta neta media por persona'
    assert a['indicador2'] == 'Renta neta media por hogar'
    rows.append({'codigo_ine': a['CUDIS'], 'distrito': names[int(a['CDIS'])], 'anio_renta': 2023, 'renta_neta_anual_persona_eur': a['dato1'], 'renta_neta_anual_hogar_eur': a['dato2']})
assert len(rows) == len({r['codigo_ine'] for r in rows}) == 21
rows.sort(key=lambda r:r['codigo_ine'])
(BASE/'renta_distritos_2023.json').write_text(json.dumps({'fuente':SOURCE,'consulta':QUERY,'fecha_consulta':'2026-09-12','datos':rows},ensure_ascii=False,indent=2)+'\n')
for r in rows:
    if r['codigo_ine'][-2:] in ('05','09','20','21'): print(r)
