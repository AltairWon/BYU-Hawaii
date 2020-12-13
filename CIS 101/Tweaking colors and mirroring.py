def blueify():
  for pixel in getPixels(pict):
    b = getBlue(pixel)*2
    r = getRed(pixel)/2
    g = getGreen(pixel)/2
    color = makeColor(r,g,b)
    setColor(pixel,color)
    
def grayScale(pict):
 for pixel in getPixels(pict):
  value = getRed(pixel) + getBlue(pixel) + getGreen(pixel)
  newValue = value/3
  newColor = makeColor(newValue,newValue,newValue)
  setColor(pixel,newColor)

def negative(pict):
  for pixel in getPixels(pict):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    color = makeColor(255-r, 255-g, 255-b)
    setColor(pixel,color)
    
def decreaseBlackHalf(pict):
  pixels = getPixels(pict)
  for index in range(0,len(pixels)/2):
    pixel = pixels[index]
    color = makeColor(0,0,0)
    setColor(pixel,color)

def mirrorHalf1(pict):
 pixels = getPixels(pict)
 for index in range(0, len(pixels)/2):
  source = pixels[index]
  color = getColor(source)
  dest = pixels[len(pixels)-1-index]
  setColor(dest,color)

def mirrorHalf2(pict):
 pixels = getPixels(pict)
 for index in range(len(pixels)/2,len(pixels)):
  source = pixels[index]
  color = getColor(source)
  dest = pixels[len(pixels)-1-index]
  setColor(dest,color)
