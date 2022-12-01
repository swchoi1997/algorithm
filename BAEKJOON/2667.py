import sys
from collections import deque
input = sys.stdin.readline

dx,dy = [0, 0, 1, -1], [1, -1, 0, 0]

n = int(input())
graph = [(list(map(int,input().rstrip()))) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q. popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                cnt += 1

    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)