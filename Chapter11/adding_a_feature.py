myVector = QgsVectorLayer("F:/Mastering Geospatial Development with QGIS 3.2/qgis_sample_data/qgis_sample_data/shapefiles/alaska.shp", 
   "MyFirstVector", "ogr") 
QgsProject.instance().addMapLayer(myVector)
myDataProvider = myVector.dataProvider() 

# get feature with id 599 
features = myVector.getFeatures( QgsFeatureRequest(599) ) 
myFeature = next(features) 
# create geometry from its bounding box 
bbox = myFeature.geometry().boundingBox()  
newGeom = QgsGeometry.fromRect( bbox ) 
# create a new feature 
newFeature = QgsFeature() 
# set the fields of the feature as from myVector 
# this step only sets the column characteristic of the feature 
# not its values 
newFeature.setFields( myVector.fields() ) 
# set attributes values 
newAttributes = [1000, "Alaska", 2] 
newFeature.setAttributes( newAttributes ) 
# set the geometry of the feature 
newFeature.setGeometry( newGeom ) 
# add new feature in myVector using provider 
myDataProvider.addFeatures( [newFeature] ) 
