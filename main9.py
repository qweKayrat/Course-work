# Регулярные выражения
# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в два счёта."
# reg = "в"
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с шаблоном
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))  # месторасположение первого совпадения объекта в начале строки
# print(re.split(reg, s, 2))  # Возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "В", s, 3))  # поиск и замена

# s = "Я ищу совпадения в 2023 году. И я их найду в два счёта. [-1863]. Hello"
# reg = "[12][0-9][0-9][0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = "." # поиск любого символа
# reg = r"\."
# reg = r"[0-9[\].-]"
# reg = r"[^а-я]"
# reg = r"[^а-я]"
# print(re.findall(reg, s))
# print(ord("Ё"))
# print(ord("А"))
# print(ord("Я"))
# print(ord("я"))
# print(ord("ё"))

# s = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09.'
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения ^ в 2023 году. И я их найду в 2 счё_та. [-1863]. Hello. 20000000"
# reg = r'0+'
# print(re.findall(reg, s))

# d = 'Цифры: -------------7, +17, -42, 0012, 0.33'
# print(re.findall(r'[+-]?\d+[.\d]*', d))

# s = '06-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r' #.*', '', s))
#
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r' #.*', '', s)))
# print('Дата рождения:', re.sub(r'-', '.', '06.03.1987'))


# s = 'autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = r'\w+\s*=\s*\w+[\s\w.]*'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall(r'^[A-Za-z_0-9]')


# print(validate_login("Python_master"))
# print(validate_login("Pyt_09-4"))

# print(re.findall(r'\w+', '10 + й'))
# print(re.findall(r'\w+', '10 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '10 + й', flag=re.A))
# print(re.findall(r'\w+', '10 + й', re.A))

# text = 'hello world'
# print(re.findall(r'\w+', text))
# print(re.findall(r'\w+', text, re.DEBUG))


# s = "Я ищу совпадения ^ в 2023 году. И я их найду в 2 счё_та. [-1863]. Hello. 20000000"
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one.\w+', text, re.S))

# print(re.findall('one$',text))
# print(re.findall('one$',text, re.MULTILINE))
# print(re.findall('^two',text))
# print(re.findall('^two',text, re.M))


# print(re.findall("""[a-z.-]+ # part 1
# @    # @
# [a-z.-]+  # part 2
# """, 'test@mail.ru', re.VERBOSE))  # VERBOSE = X

# text = """Python,
# python
# PYTHON"""
# reg = '(?im)^python'
# print(re.findall(reg, text))

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
#
# print(re.findall("<.*?>", text))
#
# s = "Я ищу совпадения^ в 2023 году. И я их найду в 2 счёта. 186389. Hello."
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

# s = "<p>Изобрадение <img    alt = 'картинка' src='bg.jpg' width = '200'> - фон страницы <img alt = 'картинка'></p>"
# reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s?=\s?[^>]+>'
# print(re.findall(reg, s))
# print(re.sub(reg, '<img src="1.jpg">', s))

# s = 'Пётр, Ольга и Виталий отлично учатся!'
# reg = 'Пётр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "int = 4, float =4.0, double = 8.0f int 7"
# reg = r"int\s?=\s?\d[.\w]*|double\s?=\s?\d[.\w]*"
# reg = r"(?:int|double)\s?=\s?(?:\d[.\w]*)"
# () - сохраняющие скобки
# (?:) - не сохраняющиеся скобки
# print(re.findall(reg, s))
# print(re.search(reg, s))

# s = 'Word2016, PS6, AI5'
# reg = r"([a-z]+\d*)"
# print(re.findall(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё_та"
# reg = r'(\d)+\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s))
# m = re.search(reg, s)
# print(m)
# print(m[1])
# print(m[2])
# print(m[0])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
#
# count = 0
#
#
# def repl_count(city):
#     global count
#     count += 1
#     return f"<option value='{count}'>{city.group(1)}</option>\n"
#
#
# print("<select name 'city'>")
# print(re.sub(r'\s*(\w+)\s*', repl_count, text))
# print("</select>")

# s = 'Самолёт прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r"\2-\1-\3", s))  # 23.10.2021

# s = 'yandex.ru and yandex.com'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

