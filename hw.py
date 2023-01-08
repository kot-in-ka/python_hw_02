# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def zadacha1():
    number = int(input('Введите число: '))
    count = 1
    factorial = 1
    while count < number:
        for i in range(1, number+1):
            factorial *= i
            print(factorial)
            count += 1


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def zadacha2():
    print(f'x | y | z | ¬(X ∧ Y) ∨ Z')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f'{x} | {y} | {z} | {int( not(x and y) or z)}')


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def zadacha3():
    text1 = 'one'
    length_text1 = len(text1)
    text2 = 'onetwonine'
    list = []
    for i in range(length_text1):
        count = 0
        if text1[i] in text2:
            for a in range(len(text2)):
                if text2[a] == text1[i]:
                    count += 1
        list.append(str(text1[i]) + ' - ' + str(count))
    print(list)


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def zadacha4():
    list = [-3, -2, -1, 0, 1, 2, 3]
    list_lenght = len(list)
    move = 2
    list_new = reversed(list[-move:list_lenght])
    list = list[:-move]

    for i in list_new:
        list.insert(0, i)
    print(list)


zadacha1()
zadacha2()
zadacha3()
zadacha4()