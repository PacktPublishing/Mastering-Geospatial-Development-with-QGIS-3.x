# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([myVector])

# get data provider
myDataProvider = myVector.dataProvider()

# get feature with id 599
features = myVector.getFeatures( QgsFeatureRequest(599) )
myFeature = features.next()

# create geometry from its bounding box
bbox = myFeature.geometry().boundingBox() 
newGeom = QgsGeometry.fromRect( bbox )
# create a new feature
newFeature = QgsFeature()
# set the fields of the feature as from myVector
# this step only set the column characteristic of the feature
# not it's values
newFeature.setFields( myVector.pendingFields() )
# set attributes values
newAttributes = [1000, "Alaska", 2]
newFeature.setAttributes( newAttributes )
# set the geometry of the feature
newFeature.setGeometry( newGeom )
# add new feature in myVector using provider
myDataProvider.addFeatures( [newFeature] )

# refresh canvas and symbology
iface.mapCanvas().clearCache()
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(myVector)

