import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())

city = []
for _ in range(n):
    city.append(list(map(int,input().rstrip().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k, visited):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if city[nx][ny] <= k:
                continue
            
            if city[nx][ny] > k and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))        
result = 0

for k in range(max(map(max, city)) + 1):    
    visited = [[0] * n for j in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] > k and visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1     
                bfs(i,j, k ,visited)
            else:
                continue
    result = max(cnt, result)


print(result)

# 5
# 10 12 14 31 2
# 23 34 54 2 32
# 3 20 39 34 23
# 8 23 32 14 43
# 7 63 84 3 2