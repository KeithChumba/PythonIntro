students = ["jonathan", "stacy", "abraham", "tim", "keith", "tim", "sylvester", "stacy"]
print(students)
generatedlist = []


for n in students:
    if 4 < len(n) < 7:
        generatedlist.append(n)


for x in generatedlist:
    print(x)


for t in students:
    if len(t) > 7:
        generatedlist.append(t)

for y in generatedlist:
    print(y)


uniqueList = []
duplicateList = []


for p in students:
    if p not in uniqueList:
        uniqueList.append(p)
    elif p not in duplicateList:
        duplicateList.append(p)

print(duplicateList)
