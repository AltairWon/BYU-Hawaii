
#set the string as a
a = "6 6 * 2 7 * - 2 /"
# convert the string to array
tokens = a.split()
#make empty stack set for result
stack = []
#make for loop for Reverse Polish Notation
for element in tokens:
    #if the element is an operator, pop the next two values do the operator(+,-,*,/)
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
        stack.append(int(element))
print(stack)
