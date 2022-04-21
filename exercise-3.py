# Using a for loop, print just the last two food strings from foods. Use the slice method []

foods = ('pizza', 'tacos', 'salad')
for idx, food in enumerate(foods):
    print(f"{food} is a good food")
    print(foods[1:3])

