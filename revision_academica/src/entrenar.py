"""Revisión reproducible: selección en validación, evaluación final y ablación.
No pronostica futuras aperturas: estimación transversal de rating histórico.
"""
from pathlib import Path
import hashlib, json, time, platform
import numpy as np
import pandas as pd
import joblib, sklearn, xgboost
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.inspection import permutation_importance
from xgboost import XGBRegressor

BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'resultados'
SOURCE=BASE.parent/'data/asian_restaurants_europe.csv'
SEED=20260913
NUM=['latitude','longitude','open_days_per_week','open_hours_per_week','working_shifts_per_week']
CAT=['country','region','price_level','vegetarian_friendly','vegan_options','gluten_free']
CUISINES=['Chinese','Japanese','Thai','Korean','Vietnamese','Indian','Asian','Sushi','Dim Sum','Ramen','Noodles']
BIN=['cuisine_'+x.lower().replace(' ','_') for x in CUISINES]
POST=['food','service','value','atmosphere','log_reviews_count']

def features(df):
    x=df[NUM+CAT].copy()
    for c in NUM: x[c]=pd.to_numeric(x[c],errors='coerce')
    for c in CAT: x[c]=x[c].where(x[c].notna(),np.nan)
    tokens=df.cuisines.fillna('').map(lambda s:{v.strip().lower() for v in s.split(',')})
    for cuisine,col in zip(CUISINES,BIN): x[col]=tokens.map(lambda s:int(cuisine.lower() in s))
    for c in POST[:4]: x[c]=pd.to_numeric(df[c],errors='coerce')
    x['log_reviews_count']=np.log1p(pd.to_numeric(df.total_reviews_count,errors='coerce').clip(lower=0))
    return x

def pipeline(model,post):
    numeric=NUM+BIN+(POST if post else [])
    prep=ColumnTransformer([
        ('num',Pipeline([('impute',SimpleImputer(strategy='median',add_indicator=True)),('scale',StandardScaler())]),numeric),
        ('cat',Pipeline([('impute',SimpleImputer(strategy='constant',fill_value='Unknown')),('encode',OneHotEncoder(handle_unknown='ignore'))]),CAT)])
    return Pipeline([('prep',prep),('model',model)])

def metrics(y,p):
    return {'n':len(y),'RMSE':float(np.sqrt(mean_squared_error(y,p))),'MAE':float(mean_absolute_error(y,p)),
            'R2':float(r2_score(y,p)),'fuera_1_5':int(((p<1)|(p>5)).sum())}

def main():
    OUT.mkdir(exist_ok=True)
    df=pd.read_csv(SOURCE,low_memory=False)
    raw_n=len(df)
    # Keep restaurant identity before any transformations or splits.
    assert df.restaurant_link.notna().all()
    dup=int(df.restaurant_link.duplicated().sum())
    df=df.drop_duplicates('restaurant_link').copy()
    countries=df.groupby('country').agg(n=('restaurant_link','size'),rating_n=('avg_rating','count'),rating_mean=('avg_rating','mean')).reset_index()
    countries.to_json(OUT/'eda_paises.json',orient='records',indent=2,force_ascii=False)
    audit={'filas_asia':raw_n,'duplicados_id':dup,'etiquetas_geograficas':int(df.country.nunique()),'sin_rating':int(df.avg_rating.isna().sum()),
      'espana_n':int(df.country.eq('Spain').sum()),'missing_pct':(df.isna().mean()*100).to_dict(),
      'nota_geografica':'24 etiquetas; England, Scotland, Wales y Northern Ireland se mantienen separadas, no son 24 estados soberanos.'}
    df=df[df.avg_rating.between(1,5)].reset_index(drop=True)
    idx=np.arange(len(df))
    trainval,test=train_test_split(idx,test_size=.2,random_state=SEED,stratify=df.country)
    train,val=train_test_split(trainval,test_size=.25,random_state=SEED,stratify=df.iloc[trainval].country)
    assert not(set(train)&set(val) or set(train)&set(test) or set(val)&set(test))
    x=features(df);y=df.avg_rating
    split={str(i):'train' for i in train}
    split.update({str(i):'validation' for i in val});split.update({str(i):'test' for i in test})
    (OUT/'particiones.json').write_text(json.dumps(split))
    source_sha=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    comparisons=[];finals={};selected={};perms={};country_errors={};boot={}
    models={'Media':DummyRegressor(),'Lineal':LinearRegression(),
      'RandomForest':RandomForestRegressor(n_estimators=100,max_depth=16,min_samples_leaf=8,max_features=.8,n_jobs=4,random_state=SEED),
      'XGBoost':XGBRegressor(n_estimators=220,max_depth=4,learning_rate=.06,subsample=.85,colsample_bytree=.85,n_jobs=4,random_state=SEED,objective='reg:squarederror')}
    for name,post in [('sin_reputacion',False),('con_reputacion',True)]:
        cols=NUM+BIN+CAT+(POST if post else [])
        fitted={}
        for model_name,model in models.items():
            from sklearn.base import clone
            start=time.time();p=pipeline(clone(model),post)
            p.fit(x.iloc[train][cols],y.iloc[train])
            pred=p.predict(x.iloc[val][cols]);m=metrics(y.iloc[val],pred)
            comparisons.append({'conjunto':name,'modelo':model_name,**m,'segundos':round(time.time()-start,2)})
            fitted[model_name]=p
            print(name,model_name,m,flush=True)
        best=min([r for r in comparisons if r['conjunto']==name],key=lambda r:r['RMSE'])['modelo']
        selected[name]=best
        # Interpretation uses validation; test remains untouched during selection.
        sample=np.random.default_rng(SEED).choice(val,size=min(1200,len(val)),replace=False)
        importance=permutation_importance(fitted[best],x.iloc[sample][cols],y.iloc[sample],n_repeats=3,random_state=SEED,scoring='neg_root_mean_squared_error',n_jobs=2)
        perms[name]=sorted([{'feature':c,'delta_RMSE':float(v),'std':float(s)} for c,v,s in zip(cols,importance.importances_mean,importance.importances_std)],key=lambda r:-r['delta_RMSE'])
        p=pipeline(clone(models[best]),post).fit(x.iloc[trainval][cols],y.iloc[trainval])
        pred=p.predict(x.iloc[test][cols]);finals[name]=metrics(y.iloc[test],pred)
        baseline=DummyRegressor().fit(x.iloc[trainval][cols],y.iloc[trainval]).predict(x.iloc[test][cols])
        finals[name]['baseline_media']=metrics(y.iloc[test],baseline)
        tmp=df.iloc[test][['country']].copy();tmp['real']=y.iloc[test].values;tmp['pred']=pred
        country_errors[name]={k:metrics(g.real,g.pred.to_numpy()) for k,g in tmp.groupby('country')}
        rng=np.random.default_rng(SEED);err=np.abs(y.iloc[test].to_numpy()-pred);boot_values=[]
        for _ in range(500): boot_values.append(float(rng.choice(err,size=len(err),replace=True).mean()))
        boot[name]={'MAE_bootstrap_p025':float(np.quantile(boot_values,.025)),'MAE_bootstrap_p975':float(np.quantile(boot_values,.975)),'nota':'Incertidumbre condicional del test; no incluye deriva temporal, selección ni agrupación por cadenas.'}
        joblib.dump(p,OUT/f'modelo_{name}.joblib')
        if name=='sin_reputacion':
            sample_row=x.iloc[test][cols].iloc[0]
            (OUT/'ejemplo_entrada.json').write_text(json.dumps(sample_row.where(sample_row.notna(),None).to_dict(),ensure_ascii=False,indent=2,allow_nan=False))
            schema={c:{'type':'category','values':sorted(x.iloc[trainval][c].dropna().unique().tolist())} if c in CAT else {'type':'number','min':float(x.iloc[trainval][c].min()),'max':float(x.iloc[trainval][c].max())} for c in cols}
            (OUT/'schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2))
            pairs=x.iloc[trainval].dropna(subset=['country','region']).groupby('country').region.unique().map(lambda a:sorted(a.tolist())).to_dict()
            (OUT/'country_regions.json').write_text(json.dumps(pairs,ensure_ascii=False,indent=2))
            reference={c:{'missing_rate':float(x.iloc[trainval][c].isna().mean())} for c in cols}
            (OUT/'monitor_reference.json').write_text(json.dumps(reference,indent=2))
    report={'version':'rating-2026-09-13-v2','seed':SEED,'source_sha256':source_sha,'audit':audit,
      'split':{'train':len(train),'validation':len(val),'test':len(test)},'validation':comparisons,'selected':selected,
      'test':finals,'bootstrap':boot,'permutation_validation':perms,'country_test':country_errors,
      'runtime':{'python':platform.python_version(),'sklearn':sklearn.__version__,'xgboost':xgboost.__version__},
      'limitaciones':['Snapshot histórico; no validación temporal ni nuevas aperturas.','La muestra original ya se exploró en la versión anterior; nuevo split no equivale a validación externa independiente.',
      'Separación por establecimiento, no por cadena ni país; no prueba transferencia a geografías nuevas.','Subratings contemporáneos comparten constructo con target; la ablación mide dependencia de información reputacional.',
      'Hiperparámetros prefijados; selección de algoritmo en validación, refit 80%, test una vez por conjunto. No se ajusta a partir del test.']}
    report['model_sha256']=hashlib.sha256((OUT/'modelo_sin_reputacion.joblib').read_bytes()).hexdigest()
    (OUT/'evaluacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print('FIN',finals,flush=True)

if __name__=='__main__': main()
