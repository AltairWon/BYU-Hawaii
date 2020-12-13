from sys import argv
t = argv[1]
q = int(argv[2])
print(t*q)
for i in range(q-2):
	print(t+" "*(q-2)+t)
print(t*q)