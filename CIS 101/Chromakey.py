def purpleTeeth(pict):
 for px in getPixels(pict):
   teethColor = makeColor(243,242,224)
   x = getX(px)
   y = getY(px)
   if 680 <= x <= 808:
     if 471 <= y <= 483:
       color = getColor(px)
       if distance(color,teethColor) < 250:
         r=getRed(px)*2
         g=getGreen(px)/2
         b=getBlue(px)*2
         setColor(px,makeColor(r,g,b))

def redEye(pict):
  blackColor = makeColor(114,101,66)
  for p in getPixels(pict):
    x =getX(p)
    y =getY(p)
    if (611 <= x <= 645) and (296 <= y <= 312):
      color = getColor(p)
      if (distance(blackColor,color) < 50.0):
        setColor(p,red)
    if (787 <= x <= 813) and (268 <= y <= 286):
      color = getColor(p)
      if (distance(blackColor,color) < 50.0):
        setColor(p,red)

def orangeHair(pict):
  hairColor = makeColor(90,73,47)
  for p in getPixels(pict):
    x =getX(p)
    y =getY(p)
    if (452 <= x <= 542) and (0 <= y <= 330):
      color = getColor(p)
      if (distance(hairColor,color) < 100.0):
        setColor(p,orange)
    if (542 <= x <= 888) and (0 <= y <= 220):
      color = getColor(p)
      if (distance(hairColor,color) < 100.0):
        setColor(p,orange)
    if (888 <= x <= 930) and (0 <= y <= 296):
      color = getColor(p)
      if (distance(hairColor,color) < 95.0):
        setColor(p,orange)
        
def chromakey(src,bg):
  for px in getPixels(src):
    x = getX(px)
    y = getY(px)
    if (getRed(px) < getGreen(px) and getBlue(px) < getGreen(px)):
      bgpx = getPixel(bg,x,y)
      bgcol = getColor(bgpx)
      setColor(px,bgcol)
