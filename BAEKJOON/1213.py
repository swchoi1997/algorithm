import sys
input = sys.stdin.readline

str1 = list(map(str ,input().rstrip()))
str1.sort()

check = dict()
for i in str1:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1
a = 0
result1 = ''
result2 = ''
for i in check:
    if check[i] % 2 == 1:
        a += 1
        result2 += i
    result1 += i * (check[i] // 2)
    

if a >= 2:
    print("I'm Sorry Hansoo")

else:
    print(result1 + result2 + result1[::-1])
