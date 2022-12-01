import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    a = int(input())
    if a == 0:
        num.pop()
    else:
        num.append(a)

result = 0
for i in num:
    result += i

print(result)