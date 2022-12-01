import sys
input = sys.stdin.readline

n , m = map(int,input().split())
s = [str(input().rstrip()) for _ in range(n)]
val = [str(input().rstrip()) for _ in range(m)]

result = 0
for i in val:
    if i in s:
        result += 1

print(result)