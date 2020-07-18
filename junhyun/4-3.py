money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환할 돈은 얼마? "))

c500 = money // 500
money -= c500 * 500
c100 = money // 100
money -= c100 * 100
c50 = money // 50
money -= c50 * 50
c10 = money // 10
money -= c10 * 10

print(f"500원짜리 ==> {c500}개")
print(f"100원짜리 ==> {c100}개")
print(f"50원짜리 ==> {c50}개")
print(f"10원짜리 ==> {c10}개")
print(f"바꾸지 못한 잔돈 ==> {money}원")
