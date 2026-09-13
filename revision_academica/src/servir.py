"""Demostrador local de inferencia. Solo escucha en loopback, sin exposición pública."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import argparse, hashlib, json, math, time
import joblib, numpy as np, pandas as pd

BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'resultados'

class Predictor:
    def __init__(self):
        self.report=json.loads((OUT/'evaluacion.json').read_text())
        model_path=OUT/'modelo_sin_reputacion.joblib'
        if hashlib.sha256(model_path.read_bytes()).hexdigest()!=self.report['model_sha256']:
            raise ValueError('Hash del modelo no coincide con la versión registrada')
        self.model=joblib.load(model_path) # Solo artefacto local generado por entrenar.py.
        self.schema=json.loads((OUT/'schema.json').read_text())
        self.pairs=json.loads((OUT/'country_regions.json').read_text())
        self.stats={'requests':0,'errors':0,'successes':0,'latency_ms_total':0,'prediction_sum':0,'outside_scale':0,'missing':{k:0 for k in self.schema}}

    def predict(self,row):
        if not isinstance(row,dict) or set(row)!=set(self.schema): raise ValueError('Se requieren exactamente los campos del esquema; null indica desconocido.')
        warnings=[]
        for k,rule in self.schema.items():
            v=row[k]
            if v is None: continue
            if rule['type']=='number':
                if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v): raise ValueError(f'{k}: número finito requerido')
                if not rule['min']<=v<=rule['max']: raise ValueError(f'{k}: fuera del rango observado en entrenamiento')
                if k.startswith('cuisine_') and v not in (0,1): raise ValueError(f'{k}: solo 0 o 1')
            elif not isinstance(v,str) or v not in rule['values']: raise ValueError(f'{k}: categoría desconocida')
        if row['country'] is None or row['region'] is None: raise ValueError('País y región son obligatorios')
        if row['region'] not in self.pairs.get(row['country'],[]): raise ValueError('La región no corresponde al país en los datos de entrenamiento')
        missing=[k for k,v in row.items() if v is None]
        if len(missing)>len(row)/2: raise ValueError('Demasiados datos desconocidos para una estimación útil')
        if missing: warnings.append('Campos desconocidos imputados dentro del pipeline: '+', '.join(missing))
        x=pd.DataFrame([{k:np.nan if v is None else v for k,v in row.items()}])
        pred=float(self.model.predict(x)[0])
        if not 1<=pred<=5: warnings.append('Resultado fuera de escala; se conserva sin recorte y requiere revisión.')
        warnings.append('Estimación transversal sobre datos de 2021; no valida nuevas aperturas ni rentabilidad.')
        return {'rating_estimado':pred,'version':self.report['version'],'modelo':self.report['selected']['sin_reputacion'],
          'MAE_test_historico':self.report['test']['sin_reputacion']['MAE'],'advertencias':warnings}

def run(port):
    predictor=Predictor()
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args): pass # No IPs, inputs ni identificadores en logs.
        def send(self,status,data,kind='application/json'):
            content=json.dumps(data,ensure_ascii=False).encode() if kind=='application/json' else data
            self.send_response(status);self.send_header('Content-Type',kind+'; charset=utf-8');self.send_header('Content-Length',str(len(content)));self.end_headers();self.wfile.write(content)
        def do_GET(self):
            routes={'/health':{'status':'ok','version':predictor.report['version']},'/schema':predictor.schema,
                    '/regions':predictor.pairs,'/example':json.loads((OUT/'ejemplo_entrada.json').read_text())}
            if self.path in routes: return self.send(200,routes[self.path])
            if self.path=='/metrics':
                s=predictor.stats
                rates={k:v/max(s['successes'],1) for k,v in s['missing'].items()}
                ref=json.loads((OUT/'monitor_reference.json').read_text())
                alerts=[k for k,v in rates.items() if s['successes']>=20 and v-ref[k]['missing_rate']>.1]
                return self.send(200,{**s,'missing_rates':rates,'alert_missing_gt_10pp':alerts,'nota':'Contadores de sesión; alerta heurística desde 20 respuestas, no prueba estadística de deriva.'})
            if self.path=='/': return self.send(200,(BASE/'src/interfaz.html').read_bytes(),'text/html')
            self.send(404,{'error':'Ruta no disponible'})
        def do_POST(self):
            if self.path!='/predict': return self.send(404,{'error':'Ruta no disponible'})
            start=time.perf_counter();predictor.stats['requests']+=1
            try:
                length=int(self.headers.get('Content-Length','0'))
                if not 0<length<=16384: raise ValueError('Tamaño de petición inválido')
                row=json.loads(self.rfile.read(length));result=predictor.predict(row)
                predictor.stats['successes']+=1
                predictor.stats['prediction_sum']+=result['rating_estimado']
                predictor.stats['outside_scale']+=int(not 1<=result['rating_estimado']<=5)
                for k,v in row.items(): predictor.stats['missing'][k]+=int(v is None)
                self.send(200,result)
            except (ValueError,TypeError) as exc:
                predictor.stats['errors']+=1;self.send(400,{'error':str(exc)})
            finally: predictor.stats['latency_ms_total']+=(time.perf_counter()-start)*1000
    print(f'Demostrador: http://127.0.0.1:{port}',flush=True)
    HTTPServer(('127.0.0.1',port),Handler).serve_forever()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8765);run(parser.parse_args().port)
