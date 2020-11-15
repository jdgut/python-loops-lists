incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
def my_var(arg):
    return '{} {}'.format(arg["name"], arg["lastName"])

transformedData = list(map(my_var, incomingAJAXData))

print(transformedData)
