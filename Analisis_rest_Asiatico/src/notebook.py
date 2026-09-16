from pathlib import Path
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
B=Path(__file__).resolve().parents[1]
nb=nbformat.v4.new_notebook()
nb.cells=[nbformat.v4.new_markdown_cell('''# Anexo B — Análisis y modelización revisados\nPeng Chen · 13/09/2026\n\nLa propuesta se mantiene: análisis europeo, foco en España y predicción de rating. Madrid es una extensión de negocio. El notebook muestra resultados guardados y permite reproducir el entrenamiento con la opción explícita siguiente. Las métricas proceden de entrenar.py, ejecutado en esta revisión; no se importan métricas de la versión anterior.'''),nbformat.v4.new_code_cell('''from pathlib import Path
import json, sys, hashlib
BASE = Path.cwd()
if BASE.name == 'entrega': BASE = BASE.parent
elif BASE.name == 'TFM': BASE = BASE / 'Analisis_rest_Asiatico'
assert (BASE / 'src/entrenar.py').exists()
sys.path.insert(0,str(BASE / 'src'))
REENTRENAR = False  # True reproduce ajuste y evaluación, requiere el CSV de entrada.
if REENTRENAR:
    from entrenar import main
    main()
r = json.loads((BASE/'resultados/evaluacion.json').read_text())
print('Versión:',r['version'])
print('Partición:',r['split'])
print('SHA-256 entrada:',r['source_sha256'])
'''),nbformat.v4.new_markdown_cell('''## EDA territorial\nEtiquetas originales: England, Scotland, Wales y Northern Ireland se mantienen separadas. Frecuencia de registros no equivale a tamaño completo de mercado. Las medias no están ajustadas por composición.'''),nbformat.v4.new_code_cell('''import pandas as pd
pd.read_json(BASE/'resultados/eda_paises.json').sort_values('n',ascending=False)
'''),nbformat.v4.new_markdown_cell('''## Protocolo\n60/20/20, estratificación por país y semilla fija. Preparación ajustada en entrenamiento. Algoritmo elegido con RMSE de validación; reajuste en 80% y evaluación de test una vez por variante. Hiperparámetros prefijados. La base ya fue explorada: no es validación externa. No se aíslan cadenas ni periodos.\n\nLa ablación se compara por algoritmo en validación. En test se muestran variantes seleccionadas con algoritmos distintos; la diferencia final no se atribuye exclusivamente a las variables.'''),nbformat.v4.new_code_cell('''pd.DataFrame(r['validation'])[['conjunto','modelo','n','RMSE','MAE','R2','segundos']]
'''),nbformat.v4.new_code_cell('''pd.DataFrame({k:{a:b for a,b in v.items() if a!='baseline_media'} for k,v in r['test'].items()}).T
'''),nbformat.v4.new_markdown_cell('''## Error por territorio e incertidumbre\nNo son pruebas de causalidad o transferencia a territorios nuevos. El bootstrap remuestrea errores del mismo test y no incluye deriva, cadenas o selección del modelo.'''),nbformat.v4.new_code_cell('''pd.DataFrame(r['country_test']['sin_reputacion']).T.sort_values('n',ascending=False)
'''),nbformat.v4.new_code_cell('''pd.DataFrame(r['bootstrap']).T
'''),nbformat.v4.new_markdown_cell('''## Interpretación en validación\nPermutación individual en 1.200 filas y 3 repeticiones. Importancia positiva implica mayor error al desordenar; no mide el retorno de intervenir. Correlaciones entre variables pueden ocultar o repartir importancia.'''),nbformat.v4.new_code_cell('''from IPython.display import display, Image
for k in r['permutation_validation']:
    print(k)
    display(pd.DataFrame(r['permutation_validation'][k]).head(8))
display(Image(filename=str(BASE/'resultados/interpretacion.png')))
'''),nbformat.v4.new_markdown_cell('''## Contrato del demostrador\nSe despliega localmente la variante sin reputación por su conjunto de entradas. El ejemplo es histórico y no tiene nombre, aunque sus coordenadas pueden identificar el establecimiento. El error medio agregado no es un intervalo individual.'''),nbformat.v4.new_code_cell('''from servir import Predictor
modelo=Predictor()
entrada=json.loads((BASE/'resultados/ejemplo_entrada.json').read_text())
modelo.predict(entrada)
'''),nbformat.v4.new_markdown_cell('''## Fuentes y conclusiones\nDataset de Stefano Leone, Kaggle, versión 1, licencia declarada CC0 verificada en metadatos. Ver DERECHOS_DATOS.md. El modelo mejora la referencia histórica, con utilidad empresarial todavía por validar. No demuestra demanda futura ni rentabilidad de un buffet en Madrid. Los anexos de Madrid documentan fuentes actuales y escenarios separados del modelo.\n\nLos archivos fuente siguientes forman parte del código entregado y permiten revisar las decisiones de implementación.''')]
for name in ['entrenar.py','servir.py','verificar.py']:
 nb.cells.append(nbformat.v4.new_markdown_cell('## Código: '+name+'\n\n```python\n'+(B/'src'/name).read_text()+'\n```'))
nb.metadata['kernelspec']={'display_name':'Python 3','language':'python','name':'python3'}
NotebookClient(nb,timeout=180,resources={'metadata':{'path':str(B)}}).execute()
nbformat.write(nb,B/'entrega/anexo_modelizacion.ipynb')
exporter=HTMLExporter();body,_=exporter.from_notebook_node(nb);(B/'entrega/anexo_modelizacion.html').write_text(body)
print('Notebook ejecutado y HTML exportado')
