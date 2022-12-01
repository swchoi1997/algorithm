# import sys
# sys.setrecursionlimit(9999999)

# while True:
#     w, h = map(int,input().split())
#     if w == 0 and h == 0:
#         exit()

#     stage = []
#     for _ in range(h):
#         stage.append(list(map(int, input().split())))
    
    
#     def dfs(x, y):
#         if x <= -1 or x >= w or y <= -1 or y >= h:
#             return False
#         if stage[x][y] == 1:
#             stage[x][y] == 0

#             dfs(x - 1, y)
#             dfs(x + 1, y)
#             dfs(x, y - 1)
#             dfs(x, y + 1)
#             return True
#         return False

#     result = 0
#     for i in range(w):
#         for j in range(h):
#             if dfs(i, j) == True:
#                 result += 1
#     print(result)
 # ------- dfs 는 메모리초과 발생함 -----


from collections import deque
dx = [-1, 1, 0, 0, 1 ,1 ,-1 ,-1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                continue
            if stage[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = cnt
                q.append((nx,ny))


while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        exit()
    stage = []
    for _ in range(h):
        stage.append(list(map(int,input().split())))
    visited = [[0] * w for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if stage[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)   
                
    print(cnt)