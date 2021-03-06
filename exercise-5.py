# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

home_town = {
    'city': 'Salinas',
    'state': 'California',
    'population': 164793
}

#iterate
for key, val in home_town.items():
    print(f"{key} = {val}")


# items() method returns a view object that contains the key-value pairs of the dictionary as  tuples