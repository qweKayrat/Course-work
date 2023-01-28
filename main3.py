# match Выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case шаблон_n:
#         действие_n
#     case _:
#         действие по умолчанию

# password = "moder"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case "moderator":
#         print("Модератор")
#     case _:
#         print("Пароль не верен")
#
# day = 'среда'
# time = 17
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Вы ввели не корректное название дня недели или не рабочее время")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a==b" if a == b else "a > b"if a > b else "b > a")

# a, b = 20, 10
# print("на ноль делить нельзя" if b == 0 else a / b)
# print(a / b if b != 0 else "На ноль делить нельзя")

# try .... except
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Вы ввели не допустимый тип данных")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     if ValueError:
#         print("Вы ввели не допустимый тип данных")
#     elif ZeroDivisionError:
#         print("Нельзя делить на ноль")
# else:
#     print("Вс нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
#
# print("Код далее")

# m = input("Введите второе число: ")
# n = input("Введите первое число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы

# i = 1000
# while i < 1001:
#     print(i)
#     i -= 7

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i= ", i)
#     i += 2

# n = int(input("Введите количество звёздочек "))
#
# while n:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
#
# while a <= b:
#     print(a, end=" ")
#     if a % 2:
#         res += a
#     a += 1
# print("\nСумма нечетных чисел = ", res)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Это не целое число!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# res = 0
#
# while True:
#     n = int(input("Введите положительное целое число: "))
#     res += n
#     if not n > 0:
#         print(res)
#         break

# res = 1
#
# while True:
#     n = int(input("Введите целое число: "))
#     if n == 0:
#         print(res)
#         break
#     res *= n

# i = 0
# while i < 3:
#     # if i == 2:
#     #     break
#     if i == 2:
#         i = "a" + i
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i = ", i)
#
# print("\nЗа циклом")

# вложенный while

# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# j = 0
# while j < 5:
#     print(" " * j, "*")
#     j += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i: # 0 < 0
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# for element in collection:
# тело цикла

# for i in "Hello":
#     print(i)

# for color in "red", "orange", "yellow", "blue", 20, 0.3:
#     print(color)

# print(range(9))

# range(start(0), stop, step(1))

# for i in range(9, -1, -1):
#     print(i, end=" ")
#
# print()
# i = 9
# while i > -1:
#     print(i, end=" ")
#     i -= 1

# n = int(input("Введите целое цисло: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print("\ndone!")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# w = [letter * 2 for letter in "Hello"]
# print(w)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

#   Списки (list)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(nums[1])
# print(nums[4])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(len(nums))

#  Создание списков
# s = [5] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
#
# c = s + b
# print(c)

# n = list(range(2, 10, 2))
# print(n)
#
# n2 = [2, 4, 6, 8]
# print(n2)
#
# if n == n2:
#     print("Yes")
# else:
#     print("No")

# Генератор списков

# n = 5
# a = [i for i in range(1, n+1)]
#
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)


# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)
#
# i = 0
# while i < len(a):
#     a[i] = int(input("Введите элемент списка: "))
#     i += 1
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# a = [9, 8, 6, 4, 3]
# for i in range(len(a)): # i = счётчик
#     print(i, ": ", a[i])
#
# print()
#
# for i in a: # i = элементы списка
#     print(i)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# # for i in a:
# #     if i < 0:
# #         s += i
# print(s)

# OR lst = list(range(21,41))
# lst = [i for i in range(21, 41)]
# print(lst)
# a = 0
# b = 0
# for i in lst:
#     if i % 2 == 0:
#         a += 1
#     else:
#         b += i
#
# print(f'Количество четных элементов списка: {a}\nСумма нечетных элементов: {b}')

# a = [int(input(" -> ")) for i in range(int(input("n = ")))]
# print(a)
# sum1 = del1 = 0
# for i in range(len(a)):
#     if a[i]:
#         sum1 += a[i]
#         del1 += 1
# res = sum1 / del1
# print("Среднее арифметическое: ", res)

# a = [6, 3, 0, 8, 2]
# a[0], a[1] = a[1], a[0]
# print(a)
