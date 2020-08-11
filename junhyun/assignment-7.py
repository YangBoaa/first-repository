import json  # import json module
import re

with open("junhyun/menu.json", encoding="utf8") as json_file:
    json_data = json.load(json_file)
    data = json_data["menu"]

    lunch_list_raw = []

    for a in range(0, len(data)):
        lunch_list_raw.append(data[a]["lunch"])

    lunch_list_raw = list(filter(None, lunch_list_raw))
    print(lunch_list_raw)

    lunch_list = []

    for lunch in lunch_list_raw:
        for a in range(0, len(lunch)):
            lunch[a] = re.sub("[^a-zA-Zㄱ-힗]", "", lunch[a])
            lunch_list.append(lunch[a])
    print(lunch_list)

    count = {}

    for menu in lunch_list:
        try:
            count[menu] += 1
        except:
            count[menu] = 1

    rank = sorted(count.items(), key=lambda x: x[1], reverse=True)
    count = 1

    for menu in rank:
        if count == 6:
            break
        print(f"{count}등: {menu[0]}, {menu[1]}번")
        count += 1

