# create a list o "person" dictionaries with a name, age and a list of hobbies for each person.
person1 = {'name': 'Andronikus', 'age': 33, 'hobbies': ['read', 'geocaching']}
person2 = {'name': 'Max', 'age': 31, 'hobbies': ['programming', 'cycling']}
person3 = {'name': 'Anna', 'age': 19, 'hobbies': ['swimming']}
person4 = {'name': 'Albino', 'age': 27, 'hobbies': ['football', 'gym']}

list_person = (person1,person2, person3, person4)

# use a list comprehension to convert this list of persons in a list of names (of persons)
list_names = [person['name'] for person in list_person]

# use a list comprehension to check whether all persons are older than 20
all_age_older_20 = all([person['age'] > 20 for person in list_person])
print(all_age_older_20)

# Copy the person list such that you can safely edit the name of the first person (without changing the original list)
list_person_copy = []

for person in list_person:
    list_person_copy.append(person.copy())

# Unpack the persons of the original list into different variables and output these variables
for person in list_person:
    (name, age, hobbies) = person.values()
    print('name: ' + name + ' age: ' + str(age) + ' hobbies: ' + str(hobbies)) 