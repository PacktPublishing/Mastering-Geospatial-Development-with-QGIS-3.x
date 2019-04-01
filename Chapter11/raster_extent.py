myRaster = QgsRasterLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/raster/landcover.img",
   "MyFirstRaster") 
myRaster.isValid() 

print(myRaster.extent()) 
ext = myRaster.extent() 
print(ext.xMinimum(), ext.yMinimum(), '-', ext.xMaximum(), ext.yMaximum()) 

