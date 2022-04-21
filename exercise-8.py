# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
foods = ('pizza', 'tacos', 'salad')
for food in [food for food in foods if 'a' in food]:
    print(food)