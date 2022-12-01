import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n ,m = map(int,input().split())

cheeze = []
for _ in range(n):
    cheeze.append(list(map(int,input().rstrip().split())))


def bfs(x, y, cheeze_out): # 치즈를 꽉 채워줌
    q = deque()
    q.append((x, y))
    cheeze_out[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if cheeze[nx][ny] == 0 and cheeze_out[nx][ny] == 1:
                cheeze_out[nx][ny] = 0
                q.append((nx, ny))

cnt = 0
while True:
    cheeze_out = [[1 for _ in range(m)] for _ in range(n)]
    bfs(0,0, cheeze_out)
    # for i in cheeze:
    #     print(i)
    # print()
    for i in range(n):
        for j in range(m):
            if cheeze_out[i][j] == 1:
                cnt2 = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    
                    if cheeze_out[ni][nj] == 0:
                        cnt2 += 1
                if cnt2 >= 2:
                    cheeze[i][j] = 0
    cnt += 1
    if sum(map(sum, cheeze)) == 0:
        break
print(cnt)






