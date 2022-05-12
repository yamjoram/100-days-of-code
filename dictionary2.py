states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {

    'CA' : 'San Francisco',
    'MI' : 'Detriot',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('------------------------------')

print(" NY states has : ", cities['NY'])
print("OR states has : ", cities['OR'])

print("---------------------------------")

print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abbreviation is : ", states['Florida'])

print("--------------------------------")

print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print("---------------------------------------")

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("--------------------------------------")

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-------------------------------------")

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f" and has the {cities[abbrev]}")

print("--------------------------------------")

state = states.get('Taxes')

if not state:
    print("sorry no 'Taxes'")
