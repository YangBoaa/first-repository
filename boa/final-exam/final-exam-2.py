# 숫자 abcd...에 대해  abcd...= an + bn + cn + dn + ...(n은 자리수)가 성립하는 수가 존재합니다.
# 예를들어, 153 = 1*1*1 + 5*5*5 + 3*3*3 가 성립한다.
# 1000부터 9999까지 이러한 공식이 성립하는 수를 찾아내고, 찾아낸 숫자는 print문을 통해 출력하는 프로그램을 작성하시오.


def apple(abcd):
    abcd_list = list(str(abcd))
    length = len(str(abcd))
    result = 0

    for i in abcd_list:
        result += int(i) ** length

    return result


for i in range(1000, 10000):
    if apple(i) == i:
        print(i)
