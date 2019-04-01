myRaster = QgsRasterLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/raster/landcover.img",
   "MyFirstRaster")

print(myRaster.extent()) 
ext = myRaster.extent() 
print(ext.xMinimum(), ext.yMinimum(), '-', ext.xMaximum(), ext.yMaximum()) 

import processing
clipped_raster = processing.run("gdal:cliprasterbyextent", {'INPUT': 'F:/Mastering Geospatial Development with QGIS 3.2/Code/Code/Chapter 9/elevation.tif', 
'PROJWIN': '-1308804, 1402816, 4297746, 5885036', 'NODATA': 999, 'DATA_TYPE': 0, 
'OUTPUT': 'F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/raster/clipped2.img'})
clipped_raster['OUTPUT']

