# n = input()
# num = list(n)

# if int(n) <= 9:
#     if int(n) % 2 == 0:
#         print(int(n) // 2)
#     else:
#         print(0)

# elif int(n) >= 10 and int(n) <= 18:
#     for i in range(int(n) - 9, int(n) + 1):
#         result1, result2 = i, i
#         num1 = list(str(i))
#         for j in num1:
#             result1 += int(j)

#         if result1 == int(n):
#             print(result2)
#             break
        
#         if i == int(n):
#             print(0)

# else:
#     for i in range(int(n)-(len(num) * 9), int(n) + 1):
#         result1, result2 = i, i
#         num1 = list(str(i))
#         for j in num1:
#             result1 += int(j)
        
#         if result1 == int(n):
#             print(result2)
#             break
        
#         if i == int(n):
#             print(0)

# 위 코드를 이렇게 줄임 형주 ㄱㅅ
n = input()
num = list(n)

cnt = int(n)-(len(num) * 9)
if cnt < 0:
    cnt = 0

for i in range(cnt, int(n) + 1):
    result1 = i
    num1 = list(str(i))
    for j in num1:
        result1 += int(j)
    
    if result1 == int(n):
        print(i)
        break
       
    if i == int(n):
        print(0)
