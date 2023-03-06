# Функция с произвольным числом параметров *args , **kwargs
# args - Кортеж принимаемых аргументов
# kwargs - Словарь из принимаемых параметров

# def os_path(disk, *args, sep='\\', **kwargs):
# --- чтобы сделать принимаемый параметр формальным, его нужно прописать раньше kwargs ---
#     args = (disk, ) + args
#     if 'trim' in kwargs and kwargs['trim']:
#         args = [x.strip() for x in args]
#
#     path = sep.join(args)
#     return path


# P = os_path("F:", " ~stepik.org ",
#             ' Добрый, добрый Python ',
#             " 39\\p39. Функции.docx ",
#             sep="/", trim=False)
# print(P)  # F:/ ~stepik.org / Добрый, добрый Python / 39\p39. Функции.docx

# * - упаковывает и распаковывает кортеж

# x, *y = 1,2,3,4,5  # x = 1, y = (2,3,4,5)

# a = [1,2,3]
# x = (*a, )  # (1,2,3)

# d = (-5,5)
# range(d) - ошибка
# range(*d) - распакует кортеж и выведет цифры от -5 до 5
# list(range(*d))  # out: [range(-5,5)]
# list(*range(*d)  # out: [-5,-4,-3,-2,-1,0,1,2,3,4]

# [*range(1,4), *(False, True), *a]  #out: [1, 2, 3, False, True, 1, 2, 3]

# ** - упаковывает(в функции) и распаковывает словарь

# {**d, **d2} - Синтаксис объединения словарей, (В 1 словаре обновляются значения по одному ключу со словарём 2)

# Рекурсивная функция:

# def recursive(value):
#     print(value)
#     if value < 4:
#         recursive(value+1)
#     print(value)
# out: 1 \n 2 \n 3 \n 4 \n 4 \n 3 \n 2 \n 1

# Рекурсивная функция нахождения факториала n!
# def fact(n):
#     if n < 0:
#         return 1
#     else:
#         return n * fact(n - 1)

# Анонимные (lambda) функции:

# summ = lambda x, y: a + y

# Замыкания:

