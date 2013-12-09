def traffic_one():
	if a > b:
		print "There are too many cars:\n\t %r cars\n\t %r people." % (a, b)
	elif a < b:
		print "People have'n enough cars:\n\t %r cars\n\t %r people." % (a, b)
	else:
		print "It's good: \n\t %r cars\n\t %r people." % (a, b)

def traffic_two():
	if b > c:
		print "We need more buses:\n\t %r buses\n\t %r people." % (c, b)
	elif b < c:
		print "There are too many buses: \n\t %r buses\n\t %r people." % (c, b)
	else:
		print "It's good: \n\t %r buses\n\t %r people." % (c, b)

raw_input("Let's have a test >>> ")

raw_input("Test-1 In 1980")

a = raw_input("How many cars do you have? >>> ")
b = raw_input("How many people? >>> ")

traffic_one()
raw_input()

raw_input("Test-2 In 2010")
c = raw_input("The buses? >>> ")
b = raw_input("How many people? >>> ")

traffic_two()
