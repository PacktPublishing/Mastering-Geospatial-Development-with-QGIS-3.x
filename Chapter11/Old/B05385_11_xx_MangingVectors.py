# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapefiles/alaska.shp", "MyFirstVector", "ogr")
myVector.isValid()
