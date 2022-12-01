import sys
input = sys.stdin.readline

cube = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

n, m ,x, y, k = map(int,input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().rstrip().split())))
#1 = e 2 = w 3 = n 4 = s
# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

move = list(map(int,input().rstrip().split(" ")))
print(move)

cube[1][1] = maps[x][y]

for i in move:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        nx = nx - dx[i - 1]
        ny = ny - dy[i - 1]
        continue
    else:
        if i == 1:
            tmp1, tmp2 = cube[1][0], cube[3][1]
            cube[1][0] = cube[1][1]
            cube[1][1] = cube[1][2]
            cube[1][2] = tmp2
            cube[3][1] = tmp1
        elif i == 2:
            tmp1, tmp2 = cube[1][2], cube[3][1]
            cube[1][2] = cube[1][1]
            cube[1][1] = cube[1][0]
            cube[1][0] = tmp2
            cube[3][1] = tmp1
        elif i == 3:
            tmp1 = cube[3][1]
            cube[3][1] = cube[2][1]
            cube[2][1] = cube[1][1]
            cube[1][1] = cube[0][1]
            cube[0][1] = tmp1
        else:
            tmp1 = cube[0][1]
            cube[0][1] = cube[1][1]
            cube[1][1] = cube[2][1]
            cube[2][1] = cube[3][1]
            cube[3][1] = tmp1

        if maps[nx][ny] == 0:
            maps[nx][ny] = cube[1][1]
        else:
            cube[1][1] = maps[nx][ny]
            maps[nx][ny] = 0
        x, y = nx, ny
        print(cube[3][1])




#############################
#  import sys
# from collections import deque
# input = sys.stdin.readline

# n, m ,x, y, k = map(int,input().split())

# maps = []
# for _ in range(n):
#     maps.append(list(map(int, input().rstrip().split())))
# #1 = e 2 = w 3 = n 4 = s
# # 동 서 남 북
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# q  = deque()
# q.append(0)
# q.append(maps[x][y])
# move = list(map(int,input().rstrip().split(" ")))
# print(move)

# for i in move:
#     nx = x + dx[i - 1]
#     ny = y + dy[i - 1]

#     if nx < 0 or ny < 0 or nx >= n or ny >= m:
#         nx = nx - dx[i - 1]
#         ny = ny - dy[i - 1]
#         continue
#     else:
#         q.append(maps[nx][ny])
#         result = q.popleft()
#         x, y = nx, ny
#     print(result)




# cnt = 0
# while len(move):
#     cnt += 1 # 이동갯수를 count하려고
#     nx = x + dx[move]
#     ny = y + dy[move]

#     if nx < 0 or ny < 0 or nx >= n or ny >= m:
#         nx = nx - dx[move]
#         ny = ny - dy[move]
#         continue
#     else:
#         q.append(maps[nx][ny])
#         result = q.popleft()

#     print(result)
#     if cnt == k:
#         break
    
