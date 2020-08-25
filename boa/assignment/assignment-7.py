# 학교 정보 선택

import json  # import json module
import re
import operator
import requests
import datetime

url = "https://schoolmenukr.ml/code/api/"

school = input("학교를 입력하세요: ")

if school in "초등학교":
    url += "elementary/"
elif school in "중학교":
    url += "middle/"
elif school in "고등학교":
    url += "higt/"
else:
    url += "special/"

response = requests.get(url)
school_infos = json.loads(response.text)
print(school_infos)

query = input("날짜를 입력하세요: ")
query = query.split("-")

if len(query) == 1:
    year = int(query[0])
    month = None
    date = None
elif len(query) == 2:
    year = int(query[0])
    month = int(query[1])
    date = None
elif len(query) == 3:
    year = int(query[0])
    month = int(query[1])
    date = int(query[2])
else:
    print("Error")
    raise Exception

print("알러지를 입력 받겠습니까?\n 1: 네  2: 아니요\n")
allergy = input()

if allergy == "1":
    url += "allergy=formed&"
elif allergy == "2":
    url += "allergy=hidden&"

if year is not None and month is not None and date is not None:
    url += f"year={year}&month={month}&date={date}"
elif month is not None and year is not None:
    url += f"year={year}&month={month}"
elif year is not None:
    url += f"year={year}"

print(url)

response = requests.get(url)

json_data = json.loads(response.text)  # json 파일을 읽어서 파싱하고 사용
menu_list = json_data["menu"]
print(menu_list)

daily_lunch_list = []
for i in range(0, len(menu_list)):  # for문으로 0부터 menu_list의 길이 만큼 돌림
    rule = re.compile("[가-힣]+")  # 한글 추출
    result = rule.findall(str(menu_list[i]))  # 문자열의 단어를 정규식과 매치하여 리스트로 돌려줌
    result1 = ",".join(result).split(",")
    daily_lunch_list.append(result)  # 리스트의 result 추가

daily_lunch_list = list(filter(None, daily_lunch_list))  # None를 걸러주는 코드

final_lunch_list = []
for lunch_list in daily_lunch_list:  # lunch_list가 lunch_list 변수에 대입
    for lunch in lunch_list:  # lunch_list가 b변수에 대입
        if lunch == "송파":
            pass
        else:
            final_lunch_list.append(lunch)  # 새로운 리스트에 추가

count = {}  # 개수 세기
for i in final_lunch_list:  # final_lunch_list가 i 변수에 대입
    try:
        count[i] += 1
    except:
        count[i] = 1

# final_lunch_list의 중복된 개수대로 1씩 증가
sdict = sorted(
    count.items(), key=lambda y: y[1], reverse=True
)  # count를 순서대로 정렬하고 내림차순으로 리스트를 뒤집는다)

for a in range(0, 3):
    print(f"{a+1}등: {sdict[a][0]}, {sdict[a][1]}번")  # for문을 사용하여 a로 등수와 sdict의 리스트로 추출
