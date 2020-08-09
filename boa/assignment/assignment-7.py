import json  # import json module
import re

# with statement
with open("boa/assignment/menu.json", encoding="utf8") as json_file:
    json_data = json.load(json_file)

menu_list = json_data["menu"]

for i in range(0, len(menu_list)):

    # abc = json_data["menu"][0]["lunch"]
    Word1 = re.compile("[가-힣]+")
    result = Word1.findall(str(menu_list[i]))
    print(result)

list1=[]  
    list1.append(result)
