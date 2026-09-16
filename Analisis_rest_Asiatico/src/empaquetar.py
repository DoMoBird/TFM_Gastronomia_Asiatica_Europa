"""Paquete revisado, sin snapshots crudos ni entregables históricos contradictorios."""
from pathlib import Path
import hashlib,json
from zipfile import ZipFile,ZIP_DEFLATED
B=Path(__file__).resolve().parents[1]
T=B.parent
required=['Peng_Chen_TFM_video.mp4','Peng_Chen_Memoria_TFM.pdf','presentacion_revisada_v4.pptx','anexo_modelizacion.ipynb','anexo_modelizacion.html']
assert all((B/'entrega'/name).is_file() for name in required)
files=[]
for p in B.rglob('*'):
    if not p.is_file() or p.is_symlink() or p.name=='.DS_Store':continue
    rel=p.relative_to(B)
    if any(x in rel.parts for x in ('build','__pycache__','node_modules')):continue
    if any(x.startswith('.chart-data-') or x=='.codex-finalizer' for x in rel.parts):continue
    if p.name.startswith('guion'):continue
    if p.suffix=='.zip' or p.name in ('manifest.json','presentacion_revisada.pptx'):continue
    files.append(p)
for p in (T/'investigacion_madrid').glob('*'):
    if p.is_file() and p.suffix in ('.md','.py','.json','.ipynb','.png') :files.append(p)
files.extend([T/'investigacion_madrid/fuentes/renta_ine_2023_distritos.json',T/'notebooks/01_carga_exploracion.ipynb',T/'README.md',T/'REPRODUCIBILIDAD.md',T/'data/README.md',T/'ENTREGA_TUTORES.md',T/'Peng_Chen_Enlaces_TFM.txt'])
manifest={str(p.relative_to(T)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)}
(B/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
files.append(B/'manifest.json')
archive=B/'Peng_Chen_TFM_revision.zip'
with ZipFile(archive,'w',ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,Path('TFM')/p.relative_to(T))
with ZipFile(archive) as z:
    assert z.testzip() is None
    for rel,meta in manifest.items():assert hashlib.sha256(z.read('TFM/'+rel)).hexdigest()==meta['sha256']
print(f'{len(files)} archivos; {archive.stat().st_size/1024**2:.1f} MiB; hashes verificados')
