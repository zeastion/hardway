def papapa():
	arg1 = raw_input("Tell me what's your name? >>> ")
	print "OK, I get it."
	arg2 = raw_input("Next, why you come here? >>> ")
	print "I dont't believe it!"
	arg3 = raw_input("Which Gundam do you like? >>> ")
	raw_input("Alright, you can see the result.")
	print "[NAME  :  %s]" % arg1
	print "[WHY   :  %s]" % arg2
	print "[Gundam:  %s]" % arg3
	return arg1

print "It's a test."

raw_input("BEGIN >>> ")
Man_1 = papapa()

print "We know 1st Man --- %s " % Man_1

Man_2 = papapa()
print "It's about 2nd Man --- %s " % Man_2
