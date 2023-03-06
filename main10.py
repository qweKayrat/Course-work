
# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))  # 3
# elevator(n1)

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 8))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hell  o\tWorld "))


# Файлы

# with open('text.txt') as file:

# f = open(r'C:\Python215\Python\work\text.txt')
# f = open('text.txt', 'r')
# print(f)
# print(*f)
# print(f.closed)
# print(f.mode)
# print(f.encoding)
# print(f.name)
# f.close()
# print(f.closed)

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open('text.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('text.txt')
# print(f.readlines(14))
# print(f.readlines())
# f.close()

# f = open('text.txt')
# for line in f:
#     print(line, end="")
# f.close()

# count = 0
#
# with open('text.txt') as f:
#     print(len(f.readlines()))
#     for line in f:
#         count += 1
#
# print(count)

# f = open('zxc.txt', 'w')
# f.write("Hello\n\tWorld\n")
# f.close()

# f = open('zxc.txt', 'a')
# f.write("New text\n")
# line = ['This is line 1', 'This is line 2']
# f.writelines(line)
# f.close()

# f = open('zxc.txt', 'w')
# lst = [i ** 5 for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(str(index) + '\n')
# f.close()

# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# with open('text2.txt', 'r') as f:
#     read_file = f.readlines()
#     print(read_file)
#
# read_file[1] = "Hello world\n"
# print(read_file)
#
# with open('text2.txt', 'w') as f:
#     f.writelines(read_file)


# with open('text3.txt', 'w') as f:
#     f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
#
# with open('text3.txt', 'r') as f:
#     read_file = f.readlines()
#
# pos = int(input("Введите удаляемую строку: ")) - 1
#
# if -1 < pos < len(read_file):
#     read_file[pos] = ""
#     with open('text3.txt', 'w') as f:
#         f.writelines(read_file)
# else:
#     print("Вы ввели не корректную строку, такой строки нет")

# with open('text.txt', 'r') as f:
#     print(f.read(3))  # Hel
#     print(f.tell())  # 3 - возвращает текущую позицию условного курсора в файле
#     print(f.seek(1))  # 1 - перемещает условный курсор в заданную позицию
#     print(f.read())  # ello!
#     print(f.tell())

# with open('text1.txt', 'r+') as f:
#     print(f.write("I am learning Python"))
#     print(f.seek(3))
#     print(f.write("-new string-"))
#     print(f.tell())

# with open('text.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('text.txt', 'r+') as f:
#     for line in f:
#         print(line[:3])

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Done!')

# with open('res.txt', 'r') as f:
#     read_file = f.read().split(" ")
#     print(read_file)
#     print(len(read_file))
#     print(sum(map(float, read_file)))

# def longest_words(file):
#     with open(file, encoding='utf-8') as text:
#         w = text.read().split()
#         print(w)
# max_length = len(max(w, key=len))
# res = [word for word in w if len(word) == max_length]
# print(res)
# if len(res) == 1:
#     return res[0]
# return res
#
#
# print(longest_words('text.txt'))

# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as rf, open(write_file, 'w') as wf:
#     for line in rf:
#         line = line.replace("Строка", "Линия - ")
#         wf.write(line)
#         wf.write(line.replace("Строка", "Линия - "))

# with open('three.txt', 'w') as wf, open('one.txt', 'r') as rf1, open('two.txt', 'r') as rf2:
#     a, b = rf1.readlines(), rf2.readlines()
#     c = a + b
    #    print(c)
    #    wf.writelines(c)
    #    for line in c:
    #       wf.write(line)
    # for i, j in zip(a, b):
    #     c = i + j
    #     wf.write(c)