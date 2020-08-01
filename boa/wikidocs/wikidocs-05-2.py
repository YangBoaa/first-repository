# 모듈 만들기
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 모듈 불러오기
import mod1

print(mod1.add(2, 3))
print(mod1.sub(5, 2))

# if __name__ == "__main__": 의 의미
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


print(add(1, 4))
print(sub(5, 2))

