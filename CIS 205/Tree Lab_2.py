import sys
#set the string as a
#a = "6 6 * 2 7 * - 2 /"
# convert the string to array
filename = sys.argv[1]
f = open(filename)
#tokens = a.split()
#make empty stack set for result
#stack = []

#lines = content.split("\n")
#make for loop for Reverse Polish Notation
for line in f.readlines():	
	stack = []
	print ("Input: "+str(line))
	for element in line.rstrip().split(" "):
	#if the element is an operator, pop the next two values do the operator(+,-,*,/)
		
		#print line.split(" ")
		
		if element == '+':
			operation2 = stack.pop()
			operation1 = stack.pop()
			stack.append(operation1 + operation2)
		elif element == '-':
			operation2 = stack.pop()
			operation1 = stack.pop()
			stack.append(operation1 - operation2)
		elif element == '*':
			operation2 = stack.pop()
			operation1 = stack.pop()
			stack.append(operation1 * operation2)
		elif element == '/':
			operation2 = stack.pop()
			operation1 = stack.pop()
			stack.append(operation1 / operation2)
	#it it is a number, append the element
		else:
			#print element
			stack.append(float(element))
	#print stack
	print "Output: " + str(stack[0])
	
#make empty stack set for result
#make for loop for Reverse Polish Notation

