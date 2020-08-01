# 클래스
result = 0


def add(num):
    global result
    result += num
    return result


print(add(2))
print(add(5))

result1 = 0
result2 = 0


def add1(num):
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2


print(add1(2))
print(add1(5))
print(add2(2))
print(add2(7))


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

# 클래스와 객체
class Cookie:
    pass


x = Cookie
y = Cookie

# 사칙연산 클래스
class FourCal:
    pass


d = FourCal()
print(type(d))

# 객체에 숫자 지정할 수 있게 만들기
class FourCal:
    def setdate(self, first, second):
        self.first = first
        self.second = second
        e = 0
        e.setdate(5, 2)


# setdata 메서드의 매개변수
abc = FourCal()
abc.setdate(5, 2)

# 메서드의 또 다른 호출
abc = FourCal()
FourCal.setdate(abc, 5, 2)

# setdata 메서드의 수행문
f = FourCal()
f.setdate(5, 2)
print(f.first)
print(f.second)


class FourCal:

g = FourCal()
h = FourCal()
g.setdata(5, 2)
h.setdata(3, 7)
id(g.first)
id(h.first)

class FourCal:

    def setdate(self, first, second):
        self.first = first
        self.second = second

#더하기 기능 만들기
class FourCal:
    def setdate(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first+self.second
        return result

i=FourCal()
i.setdate(5,2)
print(i.add())

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

#생성자(Constructor)
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdate(self,first,second):
        self.first=first
        self.second=second
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

n=FourCal
n.add()

#클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result
a=MoreFourCal(5,2)
a.pow()

#메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
a=SafeFourCal(4,0)
a.div

#클래스 변수
class Family:
    lastname="김"
print(Family.lastname)
id(Family.lastname)