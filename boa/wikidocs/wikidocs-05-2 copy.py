# if __name__ == "__main__": 의 의미
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == "__main__":
    print(add(1, 4))
    print(sub(5, 2))

# 클래스나 변수 등을 포함한 모듈
PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r ** 2)


def add(a, b):
    return a + b


a = mod2.Math()
print(a.solv(2))

