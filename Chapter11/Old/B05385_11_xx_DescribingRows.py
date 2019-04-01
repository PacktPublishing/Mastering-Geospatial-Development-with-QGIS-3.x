# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
myVector.isValid()

features = myVector.getFeatures( QgsFeatureRequest( 3 ) ) 
feature = features.next()

print feature.attributes()
geom = feature.geometry()
print geom



