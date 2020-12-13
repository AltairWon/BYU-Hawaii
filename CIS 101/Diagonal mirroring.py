def mirrorDiagonal1(pict): 
 mirror1 = getWidth(pict)
 mirror2 = getHeight(pict)
 for x in range(0,mirror1):
  for y in range(0,mirror2):
   source = getPixel(pict,x,y)
   color = getColor(source)
   destination = getPixel(pict,y,x)
   setColor(destination,color)

def mirrorDiagonal2(pict):
 mirror1 = getWidth(pict)
 mirror2 = getHeight(pict)
 for x in range(0,mirror1):
  for y in range(0,mirror2):
   source = getPixel(pict,x,y)
   color = getColor(source)
   destination = getPixel(pict,getWidth(pict)-y-1,getHeight(pict)-x-1)
   setColor(destination,color)

