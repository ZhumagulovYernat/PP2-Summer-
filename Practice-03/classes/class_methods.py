class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(self.brand, "is starting")

    def info(self):
        print(self.brand, self.year)


car1 = Car("BMW", 2020)
car2 = Car("Toyota", 2022)

car1.start()
car1.info()

car2.start()
car2.info()