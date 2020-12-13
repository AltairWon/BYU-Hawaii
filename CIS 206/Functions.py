#input 
domain= input().split()
codomain = input().split()
relation= input().split()


#print Doamin
print("DOMAIN : {", end="")
a=0
for i in domain:
    print(i, end=", "*(0**(a==(len(domain)-1))))
    a+=1
print("}")  

#print Codomain
print("CODOMAIN : {", end="")
b=0
for i in codomain:
    print(i, end=", "*(0**(b==(len(codomain)-1))))
    b+=1
print("}")  

#print Relation
print("RELATION :")
print("{ ", end='')
for i in range(len(relation)):
    if i%2 == 0:
        print("(", end='')
        print(relation[i], end='')
        print(",", end='')
    else:
        print(relation[i], end='')
        print(")", end='')
        if i != len(relation)-1:
            print(", ", end='')
print(" }")

#make the domain and ranges lists to compare for the function or not a function
Rdomain=[]
Range=[]
for i in range(len(relation)):
    if i%2 == 0:
        Rdomain.append(relation[i])
    else:
        Range.append(relation[i])

#Decide the Fuction
#if domain equals domain list, it is a function
if len(domain)==len(Rdomain):
    print("This is a function.")
    #set onto function
    #set the onto as true for bijection function
    onto = True
    for i in codomain:
        #if i is in the range list, it is true so that it can be onto function
        if i in Range:    
            onto = True
        else:
            onto = False
            break

    if onto:
        print("This is onto.")
    else:
        print("**This is not onto.**")


    #set one to One
    #set one_to_one as true for bijection function
    one_to_one = True
    #set the duplication check for one to one function
    duplication_check = []
    for i in Range:
        #if i is not on the range of relation, add the duplication check list
        if i not in duplication_check:
            duplication_check.append(i)
    #if the range of relation list equals duplication check list, it is one to one
    if len(Range) == len(duplication_check):
        one_to_one = True
        print("This is one to one.")
    else:
        one_to_one = False
        print("**This is not one to one.**")

    # set bijection
    #if there are one to one functino and onto function, it is bijection
    if one_to_one & onto:
        print("This is bijection")
    else:
        print("**This is not bijection**")
else: 
    print("**This is not a fuction**")        
