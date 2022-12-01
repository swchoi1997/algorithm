#브루트포스 문제로 풀기
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
city = []
for _ in range(n):
    city.append(list(map(int,input().rstrip().split())))

chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i + 1, j + 1])

#print(chicken)
chicken_m = list(combinations(chicken,m))
#print(chicken_m)

chicken_len =[0] * len(chicken_m)
for a in range(len(chicken_m)):
    dist = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                dist_min = 1e9
                for b in range(len(chicken_m[a])):
                    dist_min = min(dist_min, abs(chicken_m[a][b][0] - (i + 1)) + abs(chicken_m[a][b][1] - (j + 1)))
                    #print(i, j, dist_min)
                dist += dist_min
                #chicken_len[a].append(dist_min)
    chicken_len[a] = dist
print(min(chicken_len))





#########################################
#bfs로 돌리면 시간초과됨
# import sys
# from collections import deque
# input= sys.stdin.readline

# n, m = map(int,input().split())

# city = []
# for _ in range(n):
#     city.append(list(map(int,input().rstrip().split())))
# visited = [[-1] * n for i in range(n)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# def bfs(x, y):
#     result = []
#     q = deque()
#     q.append([x,y])
#     visited[x][y] = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if visited[nx][ny] == -1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append([nx, ny])
#                 if city[nx][ny] == 1:
#                     result.append(visited[nx][ny])

#     print(result)
#     return sum(result)


# result = []
# for i in range(len(city)):
#     for j in range(len(city[i])):
#         if city[i][j] == 2:
#            result.append(bfs(i, j)) 

# print(result)