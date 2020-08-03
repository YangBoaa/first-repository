# 매개변수와 인수
def add(x, y):
    return x + y


print(add(3, 1))

# 입력값과 결괏값에 따른 함수의 형태
a = add(3, 4)
print(a)

# 입력값이 없는 함수
def say():
    return "Hi"


a = say()
print(a)

# 결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


add(3, 4)
a = add(3, 4)

# 입력값도 결괏값도 없는 함수
def say():
    print("Hi")


say()

# 매개변수 지정하여 호출
def add(c, d):
    return c + d


result = add(c=2, d=7)
print(result)

# 여러 개의 입력값을 받는 함수
def add_many(*arg):
    result = 0
    for i in arg:
        result = result + i
    return result


result = add_many(1, 2, 3, 4)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def add_mul(choice, *abc):
    if choice == "hello":
        result = 0
        for i in abc:
            result += i
    elif choice == "world":
        result = 1
        for i in abc:
            result *= i
    return result


result = add_mul("hello", 1, 2, 3, 4, 5)
print(result)
result = add_mul("world", 1, 2, 3, 4, 5)
print(result)

# 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name="foo", age=3)

# 함수의 결괏값은 언제나 하나
def add_and_mul(e, f):
    return e + f, e * f


result = add_and_mul(3, 4)
print(result)

# return의 또 다른 쓰임새
def say_nick(zzz):
    if zzz == "바보":
        return
    print("나의 별명은 %s 입니다." % zzz)


# 매개변수에 초깃값 미리 설정
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("양보아", 19)
say_myself("양보아", 19, False)

# 함수 안에서 선언한 변수의 효력 범위
g = 1


def vatest(g):
    g += 1


vatest(g)
print(g)

# 함수 안에서 함수 밖의 변수를 변경

# return 사용
g = 1


def vatest(g):
    g += 1
    return g


vatest(g)
print(g)

# 2. global 명령어 사용
g = 1


def vatest():
    global g
    g += 1


vatest()
print(g)

# lambda
add = lambda h, i: h + i
result = add(6, 2)
print(result)


def add(h, i):
    return h + i


result = add(6, 2)
print(result)
