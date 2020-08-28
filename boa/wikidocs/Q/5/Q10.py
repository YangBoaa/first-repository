import os

a = os.getcwd()
os.chdir("c:/workspace")
result = os.popen("dir")
print(result.read())
