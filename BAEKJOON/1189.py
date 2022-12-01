r, c ,k = map(int,input().split())
load = [list(str(input())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

result, cnt = 0, 0
dx, dy = [-1 ,0, 1, 0], [0, -1, 0, 1]

def dfs(x, y, cnt):
    global result
    if x == 0 and y == c - 1 and visited[x][y] == 0:
        if cnt + 1 == k:
            result += 1
            return
    for i in range(4):
        if x < 0 or x >= r or y < 0 or y >= c:
            continue
        if visited[x][y] == 0:
            visited[x][y] = cnt + 1
            dfs(x + dx[i], y + dy[i], cnt + 1)
            visited[x][y] = 0

for i in range(len(load)):
    for j in range(len(load[0])):
        if load[i][j] == 'T':
            visited[i][j] = -1

dfs(r - 1, 0, cnt)
print(result)