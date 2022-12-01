import sys
input = sys.stdin.readline

n, k = map(int,input().split())

level = []
for _ in range(n):
    level.append(int(input()))
level.sort()

start, end = level[0], level[-1] + k
result = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in level:
        if mid < i:
            continue
        cnt += mid - i

    if cnt > k:
        end = mid - 1
    elif cnt <= k:
        result = mid
        start = mid + 1

print(result)
