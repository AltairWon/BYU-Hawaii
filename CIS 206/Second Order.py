import math

#set the s1,s2,c1,c2, and a,b,c, for root fomula
s1 = float(input("S(1) "))
s2 = float(input("S(2) "))
c1 = int(input("c1 "))
c2 = int(input("c2 "))
a = int(1)
b = -c1
c = -c2

#make root fomula
def RootFomula(a,b,c):
    #set the D for root fomula
    D = (b ** 2) - (4*a*c)

    #distinct root
    if D > 0:
        r1 = float((-b + D**0.5)/(2*a))
        r2 = float((-b - D**0.5)/(2*a))
        p = float(((s1*r2)-s2)/(r2-r1))
        q = float(((s1*r1)-s2)/(r1-r2))

        print("r1 = " + str(r1))
        print("r2 = " + str(r2))
        print("p = " + str(p))
        print("q = " + str(q))
        print("S(n) = " + "(" + str(p) +")(" + str(r1)+ ")^(n-1) + " + "(" + str(q) + ")(" + str(r2) + ")^(n-1)")

        #make S(1) to S(10)
        for i in range(1,11):
            n = p * r1**(i - 1) + q * r2**(i - 1)
            print("S(" + str(i) + ") = " + str(n))

    #repeated root
    if D == 0:
        r1 = float(((-b)/(2*a)))
        r2 = r1
        p = float(s1)
        q = float((s2-(s1 * r1)) / (r2))

        print("r1 = " + str(r1))
        print("r2 = " + str(r2))
        print("p = " + str(p))
        print("q = " + str(q))
        print("S(n) = " + "(" + str(p) + ")(" + str(r1) + ")^(n-1) + " + "(" + str(q) + ")(n-1)(" + str(r2) + ")^(n-1)")

        # make S(1) to S(10)
        for i in range(1, 11):
            n = p * r1 ** (i - 1) + q * (i - 1) * r2 ** (i - 1)
            print("S(" + str(i) + ") = " + str(n))



RootFomula(a,b,c)
