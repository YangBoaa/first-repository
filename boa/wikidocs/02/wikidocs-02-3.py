# 리스트의 인덱싱
a = [1, 2, 3]
print(a[0] + a[2])
print(a[-1])

# 삼중 리스트에서 인덱싱
b = [1, 2, ["a", "b", ["Life", "is"]]]
print(b[2][2][0])

# 리스트의 슬라이싱
c = [1, 2, 3, 4, 5]
d = c[:2]
e = c[2:]
print(d)
print(e)

# 중첩된 리스트에서 슬라이싱
f = [1, 2, 3, ["a", "b", "c"], 4, 5]
print(f[2:5])
print(f[3][:2])

# 리스트 연산하기

# 리스트 더하기(+)
g = [1, 2, 3]
h = [4, 5, 6]
print(g + h)

# 리스트 반복하기(*)
print(g * 3)

# 리스트 길이 구하기
print(len(g))

print(str(g[2]) + "hi")

# 리스트의 수정과 삭제

# 리스트에서 값 수정하기
g = [1, 2, 3]
g[0] = 4
print(g)

# del 함수 사용해 리스트 요소 삭제하기
g = [1, 2, 3]
del g[2:]
print(g)

# 리스트에 요소 추가(append)
g = [1, 2, 3]
g.append(4)
g.append([5, 6])
print(g)

# 리스트 정렬(sort)
i = [1, 3, 4, 2]
i.sort()
print(i)

j = ["b", "c", "a"]
j.sort()
print(j)

# 리스트 뒤집기(reverse)
j = ["b", "c", "a"]
j.reverse()
print(j)

# 위치 반환(index)
g = [1, 2, 3]
print(g.index(2))
print(g.index(3))

# 리스트에 요소 삽입(insert)
g = [1, 2, 3]
g.insert(0, 4)
print(g)
g.insert(3, 5)
print(g)

# 리스트 요소 제거(remove)
k = [1, 2, 3, 1, 2, 3]
k.remove(2)
print(k)
k.remove(2)
print(k)

# 리스트 요소 끄집어내기(pop)
g = [1, 2, 3]
print(g.pop())
print(g)

# 리스트에 포함된 요소 x의 개수 세기(count)
l = [1, 2, 3, 3]
print(l.count(3))

# 리스트 확장(extend)
g = [1, 2, 3]
g.extend([4, 5])
print(g)
n = [6, 7]
g.extend(n)
print(g)
