"""Reproduce el filtro exploratorio; no clasifica formato buffet."""
from pathlib import Path
import json, hashlib
import pandas as pd
p = Path(__file__).resolve().parent
f = p / 'fuentes/censo_locales.csv'
d = pd.read_csv(f, sep=';', dtype=str).apply(lambda s: s.str.strip())
x = d[d.rotulo.fillna('').str.contains(r'sushi|kojima|ginza|azuki|sumo|ichi', case=False, regex=True)]
cols = ['id_local','rotulo','desc_distrito_local','desc_barrio_local','desc_vial_acceso','num_acceso','desc_situacion_local','fx_carga']
(p/'candidatos_censo.json').write_text(x[cols].to_json(orient='records',force_ascii=False,indent=2))
print(json.dumps({'filas':len(d),'ids_unicos':d.id_local.nunique(),'candidatos':len(x),'estados':x.desc_situacion_local.value_counts().to_dict(),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
