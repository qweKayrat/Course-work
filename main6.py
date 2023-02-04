# from math import *

# r = float(input("Введите радиус окружности: "))
# pi = pi
# L = 2*pi*r
# print("Длина окружности = ", round(2*pi*r, 2))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")

# print(dir(time))
# s = time.time()
# print(s)
# b = 749881178
#
# local = time.ctime(s)
# print(local)

# res = time.localtime()
# print(res)
# print(res.tm_mday, (".0" + str(res.tm_mon) if res.tm_mon < 10 else "." + str(res.tm_mon)), ".",
#       res.tm_year, sep="")

# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Сегодня: %B %d (%A), %Y.", time.localtime(b)))

# pause = 5
# print("Программа запущенна")
# time.sleep(pause)
# print("Программа завершена")

# mes = input("Название напоминания: ")
# t = float(input("Через сколько минут: "))
# time.sleep(t*60)
# print(mes)

# start = time.time()
# time.sleep(3)
# finish = time.time()
# res = finish - start
# print(res)
#
# start = time.monotonic()
# time.sleep(3)
# finish = time.monotonic()
# res = finish - start
# print(res)

# def get_sum(a, b):
#     print("Сумма: ")
#     return a + b


# x = 2
# y = 5

# res = get_sum(x, y)
# get_sum("10", "20")
# print(res * 2)

# def symbol(count, a, b, ):
#     for i in range(count):
#         x = b if i % 2 else a
#         print(x, end="")
#     print()


# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def result(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#     return "Числа равны"

# a1 = int(input("a = "))
# b1 = int(input("b = "))

# print("Результат:", result(a1, b1))

# def cub(a):
#     return a ** 3

# for i in range(1, 11):
#     print(i, "В кубе = ", cub(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
# x = lst.pop(0)
# z = lst.pop()
# lst.append(x)
# lst.insert(0, z)
# return lst


# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(10, 15))
# a = 10
# b = 5
#
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch < "10":
#             has_num = True
#     if len(password) > 7 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
#
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Пароль не надёжен")


# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, ))
# e = 2
# print(get_sum(1, 5, d=e))
# print("Результат: ", get_sum(d=1, a=5), sep="!!!!", end="\n\n")
# print(get_sum(d=1))

# def display_info(name, age):
#     print(f'Name: {name}\nAge: {age}')


# display_info("Ira", 23)
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# def for_print(lst):
#     for row in lst:
#         for i in row:
#             print(i, end="\t")
#         print()#
#
#
# lst1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
#
# for_print(lst1)

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s


# print("Сумма четных цифр")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def add_number(n):
#     print("n:", n, "=", id(n))
#     n = n + [4]  # != ( n += [4] )
#     print("n:", n, "=", id(n))
#     return n


# x = [1, 2, 3]
# print("x:", x, " = ", id(x))
# add_number(x)
# print("x:", x, " = ", id(x))
# print("y:", y, " = ", id(y))

# Tuple - Кортежи

# lst = [1, 2, 3]
# tpl = (1, 2, 3)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# tpl = (1, 2, 3, 4, 5, 6, 7)
# print(tpl)
# print(tpl[2])
# tpl[2] = 10
# print(tpl[1::2])

from random import randint


# s = tuple(2**i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(t3.count("l"))
# if "a" in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first: second + 1]
#         else:
#             return tpl[tpl.index(el):]

#      else:
#         return ()


# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

def range_tuple(num1, num2):
    return tuple(randint(num1, num2) for _ in range(10))


tpl1 = range_tuple(0, 5)
tpl2 = range_tuple(-5, 0)
tpl3 = tpl1 + tpl2
print(tpl1)
print(tpl2)
print(tpl3)
print("0 =", tpl3.count(0))
