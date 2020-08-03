#os
import os
os.environ
environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})

#디렉터리 위치 변경하기 - os.chdir
os.chdir("c:\windows")

#디렉터리 위치 돌려받기 - os.getcwd
os.getcwd

#시스템 명령어 호출하기 - os.system
os.system("dir")

#실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
f = os.popen("dir")
print(f.read())
