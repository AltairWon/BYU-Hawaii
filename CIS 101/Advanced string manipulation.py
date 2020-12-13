def upper():
  list = ["The","dog","ran","a","long","way."]
  for p in range(0,len(list)):
    if p % 2 == 1:
      list[p]=list[p].upper()
  print " ".join(list)

def secretMessage():
  str = raw_input("What is the Secret Words? ")
  for a in str:
    print ord(a)
    
gender = "MFFMMMFFMFMMFFFMF"
def percentGenders(gender):
  male = round(float(gender.count("M") * 1.0 / len(gender)), 2)
  female = round(float(gender.count("F") * 1.0 / len(gender)), 2)
  print "There are " + str(male) + " males, and " + str(female) + " females."