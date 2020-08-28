class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def minus(self, val):
        self.value -= val


cal = Calculator()
cal.add(10)
cal.minus(7)

print(cal.value)
