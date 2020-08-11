import json  # import json module
import re
import operator
import requests

url = "https://schoolmenukr.ml/api/high/B100000593?year=2018&month=5"
response = requests.get(url)
# with문과 json모듈을 이용하면 dictionary로 쉽게 사용 가능

json_data = json.loads(response.text)  # json 파일을 읽어서 파싱하고 사용
menu_list = json_data["menu"]


lunch_list = []
for i in range(0, len(menu_list)):  # for문으로 0부터 menu_list의 길이 만큼 돌림
    rule = re.compile("[가-힣]+")  # 한글 추출
    result = rule.findall(str(menu_list[i]))  # 문자열의 단어를 정규식과 매치하여 리스트로 돌려줌
    result1 = ",".join(result).split(",")
    lunch_list.append(result)  # 리스트의 result 추가

lunch_list = list(filter(None, lunch_list))  # None를 걸러주는 코드
print(lunch_list)
final_lunch_list = []
for a in lunch_list:  # lunch_list가 a 변수에 대입
    for b in a:  # a가 b변수에 대입
        final_lunch_list.append(b)  # 새로운 리스트에 추가


count = {}  # 개수 세기
for v in final_lunch_list:  # final_lunch_list가 v 변수에 대입
    try:
        count[v] += 1
    except:
        count[v] = 1

# final_lunch_list의 중복된 개수대로 1씩 증가


sdict = sorted(
    count.items(), key=lambda y: y[1], reverse=True
)  # count를 순서대로 정렬하고 내림차순으로 리스트를 뒤집는다)

for a in range(0, 3):
    print(f"{a+1}등: {sdict[a][0]}, {sdict[a][1]}번")  # for문을 사용하여 a로 등수와 sdict의 리스트로 추출

