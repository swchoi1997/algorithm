from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
maps = [i for i in range(101)]
check = [0] * 101
for i in range(n + m):
    a, b = map(int,input().split())
    maps[a] = b

q = deque()
q.append(1)
while q:
    x = q.popleft()
    curr = maps[x]
    for i in range(1, 7):
        nx = curr + i

        if nx > 100:
            break

        if check[nx] == 0:
            check[nx] = check[x] + 1
            q.append(nx)

print(check)
