from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1] #상하좌우 대각
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(stage,i, j):
    visited = [[0] * m for i in range(n)]
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if stage[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

            if stage[nx][ny] == 1 and visited[nx][ny] == 0:
                return visited[x][y]


n, m = map(int,input().rstrip().split())


stage = []  
for _ in range(n):
    stage.append(list(map(int,input().rstrip().split())))


result = 0
for i in range(n):
    for j in range(m):
        if stage[i][j] == 0:
            a = bfs(stage, i, j)
            result = max(result, a)

print(result)
            


#처음에 다른 1에서 1사이 거리인줄알고 계속 오답을 나타냈음 그러나 그냥 각 자리에서 1까지 거리를 계산하면 됨