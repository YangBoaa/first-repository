money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = input("교환할 돈은 얼마?")

c500 = input("500원짜리 ==>", money)
c500 += int(money / 500)
money = money - c500 * 500

c100 = input("100원짜리 ==>", money)
c500 += int(money / 100)
money = money - c100 * 100

c50 = input("50원짜리 ==>", money)
c500 += int(money / 50)
money = money - c50 * 50

c10 = input("10원짜리 ==>", money)
c500 += int(money / 10)
money = money - c10 * 10

print("바꾸지 못한 잔돈 ==>")
