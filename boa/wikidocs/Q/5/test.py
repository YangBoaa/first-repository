class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def minus(self):
        result = self.first - self.second
        return result


cal = Calculator()
cal.setdata(10, 7)
print(cal.minus())
