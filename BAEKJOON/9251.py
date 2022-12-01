import sys
input = sys.stdin.readline

str1 = list(map(str, input().rstrip()))
str2 = list(map(str, input().rstrip()))

result = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            result[i][j] = result[i - 1][j - 1] + 1
        else:
            result[i][j] = max(result[i - 1][j], result[i][j - 1])

print(result[-1][-1])



# result = []
# for i in range(len(str1)):
#     point1 = i
#     point2 = 0
#     tmp = 0
#     while True:
#         if point1 == len(str1):
#             break

#         if str1[point1] == str2[point2]:
#             tmp += 1
#             point1 += 1
#             point2 += 1
#             if point2 == len(str2):
#                 point2 = len(str2) - 1
            
#             if point1 == len(str1):
#                 break
#         elif str1[point1] != str2[point2]:
#             point2 += 1
#             if point2 == len(str2):
#                 point1 += 1
#                 point2 = len(str2) - 1
            
    
#     result.append(tmp)
# print(result)            
# print(max(result))

