# import sys

# input = sys.stdin.readline

# str1 = input().rstrip()

# boomstr = input().rstrip()


# while True: 
#     if boomstr not in str1:
#         break
    
#     str1 = str1.replace(boomstr, '')

# if not str1:
#     print('FRULA')
# else:
#     print(str1)        

# ---------- 시간초과 ------------
# from collections import deque

# import sys

# input = sys.stdin.readline

# str1 = deque(input().rstrip())

# boomstr = list(input().rstrip())
# # boom = {a : i for i,a in enumerate(boomstr)}
# boom = {i : boomstr[i] for i in range(len(boomstr))}
# print(boom)

# str2 = []
# cnt = 0
# while str1:
#     a = str1.popleft()
    
#     if a == boomstr[cnt]:
#         cnt += 1
#     else:
#         if a == boomstr[0]:
#             cnt = 1
#         else:
#             cnt = 0

#     str2.append(a)

#     if len(boomstr) == cnt:
#         for i in range(len(boomstr)):
#             str2.pop()
#             cnt = 0

# print(str2)


import sys

input = sys.stdin.readline

str1 = input().rstrip()
boomstr = input().rstrip()

str2 = []
for i in str1:
    str2.append(i)
    if i == boomstr[-1] and len(str2) >= len(boomstr):
        if ''.join(str2[-len(boomstr):]) == boomstr:
            del str2[-len(boomstr):]

if not str2:
    print('FRULA')
else:
    for i in str2:
        print(i, end = '')




