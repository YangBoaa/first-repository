# 딕셔너리 쌍 추가, 삭제하기

# 딕셔너리 쌍 추가하기
a = {1: "a"}
a[2] = "b"
print(a)

a["name"] = "pey"
print(a)

a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# 딕셔너리에서 Key 사용해 Value 얻기
date = {"month": 8, "day": 25}
print(date["month"])
print(date["day"])

b = {1: "a", "b": 2}
print(b[1])
print(b["b"])

dic = {"name": "pey", "phone": "01099460778", "birth": "0126"}
print(dic["name"])
print(dic["phone"])
print(dic["birth"])

# Key 리스트 만들기(keys)
dic = {"name": "pey", "phone": "01099460778", "birth": "0126"}
print(dic.keys())

for i in dic.keys():
    print(i)

print(list(dic.keys()))

# Value 리스트 만들기(values)
print(dic.values())

# Key, Value 쌍 얻기(items)
print(dic.items())

# Key: Value 쌍 모두 지우기(clear)
dic.clear()
print(dic)

# Key로 Value얻기(get)
dic = {"name": "pey", "phone": "01099460778", "birth": "0126"}
print(dic.get("name"))
print(dic.get("birth"))

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
dic = {"name": "pey", "phone": "01099460778", "birth": "0126"}
print("phone" in dic)
print("email" in dic)

