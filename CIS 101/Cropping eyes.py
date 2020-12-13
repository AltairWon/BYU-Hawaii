def copyPicture(pict):
  canvas = makeEmptyPicture(1000,1000)
  targetX = 400
  for x in range(206,302):
    targetX += 1
    targetY = 400
    for y in range(91,136):
      targetY += 1
      p = getPixel(pict,x,y)
      color = getColor(p)
      d = getPixel(canvas,targetX,targetY)
      setColor(d,color)
  explore(canvas)
  return canvas
  
def copyPicture1(canvas1,dY,dX,pict):
  targetX = dX
  for x in range(206,302):
    targetX += 1
    targetY = dY
    for y in range(91,136):
      targetY += 1
      p = getPixel(pict,x,y)
      color = getColor(p)
      d = getPixel(canvas1,targetX,targetY)
      setColor(d,color)
  
def copyPicture2(pict):
  copyPicture1(canvas1,400,400,pict)
  copyPicture1(canvas1,500,400,pict)
  explore(canvas1)
  return canvas1
  
