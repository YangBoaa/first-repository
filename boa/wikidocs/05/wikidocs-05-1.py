# 클래스
result = 0


def add(num):
    global result
    result += num
    return result


print(add(2))
print(add(5))

result1 = 0
result2 = 0


def add1(num):
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2


print(add1(2))
print(add1(5))
print(add2(2))
print(add2(7))
