# Tupels - circular brackets

cars = ("Mercedes", "R34", "Pagani", "Supra", "GTR")
print(cars)
for gari in \
        cars:
    print(gari)
print(cars[2:])
# Tupels does not allow item replacement ie cars[0] = "Mercedes Benz"

# Lists - square brackets - allows item replacement

colours = ["Red", "Green", "Purple", "Blue", "Gray", "Black"]
print(colours)
colours[3] = "Navy Blue"
print(colours)
for rangi in colours:
    print(rangi)
colours.reverse()
print(colours)
colours.pop(4)
print(colours)
colours.sort(reverse=True)
print(colours)
colours.sort()
print(colours)

# Dictionaries - cali brackets

students = {"adm1": "Tracy", "adm2": "Moses"}
for funguo in students.keys():
    print(funguo)
for names in students.values():
    print(names)
print(students["adm1"])

# Sets - cali brackets

ranks = {1, 5, 8, 4, 0, 5, 3, 2, 1, 6, 8, 10, 11, 12, 10}
print(ranks)

animals = ["elephant", "giraffe", "zebra", "lion", "rat"]
print(animals)
generatedlist = []
for n in animals:
    if len(n) >= 5:
        generatedlist.append(n)

for x in generatedlist:
    print(x)
