#this is meant to be runs a script from within QGIS
#Processing -> Toolbox -> Scripts -> Add script from file
# this makes a local copy of the script in C:\Users\YourName\.qgis2\processing\scripts

##input_layer=vector
#nplots_field=field input_layer
#output_layer=output vector
from qgis.core import *
from PyQt4.QtCore import *
from math import *
import numpy as np

#create empty point layer to add to
#points= QgsVectorLayer("Point?crs=epsg:4326&field=mytext:string(255)&field=mytext2:string(255)", "temporary_points", "memory")
#pr = points.dataProvider()
#pr.addAttributes([ QgsField("X", QVariant.Double), QgsField("Y", QVariant.Double) ])
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
        dist=sqrt(area / NPoints)
        distInf = sqrt(area / (NPoints + 2))
        distSup =sqrt(area /(NPoints - min(2, NPoints-1)))
        inshape=polygon.geometry().contains(pt)
    print "xmax:",xmax,"\n","ymax:",ymax,"\n","xmin:",xmin,"\n","ymin",ymin,"\n","index",index,"\n","area:",area,"\n","distInf:",distInf,"\n","distSup:",distSup,"\n",inshape

#print_specs()

#python implementation of pseudocode?

NPoints=20
MaxReps=30
for polygon in inlayer.getFeatures():
    bounds = polygon.geometry().boundingBox()
    rep=0
    xmin=bounds.xMinimum()
    ymin=bounds.yMinimum()
    xmax = bounds.xMaximum()
    ymax = bounds.yMaximum()
    testing=[]
    area = polygon.geometry().area() 
    dist=sqrt(area / NPoints)
    distInf = sqrt(area / (NPoints + 2))
    distSup =sqrt(area /(NPoints - min(2, NPoints-1)))
   pointsIn=len(testing)
    firstTime=True
    while pointsIn != NPoints and rep<MaxReps:
        if not firstTime: #if I am reading the Cpp correctly, if firstTime = False, we delete everything and try again?
            testing=[]
        rep+=1
        print "rep=",rep
        for i in np.arange(xmin,xmax,dist):
            for j in np.arange(ymin,ymax,dist):
                if polygon.geometry().contains (QgsPoint(i,j)):
                    #feat = QgsFeature()
                    # feat.setAttributes([x,y])
                    # pt=QgsPoint(x,y)
                    # fet.setGeometry(QgsGeometry.fromPoint(pt))
                    # pr.addFeatures([fet])
                    testing.append([i,j])
        pointsIn=len(testing)
        print "sup,inf, dist is:" , [distSup,distInf,dist]
            #print "y=", y
            #print "x=", x
        print "pointsIn:", pointsIn
        print testing
        print firstTime
        if pointsIn > NPoints:
            distInf = dist
            dist = (distInf + distSup)/2
        elif pointsIn < NPoints:
            distSup = dist
            dist = (distInf + distSup)/2
        firstTime=False
print "Done!"

#add point layer to QGIS map
#QgsMapLayerRegistry.instance().addMapLayer(points)