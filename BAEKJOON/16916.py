# from collections import deque
# import sys
# input = sys.stdin.readline

# string = deque(list(input().rstrip()))

# findstr = list((input().rstrip()))
# dictstr = {string : i for i,string in enumerate(findstr)}

# print(dictstr)
# cnt = 0
# while string:
#     a = string.popleft()
#     if len(string) < len(findstr):
#         print(0)
#         exit()
#     if a == findstr[0]:
#         cnt = 1
#         for i in range(len(findstr) - 1):
#             if string[i] == findstr[i + 1]:
#                 cnt += 1
#             else:
#                 break
            
        
#     if cnt == len(findstr):
#         print(1)
#         exit()

# print(0)


def kmp(string, findstr):
    m = len(string)
    n = len(findstr)

    check = [0] * n

    pattern(findstr, check)

    i, j = 0, 0

    while i < m:
        if string[i] == findstr[j]:
            i += 1
            j += 1
        elif string[i] != findstr[j]:
            if j != 0:
                j = check[j -1]
            else:
                i += 1

        if j == n:
            print("1")
            exit()
            #j = check[j-1]

    
    print('0')

def pattern(findstr, check):
    leng = 0
    i = 1

    while i < len(findstr):
        if findstr[i] == findstr[leng]:
            leng += 1
            check[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = check[leng - 1]
            else:
                check[i] = 0
                i += 1

import sys
input = sys.stdin.readline

string = list(input().rstrip())
findstr = list(input().rstrip())

kmp(string, findstr)