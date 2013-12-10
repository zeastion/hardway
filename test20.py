def while_one(n, a):
	i = 0
	numbers = []
	
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + a
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return numbers

x = int(raw_input("Enter n >>> "))
y = int(raw_input("Enter a >>> "))

list = while_one(x, y)

for num in list:
	print num

animals = ['bear', 'tiger', 'penguin', 'zebra']
print animals[0]
