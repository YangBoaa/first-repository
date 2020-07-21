# 키보드를 통해 1에서 10 까지의 정수값을 입력하면, 이 값을 수신하여 랜덤함수를 통해 프로그램 내부에서 생성한 값과 비교를 수행한다.
# 이 때 입력한 값과 내부적으로 생성한 값이 모두 3이면 “ok”를 출력한 후 반복문을 탈출하여 프로그램을 종료합니다.
# 또한 내부에서 생성한 값이 5이면 비교를 수행하지 않고 “프로그램을 종료합니다.”를 출력한 후 반복문을 탈출하여 프로그램을 종료합니다.
# 위의 2가지 경우 이외에는 “다시 키보드로 입력을 해 주세요.”를 출력한 후 여러분이 키보드에 입력하는 것을 대기합니다. 이러한 설명에 부합하는 프로그램을 작성하세요.

import random

while True:
    num = input("input the number: ")
    rand_num = random.randrange(1, 11)
    print(f"system number: {rand_num}")
    print("=" * 25)

    if int(num) == rand_num == 3:
        print("Ok")
        break
    elif rand_num == 5:
        print("프로그램 종료")
        break
    else:
        print("다시 키보드로 입력")
        continue

