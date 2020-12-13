import math

#set the s1,c, and gn
s1 = float(input("S(1) "))
c = float(input("c "))
gn = float(input("G(n) "))

print("S(n) = " + str(c) + "^(n-1) * " + str(s1) + " + sigma(" + str(c) + "^(n-1) * " + str(gn) + ")")

# make S(1) to S(10)
for i in range(1, 11):
    result = (c ** (i-1)) * s1

    for n in range(2,i+1):
        result += (c ** (i-n))* gn

    print("S(" + str(i) + ") = " + str(result))
