myVector = QgsVectorLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/shapefiles/alaska.shp", 
   "MyFirstVector", "ogr") 
QgsProject.instance().addMapLayer(myVector)
myDataProvider = myVector.dataProvider() 

columnIndex = myVector.fields().indexFromName( "AREA_MI" ) 
newColumnValueMap = { columnIndex : 0  } 
newAttributesValuesMap = { myFeature.id() : newColumnValueMap  } 
myDataProvider.changeAttributeValues( newAttributesValuesMap) 
