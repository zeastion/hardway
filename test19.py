the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pear', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for sth in change:
	print "I got %r" % sth

elements = []

for i in range(0, 6):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i


test = []

for i in fruits:
	print "Adding %s to the list." % i
	test.append(i)

for i in test:
	print "test fruit is %s." % i
