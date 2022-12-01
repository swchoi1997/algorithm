# import sys
# from itertools import permutations

# num = list(map(int, input().rstrip()))

# num.sort(reverse=True)

# if 0 not in num:
#     print(-1)
#     exit()

# else:
#     num.pop()

# a = list(permutations(num, len(num)))

# for i in a:
#     result = 0
#     for j in range(len(i)):
#         result += i[j] * (10 ** (len(i) - j)) 
    
#     if result % 30 == 0:
#         print(result)
#         exit()
#     else:
#         continue

# print(-1)

import sys
num = list(map(int, input().rstrip()))
num.sort(reverse=True)
if 0 not in num:
    print(-1)
    exit()
else:
    num.pop()
if sum(num) % 3 != 0:
    print(-1)
    exit()
else:
    result = ''.join(map(str, num)) + '0'
    print(result)

