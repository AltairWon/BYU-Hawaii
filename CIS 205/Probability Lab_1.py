import random
#make count, better to change, and better to stay as 0
count = 0
better = 0
stay = 0
#make the while loop for the game trials
while count < 100:
	#make the array for the game list
	game = [1,2,3]
	#set pizzadoor as random picked door
	pizzadoor = random.choice(game)
	print ("*****Round #" + str(count) + "*****")
	print("Host: Which door do you choose?")
	#set playersdoor as random picked door
	playersdoor = random.choice(game)
	print ("Player: I choose door " + str(playersdoor))
	#make while loop to make sure the hostdoor is not pizzadoor and playersdoor
	while True:
		#set host door as random picked door
		hostdoor = random.choice(game)
		#if hostdoor is pizzadoor and playersdoor, put continue to change
		#until hostdoor is not pizzadoor and playersdoor
		if hostdoor == pizzadoor or hostdoor == playersdoor:
			continue
		else:
			print ("Host: Look! There are spiders behind door #" + str(hostdoor) +(" Do you want to change your choice? (y/n)"))
			break
	#make the question array list for choosing 1 as no 2 as yes
	question = [1,2]
	#set question as random picked in question arraylist
	question = random.choice(question)
	#if players do not change door
	if question == 1:
		print "Player: No. That's my final decision!"
		#if players are good to choose or not
		if playersdoor == pizzadoor:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". I'm glad you stayed with your original choice!")
			stay += 1
		else:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". Too bad you did not listen to me! Enjoy your spiders!")
			better += 1
	#if players change door
	if question == 2:
		#make while loop for changing the second door is not same as first choice door
		while True:
			#second door as random picked door
			#set the second door if the second door is same as first door or not
			seconddoor = random.choice(game)
			if seconddoor == playersdoor:
				continue
			else:
				print ("Plyaer: Yes, let's try door #" + str(seconddoor) + " instead.")
				break
		#if players are good to change the door or not
		if seconddoor == pizzadoor:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". I'm glad you stayed with your original choice!")
			stay += 1
		else:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". Too bad you did not listen to me! Enjoy your spiders!")
			better += 1
	count += 1
#print the count, better to change, and better to stay
print ("Out of " + str(count) + " trials, " + str(better) +" times it was better to change, and " + str(stay) + " times it was better to stay.")

