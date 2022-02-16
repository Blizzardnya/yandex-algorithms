def make_prefix_sums(items):
    pref_sums = [0] * (len(items) + 1)

    for i in range(1, len(items) + 1):
        if items[i-1] <= 0:
            pref_sums[i] = 0
        else:
            pref_sums[i] = pref_sums[i-1] + items[i-1]

    return pref_sums


def realization():
    n = int(input())
    a = list(map(int, input().split()))

    pref_sums = make_prefix_sums(a)
    print(pref_sums)
    print(max(pref_sums))


if __name__ == '__main__':
    realization()
