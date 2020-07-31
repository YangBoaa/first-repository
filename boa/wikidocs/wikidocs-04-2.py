# input 사용
number = input("숫자를 입력하세요 : ")
print(number)

# print 자세히 알기
a = 123
print(a)

a = "Python"
print(a)

a = [1, 2, 3]
print(a)

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("나는" "너무" "피곤 하다")
print("나는" + "너무" + "피곤 하다")

# 문자열 띄어쓰기는 콤마로 한다
print("나는", "너무", "피곤 하다")

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=" ")
