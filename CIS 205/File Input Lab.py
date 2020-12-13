import sys

##handle if the users forget to put the command line
if len(sys.argv) < 2:
	print "You forget to put the command line, try again!"
	##exit the program
	sys.exit(1)

##set the file argument as 1
filename = sys.argv[1] 
##set open filename as f
f = open(filename,"r")
##set reading line as lines
lines = f.readlines()


##set the count of eight as 0 because it starts 0
eightCount = 0


## making for loop for reading the line in lines
for line in lines:
	## making for loop for reading the characters in each lines
	for character in line:
		if character in "8":
			eightCount += 1
			
print str(eightCount) + " eights"
f.close()