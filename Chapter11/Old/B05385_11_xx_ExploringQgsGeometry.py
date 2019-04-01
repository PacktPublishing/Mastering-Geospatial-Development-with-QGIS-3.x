# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
myVector.isValid()

features = myVector.getFeatures( QgsFeatureRequest( 3 ) ) 
feature = features.next()

geom = feature.geometry()
print "Is this a Polygon?", geom.type() == QGis.Polygon
print "it's length is", geom.length()
print "it's area measure", geom.area()
print "Is it multipart?", geom.isMultipart()

# rest of code used in the paragraph
myVector.crs().mapUnits()
myPoint = QgsGeometry.fromWkt('POINT(  -195935.165    7663900.585  )')
newPoint = QgsPoint( -195935.165, 7663900.585)
myPoint = QgsGeometry.fromPoint( newPoint )
