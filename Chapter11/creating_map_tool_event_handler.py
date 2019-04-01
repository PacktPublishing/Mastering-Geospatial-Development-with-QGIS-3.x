from qgis.gui import QgsMapToolEmitPoint 
myMapTool =  QgsMapToolEmitPoint(iface.mapCanvas()) 

def showCoordinates(currentPos): 
    print("move coordinate %d - %d" % (currentPos.x(), currentPos.y()))

iface.mapCanvas().xyCoordinates.connect(showCoordinates)

# import the Qt module that contain mouse button definitions like
# Qt.LeftButton or  Qt.RightButton used later 
from PyQt5.QtCore import Qt 
# create handler 
def manageClick(currentPos, clickedButton): 
    if(clickedButton == Qt.LeftButton): 
        print("Clicked on %d - %d" % ( currentPos .x(), currentPos.y())) 
    if(clickedButton == Qt.RightButton): 
        # reset to the previous mapTool 
        iface.mapCanvas().setMapTool(previousMapTool) 
        # clean remove myMapTool and relative handlers 
        myMapTool.deleteLater() 

myMapTool.canvasClicked.connect(manageClick) 
iface.mapCanvas().setMapTool( myMapTool ) 




