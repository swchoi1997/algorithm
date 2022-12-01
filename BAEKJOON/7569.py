from collections import deque
import sys
input = sys.stdin.readline

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0,0,0,0,1,-1]

box = []
m,n,h = map(int,input().split())
for _ in range(h):
    tomato = [list(map(int,input().split())) for _ in range(n)]
    box.append(tomato)


def bfs(q):
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                q.append([nx, ny, nz])

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i,j,k])
bfs(q)


result = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
            result = max(result, k)

print(result - 1)


# from collections import deque
# import sys
# sys.setrecursionlimit(1000000)

# input = sys.stdin.readline

# dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
# INF = 10000000000

# m, n, h = map(int,input().split())

# box = []
# for j in range(h):
#     for _ in range(n):
#         tmpbox = list(map(int,input().split()))
#         tmpbox.append(j)
#         box.append(tmpbox)

# check = [[INF] * m for _ in range(n * h)]

# cnt =0
# def bfs(x, y, floor, cnt):

#     q = deque()
#     q.append([x, y, floor])
#     check[x][y] = cnt
#     while q:
#         x, y, floor = q.popleft()
        
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
            
#             if ny < 0 or ny >= m or nx < 0 or nx >= (n * h) or  box[nx][-1] != floor:
#                 continue
            
#             if box[nx][ny] == 0:
#                 if check[nx][ny] > check[x][y] + 1:
#                     check[nx][ny] = check[x][y] + 1
#                     q.append([nx, ny, floor])
                
#         if x - n >= 0 and box[x - n][y] == 0 and check[x - n][y] == INF:
#             bfs(x - n, y, box[x-n][-1], cnt + 1)
#         if x + n < (n*h) and box[x + n][y] == 0 and check[x + n][y] == INF:
#             bfs(x + n, y, box[x + n][-1], cnt + 1)
#     return

# for i in range(len(box)):
#     for j in range(len(box[i]) - 1):
#         if box[i][j] == 1 and check[i][j] == INF:
#             bfs(i, j, box[i][-1], 0)
#             check[i][j] = 1
#         if box[i][j] == -1:
#             check[i][j] = -1


# for i in check:
#     if INF in i:
#         print(-1)
#         exit()


# print(max(map(max, check)))


