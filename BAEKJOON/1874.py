# import sys
# input = sys.stdin.readline

# n = int(input())
# arr= []
# for _ in range(n):
#     arr.append(int(input()))

# arr2 = []
# result = []
# num = 1
# for i in range(len(arr)):
#     if arr2: #arr2가 차 있을때
#         if arr[i] != arr2[-1]:
#             if arr2[-1] > arr[i]:
#                 print('NO')
#                 exit()
#             else:
#                 for j in range(num, arr[i] + 1):
#                     arr2.append(j)
#                     result.append('+')
#                     num += 1
#                 arr2.pop()
#                 result.append('-')

#         else:
#             arr2.pop()
#             result.append('-')
    
#     else: #arr2가 비어있으면
#         for j in range(num, arr[i] + 1):
#             arr2.append(j)
#             result.append('+')
#             num += 1
#         arr2.pop()
#         result.append('-')
# for i in result:
#     print(i)

# print(result)
##################################################################################################################
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr2 = []
result = []
num = 1
for i in range(len(arr)):
    if not arr2:
        for j in range(num, arr[i]+ 1):
            arr2.append(j)
            result.append('+')
            num += 1
        arr2.pop()
        result.append('-')
    else:
        if arr2[-1] == arr[i]:
            arr2.pop()
            result.append('-')
            
        else:
            if arr[i] > arr2[-1]:
                for j in range(num, arr[i] + 1):
                    arr2.append(j)
                    result.append('+')
                    num += 1
                arr2.pop()
                result.append('-')
            else:
                print('NO')
                exit()

for i in result:
    print(i)
