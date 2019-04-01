# README
# Substitute the string "/qgis_sample_data/raster/alaska.img"
# writing the corect path to alaska.img depending where your
# qgis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
myVector.isValid()

print myVector.extent().toString()

myVector.featureCount()

myVector.capabilitiesString()


