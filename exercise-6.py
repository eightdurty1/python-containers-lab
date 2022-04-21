# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.

# enumerate() adds a counter to an iretable and returns it in a form of enumerating object.

cohort = []
foods = ('pizza', 'tacos', 'salad')
students = ['israel', 'marissa', 'natalie']
# \with a for loop,
for index_num, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index_num]
    })

for student in cohort:
    print(student)