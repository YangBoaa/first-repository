class MaxLimitCalculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def q(self):
        if self.first + self.second == 110:
            print("!")
        else:
            return self.first + self.second


cal = MaxLimitCalculator()
cal.add(50)  # 50 더하기
cal.add(60)  # 60 더하기

print(cal.value)