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

# create new geometry basing on bbox
oldGeom = myFeature.geometry()
bbox = oldGeom.boundingBox() 
newGeom = QgsGeometry.fromRect( bbox )
# update geometry in the vector using EditingBuffer
myVector.startEditing()
myVector.changeGeometry( myFeature.id(), newGeom )
myVector.commitChanges()
