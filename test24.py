def title():

	print '-' * 10

states = {

	'Liao Ning' : 'LN',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'

}

cities = {

	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville',
	'LN' : 'Shen Yang'

}

cities['NY'] = 'New York'
cities['SY'] = 'Shen Yang'

title()
print "NY State has: ", cities['NY']
print "Liao Ning has: ", cities['SY']

title()
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

title()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

title()
for a, b in states.items():
	print "%s is test abb %s" % (a, b)

title()
for a, b in states.items():
	print "%s state is abbreviated %s and has city %s" % (a, b, cities[b])

title()
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exit')
print "The city for the state 'TX' is: %s" % city
