# 간단한 메모장 만들기
import sys

option = sys.argv[1]

if option == "-a":  # 메모장 내용 추가
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write("\n")
    f.close()
elif option == "-v":  # 메모장 내용 읽기
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)
