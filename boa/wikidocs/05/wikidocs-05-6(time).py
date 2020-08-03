# time

# time.time
import time

print(time.time())

# time.localtime
print(time.localtime(time.time()))

# time.asctime
print(time.asctime(time.localtime(time.time())))

# time.ctime
print(time.ctime())

# time.strftime
print(time.strftime("출력할 형식 포맷 코드", time.localtime(time.time())))

# timr.strftime
import time

print(time.strftime("%x", time.localtime(time.time())))

# time.sleep
import time

for i in range(10):
    print(i)
    time.sleep(1)
