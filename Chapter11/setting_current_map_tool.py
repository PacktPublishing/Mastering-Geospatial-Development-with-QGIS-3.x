# import the map tool to use 
from qgis.gui import QgsMapToolZoom 
# get previous map tool and print it 
oldMapTool = iface.mapCanvas().mapTool() 
print("Previous map tool is a", oldMapTool) 
# create a zoom map tool pointing to the current canvas 
# the boolean parameter is False to zoom in and True to zoom out 
newMapTool = QgsMapToolZoom( iface.mapCanvas(), False) 
# set the current map tool and print it 
iface.mapCanvas().setMapTool( newMapTool ) 
print("Current map tool is a", iface.mapCanvas().mapTool()) 
# 
# here is your code 
# 
# set the previous map tool and print it 
iface.mapCanvas().setMapTool( oldMapTool ) 
print("Current map tool is a ", iface.mapCanvas().mapTool()) 

previousMapTool = iface.mapCanvas().mapTool() 
from qgis.gui import QgsMapToolEmitPoint 
myMapTool =  QgsMapToolEmitPoint(iface.mapCanvas()) 

def showCoordinates(currentPos): 
    print("move coordinate %d - %d" % (currentPos.x(), currentPos.y()))

iface.mapCanvas().xyCoordinates.connect( showCoordinates ) 



