import json  # import json module
import re
import operator

# with문과 json모듈을 이용하면 dictionary로 쉽게 사용 가능

# with statement
with open(
    "boa/assignment/menu.json", encoding="utf8"
) as json_file:  # 파일을 열고 한글을 위해 utf8로 변환

    json_data = json.load(json_file)  # json 파일을 읽어서 파싱하고 사용
    menu_list = json_data["menu"]

    print("=" * 50)
    print(menu_list)

    list1 = []
    for i in range(0, len(menu_list)):  # for문으로 0부터 menu_list의 길이 만큼 돌림
        Word1 = re.compile("[가-힣]+")  # 한글 추출
        result = Word1.findall(str(menu_list[i]))  # 문자열의 단어를 정규식과 매치하여 리스트로 돌려줌
        list1.append(result)  # 리스트의 result 추가

    print("=" * 50)
    print(list1)

    list1 = list(filter(None, list1))  # None를 걸러주는 코드

    print("=" * 50)
    print(list1)

    listt = []
    for a in list1:  # list1가 a 변수에 대입
        for b in a:  # a가 b변수에 대입
            listt.append(b)  # 새로운 리스트에 추가

    print("=" * 50)
    print(listt)

    count = {}  # 개수 세기
    for v in listt:  # listt가 v 변수에 대입
        try:
            count[v] += 1
        except:
            count[v] = 1

    # listt의 중복된 개수대로 1씩 증가
    print("=" * 50)
    print(count)

    sdict = sorted(
        count.items(), key=lambda y: y[1], reverse=True
    )  # count를 순서대로 정렬하고 내림차순으로 리스트를 뒤집는다

    print("=" * 50)
    print(sdict)
    print("=" * 50)

    for a in range(0, 3):
        print(
            f"{a+1}등: {sdict[a][0]}, {sdict[a][1]}번"
        )  # for문을 사용하여 a로 등수와 sdict의 리스트로 추출

