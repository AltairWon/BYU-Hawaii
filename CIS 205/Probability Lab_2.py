import random
#make the while loop for the game trials
while True:
	#make the array for the game list
	game = [1,2,3]
	#set pizzadoor as random picked door
	pizzadoor = random.choice(game)
	print ("Welcome back to THAT'S DISGUSTING!")
	#ask player to choose the door
	playersdoor = input("Host: Which door do you choose?")
	print ("Player: I choose door " + str(playersdoor))
	#make while loop to make sure the hostdoor is not pizzadoor and playersdoor
	while True:
		#set host door as random picked door
		hostdoor = random.choice(game)
		if hostdoor == pizzadoor or hostdoor == playersdoor:
			continue
		else:
			print ("Host: Look! There are spiders behind door #" + str(hostdoor))
			break
	#make the question for players to change door or not
	question = raw_input("Do you want to change your choice? (y/n)")
	#if players do not change door
	if question == "n":
		print "Player: No. That's my final decision!"
		#if players are good to choose or not
		if playersdoor == pizzadoor:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". I'm glad you stayed with your original choice!")
		else:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". Too bad you did not listen to me! Enjoy your spiders!")
	#if players change door
	if question == "y":
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
		else:
			print("Look! The pizza was behind door #" + str(pizzadoor) + ". Too bad you did not listen to me! Enjoy your spiders!")
	#put the question to restart the game or not
	lastquestion = raw_input("Would you like to play again? (y/n)")
	if lastquestion == "y":
		continue
	if lastquestion == "n":
		print ("*******Get out of here*******")
		break
