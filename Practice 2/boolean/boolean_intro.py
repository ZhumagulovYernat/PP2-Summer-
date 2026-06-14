is_student = True
is_teacher = False

print(is_student)
print(is_teacher)





age = 20

print(age > 18)
print(age < 18)
print(age == 20)




is_raining = True

if is_raining:
    print("Возьми зонтик")
else:
    print("Погода хорошая")







age = 20
has_ticket = True

print(age >= 18 and has_ticket)





age = 19
has_passport = True

if age >= 18 and has_passport:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")



password = input("Введите пароль: ")

if password == "1234":
    print("Верный пароль")
else:
    print("Неверный пароль")




temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("Идём гулять!")
else:
    print("Остаёмся дома")