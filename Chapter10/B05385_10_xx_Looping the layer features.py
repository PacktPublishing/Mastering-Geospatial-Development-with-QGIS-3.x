# README
# step 1) execute steps from MyFist PyQGIS code snippet
# step 2) execute the code in the Python Console
for feature in layer.getFeatures():
	print "Feature %d has attributes and geometry:" % feature.id()
	print feature.attributes()
	print feature.geometry().asPoint()
