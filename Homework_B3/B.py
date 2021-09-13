"""
Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES
(в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""


def realization():
    inp_list = list(map(int, input().split()))

    duplicates = {}

    for item in inp_list:
        if duplicates.get(item):
            print('YES')
        else:
            duplicates[item] = 1
            print('NO')


if __name__ == '__main__':
    realization()
