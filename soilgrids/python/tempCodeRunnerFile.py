*#TODO Primero cargue la clase WebCoverageService desde OWSLib y cree una conexión a un servicio disponible desde https://maps.isric.org/:
from owslib.wcs import WebCoverageService
wcs = WebCoverageService('https://maps.isric.org/mapserv?map=/map/ocs.map', version='2.0.1') #! Se emplea el ocs (Soil organic carbon stock)
#TODO Incorporar un cuadro delimitador que coincida para el ejemplo la Región Junín del Perú
bbox = (-8486988.061220681, -1438756.3180922759, -8103389.852369716, -1150398.5580024184) #! Uso de la Proyección Homolosine(EPSG:152160)
#TODO El método getCoverage ahora se puede usar para buscar el segmento del mapa dentro del cuadro delimitador.
response = wcs.getCoverage(
    #! Para obtener la lista de este parámetro usamos: print(list(wcs.contents))
    identifier='ocs_0-30cm_mean',  
    crs='urn:ogc:def:crs:EPSG::152160',
    bbox=bbox,
    resx=250, resy=250, #! Resolución de 250m
    #! Para obtener los formatos disponibles usamos: wcs.contents['ocs_0-30cm_mean'].supportedFormats
    format='GEOTIFF_INT16')
#TODO Ahora busque la cobertura de Junín y guárdela en el disco:
with open('./output/junin_ocs_0-30_mean.tif', 'wb') as file:
    file.write(response.read())
#TODO Interacción empleando la librería Rasterio
import rasterio 
ocs = rasterio.open("./outputs/junin_ocs_0-30_mean.tif", driver="GTiff")
#TODO Visualizamos nuestro mapa con la clase Plot
from rasterio import Plot
plot.show(ocs,  title='Mean ocs between 0 and 30 cm deep in Junin-Peru', cmap='gist_rainbow'))  # ! Para determinar los colores del mapa revisar https://matplotlib.org/stable/tutorials/colors/colormaps.html
