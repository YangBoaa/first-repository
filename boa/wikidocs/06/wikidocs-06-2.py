# 3과 5의 배수 합하기
a = 1
while a < 1000:
    print(a)
    a += 1

result = 0
for a in range(1, 1000):
    if a % 3 == 0 or a % 5 == 0:
        result += a
print(result)
