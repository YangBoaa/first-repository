# 06-4, 06-5 문제 중 4줄에서 오류가 뜨는 이유


# 간단한 메모장 만들기
import sys

option = sys.argv[1]

if option == "-a":
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write("\n")
    f.close()
elif option == "-v":
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)

# 탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)

f = open(dst, "w")
f.write(space_content)
f.close()
