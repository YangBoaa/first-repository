# 학교 정보 선택

import json  # import json module
import re
import operator
import requests
import datetime

url = "https://schoolmenukr.ml/code/api?"

school = input("학교를 입력하세요: ")
url += f"q={school}"
response = requests.get(url)

school_data = json.loads(response.text)
school_code = school_data["school_infos"][0]["code"]

if "초등학교" in school:
    school_type = "elementary"
elif "중학교" in school:
    school_type = "middle"
elif "고등학교" in school:
    school_type = "high"
else:
    school_type = "special"

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
    allergy_code = "allergy=formed"
elif allergy == "2":
    allergy_code = "allergy=hidden"

url = f"https://schoolmenukr.ml/code/api?{school_type}/{school_code}/{allergy_code}&"

if year is not None and month is not None and date is not None:
    url += f"year={year}&month={month}&date={date}"
elif month is not None and year is not None:
    url += f"year={year}&month={month}"
elif year is not None:
    url += f"year={year}"

response = requests.get(url)

json_data = json.loads(response.text)  # json 파일을 읽어서 파싱하고 사용
print(json_data)
