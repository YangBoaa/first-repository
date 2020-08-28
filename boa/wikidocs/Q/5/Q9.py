import sys

a = sys.argv[1:]
result = 0
for b in a:
    result += int(b)

print(result)
