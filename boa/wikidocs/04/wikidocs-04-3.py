# 파일 생성
a = open("d:/과외/새파일.txt", "w")
a.close()

# 파일을 쓰기 모드로 열어 출력값 적기
b = open("d:/과외/새파일.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    b.write(data)
b.close()

# readline() 함수 이용하기
x = open("d:/과외/새파일.txt", "r")
line = x.readline()
print(line)
x.close()

y = open("d:/과외/새파일.txt", "r")
while True:
    line = y.readline()
    if not line:
        break
    print(line)
y.close()

while 1:
    data = input()
    if not data:
        break
    print(data)

# readlines 함수 사용하기
abc = open("d:/과외/새파일.txt", "r")
lines = abc.readlines()
for line in lines:
    print(line)
abc.close()

# read 함수 사용하기
z = open("d:/과외/새파일.txt", "r")
data = z.read()
print(data)
z.close()

# 파일에 새로운 내용 추가
c = open("d:/과외/새파일.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    c.write(data)
c.close()

# with문과 함께 사용
d = open("foo.txt", "w")
d.write("Life is too short, you need python")
d.close()
with open("foo.txt", "w") as d:
    d.write("Life is too short, you need python")

# sys 모듈로 매개변수 주기
import sys

aaa = sys.argv[1:]
for i in aaa:
    print(i.upper(), end=" ")
