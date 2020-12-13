import sys

#put the words if the users did not put the command line
if len(sys.argv) < 2:
    print ("You forget to put the command line, try again!")
    sys.exit(1)

#set the file name and read the file texts.
filename = sys.argv[1]
f = open(filename,"r")

def statement():
    for sentence in f:
        print(sentence)
		#set the sentence if there are lower case and split each words
        a = sentence.lower()
        b = a.split()
        #making if statements if the sentences are statement
        if len(b) != 1 and "?" not in a and "what" not in b and "where" not in b and "how" not in b and "why" not in b and "who" not in b and "when" not in b and "he" not in b and "his" not in b and "she" not in b and "her" not in b and "it" not in b and "its" not in b and "they" not in b and "their" not in b:
            print("statement")
            print("///////////////////////")
        else:
            print("Not Statement")
            print("///////////////////////")

statement()