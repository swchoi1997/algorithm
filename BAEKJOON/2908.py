# a1, a2 = map(int, input().split())

# new_a1 = list(str(a1))
# new_a1.reverse()
# new_a2 = list(str(a2))
# new_a2.reverse()

# _a1, _a2 = '', ''
# for i in new_a1:
#     _a1 += i
# for j in new_a2:
#     _a2 += j

# print(max(int(_a1), int(_a2)))

a, b = input().split() # 처음부터 문자로 숫자를 입력받고
a = int(a[::-1])
b = int(b[::-1])
print(max(a, b))