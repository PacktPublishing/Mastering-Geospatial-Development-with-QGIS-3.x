from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QColor 
from qgis.core import Qgis 
from qgis.gui import QgsMapToolEmitPoint, QgsRubberBand 
 
previousMapTool = iface.mapCanvas().mapTool() 
myMapTool =  QgsMapToolEmitPoint( iface.mapCanvas() ) 
 
# create the polygon rubber band associated to the current canvas 
myRubberBand = QgsRubberBand(iface.mapCanvas(), Qgis.Polygon) 
# set rubber band style 
color = QColor("red") 
color.setAlpha(50) 
myRubberBand.setColor(color) 
 
def showCoordinates( currentPos ): 
  if myRubberBand and myRubberBand.numberOfVertices(): 
    myRubberBand.removeLastPoint() 
    myRubberBand.addPoint(currentPos) 
 
iface.mapCanvas().xyCoordinates.connect( showCoordinates )  
 
def manageClick(currentPos, clickedButton): 
  if clickedButton == Qt.LeftButton: 
    myRubberBand.addPoint( currentPos ) 
  # terminate rubber band editing session 
  if clickedButton == Qt.RightButton: 
    # remove showCoordinates map canvas callback 
    iface.mapCanvas().xyCoordinates.disconnect( showCoordinates )  
    # reset to the previous mapTool 
    iface.mapCanvas().setMapTool( previousMapTool ) 
    # clean remove myMapTool and relative handlers 
    myMapTool.deleteLater() 
    # remove the rubber band from the canvas 
    iface.mapCanvas().scene().removeItem(myRubberBand) 
 
myMapTool.canvasClicked.connect( manageClick ) 
 
iface.mapCanvas().setMapTool( myMapTool ) 
