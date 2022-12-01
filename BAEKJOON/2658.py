import sys
from collections import deque
input = sys.stdin.readline

#상하좌우
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

graph = [list(map(int,input().rstrip())) for _ in range(10)]
graph_sum = sum(list(map(sum, graph)))
if graph_sum < 3: # 1 이 두개잇으면 그냥 아무것도 아닌 직선임
    print(0)
    exit()

visited = [[0]* 10 for _ in range(10)]
gak = [] # 3 전용
gikgak = []
elsegak = []

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        gakcnt = 0
        for a in range(8):
            nx, ny = x + dx[a], y + dy[a]

            if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                continue
            if graph[nx][ny] == 1:
                gakcnt += 1

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
        if graph_sum == 3:
            if gakcnt == 2:
                gak.append((x, y))
        else:
            if gakcnt == 2:
                elsegak.append((x, y))            
            elif gakcnt == 3:
                gikgak.append((x, y))


cnt = 0 #삼각형이몇개있는지 확인하는 cnt
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            if cnt >= 2: # 삼각형이 2개 이상으로 판별될 경우 & 어떠한 도형이든 두개 있을경우
                print(0)
                exit()
            bfs(i,j)

print(gikgak, elsegak)
if graph_sum == 3:
    print(gak)
else:    
    if len(gikgak) > 1 or len(elsegak) > 2:
        print(0)
        exit()

# 0000000000
# 0000001000
# 0000011000
# 0000011000
# 0001111000
# 0000111000
# 0000011000
# 0000001000
# 0000000000
# 0000000000

# 0000000000
# 0000001000
# 0000011000
# 0000101000
# 0001111000
# 0000101000
# 0000011000
# 0000001000
# 0000000000
# 0000000000


# 0000000000
# 0000001000
# 0000011000
# 0000011000
# 0001111000
# 0000111000
# 0000011000
# 0000001000
# 0000000000
# 0000000000

# 0010000000
# 0011001000
# 0000011000
# 0000111000
# 0001111000
# 0000111000
# 0000011000
# 0000001000
# 0000000000
# 0000000000

# 0000000000
# 0001111100
# 0001111000
# 0001110000
# 0001100000
# 0001000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000

# 0000000000
# 0001111100
# 0001111100
# 0001111100
# 0001111100
# 0001111100
# 0000000000
# 0000000000
# 0000000000
# 0000000000

# 0000000000
# 0000001000
# 0000011000
# 0001100000
# 0001000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000

# 0000000000
# 0000001000
# 0000011000
# 0000000000
# 0000011000
# 0000001000
# 0000000000
# 0000000000
# 0000000000
# 0000000000


# 0000000000
# 0000001000
# 0000011000
# 0000111000
# 0001111000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000

# 0000000000
# 0000001000
# 0000011000
# 0000111000
# 0000011000
# 0000001000
# 0000000000
# 0000000000
# 0000000000
# 0000000000

# def bfs2(x, y):
#     q = deque()
#     q.append([x, y])
#     visited[x][y] = 1

#     while q:
#         x, y = q.popleft()
#         gakcnt = 0
#         for a in range(8):
#             nx, ny = x + dx[a], y + dy[a]

#             if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
#                 continue
#             if graph[nx][ny] == 1:
#                 gakcnt += 1

#             if graph[nx][ny] == 1 and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 q.append([nx, ny])
#         if gakcnt == 2:
#             gak.append((x, y))            
        



# cnt3 = 0
# if sum(graph) == 3:
#     for i in range(10):
#         for j in range(10):
#             if graph[i][j] == 1 and visited[i][j] == 0:
#                 cnt3 += 1
#                 if cnt3 >= 2: # 삼각형이 2개 이상으로 판별될 경우 & 어떠한 도형이든 두개 있을경우
#                     print(0)
#                     exit()
#                 bfs2(i,j)

#     print(gak)    
#     exit()