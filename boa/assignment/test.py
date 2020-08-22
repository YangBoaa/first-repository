date = input("날짜를 입력하세요: ")
year = None
month = None
day = None

print(date.split("-"))

if qurey == month is None and date is None:
    qurey = year
elif qurey == date is None:
    qurey = year + month

if month is not None and year is not None:
    print(year + month)
elif year is not None:
    print(year)
