import os, glob
import os.path

a = r"C:\workspace\first-repository\boa\wikidos\Q\5"
files = os.listdir(a)
condition = "*.py"
csvfiles = glob.glob(condition)
print(csvfiles)
