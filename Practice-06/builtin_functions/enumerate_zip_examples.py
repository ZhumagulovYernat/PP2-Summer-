names = ["Alex", "John", "Maria"]
scores = [90, 85, 95]


for index, name in enumerate(names):
    print(index, name)


for name, score in zip(names, scores):
    print(name, score)


students = list(zip(names, scores))

print(students)