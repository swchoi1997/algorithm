import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
rgb = [list(map(str,input().rstrip())) for _ in range(n)]
visited1 = [[0]* n for _ in range(n)]
visited2 = [[0]* n for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(visited1, color, x, y):
    q1 = deque()
    q1.append([x, y])
    visited1[x][y] = color
    while q1:
        x1, y1 = q1.popleft()
        for i in range(4):
            nx, ny = x1 + dx[i], y1 + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited1[nx][ny] == 0 and rgb[nx][ny] == color:
                visited1[nx][ny] = color
                q1.append([nx, ny])
            
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs(visited1,rgb[i][j], i, j)
            cnt1 += 1
for i in range(n):
    for j in range(n):
        if rgb[i][j] == 'G':
            rgb[i][j] = 'R'
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            bfs(visited2, rgb[i][j], i, j)
            cnt2 += 1

print(cnt1, cnt2)
        
