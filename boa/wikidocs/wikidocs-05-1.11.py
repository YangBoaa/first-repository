#곱하기,빼기,나누기 기능
class FourCal:
    def setdate(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first+self.second
        return result
     def mul(self):
        result=self.first*self.second
        return result
     def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

j=FourCal()
k=FourCal()
j.setdate(5,2)
k.setdate(3,8)

j.add()
j.mul()
j.div()
k.add()
k.mul()
k.div()

