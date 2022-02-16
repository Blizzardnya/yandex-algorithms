def realization():
    inp = input()

    count = 0

    for letter in inp:
        if letter == '(':
            count += 1
        else:
            count -= 1

    return 'YES' if count == 0 else 'NO'


if __name__ == '__main__':
    print(realization())
