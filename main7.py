# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
# add2 = outer(6)
# print(add2(11))
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res2 = func('Сочи')
# res1()
# res2()
# res2()

# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "Chris": 85,
#     "David": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69,
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(80, 101)
# B = make(70, 80)
# C = make(50, 70)
# D = make(0, 50)
#
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# Анонимные функции (lambda)

# def name(x, y):
#     return x + y
#
#
# print(name(3, 5))
# print((lambda x, y: x + y)(1, 2))
# (lambda x, y: print(x + y))(1, 2)
#

# func = lambda x, y: x + y  # так записывать нельзя! используй def
# print(func(1, 2))
# print(func("a", "b"))

# print((lambda x, y: x ** 2, y ** 2))
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda *args: args)(2, 5))

# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
# for t in c:
#     print(t("abc_"))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# add2 = outer1(5)
# print(add2(1))
#
# outer2 = (lambda n: lambda x: n + x)
# print(outer2(5)(11))

# sum3 = (lambda n: lambda x: lambda y: print(n + x + y))
# sum3(2)(4)(6)

# def func(i):
#     return i[1]
#
#
# d = {"d": 10, "b": 15, "c": 4}
# a = sorted(d)
# print(a)
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# list_d.sort(key=func)
# print(dict(list_d))

# players = [
#     {"name": "Антон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федор", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda i: i["last name"])
# print(res)
# res = sorted(players, key=lambda i: i["rating"], reverse=True)
# print(res)


# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# 12,3
# print(a[0](4, 10))

# a = {"one": lambda x: x - 1, "two": lambda x: x * (-1), "three": lambda x: x ** 5}
#
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a["two"](i))
#     elif i > 0:
#         print(a["one"](i))
#     else:
#         print(a["three"](i))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница")
# }
#
# d[2]()

# print((lambda a, b, c: a if a < b else b if b < c else c)(15, 10, 13))
# print((lambda a, b, c: a if a < b and a < c else b if b < c and b < a else c)((15, 10, 13))


# map(func,iterables), filter(func, iterables)

# Map

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# a = list(map(mult, lst))
# print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a1)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# t3 = tuple(map(int, t))
# print(t2)
# print(t3)

# areas = [3.563535, 7.434326, 8.245765, 4.467538, 9.135163, 6.411567]
#
# areas1 = list(map(round, areas, [2]*len(areas)))
# print(areas1)


# st = ["a", "b", "c", "d", 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))

# Filter

# t = ('abcd', 'abc', 'cdfrg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 64, 69, 86, 76, 75, 23, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print("[10; 20] = ", list(filter(lambda s: 9 < s < 21, lst)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"

#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():
#     print("Тело функции 'func_test'")
#
#
# func_test()
# test = my_decorator(func_test)
# test()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, '\n')
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор", )

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма", "+")
# def summa(a, b, ):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 6)
# sub(10, 5)

# https://www.youtube.com/playlist?list=PLKhF725nEal1za5jO8xSxbm9HyonmEGo-


# print(int('19'))
# print(int('19.5'))  # ValueError

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(18))  #0b10010
# print(oct(18))  #0o22
# print(hex(18))  #0x12
# bin() - Перевод в двоичную систему счисления
# oct() - Перевод в восьмиричную систему счисления
# hex() - Перевод в шестнадцатиричную систему счисления

# print(0b10010)
# print(0o22)
# print(0x12)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# print(e * -3)

# s = "Hello"
# print(s[1])
# print(s[-5])
# print(s[1:4])
# print(s[::-1])

# s = 'python'  # pytton
# s[3] = 't'  # TypeError
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_to_str(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 += s[i]
#         i += 1
# for i in s:
#     if i == c_old:
#         i = c_new
#     c2 += i
# return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nythot. Nytnot очень интересный язык программирования."
# str2 = change_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)


# print("Привет")
# print(u"Привет")

# print("C:\folder\file.txt")
# print(r"C:\\folder\\file.txt")
# print(r"C:\folder\file.txt\\"[:-1])
# print(r"C:\folder\file.txt" + "\\")


# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print(f"Меня зовут {name}. Мне {age} лет")

from math import pi

# print(f"Число PI: {pi}")
# print(f"Число PI: {round(pi, 2)}")
# print(f"Число PI: {pi:.2f}")

# x = 10
# y = 5
# print(f'{x=}, {y=}')
# print(f'{x} x {y} / 2 = {x * y / 2}')

# a = 74
# print(f'{{{{{a}}}}}')  # Экранирование {} нужно дополнительными {}

# dir_name = 'my_doc'
# file_name = "data.txt"
# print(fr'home\{dir_name}\{file_name}')

# s = "Много " \
#     "строк"
# s2 = ''
# s3 = """Много
#     строк"""
# s4 = '''Много
#     строк'''
# print(s)
# print(s3)
# print(s4)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра.
#     :param h: положительное число, высота цилиндра.
#     :return: положительное число, площадь цилиндра.
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
