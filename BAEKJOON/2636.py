import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int,input().split())
cheeze = []
for _ in range(n):
    cheeze.append(list(map(int,input().rstrip().split())))

def bfs1(x, y, cheeze_out):
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

arr = []
arr.append(sum(map(sum, cheeze))) # 처음에 아무것도 안했을때 치즈의 합
cnt = 0
while True:
    cheeze_out = [[(1) for i in range(m)] for i in range(n)]
    bfs1(0,0, cheeze_out) # 제일 밖에 있는 치즈 알기위한 bfs   
    
    for i in range(n):
        for j in range(m):
            if cheeze_out[i][j] == 1:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if cheeze_out[ni][nj] == 0:
                        cheeze[i][j] = 0 
                        continue

    cnt += 1   
    result = sum(map(sum, cheeze))
    arr.append(result) 
    if result == 0:
        break      
    
print(cnt)

print(arr[-2])

                    