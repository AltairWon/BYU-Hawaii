def makeSunset(pict):
  for p in getPixels(pict):
    value = getBlue(p)
    setBlue(p,value*0.7)
    value = getGreen(p)
    setGreen(p,value*0.7)
  explore(pict)

def makeSunset2(pict):
  x = 0
  pixels = getPixels(pict)
  while x < len(pixels):
    setBlue(pixels[x],getBlue(pixels[x])*0.7)
    setGreen(pixels[x],getGreen(pixels[x])*0.7)
    x += 1
  explore(pict)

def rotatePict(pict):
  canvas = makeEmptyPicture(500,500)
  for x in range(0,getWidth(pict)):
    for y in range(0,getHeight(pict)):
      source = getPixel(pict,x,y)
      color = getColor(source)
      targetY=x
      targetX = getWidth(pict)-1-y
      dest = getPixel(canvas,targetX,targetY)
      setColor(dest,color)
      targetY += 1
    targetX += 1
  explore(canvas)

def rotatePict2(pict):
  canvas = makeEmptyPicture(500,500)
  x = 0
  pixel = getPixels(pict)
  while x < len(pixel):
    color = getColor(pixel[x])
    p = getX(pixel[x])
    q = getY(pixel[x])
    rotatedX = getWidth(pict)-q-1
    rotatedY = p
    rotatedPixel = getPixel(canvas,rotatedX,rotatedY)
    setColor(rotatedPixel,color)
    x += 1
  explore(canvas)