# 변수는 어떻게 만들까?
a = 1
b = "hi"
c = [1, 2, 3]

print(id(c))

# 리스트를 복사하고자 할 때
c = [1, 2, 3]
d = c
print(id(c))
print(id(d))

print(c is d)

# [:] 이용
c = [1, 2, 3]
e = c[:]
c[2] = 4
print(c)
print(e)

# copy 모듈 이용
from copy import copy

e = copy(c)
print(b is a)

# 변수를 만드는 여러가지 방법
x, y = ("python", "life")
[x, b] = ["python", "life"]
x = b = "python"

x = 10
y = 20
x, y = y, x
print(x)
print(y)
