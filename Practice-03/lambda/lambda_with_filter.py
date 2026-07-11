numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


ages = [12, 18, 20, 15, 25]

adults = list(filter(lambda age: age >= 18, ages))
print(adults)


words = ["apple", "cat", "banana", "dog"]

long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)