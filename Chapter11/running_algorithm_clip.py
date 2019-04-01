myRaster = QgsRasterLayer("F:/Mastering Geospatial Development with QGIS 3.2/Code/Code/Chapter 9/elevation.tif",
   "MyFirstRaster") 
myRaster.isValid() 

print(myRaster.extent()) 
ext = myRaster.extent() 
print(ext.xMinimum(), ext.yMinimum(), '-', ext.xMaximum(), ext.yMaximum()) 




