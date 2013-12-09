people = int(raw_input("How many people?"))
cats = int(raw_input("How many cats?"))
dogs = int(raw_input("How many dogs?"))

if people < cats:
	print "There are: \n %d people\n %d cats\n------" % (people, cats)
	print "Too many cats! The world is doomed!"

if people > cats:
	print "There are: \n %d people\n %d cats\n------" % (people, cats)
	print "Not many cats! The world is saved!"

if people < dogs:
	print "There are: \n %d people\n %d dogs\n------" % (people, dogs)
	print "The world is drooled on!"

if people > dogs:
	print "There are: \n %d people\n %d dogs\n------" % (people, dogs)
	print "The world is dry!"	
