def student(name, age):
    print(name, age)

student("Tom", 20)


def power(number, degree=2):
    print(number ** degree)

power(5)
power(5, 3)


def fruits(*items):
    for item in items:
        print(item)

fruits("apple", "banana", "orange")


def person(**info):
    for key, value in info.items():
        print(key, ":", value)

person(name="Alice", age=21, city="London")