##input_layer=vector
##nplots_field=field input_layer
##output_layer=output vector


#psuedocode
NPoints=0
MaxReps=300
#create empty point layer to add to
# outPoints=CreateType(point)
# add.field(outPoints,X)
# add.field(outPoints,Y)

points= QgsVectorLayer("Point?crs=epsg:4326&field=mytext:string(255)&field=mytext2:string(255)", "temporary_points", "memory")
pr = points.dataProvider()
pr.addAttributes([ QgsField("X", QVariant.String), QgsField("Y", QVariant.String) ]) # need to change to float?
#iterate through stands
for i in stands
    shape= getshape(i)
    area=GetArea
    dist=sqrt(area/iPoints)
    extent = getExtent()

inlayer = processing.getObject(input_layer)

def printmaxs():
    for polygon in inlayer.getFeatures():
        bounds = polygon.geometry().boundingBox().toString()
        xmin = bounds.xMinimum()
        xmax = bounds.xMaximum()
        ymin = bounds.yMinimum()
        ymax = bounds.yMaximum()
        index = QgsSpatialIndex()
    print xmax,"\n",ymax,"\n",xmin,"\n",ymin,"\n",index
printmaxs()

    distInf = sqrt(area / (NPoints + 2))
    distSup = sqrt(area /(NPoints - min(2, NPoints-1)))

pointsIn=0
while PointsIn != Npoints & rep<MaxReps # cpp alog uses a do-while, not sure hwo to emulate in python
for (x=extent.xmin to extent.xmax by x+dist)
    for(y=extent.ymin to extent.ymax by y+dist)
        if shape contains (x,y)
        shape2=Add_shape()
        shape2=Set_value(0,x)
        shape2=Set_value(1,y)
        PointsIn+=1
        rep +=1

x=extent.xmin
y=extent.ymin
if not x >= extent.xmax
    if not y >= extent.ymax
        if shape contains (x,y) # no idea how to write this in non psuedo code
            fet = QgsFeature()
            fet.setAttributes(["hello","hello"])
            pt=QgsPoint(x,y)
            fet.setGeometry(QgsGeometry.fromPoint(bbox1))
            pr.addFeatures([fet])
        y+=dist
    x+=dist
continue #? needed?

#no idea how to nest the tail end of this with above loops
if PointsIn > Npoints
    distInf = dist
    dist = (distInf + distSup)/2
elif PointsIn < Npoints
    distSup = dist
    dist = (distInf + distSup)/2


QgsMapLayerRegistry.instance().addMapLayer(points)

return outPoints
