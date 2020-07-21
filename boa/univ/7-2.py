x = {
    "커피": "빵",
    "돈가스": "냉모밀",
}

while True:
    y = input(str(list(x.keys())) + "중 좋아하는 음식은?")

    if y == "커피":
        print(x.get("커피"))
    elif y == "돈가스":
        print(x.get("돈가스"))
    elif y == "끝":
        break
