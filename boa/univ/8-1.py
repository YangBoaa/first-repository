s = "abcde"
s_list = list(s)  # reverse 함수를 사용하기 위해 문자열을 list로 치환
s_list.reverse()  # reverse 함수를 사용해 문자열 리스트를 거꾸로 뒤집음

print("".join(s_list))
print(" ".join(s_list))
print("!".join(s_list))
