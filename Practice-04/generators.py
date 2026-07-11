def squares(n):
    for i in range(n + 1):
        yield i * i


n = int(input("Enter number: "))

for value in squares(n):
    print(value)


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


numbers = []

for value in even_numbers(n):
    numbers.append(str(value))

print(",".join(numbers))


def divisible_by_three_four(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for value in divisible_by_three_four(n):
    print(value)


def squares_range(a, b):
    for i in range(a, b + 1):
        yield i * i


for value in squares_range(3, 7):
    print(value)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1


for value in countdown(5):
    print(value)