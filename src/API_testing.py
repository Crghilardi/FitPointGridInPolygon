##input_layer=vector
##nplots_field=field input_layer
##output_layer=output vector

from qgis.core import *
from PyQt4.QtCore import *

inlayer = processing.getObject(input_layer)
#dissolve_field_index = inlayer.fieldNameIndex(nplots_field)

#xmin = input_layer.extent().xMinimum()
#print xmin
#xmax = layer2.extent().xMaximum()
#ymin = layer2.extent().yMinimum()
#ymax = layer2.extent().yMaximum()

def printBB():
    #feature =iface.activeLayer().selectedFeatures()[0]
    for i in inlayer.getFeatures():
        feature=i
        print feature.geometry().boundingBox().toString()#returns string
       #print feature.geometry().boundingBox() #return rectangle object
       
#printBB()

points= QgsVectorLayer("Point?crs=epsg:4326&field=mytext:string(255)&field=mytext2:string(255)", "temporary_points", "memory")
pr = points.dataProvider()
pr.addAttributes([ QgsField("ID", QVariant.String), QgsField("latStart", QVariant.String) ])

fet = QgsFeature()
fet.setAttributes(["hello","hello"])
bbox1=QgsPoint(-117.2369213055731905,41.99459936657525820)
bbox2=QgsPoint(-111.0467712998081566,48.9999503730995016)
#bbox3=QgsPoint(-117.2369213055731905,41.99459936657525820,-111.0467712998081566, 48.9999503730995016)

fet.setGeometry(QgsGeometry.fromPoint(bbox1))

fet2 = QgsFeature()
fet2.setGeometry(QgsGeometry.fromPoint(bbox2))
pr.addFeatures([fet])


QgsMapLayerRegistry.instance().addMapLayer(points)

# add a feature

#fet.setAttributes(["hello","hello"])
