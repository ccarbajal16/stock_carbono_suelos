## Soilgrids 250m empleando servicios WCS

<img src="https://www.isric.org/themes/custom/basic/logo.svg" alt="Logo ISRIC">

Vamos a describir el procedimiento seguido para descargar capas ráster del [Soilgrids](https://www.isric.org/explore/soilgrids) (global gridded soil information), con el objetivo de contar con este grupo de datos destinado a realizar mapeo digital de suelos. En general SoilGrids produce mapas de las propiedades del suelo para todo el mundo con una resolución espacial media (tamaño de celda de 250 m) utilizando métodos de aprendizaje automático de última generación para generar los modelos necesarios. Toma como entrada las observaciones del suelo de aproximadamente 240 000 lugares en todo el mundo y más de 400 covariables ambientales globales que describen la vegetación, la morfología del terreno, el clima, la geología y la hidrología[^1]. Mayor información al respecto lo pueden revisar en [https://www.isric.org/explore/soilgrids](https://www.isric.org/explore/soilgrids).

### Coberturas WCS

Existen varias opciones para acceder a los datos del Soilgrids con una resolución de 250m, en esta oportunidad.

### Uso de Python

Para usar Python tenemos la siguiente opción.

[^1]: <a href="https://soil.copernicus.org/articles/7/217/2021/">SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty</a>
