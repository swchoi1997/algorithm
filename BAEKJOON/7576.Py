from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y, q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue
          
            if case[nx][ny] == 0:
                case[nx][ny] = case[x][y] + 1
                q.append((nx,ny))

    

n, m = map(int,input().split())
case =[list(map(int,input().split())) for _ in range(m)]

q = deque()
for i in range(m):
    for j in range(n):
        if case[i][j] == 1:
            q.append((i,j))
# 큐에 일단 1인 즉 익은 토마토를 다 넣은다음 bfs를 돌리면 익은쪽이 차례대로 하나하나 나오면서 돌아감
bfs(i, j, q)

result = 0
for i in case:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        else:
            result = max(result, j)

print(result - 1)