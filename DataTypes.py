# ord()  # Определение кода символа
# chr() # Определение символа из кода символа ASCII
# bin() - Перевод в двоичную систему счисления
# oct() - Перевод в восьмиричную систему счисления
# hex() - Перевод в шестнадцатиричную систему счисления

# String - Строка

# String.upper()  # Возвращает строку с буквами в большом регистре
# String.lower()  # Возвращает строку с буквами в маленьком регистре

# String.count(sub, star, end)  # Определяет число вхождений подстроки в строке

# String.find(sub, star, end)  # Возвращает индекс первого найденного вхождения
# String.frind(sub, star, end)  # Возвращает индекс первого найденного вхождения при поиске справа
# String.index(sub, star, end)  # Возвращает индекс первого найденного вхождения

# String.replace(old, new, count=-1)  # Заменяет строку old на new

# String.isalpha()  # Определяет: состоит ли строка целиком из буквенных символов
# String.isdigit()  # Определяет: состоит ли строка целиком из цифр

# String.rjust(width[, fillchar = ‘ ‘])  #  Расширяет строку, добавляя символы слева
# String.ljust(width[, fillchar = ‘ ‘])  #  Расширяет строку, добавляя символы справа

# String.split(sep=None, maxsplit=-1)  #  Разбивает строку на подстроки
# String.join(список)  # Объединяет коллекцию в строку

# String.strip()  # Удаляет пробелы и переносы строк справа и слева
# String.rstrip()  #  Удаляет пробелы и переносы строк справа
# String.lstrip()  #  Удаляет пробелы и переносы строк слева

# List - Список

# List.index(sub, star, end)  # Возвращает индекс первого найденного вхождения
# List.count(sub, star, end)  # Определяет число вхождений подстроки в строке

# List.append(99)  # добавляет 1 элемент в конце списка
# List.extend([sub, sub, sub])  # добавляет список элементов в конце списка
# List.insert(index, sub)  # Добавляет элемент по заданному индексу
# List.remove(sub)  # Удаляет первый по найденному совпадению элемент из списка по значению
# List.clear()  # Полностью очищает список

# List.pop(0)  # удаляет элемент по индексу (index)
# List.pop()  # удаляет последний элемент из списка () и возвращает удалённый элемент

# List.copy() # возвращает копию списка, так создаются элементы с разными ячейками памяти

# List.sort()  # отсортировали список по возрастанию (reverse=False)
# List.reverse()  # перестроили элементы списка в обратном порядке индексов


# List comprehension Фишки

# Matrix = [[a for a in range(3)] for b in range(4)]
# out: [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = [x
#      for row in A
#      for x in row
#      ]
# out: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Транспонирование матрицы:
# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# A = [[row[i] for row in A] for i in renge(len(A[0]))]
# out:
# [1, 2, 3, 4]             [1, 5, 9]
# [5, 6, 7, 8]        ->   [2, 6, 10]
# [9, 10, 11, 12]          [3, 7, 11]
#                          [4, 8, 12]

# g = [u**2 for u in [x+1 for x in range(5)]]

# Dict - Словарь

# dict(key=value, key=value,..)  # Создание словаря
# Dict.fromkeys[список[, значение по умолчанию] # Формирует словарь с заданными ключами и некоторым значением

# d[key]  # Получение значения по ключу, если ввести несуществующий ключ => Ошибка
# Dict.get(key)  # Получение значения по ключу, если ввести несуществующий ключ возвратит None или значение по умолчанию
# Dict.get(key, False), если ввести не существующий ключ, возвратит False
# Dict.setdefault[key[, default]] # Возвращает значение по ключу, если ключ в словаре отсутствует, то создаёт запись в словаре с
# не существующем ключом, и заданным значением{default}

# Dict.keys()  # Возвращает список ключей
# Dict.value()  # Возвращает список значение
# Dict.items()  # Возвращает Кортеж ключ, значение (key, value)

# Dict.update(Dict2)  # Обновление Словаря 1, Словарём2 (В 1 словарь обновляются и добавляются значения словаря2 )
# Пример D1 = {'one': 1, 'two': 2} || D2 = {'two': 'Два', 'three': 'Три'}
# D1.update(D2)  => {'one': 1, 'two': 'Два', 'three': 'Три'}
# D3 = {**D, **D2}  # Синтаксис объединения словарей, (В 1 словаре обновляются значения по одному ключу со словарём 2)
# После версии Python 3.9 объединить словарь можно ещё так:
# D1 | D2

# Dict.copy()  # Возвращает копию словаря, так создаются элементы с разными ячейками памяти
# Dict2 = dict(Dict) # Способ копирования словаря, с разными ячейками памяти

# Dict.clear()  # Полностью очищает словарь
# del Dict[key] # удаление из словаря по ключу
# Dict.pop(key, val)  # удаляет элемент по ключу, возвращается значение ключа, если ключ не найден вернёт val
# Dict.popitem()  # удаляет "Случайный"(Последний) выбранный ключ и возвращает удалённую пару (ключ:значение)
# Dict(словарь) является не упорядоченной коллекцией до версии 3.7

# Tuple - Кортеж

# a = (1,)  # Создание кортежа
# a = tuple()  # Создание кортежа

# a = a + (1,)  # Объединение кортежей
# b = (0,) * 10  # Дублирование кортежа

# Set - Множества
# Множества - неупорядоченная коллекция _Уникальных_ элементов

# s = {1, 2, 3, 4, "set"}
# s = Set()  # Создание множества (Пустого если не передали ничего)

# Set.add(value)  # Добавление значения (одного) в множества, если значение уже имеется в множестве ничего не произойдёт
# Set.update(iterable)  # Добавляет значения в множества, необходимо передать любой итерированный объект

# Set.discard(value)  # Удаление значения из множества, если значения нет в множестве ничего не произойдёт
# Set.remove()  # Удаление значения из множества, если значения нет в множестве выпадет ошибка
# Set.pop()  # Удаление случайного значения из множества, т.к. множества не упорядоченная коллекция возвращает удалённый объект
# Set.clear()  # Удаление всех элементов из множества

# Операции над множествами:

# Общие элементы
# Set1 & Set2 # Будут выделены элементы общие для этих множеств, исходные множества не изменяются
# Set1 &= Set2  # Множество1 изменится на общие элементы множества1 и множества2
# Если общих элементов нет, на выходе получится пустое множество
# Set1.intersection(Set2) # == ( Set1 & Set2 )
# Set1.intersection_update(Set2) # == ( Set1 &= Set2 )

# Объединение элементов
# Set1 | Set2 # Объединение двух множеств, исходные множества не изменяются
# Set1 |= Set2  # Множество1 изменится на объединение двух множеств
# Set1.union(Set2) # == ( Set1 | Set2 )

# Вычитание
# Set1 - Set2 # Удаление элементов множества1, которые есть и в множестве2, не изменяет исхожные множества
# Set1 -= Set2  # Множество1 изменится из него удалятся схожие элементы с множества2

# Симметричная разность
# Set1 ^ Set2 # Будут выделены только несхожие элементы множеств, исходные множества не изменятся
# Set1 ^= Set2 # В Множестве1 будут записаны несхожие элементы множеств 1 и 2

