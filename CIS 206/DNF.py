#set the input file for first input
first = input().split()
#second input is line, so just put and do not use
second = input()
#put array for DNF and CND
DNF =[]
CNF = []
#set the length for the boolean expression. put -1 for not using the OUT
length = len(first) -1
#count the numberRow 
numberRow = 2**length

for i in range(numberRow):
    mo = input().split()
    b = mo[len(mo)-1]
    #setting the DNF 
    #if the OUT is 1, it means DNF
    if( b == "1"):
        string = ""
        for j in range(0, len(mo)-1):
            if(mo[j] == "1"):
                string +=  first[j]
            else:
                string += first[j] + "'"
        DNF.append(string)
    #setting the CNF
    #if the OUT is 0, it means CNF
    else:
        string2 = "("
        for j in range(0, len(mo)-1):
            if(mo[j] == "0"):
                string2 += first[j]
            else:
                string2 += first[j] +"'"
            
            if(j != len(mo)-2):
                string2 += " + "
        string2 += ")"
        CNF.append(string2)


output = DNF[0]
for i in range(1, len(DNF)):
    output += " + " + DNF[i]
print(output)

print("CNF: " + "".join(CNF))





