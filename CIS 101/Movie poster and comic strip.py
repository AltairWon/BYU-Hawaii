def copyPicture():
  pict = makePicture('C:\Users\student\Desktop\owen.png')
  canvas = makeEmptyPicture(1000,1000)
  targetX = 250
  for x in range(0,getWidth(pict)):
    targetX += 1
    targetY = 300
    for y in range(0,getHeight(pict)):
      targetY += 1
      source = getPixel(pict,x,y)
      color = getColor(source)
      dest = getPixel(canvas,targetX,targetY)
      setColor(dest,color)
      str = "Star Wars is coming!!!"
      addText(pict,59,196,str)
  return canvas

def threePicture():
  pict1 = makePicture('C:\Users\student\Desktop\starwars.png')
  canvas = makeEmptyPicture(1000,1000)
  targetX = 0
  for x in range(0,getWidth(pict1)):
    targetX += 1
    targetY = 0
    for y in range(0,getHeight(pict1)):
      targetY += 1
      source = getPixel(pict1,x,y)
      color = getColor(source)
      dest = getPixel(canvas,targetX,targetY)
      setColor(dest,color)
      str = "Want to watch the Star Wars?"
      addText(pict1,92,143,str,blue)
  pict2 = makePicture('C:\Users\student\Desktop\owen.png')
  targetX = 300
  for x in range(0,getWidth(pict2)):
    targetX += 1
    targetY = 0
    for y in range(0,getHeight(pict2)):
      targetY += 1
      source = getPixel(pict2,x,y)
      color = getColor(source)
      dest = getPixel(canvas,targetX,targetY)
      setColor(dest,color)
      str = "You can see this old man name is Owen."
      addText(pict2,59,196,str)
  pict3 = makePicture('C:\Users\student\Desktop\darthvader.png')
  targetX = 600
  for x in range(0,getWidth(pict3)):
    targetX += 1
    targetY = 0
    for y in range(0,getHeight(pict3)):
      targetY += 1
      source = getPixel(pict3,x,y)
      color = getColor(source)
      dest = getPixel(canvas,targetX,targetY)
      setColor(dest,color)
      str = "If you don't watch, Darth Vader will follow you."
      addText(pict3,32,66,str,red)    
  return canvas