# SoilGrids 250m empleando servicios WCS

<img src="https://www.isric.org/themes/custom/basic/logo.svg" alt="Logo ISRIC">

![](images/SoilGrids_banner_web.png)

Vamos a describir el procedimiento seguido para descargar capas ráster del [SoilGrids](https://www.isric.org/explore/soilgrids) (global gridded soil information), con el objetivo de contar con este grupo de datos destinado a realizar mapeo digital de suelos. En general SoilGrids produce mapas de las propiedades del suelo para todo el mundo con una resolución espacial media (tamaño de celda de 250 m) utilizando métodos de aprendizaje automático de última generación para generar los modelos necesarios. Toma como entrada las observaciones del suelo de aproximadamente 240 000 lugares en todo el mundo y más de 400 covariables ambientales globales que describen la vegetación, la morfología del terreno, el clima, la geología y la hidrología<sup id="a1">[1](#f1)</sup>. Mayor información al respecto lo pueden revisar en [https://www.isric.org/explore/soilgrids](https://www.isric.org/explore/soilgrids).

### Servicio WCS (Web Coverage Service)

Existen varias opciones para acceder a los datos del SoilGrids con una resolución de 250m, en esta oportunidad se presenta el que está disponible empleando un servicio [WCS](https://es.wikipedia.org/wiki/Web_Coverage_Service), siendo uno de los estándares emitidos por el [Open Geospatial Consortium (OGC)](https://www.ogc.org/), a través del cual podemos obtener mapas ráster desde un navegador web o desde cualquier otro programa que utilice el protocolo. Existe la posibilidad de emplear un Software SIG como [QGIS](http://www.qgis.org/es/site/) para realizar la descarga de un ámbito determinado a través de servicios web que incluye también el servicios [WMS](https://www.isric.org/instruction-wms). Nosotros vamos a reproducir los scripts de Python y R disponibles con ejemplos desde [aquí](https://git.wur.nl/isric/soilgrids/soilgrids.notebooks).

### Uso de Python

Para un acceso fácil a los servicios WCS a través de Python contamos con la libreria [OWSLib](https://geopython.github.io/OWSLib/). 

### Uso de R
____________________________________

<b id="f1">1.</b><a href="https://soil.copernicus.org/articles/7/217/2021/">SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty</a>[↩](#a1)
