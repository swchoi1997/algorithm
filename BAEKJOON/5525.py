import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
io = list(map(str, input().rstrip()))
        

#### 50 ####
pn = 'OI' * n
pn = list(pn)
result = 0
for i in range(len(io) - 2 * n):
    if io[i] == "I":
        cnt = 0
        for j in range(1, 2 * n + 1):
            if io[i + j] == pn[j-1]:
                cnt += 1
            else:
                break

        if cnt == 2 * n: result += 1
        else: continue

print(result)



#### 50 ####
# # IOIOIOI.... 을 list 로 만들어줌
# pn = 'IO' * n + 'I'
# pn = list(pn)

# # 확인해야하는 io길이와 pn 길이가 같다면 1아니면 0 이 나오기 때문에 
# if len(io) - len(pn) == 0:
#     cnt = 0
#     for i in range(len(pn)):
#         if io[i] == pn[i]:
#             cnt += 1
#     print(1) if cnt == len(io) else print(0)
# else:
#     result = 0
#     for i in range(len(io) - len(pn)):
#         if io[i] == 'I':
#             cnt = 0
#             for j in range(len(pn)):
#                 if io[i + j] == pn[j]: cnt += 1
#                 else: break
#             if cnt == len(pn):
#                 result += 1
#             else:
#                 continue

# print(result)