def other():
	print "It's not a good choice!"
	choice = raw_input("Do you want to return? 'y' or 'n'")
	if choice == 'y':
		print "return?You can't!! Ahahahha~~~"
	elif choice == 'n':
		print "Go west!"
	else:
		print "-.-"

print "You enter a dark room with two doors.Do you go through door #1 or door #2?"

door = raw_input(">>> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.What do you do?"
	print "1- Take the cake."
	print "2- Scream at the bear."
	bear = raw_input(">>> ")
	
	if bear == "1":
		print "The bear eats your face off.Good job!"
	elif bear == "2":
		print "The bear eats your legs off.Good job!"
	else:
		other()

elif door == "2":
	print """You stare into the endless abyee at Cthulhu's ratina.\n1- Blueberries.\n2- Yellow jacket clothespins.\n3- Understanding revolvers yelling melodies."""
	insanity = raw_input(">>> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.Good job!"

else:
	other()
	
