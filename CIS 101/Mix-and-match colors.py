def decreaseRed(pict):
  for pixel in getPixels(pict):
    value = getRed(pixel)
    setRed(pixel,value*0.5)
    
def decreaseBlue(pict):
  for pixel in getPixels(pict):
    value = getBlue(pixel)
    setBlue(pixel,value*0.5)
    
def decreaseGreen(pict):
  for pixel in getPixels(pict):
    value = getGreen(pixel)
    setGreen(pixel,value*0.5)
    
def swapValue(pict):
  for pixel in getPixels(pict):
    red = getRed(pixel)
    green = getGreen(pixel)
    blue = getBlue(pixel)
    newcolor = makeColor(blue, green, red)
    setColor(pixel, newcolor)
    
def zeroValue(pict):
  for pixel in getPixels(pict):
    newcolor = makeColor(0,0,0)
    setColor(pixel,newcolor)
    
def highValue(pict):
  for pixel in getPixels(pict):
    newcolor = makeColor(255,255,255)
    setColor(pixel,newcolor)