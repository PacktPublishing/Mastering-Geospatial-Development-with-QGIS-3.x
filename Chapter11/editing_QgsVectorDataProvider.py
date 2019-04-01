myVector = QgsVectorLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/shapefiles/alaska.shp", 
   "MyFirstVector", "ogr") 
QgsProject.instance().addMapLayer(myVector)
myDataProvider = myVector.dataProvider() 
print(myDataProvider) 

features = myVector.getFeatures(QgsFeatureRequest(599)) 
myFeature = next(features) 

   


