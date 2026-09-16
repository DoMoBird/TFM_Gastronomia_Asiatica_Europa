from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parents[1];O=B/'resultados';r=json.loads((O/'evaluacion.json').read_text())
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
d=pd.read_json(O/'eda_paises.json').sort_values('n',ascending=False).head(8)
f,a=plt.subplots(figsize=(8,3.6));a.barh(d.country[::-1],d.n[::-1],color='#8C1D22');a.set(xlabel='Registros asiáticos del snapshot',title='Distribución por etiqueta territorial');f.tight_layout();f.savefig(O/'paises.png',dpi=170);plt.close(f)
names=['Media de entrenamiento','Sin reputación (RF)','Con reputación (XGB)'];v=[r['test']['sin_reputacion']['baseline_media']['RMSE'],r['test']['sin_reputacion']['RMSE'],r['test']['con_reputacion']['RMSE']]
f,a=plt.subplots(figsize=(8,3.2));bars=a.barh(names[::-1],v[::-1],color=['#8C1D22','#536C76','#B9B9B9']);a.set(xlabel='RMSE en test (menor es mejor)',xlim=(0,.8));a.bar_label(bars,fmt='%.3f',padding=5);f.tight_layout();f.savefig(O/'metricas.png',dpi=170);plt.close(f)
f,axs=plt.subplots(1,2,figsize=(9,3.7))
for ax,k,title in zip(axs,['sin_reputacion','con_reputacion'],['Sin reputación','Con reputación']):
 data=r['permutation_validation'][k][:5][::-1];ax.barh([v['feature'] for v in data],[v['delta_RMSE'] for v in data],color='#8C1D22');ax.set(title=title,xlabel='Aumento de RMSE al permutar')
f.tight_layout();f.savefig(O/'interpretacion.png',dpi=170);plt.close(f)
df=pd.read_csv(B.parent/'data/asian_restaurants_europe.csv',low_memory=False)
cuisines=df.cuisines.fillna('').str.split(',').explode().str.strip().value_counts().head(8).to_dict()
extra={'cuisines_top':cuisines,'espana_ciudad_missing_pct':float(df.loc[df.country.eq('Spain'),'city'].isna().mean()*100),'rating_quantiles':df.avg_rating.quantile([.25,.5,.75]).to_dict(),'reviews_rating_corr':float(df[['total_reviews_count','avg_rating']].corr().iloc[0,1])}
(O/'eda_extra.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2))
