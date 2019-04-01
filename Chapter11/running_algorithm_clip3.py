myRaster = QgsRasterLayer("F:/Mastering Geospatial Development with QGIS 3.2/Code/Code/Chapter 9/elevation.tif",
   "MyFirstRaster")
#print(myRaster.extent()) 
ext = myRaster.extent() 
print("x-minimum: ", ext.xMinimum(), "x-maximum: ", ext.xMaximum(), "\n", "y-minimum", ext.yMinimum(), "y-maximum", ext.yMaximum()) 

import processing
clipped_raster = processing.run("gdal:cliprasterbyextent", {'INPUT': 'F:/Mastering Geospatial Development with QGIS 3.2/Code/Code/Chapter 9/elevation.tif', 'PROJWIN': '440000, 460000, 4030000, 4045000', 'NODATA': 999, 'DATA_TYPE': 0, 'OUTPUT': 'F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/raster/clipped.tif'})
clipped_raster['OUTPUT']

