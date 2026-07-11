class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


student1 = Student("Alex", 20)
student2 = Student("Anna", 22)

student1.show_info()
student2.show_info()