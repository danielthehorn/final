import sys
subject = ""
filename = raw_input("Please enter the name of the .csv file (in the same folder as this program): ")
data = open(filename, 'r')
lines = data.readlines()

full_ratings = {}
rated_list = []
for i in range(1,len(lines)):
	info = lines[i].rstrip().split(",")
	full_ratings[info[1]] = info[2:len(info)]
	rated_list.append(info[1])

use_list = []

line_one = lines[0].rstrip().split(",")
subject_name = line_one[1]

def create_use_list():
	for i in range(2, len(line_one)):
		response = ""
		while response != "Y" and response != "N":
			response = raw_input("Use " + line_one[i] + " in calculations? (Y/N)")
			if response == "Y":
				use_list.append(i-2)
			elif response != "N":
				print "Please respond with Y or N."
	if use_list == []:
		print "\nError: Must use at least one ratings list.\nStarting over:\n"
		create_use_list()

create_use_list()

def landing_page():
	print """
To calculate the rating for a certain subject, enter C.
To find the highest-rated subject, press F.
To end the program, press X.
"""
	resp = raw_input("> ")
	if resp == "C":
		print_rating()
	elif resp == "F":
		print "The " + subject_name + " with the highest rating is " + find_best()[0] + " with a rating of " + str(find_best()[1]) + "."
	elif resp == "X":
		sys.exit()
	landing_page()

def print_rating():
	loop = True
	while loop == True:
		global subject
		subject = raw_input(subject_name.title() + ": ")
		current_stuff = full_ratings.get(subject, False)
		if not current_stuff:
			print "No ratings found for " + subject + "."
			try_again = ""
			while try_again != "Y" and try_again != "N":
				try_again = raw_input("Try again? (Y/N)")
				if try_again == "N":
					loop = False
				elif try_again != "Y":
					print "Please respond with Y or N."
		total = 0.0
		items = len(use_list)
		for item in use_list:
			total += float(current_stuff[item])
		average = total / items
		loop = False
		print "The rating for " + subject + " is " + str(average) + "."

def find_best():
	best = 0
	best_one = ""
	for item in rated_list:
		current_stuff = full_ratings[item]
		total = 0.0
		items = len(use_list)
		for rat in use_list:
			total += float(current_stuff[rat])
		average = total / items
		if average > best:
			best = average
			best_one = item
	listy_boi = [best_one, best]
	return listy_boi

landing_page()
