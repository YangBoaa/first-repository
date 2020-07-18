while 1:
    print("두개의 숫자를 입력하세요: ")
    num1 = float(input(""))
    num2 = float(input(""))

    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2

    print("원하는 연산의 숫자를 입력하세요: \n")
    print("1 = +, 2 = -, 3 = *, 4 = /")

    a = int(input(""))

    if a == 1:
        print(result1)
    else:
        if a == 2:
            print(result2)
        else:
            if a == 3:
                print(result3)
            else:
                if a == 4:
                    print(result4)
                else:
                    print("다시 입력해주세요")

