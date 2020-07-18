while True:
    num1 = int(input("계산할 첫 번째 수를 입력하세요 : "))

    if str(num1) == "0":
        break

    num2 = int(input("계산할 두 번째 수를 입력하세요 : "))

    a = input("계산할 연산자를 입력하세요 : ")
    if a == "+":
        print(num1 + num2)
    elif a == "-":
        print(num1 - num2)
    elif a == "*":
        print(num1 * num2)
    elif a == "/":
        print(num1 / num2)
