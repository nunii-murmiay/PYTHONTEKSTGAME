# name = input("Введите имя: ") #str - строка
# age = int(input("Введите возраст: "))  #int
# point = float(input("Введите оценку: "))  #float - число с плавующей точкой
# is_active = bool(input("Введите активность: "))  #bool(True/False)


# print("тип данных переменной age:", type(age))
# print("тип данных переменной point:", type(point))
# print("тип данных переменной name:", type(name))
# print("тип данных переменной is_active:", type(is_active))
# print("имя:",name, "возраст:", age, "оценка:", point, "активность:", is_active)

# print(float(4))
# print(str(5))
# print(int(4.5))


# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b) #целочисленое деление
# print(a % b) #нахождение остатка от деления
# print(a ** b)

#Операторы сравнения
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


#Логический оператор
# print((a == b) and (a > 10))
# print((a == b) or (a > 10))
# print(not(a > 10))

#Оператор присваивания
# a = a + 10
# a += 10
# a -= 10
# a += 1
# print(a)

# a = int(input("ВВедите число a: "))
# b = int(input("ВВедите число b: "))
# if a < 10:
#     print("a < 10")
# elif a == 10 and b == 4:
#     print("a == 10 and b == 4")
# else:
#     print("неизвестный пользователь")

#тернарный оператор
# print("чётная" if a % 2 == 0 else "нечётная")

# Цикл while
# a = int(input("Введите a: "))
# while a <= 10:
#     print(a)
#     a += 1

# print("не в цикле")


#цикл for
# a = int(input("Введите число a: "))
# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)

# оператор выьора match-case
# a = input("Введите значение: ")
# match a:
#     case "+": print(10 + 9)
#     case "-": print(10 - 9)
#     case "*": print(10 * 9)
#     case "/": print(10 / 9)
#     case _: print("неизвестное значение")

# списки
# names = ["gru", "vasia"]
# print(names)
# print(names[0], names[1])
# print(names[-1], names[-2])

# #добавление
# names.append("коля") #доьавдение нового элемента в конец списка
# print(names)
# names.insert(0, "Эдик")# добавление нового элемента на определённое место
# print(names)
# names.extend([1, 2])# добавляет все элементы из другого списка
# print(names)
# #удаление
# names.remove(1)#удаление пкрвого найденного элемента из списка
# print(names)
# name = names.pop()#удаляет и возвращает элемент с указанного индекса
# #по умолчанию - последний элемент.
# print("Удалённый элемент:", name)
# print(names)
# del names[0]
# print(names)
# # names.clear()
# # print(names)
# #Поиск элементов
# print(names.index("gru"))#возвращает индекс первого найденногот элемента
# print(names.count("vasia"))#Возвращает кол-во вхождений элемента в списки


# #сортировка
# numbers = [2, 3, 6, 1, 12, 5]
# numbers.sort(reverse=True)
# print("числа: ", numbers)
# names.sort(reverse=True)#сортировка в алфавитном порядке
# print(names)
# names.reverse()#сортировка в обратном порядке
# print(names)
# print(len(names))#сортировка количесива элементов в списке
# print(len(numbers))

# #Срезы
# #[start:tnd:step]
# print(numbers)
# print(numbers[::2])#нечётные
# print(numbers[1::2])#чётные

# print(numbers)
# print(numbers[3:])
# print(numbers[:4])
# print(numbers[1:5])
# print(numbers[::2])
# print(numbers[::3])
# print(numbers[::4])

# вложенные списки
# numbers = [
#     [1, 2, 3], #=0
#     [4, 5, 6], #=1
#     [7, 8, 9]  #=2
# ]

# print(numbers[0][-1])

# for i in numbers:
#     for j in i:
#         print(j)


# numbers = [i for i in range(1, 21, 2)] #если после 21 поставить число, то мы получим шаг,
# # к примеру: [1, 21, 2] - каждое второе число будет пропускаться
# print(numbers)
# print(min(numbers), max(numbers), sum(numbers))

#конкатенация
# print([1, 2, 3] + [4, 5, 6]) # соединяем строки
# print("строка" + "дебил")# соединяем строки
# print([1, 2, 3] * 3) #выводим строку 3 раза подряд

# numbers = [1, 2, 3, 6]
# a, b, c, d = numbers
# print(a, b, c, d)

# a, *b, c = numbers # * может расспаковаться несколько элементов
# print(a, b, c)

# a, _, b, _ = numbers
# print(a, b)


# кортеж (tuples)
# names = ("Петя", "Вася", "Коля", "Вася")
# print(names[0], names[1], names[2])
# print(names[-1], names[-2], names[-3])

# print(names[1:])
# print((1, 2, 3) + (4, 5))
# print((1, 2, 3) * 3)
# # a, b, c = names
# # print(a, b, c)

# print(names.count("Вася"))
# print(names.index("Вася"))

# numbers = (
# (1, 2, 3),
# (4, 5, 6),
# (7, 8, 9)  #=2
# )
# print(numbers[1][-1])

# for i in numbers:
#     for j in i:
#         print(j)


# names = {"Петя", "Вася", "Коля", "Вася"}
# print(names)
#
# names.add("Эдик")
# print(names)
# names.remove("Вася")
# print(names)
# names.discard("Сеня")
# print(names)
#
# name = names.pop()
# print(name, names)
# names.clear()
# print(names)


# # множества
# names = {"Петя", "Вася", "Коля", "Вася"}
# names1 = {"Катя", "Вера", "Соня", "Коля"}
# # объединение
# print(names.union(names1))
# print(names | names1)
# # пересечение
# print(names.intersection(names1))
# print(names & names1)
# # разность
# print(names.difference(names))
# print(names1 - names)
# # симметричная разность
# print(names.symmetric_difference(names1))
# print(names ^ names1)


# Словарь
student = {
    "name": "Петя",
    "age": 18,
    "marks": [85, 92, 78, 90]
}
print(student)
print(student["name"], student["age"], student["marks"])
student["age"] = 20 #Изменение начение
print(student)
student["city"] = "Москва"#добавление новой пары "ключ: значение"
print(student)
# del student["city"]#удаение с помощью оператора значение по ключу
# print(student)
# name = student.pop("name") #удаление и возвращение удаленного значения по ключу
# print(name, student )
# student.clear()#Очистка словаря
# print(student)

#Методы словарей
print(student["name"])
print(student.get("name", "Неизвестное значение"))
