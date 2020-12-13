def blakcAndwhite(pict):
  for p in getPixels(pict):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if(r < 100):
      setRed(p,0)
    if(r > 100):
      setRed(p,255)
    if(g < 100):
      setGreen(p,0)
    if(g > 100):
      setGreen(p,255)
    if(b > 100):
      setBlue(p,0)
    if(b < 100):
      setBlue(p,255)
      
def pinkColor(pict):
  for px in getPixels(pict):
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    if (r and g and b > 100):
      setColor(px,pink)