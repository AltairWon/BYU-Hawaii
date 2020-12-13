from sys import argv

filename = argv[1] 
f = open(filename,"r")
lines = f.readlines()

linesCount = 0
characterCount = 0
vowelsCount = 0
consonantsCount = 0
lowercaseCount = 0
uppercaseCount = 0

for line in lines:
	linesCount += 1
	for character in line:
		characterCount += 1
		if character.lower() in 'aeiou':
			vowelsCount += 1		
		elif character.lower() in "bcdfghjklmnpqrstvwxyz":
			consonantsCount += 1	
		if character in "abcdefghijklmnopqrstuvwxyz":
			lowercaseCount += 1		
		elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			uppercaseCount += 1
			
print linesCount			
print characterCount
print vowelsCount
print consonantsCount
print lowercaseCount
print uppercaseCount
f.close()