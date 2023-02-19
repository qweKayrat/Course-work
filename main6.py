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

# def range_tuple(num1, num2):
#     return tuple(randint(num1, num2) for _ in range(10))


# tpl1 = range_tuple(0, 5)
# tpl2 = range_tuple(-5, 0)
# tpl3 = tpl1 + tpl2
# print(tpl1)
# print(tpl2)
# print(tpl3)
# print("0 =", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["Hello", "world"])
# print(t, id(t))

# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t  # Распаковка кортежа
# print(x, y, z)

# def get_user():
#     name, age, is_married = "Tom", 22, False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# first_name, year, married = get_user()
# print(first_name, year, married)

# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst = list(tpl)
# print(type(lst))
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Мюнхен", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )

# print(countries)

# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "\nНаселение:", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, " (население: ", city_population, ")", sep="")

# Множество - set

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("Hello")
# print(type(a))
# print(a)

# s = {x*x for x in range(10)}
# print(s)

# def to_set(lst):
#     s = set(lst)
#     return s, len(s)

# a = "я обычная строка"
# b = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(a))
# print(to_set(b))

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {i for i in lst if "a" not in i}
# a = {"A"+i[1:] if i[0] == "a" else "B"+i[1:] for i in lst}
# a = {i.capitalize() if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"}
# print(a)

# for i in lst:
#     if i[1] == "c":
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}

# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# str1 = set(input("Введите первую строку: "))
# str2 = set(input("Введите вторую строку: "))
# print("Общими буквами являются:\n", str1 & str2)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}

# print(a <= b)
# print(a >= b)
# print(a != b)

# music = {"Костя", "Женя", "Илья"}
# drawing = {"Марина", "Женя", "Света"}
# print("Только с одним хоби", music ^ drawing)
# print("Ходят на два кружка", music & drawing)
# print("Рисованием занимаются: ", drawing - music)

# frozenset (замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset("hello")
# print(a)

# Dict - Словарь
# from random import randint

# d = {i: randint(1, 100) for i in range(1, 11)}
# d = {str(i) + "-й элемент": randint(1, 100) for i in range(1, 11)}
# d = {input("Ключ: "): input("Значение: ") for i in range(3)}
# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# d["two"] = 200
# d["one"] += 100
# print(d)

# for key, val in d.items():
#     print(key, val)

# dct = {i: input("--> ") for i in range(1, 5)}
# print(dct)
# dl = int(input("Какой ключ изменить: "))
# try:
#     del dct[dl]
#     print(dct)
# except KeyError:
#     print("Элемента с таким ключом: ", dl, ",нет в словаре ")
#
# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i3-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400],
# }
# for key, values in goods.items():
#     print(f'{key}) {values[0]} - {values[1]} шт. по {values[2]}руб')
#
# while True:
#     num = input("№ ")
#     if num != '0':
#         qty = int(input("Количество: "))
#         goods[num][1] += qty
#     else:
#         break
#
# for key, values in goods.items():
#     print(f'{key}) {values[0]} - {values[1]} шт. по {values[2]}руб')

# d = {"a": 1, "b": 2, "c": 3}
# value = d.get('b1', 'Такого ключа нет')
# print(value)
# print(d.keys())
# print(d.values())
# print(d.items())
# item = d.pop('e', 5) - если ключа 'e' нет в словаре, вернёт 5
# item = d.setdefault('e',100)
# print(item)
# d.update({('b', 4), ('r', 7)})
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop("name")
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# a = {'b': 1, 'a': 4, 'd': 2, 'c': 3}
# d = list(a.items())
# print(d)
# n, m = zip(*d)
# print(n)
# print(m)
#
# c = list(zip(n, m))
# print(c)
# c.sort()
# print(c)
#
# Сортировка словаря преобразовывая в список
# c = list(zip(m, n))
# print(c)
# c.sort()
# print(c)
# print(dict(c))
# c = {v: k for k, v in c}
# print(c)


# month = ['January', 'February', 'March']
# total_sales = [52_000.00, 51_000.00, 48_000.00]
# prod_cost = [46_800.00, 45_900.00, 43_200.00]
#
# for sales, costs, m in zip(total_sales,prod_cost,month):
#     profit = sales - costs
#     print(f'Чистая прибыль в {m} = {profit}')

# one = {'a': 1, "b": 2}
# two = {'c': 3, "d": 4}
# print({**one, **two})

# data = ['red', 'green', 'blue']
# ind = 1
# for i in data:
#     print(ind, i)
#     ind += 1
# print()
# for n, i in enumerate(data, 1): # enumerate(data, start = 1)
#     print(n, i)

# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
# for i, (j, v) in enumerate(dict_one.items(), 1):
#     print(i, j, "->", v)

# def to_dict(*args):
#     return {k: k for k in args}
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))

# def qew(*args):
#     avg = sum(args) / len(args)
#     print("Средняя арифметическая = ",avg)
#     return [x for x in args if x < avg]
#
# print(qew(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(qew(3, 6, 1, 9, 5))


# def print_scores(student, *scores):
#     print('\nStudent name:', student)
#     for score in scores:
#         print(score, end=" ")
# print(*scores)
# print()


# print_scores("Jonathan", 10, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33, 56)

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def intro(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#     print()

# intro(name='Irina', surname='Sharma', age=22)
# intro(name='Igor', surname='Wood', email='igor@gmail.com', age=25, phone=89235164532)

# my_dict = {'one': 'first'}
#
# def db(**kwargs):
#     return my_dict.update(kwargs)
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print("my_dict =", my_dict)

# def func1(*args):
#     print(args[0])
#
# func1(1, 2, 3, 4, 5, 6)


# def func(first, *args, **kwargs):
#     return first, args, kwargs
# print(func(5, 4, 8, 8, 7, a=6, b=2, c=10))

# Область видимости (score)

# name = 'Tom'
#
# def hi():
#     global name, surname
#     name = 'Sam'
#     surname = 'Johnson'
#     print("Hello", name)
#
# def bye():
#     print("Good by", name)
#
# hi()
# bye()
# print(name, surname)

# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func()
# x = 3
#
# def add_two(a):
#     x = 2
#
#     def add_some():
# x = 5
# return a + x
#
# return add_some()
#
# print(add_two(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# def outer_func(who):
#     def inner_func():
#         print("Hello", who)
#
#     inner_func()

# outer_func("World!")


# def fun1():
#     a = 6
#
# def fun2(b):
#     a = 4
#     print("Сумма:", a + b)
#
# print('a =', a)
# fun2(4)
#
# fun1()

# x = 25
# t = 0
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
# fn()
# z = x + t
# print(z)  # 55


# def fn1():
#     x = 25
#
#     def fn2():
x = 33


#
# def fn3():
#     nonlocal x
#     x = 55
#
# fn3()
# print("fn2.x =", x)
#
# fn2()
# print("fn1.x =", x)
#
# fn1()


# def outer(a1, a2, b1, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
# print(outer(2, 3, 5, 7))


