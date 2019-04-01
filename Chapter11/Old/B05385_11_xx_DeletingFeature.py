# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([myVector])

# get data provider
myDataProvider = myVector.dataProvider()
print myDataProvider

# delete feature with id 599
myDataProvider.deleteFeatures([599])

# refresh canvas and symbology
iface.mapCanvas().clearCache()
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(myVector)
