# Acceso al TFM — Peng Chen

## Estado de la entrega

Memoria, vídeo y anexos disponibles. Vídeo MP4 de 4 min 35,90 s y 9,69 MB, con voz del alumno. Se conserva la grabación y su montaje, convertidos desde MOV a H.264/AAC. No consta una entrega en la plataforma docente.

[Descargar vídeo MP4](https://github.com/DoMoBird/TFM_Gastronomia_Asiatica_Europa/raw/refs/heads/main/revision_academica/entrega/Peng_Chen_TFM_video.mp4). Si GitHub no ofrece reproducción en la página, descargar y abrir el archivo con un reproductor.

## Orden de revisión

1. [Memoria PDF](revision_academica/entrega/memoria_revisada.pdf).
2. [Anexo de modelización ejecutado](revision_academica/entrega/anexo_modelizacion.html) y [notebook](revision_academica/entrega/anexo_modelizacion.ipynb). Descargar el HTML para visualizarlo localmente.
3. [Presentación](revision_academica/entrega/presentacion_revisada_v4.pptx).
4. [Modelos y evaluación](revision_academica/resultados/) y [código](revision_academica/src/).
5. [Derechos de datos](revision_academica/DERECHOS_DATOS.md), [reproducibilidad](REPRODUCIBILIDAD.md) e [investigación complementaria de Madrid](investigacion_madrid/README.md).

## Descarga

[Descargar paquete revisado](https://github.com/DoMoBird/TFM_Gastronomia_Asiatica_Europa/raw/refs/heads/main/revision_academica/Peng_Chen_TFM_revision.zip).

El ZIP contiene el vídeo y la revisión vigente, modelos entrenados, resultados, código, notebook de carga y análisis complementario. `revision_academica/manifest.json` registra tamaños y SHA-256 para comprobar los archivos. El archivo histórico está en Git, pero sus entregables obsoletos no forman parte del ZIP revisado.

Los guiones personales de grabación se conservan solo localmente. No se incluyen entornos Python, cachés, archivos temporales ni copias de menús de terceros. Los CSV originales grandes de TripAdvisor, censo y padrón no están incluidos. Las fuentes y fechas figuran en `data/README.md` y los informes de `investigacion_madrid/`. Los resúmenes y resultados usados están incluidos. Descargar una fuente municipal actual puede producir datos distintos al snapshot analizado.

## Aplicación del modelo

El modelo funciona localmente. `http://127.0.0.1:8765/` solo sirve en el ordenador que ejecuta el servidor y no es un enlace público para los tutores. Tras descargar el proyecto e instalar las dependencias, seguir `REPRODUCIBILIDAD.md` para iniciarlo. Los modelos incluidos permiten probar la inferencia sin descargar los CSV.

## Canal de entrega

La guía docente, páginas 7–8, exige memoria, vídeo y anexos. Si el material no cabe en la plataforma, permite subir un documento de texto con una URL a un repositorio accesible. El fichero `Peng_Chen_Enlaces_TFM.txt` contiene los enlaces al vídeo, memoria y paquete para subirlo a la plataforma docente. El repositorio es público en la comprobación realizada; no se ha cambiado su visibilidad.
