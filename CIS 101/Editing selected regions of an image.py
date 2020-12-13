def fourSide(pict, color, numb):
  bottom = getHeight(pict)-numb
  top = getWidth(pict)-numb
  for px in getPixels(pict):
    x = getX(px)
    y = getY(px)
    if x < numb:
      setColor(px,color)
    if x > top:
      setColor(px,color)
    if y < numb:
      setColor(px,color)
    if y > bottom:
      setColor(px,color)

def halfColor(pict):
  half = getWidth(pict)/2
  for p in getPixels(pict):
    x = getX(p)
    if x < half:
      color = getColor(p)
      setColor(p,makeLighter(color))
    if x > half:
      value = getRed(p) + getBlue(p) + getGreen(p)
      newValue = value/3
      newColor = makeColor(newValue,newValue,newValue)
      setColor(p,newColor)

def threeColor(pict):
  top = getHeight(pict)/3
  bottom = getHeight(pict)-top
  for px in getPixels(pict):
    y = getY(px)
    if y < top:
      color = getColor(px)
      setColor(px,makeBrighter(color))
    if top < y < bottom:
      r = getRed(px)
      g = getGreen(px)*0.7
      b = getBlue(px)*0.7
      color = makeColor(r,g,b)
      setColor(px,color)
    if y > bottom:
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      newColor = makeColor(255-r,255-g,255-b)
      setColor(px,newColor)


