def GuGu(n):
    result = []
    result.append(n * 1)
    result.append(n * 2)
    result.append(n * 3)
    result.append(n * 4)
    result.append(n * 5)
    result.append(n * 6)
    result.append(n * 7)
    result.append(n * 8)
    result.append(n * 9)
    return result


print(GuGu(2))

a = 1
while a < 10:
    print(a)
    a += 1


def GuGu(n):
    result = []
    a = 1
    while a < 10:
        result.append(n * a)
        a += 1
    return result


print(GuGu(2))
