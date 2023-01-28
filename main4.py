# Срезы
# список[start:stop:step]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[::2])
# print(a[::-1])
# print(a[3:20])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# a = "Hello"
# print(a[1:3])

# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:5]
# print(a)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a[6:7] = [99, 22]  # добавление элементов срезом,  не используется =(
# print(a)
# a.append(99)  # добавляет 1 элемент в конце списка
# print(a)
# a.extend([5, 4, 2])  # добавляет список элементов в конце списка
# print(a)
# a.extend("add")
# print(a)

# a = []
# a.extend([i**2 for i in range(1, 11)])
# ИЛИ [a.extend([i**2]) for i in range(1, 11)]
# ИЛИ for i in range(1, 11):
#     a.extend([i**2])
# print(a)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2, 100)  # Добавляет элемент по заданному индексу
# # insert(index,value)
# print(a)
# a.insert(0, 200)
# print(a)
# a.insert(len(a), 100)  # Добавление элемента в конец списка
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, " не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)
# ИЛИ более громозкий код
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.remove(2)  # Удаляет первый по найденному совпадению элемент из списка по значению
# print(a)
#
# last = a.pop()  # удаляет последний элемент из списка () и возвращает удалённый элемент
# print(a)
# print(last)
# second = a.pop(0)  # удаляет элемент по индексу (index)
# print(a)
# print(second)
# a.clear()  # Полностью очищает список
# print(a)

# lst = [int(input("->")) for i in range(int(input("n = ")))]
# k = int(input("Введите индекс:\nk = "))
# lst.pop(k)
# print(lst)

# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(2)  # Считает количество заданных значений в списке.
# print(num)

# b = 8
# if b in a:
#     ind = a.index(b, 4, -1)  # Возвращает положение первого индекса по заданному значению
# index(value, start, stop)
#     print(ind)

# c = [1, 2, 3]
# d = c Не корректно будет отрабатывать, т.к. списки "d" и "c" будут ссылаться на одну ячейку
# памяти, из-за этого изменение одного списка будет влечь за собой изменение другого
# d = c.copy() # возвращает копию списка, так создаются элементы с разными ячейками памяти
# print("c = ", c)
# print("d = ", d)
#
# c.append(4)
# d.insert(0, 100)
#
# print("c = ", c)
# print("d = ", d)

# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# a.reverse()  # перестроили элементы списка в обратном порядке индексов
# print(a)
#
# a.sort()  # отсортировали список по возрастанию
# print(a)
#
# a.sort(reverse=False)
# print(a)
#
# a.sort(reverse=True)
# print(a)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len, reverse=True)

# b = sorted(a, reverse=True)  # Сохраняет сортированную копию списка
# print("b =", b)
# print("a =", a)
