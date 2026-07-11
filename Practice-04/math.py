import math
import random


degree = 15

radian = math.radians(degree)

print("Radian:", round(radian, 6))


height = 5
base1 = 5
base2 = 6

trapezoid_area = ((base1 + base2) / 2) * height

print("Trapezoid area:", trapezoid_area)


sides = 4
side_length = 25

polygon_area = (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

print("Polygon area:", round(polygon_area))


base = 5
height = 6

parallelogram_area = base * height

print("Parallelogram area:", float(parallelogram_area))


numbers = [5, 10, 15, -3]

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Absolute:", abs(-20))
print("Round:", round(5.678))
print("Power:", pow(2, 3))


print("Square root:", math.sqrt(25))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("PI:", math.pi)


print("Random number:", random.random())
print("Random integer:", random.randint(1, 10))

colors = ["red", "blue", "green"]

print("Random choice:", random.choice(colors))

random.shuffle(colors)

print("Shuffled list:", colors)