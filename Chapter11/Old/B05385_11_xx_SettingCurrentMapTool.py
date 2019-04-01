# import the map tool to use
from qgis.gui import QgsMapToolZoom

# get previous map tool and print it
oldMapTool = iface.mapCanvas().mapTool()
print "Previous map toos is a", oldMapTool

# create a zoom map tool pointing to the current canvas
# the boolean parameter is False to zoom in and True to zoom out
newMapTool = QgsMapToolZoom( iface.mapCanvas(), False)

# set the current map tool and print it
iface.mapCanvas().setMapTool( newMapTool )
print "Current map toos is a", iface.mapCanvas().mapTool()

#
# here your code
#
# set the previous map tool and print it
iface.mapCanvas().setMapTool( oldMapTool )
print "Current map toos is a ", iface.mapCanvas().mapTool()

