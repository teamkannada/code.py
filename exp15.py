person = {
    'name': 'dr.sagar',
    'age': 35,
    'city': 'dharwad',
    'college': 'Gfgc Dharwad',
    'position': 'Assistant professor'
}

print(person['name'])

person['age'] = 36
print(person['age'])

person['department'] = 'computer science'

if 'city' in person:
    print(person['city'])

for key, value in person.items():
    print(f"{key}: {value}")
