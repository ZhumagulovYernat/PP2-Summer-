class Student:
    school = "Python School"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Alex", 20)
student2 = Student("Anna", 22)

print(student1.name)
print(student1.age)
print(student1.school)

print(student2.name)
print(student2.age)
print(student2.school)

Student.school = "New School"

print(student1.school)
print(student2.school)