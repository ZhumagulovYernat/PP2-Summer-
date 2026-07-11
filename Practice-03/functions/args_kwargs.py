def numbers(*args):
    print(args)
    print(sum(args))

numbers(5, 10, 15)
numbers(1, 2, 3, 4, 5)


def information(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

information(name="Anna", age=20, city="Paris")


def student(name, *subjects):
    print(name)
    for subject in subjects:
        print(subject)

student("Mike", "Math", "Physics", "English")


def profile(name, **info):
    print(name)
    for key, value in info.items():
        print(key, value)

profile("Tom", age=22, country="USA", university="MIT")