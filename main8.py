# print(ord("a"))
# print(ord("#"))
# print(ord("м"))
#
# while True:
#     n = input("->")
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# Практика
# my_str = "Test string for me"
# arr = [ord(i) for i in my_str]
# print("ASCII коды:", arr)
#
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
#
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
#
# print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))  # Из кода символа получаем символ
# print(chr(1080))

# a, b = 97, 122
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")
#
# print()
#
# while b < a + 1:
#     print(chr(b), end=" ")
#     b += 1


# from random import randint
#
# short = 7
# long = 10
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     password = ""
#     for i in range(rand_len):
#         password += chr(randint(min_ASCII, max_ASCII))
#     return password
#
#
# print("Случайный пароль:", random_password())

# Методы строк
# print(dir(list), "\n")
# print(dir(str))

# s = 'hello, WORLD! I am learning Python.'

# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.lower())  # hello, world! i am learning python.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.

# print(s.lower().count("h"))  # подсчёт количества вхождений подстроки в строку
# print(s.count("h", 1))

# print(s.find("h"))  # Возвращает первый индекс, который соответствует началу подстроки или -1 если элемента нет
# print(s.rfind("h"))
# print(s.index("h"))
# print(s.rindex("h"))

# st = input("Введите два слова через пробел: ")
# st = 'один два'
# defies = st.find(" ")
# print(st[defies+1:] + " " + st[:defies])

# s1 = "ab12c59p7dq"
# digits = []
# for symbol in s1:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
#         digits += [int(symbol)]
#
# print(digits)

# st = "the original words and form of a written or printed work"
# ch = "f"
# if st.count(ch) == 1:
#     print(st.find(ch))
# elif st.count(ch) >= 2:
#     print(st.find(ch), st.rfind(ch))

# print(s.endswith('lo', 0, 5))  # проверка окончания строки, подстрокой, start, end
# print(s.startswith('I am', 14))  # проверка начала строки, подстрокой, start, end

# print('abc123'.isalnum())  # состоит ли строка из букв и цифр
# print('abcABC'.isalpha())  # состоит ли строка из букв
# print('1234'.isdigit())  # состоит ли строка из цифр
# print('abc'.islower())  # состоит ли строка из символов букв в нижнем регистре (могут быть и любые символы)
# print('abc'.isupper())  # состоит ли строка из символов букв в верхнем регистре (могут быть и любые символы)

# print('py'.center(10))  # возвращает строку по центру
# print('py'.center(10, "-"))  # возвращает строку по центру

# print('   py'.lstrip())
# print('py   '.rstrip())
# print('   py   '.strip())

# print('https://www.python.org'.lstrip("/:pthsworg"))
# print('https://www.python.org'.rstrip("/:pthsworg"))
# print('https://www.python.org'.strip("/:pthsworg"))
#
# print('https://www.python.org'.lstrip("/:pths").rstrip("worg."))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("N", "P"))

# s = 'Замените в этой строке все появления "о" на букву "О", кроме первого и последнего вхождения'
# a = s[:s.find("о") + 1]
# b = s[s.find("о") + 1:s.rfind("о")]
# c = s[s.rfind("о"):]
# s = a + b.replace("о", "О") + c
# print(s)

# first = s.find("о")
# last = s.rfind("о")
# print(s[:first+1] + s[first+1:last].replace("о", "О") + s[last:])

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
# print('..'.join(['1', '2']))
# print(":".join("Hello"))
#
# print('H:e:l:l:o'.split(":"))
# print("Строка разделенная пробелами.".split())
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))

a = input("Введите Фио: ").split()
print(f'{a[0].capitalize()} {a[1][0].upper()}. {a[2][0].upper()}.')
