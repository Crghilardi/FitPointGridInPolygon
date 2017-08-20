#this is meant to be run as a script from within QGIS
#Processing -> Toolbox -> Scripts -> Add script from file
# this makes a local copy of the script in C:\Users\YourName\.qgis2\processing\scripts

##input_layer=vector
#nplots_field=field input_layer
#output_layer=output vector
from qgis.core import *
from PyQt4.QtCore import *
from math import *

#TO DO:
#I have no idea how to handle CRS/units with this...?

NPoints=25
MaxReps=6

#testing point
pt=QgsPoint(-115.00886,44.15480)

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
    print xmax,"\n",ymax,"\n",xmin,"\n",ymin,"\n",index,"\n",area,"\n",distInf,"\n",distSup,"\n",inshape
#print_specs()

#output from Idaho only WGS84
xmax=-111.0467713
ymax=48.9999503731
#xmin=-117.236921306
#ymin=41.9945993666
#<qgis._core.QgsSpatialIndex object at 0x0000000022C969D8>
area=24.3915951649
dist=4.87831903298 #~ approx, did on calculator
distInf=0.95046957527
distSup=1.02980781586
#True


xmin=-116.236921306 #known interior point for testing
ymin=42.9945993666


for polygon in inlayer.getFeatures():

    pointsIn=0
    rep=0

    x=xmin
    y=ymin
    testing=[] #for testing
    distInf=0.95046957527
    distSup=1.02980781586
#python implementation of pseudocode?
    firstTime=True
    rep+=1
    while pointsIn != NPoints and rep <= MaxReps:
        if not firstTime: #if I am reading the Cpp correctly, if firstTime = False, we delete everything and try again?
            testing=[] #this is overwriting, if you change to testing=testing it contains the stsrting point
        if not x >= xmax:
            if not y >= ymax:
                if polygon.geometry().contains (QgsPoint(x,y)):
                #feat = QgsFeature()
                # feat.setAttributes([x,y])
                # pt=QgsPoint(x,y)
                # fet.setGeometry(QgsGeometry.fromPoint(pt))
                # pr.addFeatures([fet])
                    testing.append([x,y]) # for testing
                    pointsIn+=1
        if pointsIn > NPoints:
            distInf = dist
            dist = (distInf + distSup)/2
        elif pointsIn < NPoints:
            distSup = dist
            dist = (distInf + distSup)/2
        #print "y=", y
            y+=dist
        #print "x=", x
            x+=dist
    firstTime=False
    # no idea how to nest the tail end of this with above loops
       
    print testing
print "Done!"

#add point layer to QGIS map
#QgsMapLayerRegistry.instance().addMapLayer(points)