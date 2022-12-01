import sys
input = sys.stdin.readline

s = list(map(str, input().rstrip()))
n = int(input())
result = 0
for _ in range(n):
    check = list(map(str, input().rstrip()))
    cnt = 0
    for i in range(10):
        if check[i] == s[0]:
            cnt += 1
            for j in range(1, len(s)):
                curr = i + j
                if curr >= 10: curr = curr % 10
                if check[curr] == s[j]: cnt += 1
    
    if cnt >= len(s):
        result += 1

print(result)                