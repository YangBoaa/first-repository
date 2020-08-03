# 더하기 기능 만들기
class FourCal:
    def setdate(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


i = FourCal()
i.setdate(5, 2)
print(i.add())
