#psuedocode
Npoints
MaxReps
#create empty point layer to add to
outPoints=CreateType(point)
add.field(outPoints,X)
add.field(outPoints,Y)

#iterate through stands
for i in stands
    shape= getshape(i)
    area=GetArea
    dist=sqrt(area/iPoints)
    extent = getExtent()

    DistInf = sqrt(dArea / (NPoints + 2))
    DistSup = sqrt(Area /(NPoints - min(2, NPoints-1)))



pointsIN=0
for (x=extent.xmin to extent.xmax by x+dist)
    for(y=extent.ymin to extent.ymax by y+dist)
        if shape contains (x,y)
        shape2=Add_shape()
        shape2=Set_value(0,x)
        shape2=Set_value(1,y)
        PointsIn+=1
        rep +=1

if PointsIn > Npoints
    distInf = dist
    dist = (distInf + distSup)/2
elif PointsIn < Npoints
    distSup = dist
    dist = (distInf + distSup)/2

while PointsIn != Npoints & rep<MaxReps

assign (points)

return outPoints
