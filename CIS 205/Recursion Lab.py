import sys

#put the words if the users did not put the command line
if len(sys.argv) < 2:
    print ("You forget to put the command line, try again!")
    sys.exit(1)

#set the file name and read the file texts.
filename = sys.argv[1]
f = open(filename,"r")

#make the list array of the file lines
A = f.read().split()

#convert string into int 
for i in range(len(A)):
	A[i] = int(A[i])
	
##Making N
N = len(A)-1

#Making functions of sort205 and divide(p,r)
#sorting the list
def sort205(p,r):
	if (p < r):
		q = divide(p,r)
		sort205(p,q-1)
		sort205(q+1,r)

def divide(p,r):
	x = A[r]
	i = p-1
	
	for j in range(p,r):
		if (A[j] <= x):
			i += 1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[r] = A[r],A[i+1]
	return (i+1)

sort205(0,N)
print A
