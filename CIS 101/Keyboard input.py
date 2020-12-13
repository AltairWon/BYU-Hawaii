def keyboardInput():
	fresh = range(0,30)
	sopho = range(30,60)
	junior = range(60,90)
	while 1:
		name = raw_input("What is your name? ")
		credit = raw_input("What credit did you take? ")
		credit = int(credit)
		if credit in fresh:
			print "Your name is "+name+" and you are Freshman."
		elif credit in sopho:
			print "Your name is "+name+" and you are Sophomore."
		elif credit in junior:
			print "Your name is "+name+" and you are Junior."
		elif credit < 0:
			break
		else:
			print "Your name is "+name+" and you are Senior."
		
print "Show me your name and credit!"
keyboardInput()
