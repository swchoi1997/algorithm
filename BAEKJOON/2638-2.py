import sys
from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

n, m = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(n)]


#치즈 내부를 전부 1로 채워줌
def bfs1(x, y, cheeze, cheeze2):
    q = deque()
    q.append([x, y])
    cheeze2[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if cheeze2[nx][ny] == 1 and cheeze[nx][ny] == 0:
                cheeze2[nx][ny] = 0
                q.append([nx, ny])

def disappear_cheeze(x, y, cheeze1, cheeze2):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if cheeze2[nx][ny] == 0:
            cnt += 1
    
    if cnt >= 2:
        cheeze1[x][y] = 0

    return
    

_times = 0
while True:
    full_cheeze = [[1] * m for _ in range(n)]
    bfs1(0, 0, cheeze ,full_cheeze)
    
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                disappear_cheeze(i, j, cheeze, full_cheeze)

    _times += 1

    if sum(map(sum, cheeze)) == 0:
        print(_times)
        break