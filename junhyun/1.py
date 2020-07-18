while True:
    print("두개의 숫자를 입력하세요: ")
    num1 = float(input(""))
    num2 = float(input(""))

    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2

    print("원하는 연산의 숫자를 입력하세요: \n")
    print("1 = +, 2 = -, 3 = *, 4 = /, 5 = 종료")

    a = int(input(""))

    if a == 1:
        print(result1)
    elif a == 2:
        print(result2)
    elif a == 3:
        print(result3)
    elif a == 4:
        print(result4)
    elif a == 5:
        break
    else:
        print("허용되지 않음")
        break
