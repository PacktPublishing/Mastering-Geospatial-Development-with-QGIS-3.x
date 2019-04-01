myVector = QgsVectorLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/shapefiles/alaska.shp", 
   "MyFirstVector", "ogr") 
QgsProject.instance().addMapLayer(myVector)

features = myVector.getFeatures(QgsFeatureRequest(599)) 
myFeature = next(features) 
myDataProvider = myVector.dataProvider() 

oldGeom = myFeature.geometry() 
bbox = oldGeom.boundingBox()  
newGeom = QgsGeometry.fromRect( bbox ) 
newGeomMap = { myFeature.id() : newGeom  } 
myDataProvider.changeGeometryValues( newGeomMap ) 

   


