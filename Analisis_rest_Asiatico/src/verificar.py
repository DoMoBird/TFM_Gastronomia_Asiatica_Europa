"""Pruebas de contrato y paridad: no reentrena ni cambia la selección."""
import copy,json,sys
from pathlib import Path
import numpy as np,pandas as pd
from servir import Predictor
p=Predictor();base=Path(__file__).resolve().parents[1]
r=json.loads((base/'resultados/ejemplo_entrada.json').read_text())
pred=p.predict(r)['rating_estimado']
direct=float(p.model.predict(pd.DataFrame([{k:np.nan if v is None else v for k,v in r.items()}]))[0])
assert abs(pred-direct)<1e-12
invalid=[{**r,'latitude':999},{**r,'country':'Atlantis'},{**r,'latitude':float('nan')},{**r,'cuisine_chinese':.5},{**r,'extra':1},{**r,'country':None},[]]
other=next(c for c in p.pairs if r['region'] not in p.pairs[c]);invalid.append({**r,'country':other})
for row in invalid:
 try:p.predict(row)
 except ValueError:pass
 else:raise AssertionError('Entrada inválida aceptada')
sparse={**r,'latitude':None};assert any('imputados' in w for w in p.predict(sparse)['advertencias'])
assert not any(x in p.schema for x in ['food','service','value','atmosphere','log_reviews_count','avg_rating'])
print('OK: paridad, 8 rechazos, imputación explícita y ausencia de reputación en API')
