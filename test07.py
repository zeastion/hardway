def print_two(*staffs):
	staff1, staff2 = staffs
	print "staff1: %r, staff2: %r" % (staff1, staff2)

def print_two_again(staff1, staff2):
	print "staff1: %r, staff2: %r" % (staff1, staff2)

def print_one(staff1):
	print "staff1: %r" % staff1

def print_none():
	print "I got nothing."

print_two("LEE", "LEVIS")
print_two_again("LEE~", "LEVIS~")
print_one("Debby")
print_none()
