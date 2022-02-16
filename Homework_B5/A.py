def make_prefix_sums(items):
    pref_sums = [0] * (len(items) + 1)

    for i in range(1, len(items) + 1):
        pref_sums[i] = pref_sums[i-1] + items[i-1]

    return pref_sums


def realization():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    pref_sums = make_prefix_sums(a)

    for i in range(q):
        start, end = map(int, input().split())
        print(pref_sums[end] - pref_sums[start-1])


if __name__ == '__main__':
    realization()
