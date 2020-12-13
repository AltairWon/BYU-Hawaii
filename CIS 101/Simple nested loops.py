def mirrorHalf(pict):
 for x in range(0,20):
   for y in range(0,getHeight(pict)):
    source = getPixel(pict,x,y)
    color = getColor(source)
    destination = getPixel(pict,40-x,y)
    setColor(destination,color)

def nestedLoop(pict):
  for x in range(0,getWidth(pict)):
    top = getHeight(pict)/3
    bottom = getHeight(pict)-top
    for y in range(0,top):
      destination = getPixel(pict,x,y)
      value = getRed(destination)
      setRed(destination,value*0.7)
    for y in range(bottom,getHeight(pict)):
      destination = getPixel(pict,x,y)
      value = getBlue(destination)
      setBlue(destination,value*0)

def threeColor(pict):
  for x in range(0,getWidth(pict)):
    top = getHeight(pict)/3
    bottom = getHeight(pict)-top
    for y in range(0,top):
      destination = getPixel(pict,x,y)
      value = getColor(destination)
      setColor(destination,makeBrighter(value))
    for y in range(top,bottom):
      destination2 = getPixel(pict,x,y)
      r = getRed(destination2)
      g = getGreen(destination2)*0.7
      b = getBlue(destination2)*0.7
      color = makeColor(r,g,b)
      setColor(destination2,color)
    for y in range(bottom,getHeight(pict)):
      destination3 = getPixel(pict,x,y)
      r = getRed(destination3)
      g = getGreen(destination3)
      b = getBlue(destination3)
      newColor = makeColor(255-r,255-g,255-b)
      setColor(destination3,newColor)
      


