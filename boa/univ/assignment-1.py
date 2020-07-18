a = 100
b = 20
res = a + b

print(a, "+", b, "=", bin(res))
print(a, "+", b, "=", oct(res))
print(a, "+", b, "=", res)
print(a, "+", b, "=", hex(res))

res = a - b
print(a, "-", b, "=", bin(res))
print(a, "-", b, "=", oct(res))
print(a, "-", b, "=", res)
print(a, "-", b, "=", hex(res))

res = a * b
print(a, "*", b, "=", bin(res))
print(a, "*", b, "=", oct(res))
print(a, "*", b, "=", res)
print(a, "*", b, "=", hex(res))

res = int(a / b)
print(a, "/", b, "=", bin(res))
print(a, "/", b, "=", oct(res))
print(a, "/", b, "=", res)
print(a, "/", b, "=", hex(res))
