def makePerson(canvas,x,y):
  addOvalFilled(canvas,0+x,0+y,60,60,makeColor(232,178,120))   
  addOvalFilled(canvas,10+x,18+y,15,15,white) 
  addOvalFilled(canvas,35+x,18+y,15,15,white)
  addOvalFilled(canvas,13+x,20+y,10,10,black)
  addOvalFilled(canvas,38+x,20+y,10,10,black) 
  addOvalFilled(canvas,24+x,37+y,10,10,black) 
  addArc(canvas,20+x,37+y,20,20,180,180,black)
  
  
def manyPeople():
  canvas = makeEmptyPicture(300,300)
  x = 0
  y = 0
  for i in range(5):
    for j in range(5):
      makePerson(canvas,x,y)
      x += 60
    x = 0
    y += 60
  explore(canvas)