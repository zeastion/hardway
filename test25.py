dict = {

	'Name' : 'ZEA',
	'Age' : 25

}

print "Value : %s" % dict.get('Age')
print "ZEA : %s" % dict.get('ZEA')
print "Value also : %s" % dict['Age']

print "Value then : %s" % dict.get('Sex', None)

print dict
