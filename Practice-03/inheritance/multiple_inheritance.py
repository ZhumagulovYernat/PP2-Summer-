class Father:
    def skill(self):
        print("Driving")


class Mother:
    def hobby(self):
        print("Cooking")


class Child(Father, Mother):
    def show(self):
        print("Child")


child = Child()

child.skill()
child.hobby()
child.show()