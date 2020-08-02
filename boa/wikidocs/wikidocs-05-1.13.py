# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


a = MoreFourCal(5, 2)
a.pow()
