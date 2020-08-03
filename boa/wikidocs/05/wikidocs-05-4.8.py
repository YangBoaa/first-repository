# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명입니다."
