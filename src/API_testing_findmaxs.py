##input_layer=vector

from qgis.core import *
import processing

inlayer = processing.getObject(input_layer)
def printmaxs():
    for polygon in inlayer.getFeatures():
        bounds = polygon.geometry().boundingBox() #if string wanted
        xmin = bounds.xMinimum()
        xmax = bounds.xMaximum()
        ymin = bounds.yMinimum()
        ymax = bounds.yMaximum()
        index = QgsSpatialIndex()
    print xmax,"\n",ymax,"\n",xmin,"\n",ymin,"\n",index
printmaxs()
