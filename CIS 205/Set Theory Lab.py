import sys
#import itertools module - make sets repeat data and make sets to Cartesian product
import itertools

#put the words if the users did not put the command line
if len(sys.argv) < 2:
    print ("You forget to put the command line, try again!")
    sys.exit(1)
	
#set the file name and read the file texts.
filename = sys.argv[1]
##f = open(filename,"r")

#make sets for A and B
lines = []
file = open(filename)
for line in file:
  lines.append(line.rstrip())
A = lines[0].split(" ")
B = lines[1].split(" ")

#make sets for intersection
def intersection (setA,setB):
	inter = []
	for a in setA:
		for b in setB:
			if a == b:
				inter.append(a)
	print "A intersect B = {" +','.join(inter)+ "}"
	
#make sets for union
def union (setA,setB):
	uni = []
	for a in setA:
		uni.append(a)
	for b in setB:
		if b not in uni:
			uni.append(b)
	print "A union B = {" +','.join(uni)+ "}"
	
#make sets for difference of sets
def difference1 (setA,setB):
	diff1 = setA
	for a in setA:
		for b in setB:
			if a==b:
				diff1.remove(b)
	print "A - B = {" +','.join(diff1)+ "}"

def difference2 (setA,setB):
	diff2 = setB
	for a in setA:
		print a
		for b in setB:
			#print b
			if a==b:
				diff2.remove(a)
	print "B - A = {" +','.join(diff2)+ "}"
	
#make the sets for cartesian product
def cartesian1 (setA,setB):
	car1 = []
	for a in setA:
		for b in setB:
			car1.extend((a,b))
	print "A x B = {" + ','.join(car1)+ "}"

def cartesian2 (setA,setB):
	car2 = []
	for a in setA:
		for b in setB:
			car2.extend((b,a))
	print "B x A = {" +','.join(car2)+ "}"


#print the sets
print "A = {" +','.join(A)+ "}"
print "B = {" +','.join(B)+ "}"
intersection (A,B)
union (A,B)
difference1 (A,B)
difference2 (A,B)
cartesian1 (A,B)
cartesian2 (A,B)
