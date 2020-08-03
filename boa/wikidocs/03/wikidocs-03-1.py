# "돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다."
money = 2000
if money >= 3400:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 비교연산자
x = 7
y = 3
print(x > y)
print(x < y)
print(x == y)
print(x != y)

# x in s, x not in s
print(2 in [1, 2, 3])
print(2 not in [1, 2, 3])

print("d" in ("a", "b", "c"))
print("q" not in "python")

pocket = ["paper", "cellphone", "money"]
if pocket[2] in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]
pocket = ["paper", "cellphone", "money"]
if pocket[2] in pocket:
    pass
else:
    print("카드를 꺼내라")

# elif
pocket = ["money", "cellphone"]
card = True
if "money" in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

# 조건부 표현식
score = 40
if score >= 50:
    print("success")
else:
    print("failure")

