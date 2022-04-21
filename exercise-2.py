# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = ('pizza', 'tacos', 'salad')
for idx, food in enumerate(foods):
    print(f"{food} is a good food")