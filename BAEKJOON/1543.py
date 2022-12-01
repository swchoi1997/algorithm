import sys
from collections import deque
input = sys.stdin.readline

docu = list(map(str, input().rstrip()))
check = list(map(str, input().rstrip()))

result = 0

i = 0 
while True:
    cnt = 0
    if docu[i] == check[0]:
        for j in range(len(check)):
            if i + j >= len(docu):
                print(result)
                exit()
            if docu[i + j] == check[j]:
                cnt += 1
        
    if cnt == len(check):
        i += cnt
        # print(i)
        result += 1
    else:
        i += 1
        # print(i)

    if i >= len(docu):
        print(result)
        exit()






# for i in range(len(docu)):
#     cnt = 0
#     if docu[i] == check[0]:
#         cnt = 0
#         for j in range(len(check)):
#             if docu[i + j] == check[j]:
#                 cnt += 1
            
#         if cnt == len(check):




