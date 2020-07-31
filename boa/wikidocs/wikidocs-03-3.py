# 전형적인 for문
a = ["1", "2", "3"]
for i in a:
    print(i)

# 다양한 for문의 사용
b = [(1, 2), (3, 4), (5, 6)]
for (first, last) in b:
    print(first + last)

# for문의 응용
marks = [82, 79, 65, 54, 90]
number = 0
for mark in marks:
    number += 1
    if mark >= 70:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue
marks = [82, 79, 65, 54, 90]
number = 0
for mark in marks:
    number += 1
    if mark < 70:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for문과 함께 자주 사용하는 range 함수
x = range(10)
print(x)

# range 함수의 예시 살펴보기
y = 0
for i in range(1, 11):
    y += i
    print(y)

marks = [82, 79, 65, 54, 90]
for number in range(len(marks)):
    if marks[number] < 70:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 이용한 구구단
for a in range(2, 10):
    for b in range(1, 10):
        print(a * b, end=" ")
    print("")

# 리스트 내포 사용하기
c = [1, 2, 3, 4]
result = [num * 2 for num in c]
print(result)

c = [1, 2, 3, 4]
result = [num * 2 for num in c if num % 2 == 0]
print(result)

result = [d * e for d in range(2, 10) for e in range(1, 10)]
print(result)
