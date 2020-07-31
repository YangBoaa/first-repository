x = {
    "떡볶이": "튀김",
    "짜장면": "단무지",
    "라면": "김치",
    "피자": "피클",
    "맥주": "꼬치",
    "치킨": "치킨무",
    "삼겹살": "마늘",
}
while True:
    y = input(str(list(x.keys())) + "중 좋아하는 음식은?")

    if y == "떡볶이":
        print(x.get("떡볶이"))

    elif y == "짜장면":
        print(x.get("짜장면"))

    elif y == "라면":
        print(x.get("라면"))

    elif y == "피자":
        print(x.get("피자"))

    elif y == "맥주":
        print(x.get("맥주"))

    elif y == "치킨":
        print(x.get("치킨"))

    elif y == "삼겹살":
        print(x.get("삼겹살"))

    elif y == "끝":
        break

    else:
        print("그런 음식이 없습니다. 확인해 보세요.")

