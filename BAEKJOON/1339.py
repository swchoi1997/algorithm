# alpha = [0] * 26

# a = int(input())

# arr = [[] for i in range(10)]
# arr2 = []
# for _ in range(a):
#     a = list(input())
    
#     arr2.append(a)

#     lena = len(a) - 1

#     for i in range(len(a)):
#         arr[lena].append(a[i])
#         lena -= 1

# number = 9
# for i in reversed(arr):
#     if len(i) == 0:
#         continue
    
#     for j in range(len(i)):
#         num = ord(i[j]) - 65
#         if alpha[num] == 0:
#             alpha[num] = number
#             number -= 1
#         else:
#             continue


# result = 0
# for i in arr2:
#     strtoint = ''
#     for j in range(len(i)):
#         num = ord(i[j]) - 65
#         i[j] = str(alpha[num])
#         strtoint += i[j]
#     result += int(strtoint)

# print(result)



import sys 
input = sys.stdin.readline

alpha = [0] * 26

a = int(input().rstrip())


for _ in range(a):
    b = list(input().rstrip())
    
    for i in range(len(b)):
        alpha[ord(b[i]) - 65] += 10**(len(b) - (i + 1))

alpha.sort(reverse=True)

num = 9
result = 0 
for i in alpha:
    if i == 0:
        break
    result += i * num
    num -= 1
    

print(result)



   
