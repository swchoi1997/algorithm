import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n, m = map(int,input().split())
stage = [list(map(int,input().split())) for _ in range(n)]

result1 = 0

def bfs(stage):
    global result1
    cntzero = 0
    virus_loc = deque()
    for i in range(n):
        for j in range(m):
            if stage[i][j] == 0:
                cntzero += 1
            if stage[i][j] == 2:
                virus_loc.append([i, j])
    
    while virus_loc:
        x, y = virus_loc.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if stage[nx][ny] == 0:
                stage[nx][ny] = 2
                cntzero -= 1
                virus_loc.append([nx, ny])

    result1 = max(cntzero, result1)

def wall(cnt, x, y):
    if cnt == 3:
        virus_check_stage = [item[:] for item in stage]
        bfs(virus_check_stage)
        return
    else:
        if cnt == 0:
            for i in range(n):
                for j in range(m):
                    if stage[i][j] == 0:
                        stage[i][j] = 1
                        wall(cnt + 1, i, j)
                        stage[i][j] =0
        else:
            for i in range(n):
                for j in range(m):
                    if i < x:
                        continue
                    if i == x and j < y:
                        continue

                    if stage[i][j] == 0:
                        stage[i][j] = 1
                        wall(cnt + 1, i, j)
                        stage[i][j] =0

wall(0,0,0)

print(result1)