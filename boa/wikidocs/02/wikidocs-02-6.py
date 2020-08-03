# 집합 자료형
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

# 특징
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[1])

t1 = tuple(s1)
print(t1)
print(t1[1])


s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s3 & s4)
print(s3.intersection(s4))

# 합집합
print(s3 | s4)
print(s3.union(s4))

# 차집합
print(s3 - s4)
print(s4 - s3)
print(s3.difference(s4))
print(s4.difference(s3))

# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(1)
print(s1)
