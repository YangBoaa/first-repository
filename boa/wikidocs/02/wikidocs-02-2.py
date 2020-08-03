# 따옴표로 양쪽 둘러싸기
print("Hello World")

# 따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 문자열에 작은따옴표 (') 포함시키기
print("'떡볶이'는 맛있다.")

# 문자열에 큰따옴표 (") 포함시키기
print('"떡볶이"는 맛있다.')

# 연속된 따옴표 3개(""") 사용하기
mul = """
    Life is too short
    You need python
    """
print(mul)

# 이스케이프 코드
mul1 = "Life is\t too short \nYou need python"
print(mul1)

# 문자열 더해서 연결하기(Concatenation)
head = "Hello"
tail = "world"
print(head + tail)

# 문자열 곱하기
print(head * 2)
# 문자열 곱하기 응용
print("=" * 50)
print("My Progam")
print("=" * 50)

# 문자열 길이 구하기
a = "Hello world"
b = a[0] + a[1] + a[2] + a[3]
print(len(a))

# 문자열 인덱싱과 슬라이싱
print(a[7])

print(b)
print(a[0:4])

print(a[8:])
print(a[:10])
print(a[:])
print(a[5:11])

# 슬라이싱으로 문자열 나누기
x = "20010331Rainy"
year = x[:4]
day = x[4:8]
weather = x[8:]
print(year)
print(day)
print(weather)

# 문자열 바꾸기
abc = "pithon"
print(abc[:1])
print(abc[2:])
print(abc[:1] + "y" + abc[2:])

# 문자열 포매팅
print("%d시간이나 늦었어." % 2)
print("%s시간이나 늦었어." % "두")

number = 5
day1 = "삼"
print("팔월 %s일 오후 %d시로 정하자." % (day1, number))

print("Error is %d%%." % 74)

# 포맷 코드와 숫자 함께 사용하기
print("%10s" % "hi")
print("%-10sboa." % "hi")
print("%0.5f" % 3.42134234)
print("%10.5f" % 3.42134234)

# format 함수를 사용한 포매팅

print("{0}시간이나 늦었어.".format(2))
print("{0}시간이나 늦었어.".format("두"))

number1 = 5
day2 = "삼"
print("팔월 {0}일 오후 {1}시로 정하자.".format(day2, number1))

print("8월 {day2}일 오후 {number1}로 정하자.".format(day2=3, number1=5))

print("8월 {0}일 오후 {number1}시로 정하자.".format(3, number1=5))

print("{0:>7}".format("hi"))
print("{0:^7}".format("hi"))
print("{0:=^7}".format("hi"))
print("{0:!<7}".format("hi"))

aa = 3.42134234
print("{0:0.6f}".format(aa))
print("{0:10.6f}".format(aa))

print("{{ and }}".format())

# f 문자열 포매팅
d = {"name": "양보아", "age": 19}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]+1}입니다.')

print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

y = 3.42134234
print(f"{y:10.4f}")

print(f"{{ and }}")

# 문자열 관련 함수들

# 문자 개수 세기(count)
c = "habby"
print(c.count("b"))

# 위치 알려주기1(find)
z = "python is the best choice"
print(z.find("s"))
print(z.find("q"))

# 위치 알려주기2(index)
s = "Life is too short"
print(s.index("f"))

# 문자열 삽입(join)
print(",".join(["1", "2", "3", "4"]))

# 소문자를 대문자로 바꾸기(upper)
q = "hi"
print(q.upper())

# 대문자를 소문자로 바꾸기(lower)
Q = "HI"
print(q.lower())

# 왼쪽 공백 지우기(lstrip)
q = " hi "
print(q.lstrip())

# 오른쪽 공백 지우기(rstrip)
q = " hi "
print(q.rstrip())

# 양쪽 공백 지우기(strip)
q = " hi "
print(q.strip())

# 문자열 바꾸기(replace)
s = "Life is too short"
print(s.replace("Life", "Your leg"))

# 문자열 나누기(split)
s = "Life is too short"
print(s.split())
ss = "a:b:c:d"
print(ss.split(":"))
