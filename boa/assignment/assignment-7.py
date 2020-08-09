import json  # import json module
import re
import operator

# with statement
with open("boa/assignment/menu.json", encoding="utf8") as json_file:
    json_data = json.load(json_file)

    menu_list = json_data["menu"]

    list1 = []

    for i in range(0, len(menu_list)):
        Word1 = re.compile("[가-힣]+")
        result = Word1.findall(str(menu_list[i]))
        list1.append(result)
    list1 = list(filter(None, list1))

    listt = []
    for a in list1:
        for b in a:
            listt.append(b)

    count = {}
    for v in listt:
        try:
            count[v] += 1
        except:
            count[v] = 1

    sdict = sorted(count.items(), key=lambda y: y[1], reverse=True)
    print(sdict)

    for a in range(0, 5):
        print(f"{a+1}등: {sdict[a][0]},{sdict[a][1]}번")

