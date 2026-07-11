def add(a, b):
    return a + b

result = add(10, 5)
print(result)


def multiply(a, b):
    return a * b

print(multiply(4, 6))


def is_even(number):
    return number % 2 == 0

print(is_even(8))
print(is_even(7))


def full_name(first_name, last_name):
    return first_name + " " + last_name

name = full_name("John", "Smith")
print(name)