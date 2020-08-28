import random

print("로또 번호 자동 생성기")
lotto = random.sample(range(1, 46), 6)
print(lotto)
