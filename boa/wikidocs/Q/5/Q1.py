class Calculastor:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

    cal = UpgradeCalculator()
    cal.add(10)
    cal.minus(7)
    print(cal.sub())
