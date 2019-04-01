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

# change the attribute of the feature
columnIndex = myVector.pendingFields().fieldNameIndex( "AREA_MI" )
newColumnValueMap = { columnIndex : 0  }
newAttributesValuesMap = { myFeature.id() : newColumnValueMap  }
myDataProvider.changeAttributeValues( newAttributesValuesMap )

# refresh canvas and symbology
iface.mapCanvas().clearCache()
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(myVector)
