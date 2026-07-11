numbers = [5, 2, 8, 1, 3]

sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

students = [
    {"name": "Alex", "age": 20},
    {"name": "Tom", "age": 18},
    {"name": "Anna", "age": 22}
]

sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students)


words = ["python", "java", "c", "javascript"]

sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)