numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print(squares)

doubles = list(map(lambda x: x * 2, numbers))
print(doubles)

names = ["tom", "alice", "john"]

capital_names = list(map(lambda name: name.capitalize(), names))
print(capital_names)

lengths = list(map(lambda word: len(word), names))
print(lengths)