# README
# Substitute the layer string point to the correct path
# depending where your gis_sample_data are
myVector = QgsVectorLayer("/qgis_sample_data/shapfiles/alaska.shp", "MyFirstVector", "ogr")
myVector.isValid()

# get previous map tool
previousMapTool = iface.mapCanvas().mapTool()

# Creating the new map tool
from qgis.gui import QgsMapToolEmitPoint
myMapTool =  QgsMapToolEmitPoint( iface.mapCanvas() )

# Creating map canvas event handler
def showCoordinates( currentPos ):
    print  "move coordinate %d - %d" % ( currentPos .x(), currentPos.y() )

iface.mapCanvas().xyCoordinates.connect( showCoordinates )

# import the Qt module that contain mouse button definitions
from PyQt4.QtCore import Qt

# create handler
def manageClick( currentPos, clickedButton ):
    if  clickedButton == Qt.LeftButton:
        print  "Clicked on %d - %d" % ( currentPos .x(), currentPos.y() )
    if  clickedButton == Qt.RightButton:
        # reset to the previous mapTool
        iface.mapCanvas().setMapTool( previousMapTool )
        # clean remove myMapTool and relative handlers
        myMapTool.deleteLater()

myMapTool.canvasClicked.connect( manageClick )

# Setting up the new map tool
iface.mapCanvas().setMapTool( myMapTool )

# remember to execute next commented line to remove canvas listener
#iface.mapCanvas().xyCoordinates.disconnect( showCoordinates )


