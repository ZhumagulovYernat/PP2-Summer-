class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def info(self):
        print(self.name, self.age)


student = Student("Alex", 20)

student.show()
student.info()