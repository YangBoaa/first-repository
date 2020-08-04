# 탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

# 파일 읽어들이는 기능
f = open(src)
tab_content = f.read()
f.close()


# 문자열 변경 기능
space_content = tab_content.replace("!", "*")

f = open(dst, "w")
f.write(space_content)
f.close()
