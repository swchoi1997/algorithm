from collections import deque

import sys
input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, l, r = map(int,input().split())
country = [list(map(int,input().split())) for _ in range(n)]
result = 0

def bfs(i, j):
    q = deque()
    move = []
    q.append((i, j))
    move.append((i, j))
    visited[i][j] = 1
    cnt, tmpSum = 1, country[i][j]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx ,ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny <n and visited[nx][ny] == 0: # 범위내에서 # 방문하지 않았고
                if l <= abs(country[x][y] - country[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    move.append((nx, ny))
                    q.append((nx, ny))
                    cnt += 1
                    tmpSum += country[nx][ny]

    changeValue = tmpSum // cnt
    if cnt >= 2:
        return changeValue, move, cnt
    return 0, [], cnt
    

while True:
    check = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            CV, move, cnt = bfs(i, j)
            if cnt >= 2:
                check.append([CV, move])
    
    if check:
        for i in check:
            for a, b, in i[1]:
                country[a][b] = i[0]
        result += 1
    else:
        break
    
print(result)

