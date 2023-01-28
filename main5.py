# Генерация случайных данных
# import random

# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(5, 15, 2))

# from random import randint, randrange as rr

# print(randint(0, 5))
# print(rr(5, 15, 5))

# from random import *

# print(randint(0, 5))
# print(randrange(5, 15, 2))
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(choice(city_list))  # Случайный выбор элемента из списка
# print(choices(city_list, k=3))  # Случайный выбор элементов из списка

# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=3))

# shuffle(s)  # Перемешивает элементы внутри переменной
# print(s)

# city_list = "Новосибирск"
# print(choice(city_list))
# print(choices(city_list, k=3))

from random import randint

# mas = [randint(0, 20) for i in range(5)]
# print(mas)

# Функции агрегирования

# lst = [7, 12, 20, 18, 9]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# print("Hello" < 'hello')

# mas = [randint(0, 100) for i in range(10)]
# max_mas = max(mas)
# print(mas)
# print(max_mas)
# mas.remove(max_mas)
# mas.insert(0, max_mas)
# print(mas)

# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# min_lst = min(lst)
# min_ind = lst.index(min_lst)
# print("Min:", min_lst)
# print("Index min:", min_ind)

# del lst[:min_ind]
# print(lst)
# print(lst[min_ind:])

# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("!!! Список пустой")

# lst1 = [randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# lst2 = [randint(0, 10) for j in range(int(input("Введите размер второго списка: ")))]
# print("Первый список", lst1)
# print("Второй список", lst2)
#
# lst3 = lst1 + lst2
# print("Третий список", lst3)
#
# lst3 = []
# for i in lst1:
#     if i not in lst3:
#         lst3.append(i)
# for i in lst2:
#     if i not in lst3:
#         lst3.append(i)
#
# print("Элементы обоих списков без повторений", lst3)
# lst3 = []
# for i in lst1:
#     if i in lst2 and i not in lst3:
#         lst3.append(i)
# print("Общие элементы для двух списков", lst3)
#
# lst3 = [min(lst1), max(lst1), min(lst2), max(lst2)]
# print("Минимальные и максимальные элементы первого и второго списка", lst3)

# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     w = randrange(0, n)
#     if w not in s:
#         s.append(w)
# print(s)

# Вложенные списки
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# print(len(m))
# print(m)
# print(m[1][2])

# for i in range(len(m)):
#     for j in range(len(m[i])):
#         print(m[i][j], end="\t")
#     print()

# for i in m:
#     for j in i:
#         print(j, end="\t\t")
#     print()

# matrix = [[0 for x in range(5)]for y in range(3)]
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print()
# [[print(j, end="\t") for j in i] for i in matrix]

# matrix = [[0 for x in range(5)]for y in range(3)]
# ИЛИ
# matrix = []
# for i in range(3):
#     new_row = []
#     for j in range(5):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)

# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# s = 0
# for row in matrix:
#     for j in row:
#         print(j, end="\t\t")
#         if j < 0:
#             s += 1
#     print()
# print("Количество отрицательных элементов: ", s)

# n = int(input("Введите размер списка: "))
# m = [[randint(0, 100) for x in range(n)] for y in range(n)]
#
# for row in m:
#     for j in row:
#         print(j, end="\t\t")
#     print()
#
# k = m[0][0]
# for i in range(len(m)):
#     if k > m[i][i]:
#         k = m[i][i]
# print(k)

# github.com

# print("Проверка репозитория")

print("Изменили склонированный репозиторий")
