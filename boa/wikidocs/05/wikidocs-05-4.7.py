# 오류 일부러 발생시키기
class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()
