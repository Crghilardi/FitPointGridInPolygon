##harcoded path version JIC
#inpath='C:/Users/Casey/Documents/GitHub/FitPointGridInPolygon/Testing Shapefiles/Test_stands.shp

##load test_stands
#wb=QgsVectorLayer('C:/Users/Casey/Documents/GitHub/FitPointGridInPolygon/Testing Shapefiles/Test_stands.shp','TestingStands','ogr')
#QgsMapLayerRegistry.instance().addMapLayer(wb)

##load states shapefile
#wb=QgsVectorLayer('C:/Users/Casey/Documents/GitHub/FitPointGridInPolygon/Testing Shapefiles/states_WGS84.shp','States','ogr')
#QgsMapLayerRegistry.instance().addMapLayer(wb)

#load Idaho only shapefile
wb=QgsVectorLayer('C:/Users/Casey/Documents/GitHub/FitPointGridInPolygon/Testing Shapefiles/Idaho_only_WGS84.shp','Idaho','ogr')
QgsMapLayerRegistry.instance().addMapLayer(wb)



######
#Now to try and get some info from shapefiles 
wb.getFeatures() #this returns an iterator object

for i in wb.getFeatures(): 
    print i.geometry


for field in wb.fields():
    print field.name(), field.typeName() #this return attribute table info

#nothing below this works...can't figure out imports.......
#save for later 

#https://gis.stackexchange.com/questions/176170/qgis-python-find-bounding-box-for-multiple-features

#import processing
#
#from qgis.core import *

#features = QgsProcessingUtils.getFeatures(wb, context)
#for current, f in enumerate(features):
#    fGeom = f.geometry()
#    bbox = fGeom.boundingBox()
#
#xmin = layer2.extent().xMinimum()
#xmax = layer2.extent().xMaximum()
#ymin = layer2.extent().yMinimum()
#ymax = layer2.extent().yMaximum()
#




# Bbox only returns 2 points see:https://stackoverflow.com/questions/9070752/getting-the-bounding-box-of-a-vector-of-points