# a = 1
# b = 2
# print("a:", a)  # 1
# print("b:", b)  # 2
# a, b = b, a
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# Функции явного преобразования типов:
# int() - преобразует в целочисленное число
# str() - преобразует в строку
# float() - преобразует в число
# bool() - преобразует в булливое значение
# False - "", 0, null,

# num1 = "2"
# num2 = 3.5
# res = int(num1) + num2
# # res = num1 + str(num2)  # конкатенация
# print(res)
# a = 3.897
# a = round(a, 2)  # round() - функция округления
# print(a)
# print(type(a))

# num1 = "5.2"
# num2 = 10
# c = float(num1) + num2
# print(c)
# print(bool(0))

# name = "Виктор"
# age = 26
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне" , age , "лет.")
# print("Меня зовут" , name , ". Мне" , age , "лет.", sep="--", end=" ")
# default sep = " " end = "\n"
# print()
# print("я учу Python")

# name = input("Введите ваше имя:\n")
# print("Вас зовут", name)

# num = int(input("Введите число: "))
# power = int(input("Введите cтепень: "))

# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")
# num3 = input("Введите третье число: ")
# num4 = input("Введите четвертое число: ")
#
# sum1 = int(num1) + int(num2)
# sum2 = int(num3) + int(num4)
# res = round((sum1/sum2), 2)
#
# print("Результат: ", res)

# a = int(input('Введитек первое число:'))
# b = int(input('Введите второе число:'))
# c = int(input('Введите третье число:'))
# d = int(input('Введите четвертое число:'))
# print(round((a + b) / (c + d), 2))

# b1 = True
# b2 = False
# print((int(b1))) # 1
# print(b1 + 5)  # True(=1) + 5 = 6
# print((int(b2))) # 0
# print(b2 * 5)  # False(=0) * 5 = 0

# print(bool("Python"))  # True
# print(bool(""))  # False
# print(bool(9))  # True
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
#
# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)
# print(type(test))

# print(7 == 7)  # True
# print(5+2 == 5)  # False
# print(7 != 7)
# print(8 > 7)
# print(8 < 7)
# print(8 >= 8)
# print(6 <= 8)
# print("привет" > "пРивет")

# print(2 < 4 < 9)  # True && True = True
# print(3 * 3 <= 7 >= 2)  # False && True = False
# print(2 * 5 > 7 >= 4 + 3)  # True && True = True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True = True
# print(5 - 3 == 2 and 1 + 3 != 4)  # True and False = False
#
# print(5 - 3 == 2 or 1 + 3 != 4)  # True and True = True
# print(5 - 3 == 2 or 1 + 3 != 4)  # True and False = True

# print(not 9-5)
# print(not 9-9)

# cnt = 15
# if cnt < 10:
#     cnt +=1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 5
# b = 5
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = input("Введите первую сторону ")
# b = input("Введите вторую сторону ")
# c = input("Введите третью сторону ")
#
# if a != b != c:
#     print("Треугольник разносторонний")
# elif a == b == c:
#     print("Треугольник равносторонний")
# else:
#     print("Треугольник равнобедренный")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели нет")

# month = int(input("Введите номер месяца: "))
#
# if 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# elif month == 12 or month == 1 or month == 2:
#     print("Зима")
# else:
#     print("Такого месяца не существует")

# bird = int(input("Введите количество ворон от 0 до 9: "))
#
# if 0 <= bird <= 9:
#     print("На ветке", bird, end=" ")
#     if bird == 1:
#         print("ворона")
#     elif 2 <= bird <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Вы ввели большое количество ворон")

