from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

n,m = map(int,input().split())

stage = []
for _ in range(n):
    stage.append(list(map(int,input())))

def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    while q:
        x ,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
               continue
            if stage[nx][ny] == 0:
                continue
            if stage[nx][ny] == 1:
                stage[nx][ny] = stage[x][y] + 1
                q.append((nx,ny))

bfs(0,0)

print(stage[n-1][m-1])
    