    
import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n ,m = map(int,input().split())
stage = [list(map(int,input().split())) for _ in range(n)]


def melting(x, y, next_stage):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if stage[nx][ny] == 0:
            cnt += 1

    if stage[x][y] <= cnt:
        next_stage[x][y] = 0
    else:
        next_stage[x][y] = stage[x][y] - cnt

def bfs(x, y, visited):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visited[nx][ny] == 0 and stage[nx][ny] != 0:
                visited[nx][ny] = 1
                q.append([nx,ny])

time = 0
while True:
    next_stage = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):    
            if stage[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j, visited)
                cnt += 1

    if cnt >= 2:
        print(time)
        break
    
    else:
        if sum(map(sum, stage)) == 0:
            print(0)
            break
        else:
            # 빙산 녹이기
            time += 1
            for i in range(n):  
                for j in range(m):
                    if stage[i][j] != 0:
                        melting(i, j, next_stage)
            stage = [x[:] for x in next_stage]