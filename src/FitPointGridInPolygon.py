##input_layer=vector
#nplots_field=field input_layer
#output_layer=output vector
from qgis.core import *
from PyQt4.QtCore import *
from math import *

#TO DO:
#I have no idea hwo to handle CRS/units with this...

NPoints=25
MaxReps=300

#testing point
pt=QgsPoint(-115.00886,44.15480)

#create empty point layer to add to
points= QgsVectorLayer("Point?crs=epsg:4326&field=mytext:string(255)&field=mytext2:string(255)", "temporary_points", "memory")
pr = points.dataProvider()
pr.addAttributes([ QgsField("X", QVariant.Double), QgsField("Y", QVariant.Double) ]) 
# need to change to float?

#fet.setGeometry(QgsGeometry.fromPoint(bbox1))
# pr.addFeatures([fet])

#iterate through stands
inlayer = processing.getObject(input_layer)

def print_specs():
    for polygon in inlayer.getFeatures():
        bounds = polygon.geometry().boundingBox() #bounding box object
        xmin = bounds.xMinimum() 
        xmax = bounds.xMaximum()
        ymin = bounds.yMinimum()
        ymax = bounds.yMaximum()
        index = QgsSpatialIndex() #returns object
        area = polygon.geometry().area() #gets passed object
        distInf = sqrt(area / (NPoints + 2))
        distSup =sqrt(area /(NPoints - min(2, NPoints-1)))
        inshape=polygon.geometry().contains(pt)
    print xmax,"\n",ymax,"\n",xmin,"\n",ymin,"\n",index,"\n",area,"\n",distInf,"\n",distSup,"\n",inshape
print_specs()

pointsIn=0
rep=0

#while PointsIn != Npoints & rep<MaxReps 
# cpp algo uses a do-while, not sure how to emulate 100% in python

#cpp psuedo code
# for (x=xmin to xmax by x+dist)
    # for(y=ymin to ymax by y+dist)
        # if shape contains (x,y)
        # shape2=Add_shape()
        # shape2=Set_value(0,x)
        # shape2=Set_value(1,y)
        # PointsIn+=1
        # rep +=1

#python implementation of pseudocode?
# x=xmin
# y=ymin
# if not x >= xmax
    # if not y >= ymax
        # if polygon.geometry().contains (x,y)
            # feat = QgsFeature()
            # feat.setAttributes([x,y])
            # pt=QgsPoint(x,y)
            # fet.setGeometry(QgsGeometry.fromPoint(pt))
            # pr.addFeatures([fet])
        # y+=dist
    # x+=dist
    #rep+=1
# continue #? needed?

# #no idea how to nest the tail end of this with above loops
# if PointsIn > Npoints
    # distInf = dist
    # dist = (distInf + distSup)/2
# elif PointsIn < Npoints
    # distSup = dist
    # dist = (distInf + distSup)/2

#add point layer to QGIS map
QgsMapLayerRegistry.instance().addMapLayer(points)

#return outPoints
