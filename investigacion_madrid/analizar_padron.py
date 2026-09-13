from pathlib import Path
import pandas as pd
import json,hashlib
p=Path(__file__).resolve().parent
f=p/'fuentes/padron.csv'
d=pd.read_csv(f,sep=';',dtype=str).apply(lambda s:s.str.strip())
counts=['ESPANOLESHOMBRES','ESPANOLESMUJERES','EXTRANJEROSHOMBRES','EXTRANJEROSMUJERES']
for c in counts:d[c]=pd.to_numeric(d[c],errors='raise')
assert not d.duplicated().any()
assert not d.duplicated(['COD_DIST_BARRIO','COD_DIST_SECCION','COD_EDAD_INT','FX_DATOS_INI']).any()
d['poblacion']=d[counts].sum(axis=1)
for label,keys in [('distritos',['COD_DISTRITO','DESC_DISTRITO']),('barrios',['COD_DISTRITO','COD_DIST_BARRIO','DESC_BARRIO'])]:
 a=d.groupby(keys,as_index=False).poblacion.sum();assert a.poblacion.sum()==d.poblacion.sum()
 (p/f'padron_{label}.json').write_text(a.to_json(orient='records',force_ascii=False,indent=2))
meta={'fuente':'https://datos.madrid.es/dataset/200076-0-padron/resource/200076-2-padron-csv/download/200076_20260714_062859.csv','fecha_datos':d.FX_DATOS_INI.unique().tolist(),'fecha_carga':d.FX_CARGA.unique().tolist(),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'filas':len(d),'poblacion':int(d.poblacion.sum()),'distritos':d.COD_DISTRITO.nunique(),'barrios':d.COD_DIST_BARRIO.nunique(),'nota':'La sección y edad no son clave única sin barrio; no eliminar esas coincidencias.'}
(p/'control_padron.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
print(meta)
b=pd.read_json(p/'padron_barrios.json');print(b[b.COD_DIST_BARRIO.isin([506,505,2001,2101,901])].to_string(index=False))
