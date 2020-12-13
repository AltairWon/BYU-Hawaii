def pickAndShow():
    file = pickAFile()
    pict = makePicture(file)
    explore (pict)

def showFile(filename):
    picture = makePicture(filename)
    explore(picture)

def doMath(numA,numB):
    print (numA*5)+(numB*2)