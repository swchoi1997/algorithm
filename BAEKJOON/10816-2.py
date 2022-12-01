import sys
input = sys.stdin.readline

n = int(input())
num1 = list(map(int, input().split()))
m = int(input())
num2 = list(map(int, input().split()))

dict = {i : 0 for i in num2}

for i in num1:
    if i in dict:
        dict[i] += 1
    else:
        continue

for i in num2:
    print(dict[i], end = ' ')