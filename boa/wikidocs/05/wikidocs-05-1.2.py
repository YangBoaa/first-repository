# 클래스
class calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


a = calculator()
b = calculator()
c = calculator()

print(a.add(2))
print(a.add(5))
print(b.add(2))
print(b.add(7))
print(c.sub(2))
print(c.sub(5))
