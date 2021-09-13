"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том
порядке, в котором они встречаются в списке.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
"""


def realization():
    inp_list = list(map(int, input().split()))

    duplicates = {}

    for item in inp_list:
        duplicates[item] = duplicates.get(item, 0) + 1

    return ' '.join([str(item) for item in duplicates if duplicates[item] == 1])


if __name__ == '__main__':
    print(realization())
