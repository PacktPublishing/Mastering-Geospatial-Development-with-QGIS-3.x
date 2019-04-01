myVector = QgsVectorLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/shapefiles/alaska.shp", 
   "MyFirstVector", "ogr") 
QgsProject.instance().addMapLayer(myVector)

myDataProvider = myVector.dataProvider() 
# get feature with id 599 
features = myVector.getFeatures( QgsFeatureRequest(599) ) 
myFeature = next(features) 

columnIndex = myVector.fields().indexFromName( "AREA_MI" ) 
myVector.startEditing() 
myVector.changeAttributeValue( myFeature.id(), columnIndex, 0 ) 
myVector.commitChanges() 

