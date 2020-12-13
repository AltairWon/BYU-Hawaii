#from sys import argv

#print(argv)



def drawRow(r):
	stars = r
	a =  ":" + "*"*r
	return a


def won():
	##make a numbers of the piles
	piles = [0,7,5,3,1];
	for i in range(1,5):
		print str(i) + drawRow(piles[i])
	Player1 = "Player1"
	
	
	while True:
		##making the while loop if the piles are not 0
		while piles[1]+piles[2]+piles[3]+piles[4] != 0:
			##asking first question
			ask = int(input(Player1 + ", which pile?"))
			if piles[ask] == 0:
				print "Please enter a number between 1 and 4."
				continue
			elif ask < 1 or ask > 4:
				print "Please enter a number between 1 and 4."
				continue
			else:
				##asking second question
				ask2 = int(input(Player1 + ", how many to take from pile " + str(ask) +"?"))
				if ask2 <1 or ask2 > piles[ask]:
					print "Please enter a number between 1 and " + str(piles[ask]) + "."
					ask2 = int(input(Player1 + ", how many to take from pile " + str(ask) +"?"))
					continue
				else:
					## extract the pile numbers
					piles[ask] -= ask2
					for i in range(1,5):
						print str(i) + drawRow(piles[i])
					if piles[1]+piles[2]+piles[3]+piles[4] != 0:	
						if Player1 == "Player1":
							Player1 = "Player2"
						else:
							Player1 = "Player1"
			print Player1 + " is wins!"
		question = int(input("Play again? 1(Y) or2 (N)?"))
		if question == 1:
		else:
			print("bye")
		
	
	
won()
