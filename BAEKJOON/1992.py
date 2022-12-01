import sys
input = sys.stdin.readline

n = int(input().rstrip())
mov = []
for _ in range(n):
    mov.append(list(map(int,input().rstrip())))

def dq(x, y, n):
    first = mov[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if mov[i][j] != first:
                print('(', end = '')
                for a in range(2):
                    for b in range(2):
                        dq(x + n // 2 * a, y + n // 2 * b, n // 2)
                print(')', end = '')

                return
    
    if first == 1:
        print('1', end = '')
        return 
    elif first == 0:
        print('0', end = '')
        return

dq(0 ,0, n)











#     result = '' 
#     check = []
#     if n == 2:
#         check1 = []
#         for i in range(x, x + 2):
#             for j in range(y, y + 2):
#                 if mov[i][j] == 0:
#                     check1.append(0)
#                 else:
#                     check1.append(1)
#         # return check1
#         if sum(check1) == 0:
#             return 0
#         elif sum(check1) == 4:
#             return 1
#         else:
#             return check1
        
#     else:
#         check2 = []
#         # dq(x, y, n // 2)
#         # dq(x, y + n // 2, n // 2)
#         # dq(x + n // 2, y, n // 2)
#         # dq(x + n //2, y + n // 2, n // 2)
        

#         check2.append(dq(x, y, n // 2))
#         check2.append(dq(x, y + n // 2, n // 2))
#         check2.append(dq(x + n // 2, y , n // 2))
#         check2.append(dq(x + n // 2, y + n // 2, n // 2))

#         if sum(check2) == 0:
#             check.append(0)
#         elif sum(check2) == 1:
#             check.append(1)
#         else:
#             check.append(check2)
        

#     return check

# ccc = dq(0 ,0, n)
# print(ccc)

# for a in range(len(ccc)):
#     for b in range(len(ccc[a])):
#         for c in range(ccc[a][b]):
            

# 4
# 0 0 0 1
# 0 0 1 1
# 0 0 1 1
# 0 0 1 1

# 8
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 1 1
# 0 0 0 0 1 1 1 1
# 0 0 0 1 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1


# 16
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0