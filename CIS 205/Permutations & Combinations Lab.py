import sys

#put the words if the users did not put the command line
if len(sys.argv) < 2:
    print ("You forget to put the command line, try again!")
    sys.exit(1)

#set the file name and read the file texts.
filename = sys.argv[1]
f = open(filename,"r")
set = []

for line in f:  # append input textfile into empty array set
    set.append(line.strip())

    # make empty array sets of rice, meat, egg, and gravy
rice = []
meat = []
egg = []
gravy = []

# start vlalue as 0
count = 0
section = 0

for a in set:
 # if the first array is *** then add 1 in section.
    if a == ("***"):
        section += 1
        continue

    # if section is 0, then append a into rice array before it hits first ***
    if section == 0:
        rice.append(a)

    # if section is 1, then append a into meat array before it hits second ***
    if section == 1:
         meat.append(a)

    # if section is 2, then append a into egg array before it hits third ***
    if section == 2:
        egg.append(a)

    # if section is 3, then append a into gravy array before it hits fourth ***
    if section == 3:
        gravy.append(a)

# set rice - meat - egg - gravy.
for r in rice:
    for m in meat:
        for e in egg:
            for g in gravy:
                print(r + " rice, " + m + " meat, " + e + " egg, " + g + " gravy.")
                count += 1

print("=======================")
print(str(count) + " loco mocos! Collect them all.")