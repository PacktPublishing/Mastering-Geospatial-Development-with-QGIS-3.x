# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myRaster = QgsRasterLayer("/qgis_sample_data/raster/landcover.img", "MyFirtRaster")
if not myRaster.isValid():
    print "failed to load raster"

print myRaster.height(), "-", myRaster.width()

print myRaster.extent()

QgsMapLayerRegistry.instance().addMapLayer(myRaster)
