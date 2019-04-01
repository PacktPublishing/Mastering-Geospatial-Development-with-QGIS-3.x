# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
myVector.isValid()

# simple iteration over all features
for feature in myVector.getFeatures():
    feature.id()

# iteration getting only selected features
rect = QgsRectangle(  1223070.695,  2293653.357 , 9046974.211,  4184988.662) 

request =  QgsFeatureRequest()
request.setSubsetOfAttributes([0, 2])
myVector.setSubsetString('"AREA_MI" > 1000')
request.setFilterRect( rect )

for index, feature in enumerate( myVector.getFeatures( request ) ):
    print "The record %d has ID %d" % ( index, feature.id() )
