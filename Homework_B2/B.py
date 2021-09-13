"""
На Новом проспекте построили подряд 10 зданий. Каждое здание может быть либо жилым домом, либо магазином, либо офисным
зданием.

Но оказалось, что жителям некоторых домов на Новом проспекте слишком далеко приходится идти до ближайшего магазина.
Для разработки плана развития общественного транспорта на Новом проспекте мэр города попросил вас выяснить,
какое же наибольшее расстояние приходится преодолевать жителям Нового проспекта, чтобы дойти от своего дома до
ближайшего магазина.

Формат ввода
Программа получает на вход десять чисел, разделенных пробелами. Каждое число задает тип здания на Новом проспекте:
число 1 обозначает жилой дом, число 2 обозначает магазин, число 0 обозначает офисное здание. Гарантируется, что на
Новом проспекте есть хотя бы один жилой дом и хотя бы один магазин.

Формат вывода
Выведите одно целое число: наибольшее расстояние от дома до ближайшего к нему магазина. Расстояние между двумя соседними
домами считается равным 1 (то есть если два дома стоят рядом, то между ними расстояние 1, если между двумя домами есть
еще один дом, то расстояние между ними равно 2 и т.д.)
"""


def measure_distance(buildings):
    result = []
    for index, building in enumerate(buildings):
        if building != 1:
            result.append(0)
        else:
            right_list = buildings[index + 1:]
            try:
                result.append(right_list.index(2) + 1)
            except ValueError:
                result.append(-1)

    return result


def realization():
    buildings = list(map(int, input().split()))

    right = measure_distance(buildings)
    reverse = measure_distance(buildings[::-1])[::-1]

    result = []

    for i in range(len(right)):
        if right[i] < 0 and reverse[i] < 0:
            result.append(0)
        elif right[i] < 0 or reverse[i] < 0:
            result.append(right[i] if 0 > reverse[i] else reverse[i])
        else:
            result.append(right[i] if right[i] < reverse[i] else reverse[i])

    return max(result) if len(result) > 0 else ''


def lector_realization():
    d = list(map(int, input().split()))
    shop_pos = -20
    left = [0] * len(d)

    for i in range(len(d)):
        if d[i] == 2:
            shop_pos = i
        if d[i] == 1:
            left[i] = i - shop_pos

    ans = 0
    shop_pos = 30

    for i in range(len(d) - 1, -1, -1):
        if d[i] == 2:
            shop_pos = i
        if d[i] == 1:
            min_dist = min(shop_pos - i, left[i])
            ans = max(ans, min_dist)

    return ans


if __name__ == '__main__':
    print(realization())
    print(lector_realization())
