import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {FileBlob,PresentationFile} from '@oai/artifact-tool';
const B=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const SK=process.env.PRESENTATIONS_SKILL_DIR;
const {finalizePresentation}=await import(pathToFileURL(SK+'/container_tools/artifact_tool_utils.mjs').href);
const source=B+'/build/presentacion_base.pptx';
const p=await PresentationFile.importPptx(await FileBlob.load(source));
const records=(await p.inspect({kind:'slide,textbox,chart,table,layout',maxChars:60000})).ndjson.split('\n').filter(Boolean).map(x=>JSON.parse(x));
const red='#8C1D22',dark='#2B2B2B',gray='#626262';
function edit(id,text,pos,size=28,color=dark,bold=false){const q=p.resolve(id);q.text=text;if(pos)q.position={left:pos[0],top:pos[1],width:pos[2],height:pos[3]};q.text.style={typeface:'Arial',fontSize:size,color,bold,autoFit:'none'};return q;}
function add(i,text,pos,size=24,color=gray,bold=false){const q=p.slides.items[i-1].shapes.add({geometry:'textbox',position:{left:pos[0],top:pos[1],width:pos[2],height:pos[3]},fill:'none',line:{fill:'none',width:0}});q.text=text;q.text.style={typeface:'Arial',fontSize:size,color,bold,autoFit:'none'};return q;}
edit('sh/k3yl0zql','Análisis y predicción de valoración\ncon especial foco en España',null,34,'#F4E9D8');
add(1,'¿Qué permiten conocer los datos sobre estos restaurantes?',[80,402,1100,50],25,'#FFFFFF');
edit('sh/ozy1ofad','86.306 restaurantes asiáticos',null,40,dark,true);
edit('sh/b29kza94','81.315 con valoración válida para modelizar',null,31);
edit('sh/a10jqpsj','Datos publicados en 2021\nLicencia CC0 declarada por Kaggle',[80,350,1100,90],29);
edit('sh/x4r21kru','Cobertura parcial y valores ausentes\nSin información de ventas ni beneficios',[80,490,1100,100],29,red);
add(2,'Origen: 1.083.397 restaurantes europeos · 42 columnas',[80,610,1100,40],23);
edit('sh/3ah8rqlg','Distribución territorial de la muestra',null,44,red,true);
const geo=JSON.parse(await fs.readFile(B+'/resultados/eda_paises.json','utf8')).sort((a,b)=>b.n-a.n).slice(0,5).reverse();
const names={England:'Inglaterra',France:'Francia',Germany:'Alemania',Spain:'España',Italy:'Italia'};
const c3=p.resolve('ch/kvq90vu1');c3.series.getItemAt(0).categories=geo.map(x=>names[x.country]);c3.series.getItemAt(0).values=geo.map(x=>x.n);
edit('sh/298ryl4v','España: 8.295 registros. Recuentos de la plataforma, no un censo.\nEl Reino Unido aparece dividido en 4 etiquetas territoriales.',[80,575,1110,75],24,gray);
edit('sh/3ihk3et8','Información disponible para predecir',null,44,red,true);
edit('sh/rm1k7yt4','Ubicación, horarios, precio, dietas y tipos de cocina',null,30);
edit('sh/doj29oba','Añade puntuaciones de comida, servicio, valor y ambiente,\ny el número de reseñas',[80,411,1110,90],28);
edit('sh/sna103ap','Objetivo: valoración histórica de restaurantes existentes\nUso en nuevas aperturas pendiente de validación',[80,551,1100,90],26,dark,true);
edit('sh/z2tcnm5s','60 % entrenamiento · 20 % validación · 20 % test',null,28);
const table=p.resolve('tb/9cvmlsby');
const r=JSON.parse(await fs.readFile(B+'/resultados/evaluacion.json','utf8'));
const vals=r.validation.filter(x=>x.conjunto==='sin_reputacion');
for(let i=0;i<vals.length;i++){table.cells.set(i+1,0,vals[i].modelo==='RandomForest'?'Random Forest':vals[i].modelo);for(let j=1;j<3;j++)table.cells.set(i+1,j,vals[i][j===1?'RMSE':'MAE'].toFixed(3).replace('.',','));for(let j=0;j<3;j++){let cell=table.getCell(i+1,j);cell.fill=vals[i].modelo==='RandomForest'?'#F4E9D8':'#FFFFFF';cell.text.style={typeface:'Arial',fontSize:25,color:dark,bold:vals[i].modelo==='RandomForest'};}}
edit('sh/yhkbe1o7','Selección por menor RMSE. Reajuste con el 80 % antes del test.\nRandom Forest y XGBoost quedan muy próximos en validación.',[80,550,1120,90],25,gray);
edit('sh/ml07i9sv','Evaluación final: error de predicción',null,44,red,true);
edit('sh/87ipkzal','MAE = error absoluto medio en puntos de valoración\n0,462 sin reputación · 0,361 con reputación',[80,534,1110,80],27,red,true);
edit('sh/98rqt4r6','16.263 casos de test. Cambian las variables y el algoritmo.',[80,624,1110,35],23,gray);
add(6,'RMSE: cuanto menor, mejor',[80,150,1100,35],23);
edit('sh/kzmdova1','Interpretación del modelo sin reputación',null,44,red,true);
const imp=r.permutation_validation.sin_reputacion.slice(0,5).reverse();
const labels={cuisine_chinese:'Cocina china',vegan_options:'Opciones veganas',open_days_per_week:'Días abiertos',longitude:'Longitud',vegetarian_friendly:'Opciones vegetarianas'};
const c7=p.resolve('ch/xgj29sva');c7.series.getItemAt(0).categories=imp.map(x=>labels[x.feature]||x.feature);c7.series.getItemAt(0).values=imp.map(x=>Number(x.delta_RMSE.toFixed(6)));
edit('sh/ydkbm5sv','Random Forest · 1.200 casos de validación · 3 repeticiones',null,24,gray);
edit('sh/zedcfa9g','La importancia explica el modelo, no demuestra causalidad',null,27,red,true);
edit('sh/g72x4zyd','Aplicación web local',[80,185,325,90],32,red,true);
edit('sh/ri9g7uhw','Entrada validada\n\nPredicción y versión\n\nAvisos de imputación',[80,300,330,225],26);
edit('sh/6h0fypgb','Prototipo local funcional. Impacto empresarial aún sin validar.',[80,626,1120,40],25,red);
p.resolve('sl/fu1gfa1s').images.add({blob:await fs.readFile(B+'/assets/app_ejemplo_recorte.png'),contentType:'image/png',alt:'Captura real del mismo ejemplo histórico: Italy, Lombardy y valoración estimada 3.72/5. Recorte de entradas y resultado.',position:{left:435,top:190,width:755,height:395},fit:'contain'});
add(8,'Ejemplo histórico real: 3,72 / 5',[435,145,755,40],27,red,true);
add(8,'Recorte de la interfaz, con campos y resultado de la misma ejecución',[435,587,755,35],18);
edit('sh/ofq5svm5','Madrid: contexto para una decisión de inversión',null,42,red,true);
edit('sh/0b65obm9','Información incorporada',null,34,red,true);
edit('sh/nex4jq5k','Censo y padrón de 2026, renta de 2023\nPrecios y condiciones de menús publicados',null,30);
edit('sh/mdonql4z','Evidencia que todavía falta',null,34,red,true);
edit('sh/9gzml0nq','Demanda, ventas y costes de un local concreto\nLos escenarios del anexo dependen de supuestos',null,30);
edit('sh/cbu58j2h','Predicción histórica mejor que la referencia\nMAE de 0,462 puntos sin reputación',null,34,'#FFFFFF',true);
edit('sh/zelojyl8','Modelo interpretable y aplicación local reproducible\nLa rentabilidad sigue sin quedar demostrada',null,31,'#F4E9D8');
edit('sh/ydcnatkn','Siguiente paso: datos actuales, validación externa\ny evaluación de utilidad en un uso real',null,28,'#FFFFFF');
// Public speaker notes contain sources, not the student's private recording script.
for(let i=0;i<p.slides.items.length;i++){
 const old=p.slides.items[i].speakerNotes.textFrame;
 const sourceText=i===7?'Aplicación local src/servir.py e interfaz.html. Captura propia del 16/09/2026. Ejemplo histórico de resultados/ejemplo_entrada.json, salida 3.72/5.':i===8?'investigacion_madrid/FASE2_RESULTADOS.md a FASE5_RESULTADOS.md. Datos municipales 2026 e INE ADRH 2023.':'Memoria revisada y resultados/evaluacion.json, eda_paises.json, kaggle_metadata.json. Elaboración propia.';
 old.setText('Fuentes: '+sourceText);
}
await fs.mkdir(B+'/build/v3',{recursive:true});
await(await PresentationFile.exportPptx(p)).save(B+'/build/v3/candidate.pptx');
// Restore original literal-data workbooks and synchronize their cells with edited caches.
execFileSync(process.env.RUNTIME_PYTHON,[B+'/src/restaurar_libros_graficos.py',source,B+'/build/v3/candidate.pptx']);
const result=await finalizePresentation({workspaceDir:B,candidatePath:B+'/build/v3/candidate.pptx',finalPath:B+'/entrega/presentacion_revisada_v4.pptx',pythonExecutable:process.env.RUNTIME_PYTHON,integrityValidatorPath:SK+'/container_tools/inspect_presentation_package_integrity.py',layoutValidatorPath:SK+'/container_tools/inspect_presentation_layout_geometry.py',layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit','--require-native-table-slide','5'],explicitTotalSlideCount:10,requiredNativeTableOwnerSlides:[5],requiredNativeChartOwnerSlides:[3,6,7],fontPolicy:{basis:'reference',families:['Arial'],referencePath:source,referenceSha256:createHash('sha256').update(await fs.readFile(source)).digest('hex')},verifyArtifactToolImport:true,receiptPath:B+'/build/v3/validation-v4.json'});
console.log(JSON.stringify(result));
const final=await PresentationFile.importPptx(await FileBlob.load(B+'/entrega/presentacion_revisada_v4.pptx'));
for(let i=0;i<10;i++){const b=await final.export({slide:final.slides.items[i],format:'png',scale:1});await fs.writeFile(B+`/build/v3/slide-${i+1}.png`,new Uint8Array(await b.arrayBuffer()));}
