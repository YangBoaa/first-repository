import requests

url = "https://schoolmenukr.ml/api/high/B100000593?year=2018&month=5"
response = requests.get(url)

date = input("날짜를 입력하세요: ")
year = date[:4]
month = date[5:7]
day = date[8:]
print(day)

if year == "":
    year = None
elif month == "":
    month = None
elif day == "":
    day = None

if year is not None and month is not None and day is not None:
    print("!")
elif month is not None and year is not None:
    print("!!")
elif year is not None:
    print("!!!")

text = f"year:{year} "
text += year
print(text)
