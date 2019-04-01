# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([myVector])

# get data provider
myDataProvider = myVector.dataProvider()
print myDataProvider

# get feature with id 599
features = myVector.getFeatures( QgsFeatureRequest(599) )
myFeature = features.next()

# change the geometry to its bounding box
oldGeom = myFeature.geometry()
bbox = oldGeom.boundingBox() 
newGeom = QgsGeometry.fromRect( bbox )
newGeomMap = { myFeature.id() : newGeom  }
myDataProvider.changeGeometryValues( newGeomMap )

# refresh canvas and symbology
iface.mapCanvas().clearCache()
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(myVector)
