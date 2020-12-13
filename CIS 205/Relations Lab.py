import sys

#put the words if the users did not put the command line
if len(sys.argv) < 2:
    print ("You forget to put the command line, try again!")
    sys.exit(1)
else:
#set the file name and read the file texts.
	filename = sys.argv[1]
	f = open(filename,"r")
	lines = f.readlines()

# make empty array sets of title, author, and genre, and year
	title = []
	author = []
	genre = []
	year = []

	for line in lines:  # append input textfile into empty array set
		set = line.split("|")
		title.append(set[0])
		author.append(set[1])
		genre.append(set[2])
		year.append(set[3])

	#Make while loop for question about the title
	while True:
		print("Welcome to Bro. Draper's Bookshelf!\n")
		question = raw_input("Select books based on?\n [T]itle\n [A]uthor\n [G]enre\n [Y]ear\n E[X]it Program\n")
		#make the question if I want to put title, author, genre, or year
		if question.lower() == ("t"):
			secondquestion = raw_input("Please enter title: ")
			n = len(title)
			count = 0
			for i in range(0,n):
				if secondquestion.lower() in title[i].lower():
					count +=1
					print(title[i])
					print(author[i])
					print(genre[i])
					print(year[i])
			print(str(count) + " records retrieved.")
		if question.lower() == ("g"):
			secondquestion = raw_input("Please enter genre: ")
			n = len(genre)
			count = 0
			for i in range(0,n):
				if secondquestion.lower() in genre[i].lower():
					count +=1
					print(title[i])
					print(author[i])
					print(genre[i])
					print(year[i])
			print(str(count) + " records retrieved.")
		if question.lower() == ("a"):
			secondquestion = raw_input("Please enter author: ")
			n = len(author)
			count = 0
			for i in range(0,n):
				if secondquestion.lower() in author[i].lower():
					count +=1
					print(title[i])
					print(author[i])
					print(genre[i])
					print(year[i])
			print(str(count) + " records retrieved.")
		if question.lower() == ("y"):
			secondquestion = raw_input("Please enter year: ")
			n = len(year)
			count = 0
			for i in range(0,n):
				if secondquestion.lower() in year[i].lower():
					count +=1
					print(title[i])
					print(author[i])
					print(genre[i])
					print(year[i])
			print(str(count) + " records retrieved.")
		#if I want to go out, break
		if question.lower() == ("x"):
			print("Aloha oe!")
			break