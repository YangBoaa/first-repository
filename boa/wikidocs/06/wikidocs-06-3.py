# 게시판 페이징하기
def getTotalPage(a, b):
    if a % b == 0:
        return a // b
    else:
        return a // b + 1


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
