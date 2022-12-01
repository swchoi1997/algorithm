from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n , m , k = map(int,input().split())
sq = [list(map(int,input().split())) for _ in range(k)]

stage = [[0] * m for _ in range(n)]

def bfs(x, y, lx, ly):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([y, x])
    stage[y][x] = 1
    visited[y][x] = 1
    while q:
        b, a = q.popleft()
        for i in range(4):
            nx, ny = b + dy[i], a + dx[i]

            if a <= ny < lx and b <= nx < ly and visited[nx][ny] != 1:
                if stage[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    visited[nx][ny] = 1
                    stage[nx][ny] = 1
                    q.append([nx, ny])
                
def bfs2(i, j):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    stage[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<= nx < n and 0 <= ny < m and visited[nx][ny] != 1:
                if stage[nx][ny] == 0:
                    q.append([nx, ny])
                    stage[nx][ny] = 1
                    visited[nx][ny] = 1
                    cnt += 1
    
    return cnt

for i in sq:
    bfs(i[0], i[1], i[2], i[3])

result = []
cnt = 0
for i in range(len(stage)):
    for j in range(len(stage[i])):
        if stage[i][j] == 0:
            cnt += 1
            result.append(bfs2(i, j))
result.sort()

print(cnt)
for i in result:
    print(i, end = ' ')
