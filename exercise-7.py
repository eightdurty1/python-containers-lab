# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.



students = ['israel', 'marissa', 'natalie']

awesome_students = [f"{name} is awesome!" for name in students]

for student in awesome_students:
    print(student)