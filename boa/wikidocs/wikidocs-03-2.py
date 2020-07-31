# while문 만들기
food = """
1. 떡볶이
2. 치킨
3. 피자
4. 삼겹살

Enter number: """

number = 0
while number != 5:
    print(food)
    number = int(input())

# while문 강제로 빠져나가기
coffee = 5
money = 100
while money:
    print("커피가 나옵니다.")
    coffee = coffee - 1
    print("남은 커피는 %d잔 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요 : "))
    if money == 100:
        print("커피가 나옵니다.")
        coffee = coffee - 1
    elif money > 100:
        print("거스름돈 %d이고 커피가 나옵니다." % (money - 100))
        coffee = coffee - 1
    else:
        print("돈이 반환되고 커피가 나오지 않습니다.")
        print("남은 커피는 %d잔 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while문 맨 처음으로 돌아가기
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

# 무한루프
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
