import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int,input().split())
stage = []
for _ in range(r):
    stage.append(list(str(input().rstrip())))
result = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    global result
    q = set([(x, y, stage[x][y])])

    while q:
        x, y, cut = q.pop()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if stage[nx][ny] not in cut:
                next = cut + stage[nx][ny]
                q.add((nx, ny, next))
                result = max(result, len(next))
    return result

print(bfs(0,0))






# import sys
# input = sys.stdin.readline

# R, C = map(int,input().rstrip().split())

# stage = []
# for _ in range(R):
#     stage.append(list(str(input().rstrip())))
# result = 0
# cnt = 1
# visited = dict()
# dx = [-1, 1, 0, 0]
# dy = [0,0,-1,1]

# def dfs(x, y, cnt):
#     global result
#     result = max(cnt, result)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if nx < 0 or ny <0 or nx >= R or ny >= C:
#             continue
#         value = visited.get(stage[nx][ny])
#         if value == None: # 
#             visited[stage[nx][ny]] = 1
#             dfs(nx, ny, cnt + 1)
#             del visited[stage[nx][ny]]

        
# visited[stage[0][0]] = 1
# dfs(0,0,cnt)

# print(result)

#########################################

# import sys
# input = sys.stdin.readline

# R, C = map(int,input().rstrip().split())

# stage = []
# for _ in range(R):
#     stage.append(list(str(input().rstrip())))
# result = 0
# cnt = 1
# visited = dict()
# dx = [-1, 1, 0, 0]
# dy = [0,0,-1,1]

# def dfs(x, y, cnt):
#     global result
#     result = max(cnt, result)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         value = visited.get(stage[nx][ny])
#         if nx < 0 or ny <0 or nx >= R or ny >= C:
#             continue
#         if stage[nx][ny] not in visited: # 여기서 0(n)시간이 걸림
#             visited[stage[nx][ny]] = 1
#             dfs(nx, ny, cnt + 1)
#             del visited[stage[nx][ny]]

        
# visited[stage[0][0]] = 1
# dfs(0,0,cnt)

# print(result)