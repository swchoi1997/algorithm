# import sys

# input = sys.stdin.readline

# n = int(input().rstrip())
# array = list(map(int,input().rstrip().split()))

# result = array[0]

# for i in range(len(array)):
#     a = 0
#     for j in range(i, len(array)):
#         a += array[j]
        
#         result = max(result, a)

# print(result)
 # 시간초과


import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int,input().rstrip().split()))


for i in range(1, len(array)):
    array[i] = max(array[i], array[i-1] + array[i])

print(max(array))






