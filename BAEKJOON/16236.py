import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1 ,1, 0]

# 물고기가 아기 상어의 크기보다 큰 곳이면 -1을 해 줬고 작은곳이면 그 크기 넣어주고 
# 물고기와 크기가 같거나 그냥 빈칸이면 0을 넣어줬음
def fish_check(stage, stage2, s): # 아기상어가 갈 수 있는 곳을 알아보기 위한 함수
    shark_x, shark_y = 0, 0 ## 아기상어의 현재 위치
    TF = False #갈수있는 곳이 있는지 없는지 판별하는 것

    for i in range(len(stage)):
        for j in range(len(stage)):
            if stage[i][j] == 9: # 아기 상어 위치
                shark_x, shark_y = i, j
            elif stage[i][j] <= 6 and stage[i][j] > s: #물고기가 상어보다 큰경우
                stage2[i][j] = -1
            elif stage[i][j] < s and stage[i][j] > 0: # 물고기가 상어보다 작아서 잡아 먹을 수 잇는 경우
                stage2[i][j] = stage[i][j]
                TF = True

    if TF == False: # 만약 갈 수 있는 곳이 없다면! 즉 잡아 먹을곳이 없다면!!
        return -1, -1
    else:
        return shark_x, shark_y

def bfs(stage, stage2, x, y, n, check):
    q = deque()
    q.append((x, y))
    stage[x][y], check[x][y], stage2[x][y] = 0, 0, 9
    cp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if stage2[nx][ny] >= 0 and stage2[nx][ny] <= 6 and check[nx][ny] == 0:
                if stage2[nx][ny] != 0: # 먹이를 만나면 어차피 자기보다 작은거만 표시를 해놔서 0이상이면 됨
                    check[nx][ny] = check[x][y] + 1
                    cp.append([nx, ny, check[nx][ny]])
                else:
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx, ny))

    if not cp: ## 이걸 해주지 않으면 cp가 비어있는 경우가 있기때문에 index error가 날 수 잇음
        return -1, -1
        # ex
        # 3
        # 0 0 0
        # 0 0 3
        # 9 3 1
    cp.sort(key = lambda x : (x[2], x[0], x[1]))
    return cp[0][0], cp[0][1]

################# 종료 조건 ###########3
def result(x, y, count_time):
    if x == -1 and y == -1:  #탈출조건
        if count_time == 0:
            print('0')
        else:
            print(count_time)
        exit()


n = int(input())
stage = [list(map(int,input().rstrip().split())) for _ in range(n)]

eat = 0
count_time = 0
baby_shark_size = 2

while True:
    stage2 = [[0 for _ in range(n)] for _ in range(n)] # 상어가 갈 수 있는 곳을 나타내는 리스트
    check = [[0 for _ in range(n)] for _ in range(n)] # 상어가 지나간 길을 체크하는 리스트

    x, y = fish_check(stage, stage2, baby_shark_size) # 상어가 갈 수 있는 곳 체크 -1 이면 못가는곳임
    result(x, y, count_time)
    
    nx, ny = bfs(stage, stage2, x, y, n, check) # 상어가 갈수잇는 곳 중 먹이가 제일 가까운 곳 찾는 bfs
    result(nx, ny, count_time)
    eat += 1
    stage[nx][ny] = 9
    count_time += check[nx][ny]
   
    if eat == baby_shark_size:
        eat = 0
        baby_shark_size += 1

#####################################################3

  



# stage2 = [[0 for _ in range(n)] for _ in range(n)]
# check = [[0 for _ in range(n)] for _ in range(n)]

# x, y = fish_check(stage, stage2, baby_shark_size)

# for i in stage2:
#     print(i)

# print()

# if x == -1 and y == -1:
#    print('0')
#    exit()

# nx, ny = bfs(stage, stage2, baby_shark_size, x, y, n, check)
# count_time += check[nx][ny]

# if eat == baby_shark_size:
#     eat = 0
#     baby_shark_size += 1

# for j in stage:
#     print(j)

# print(nx, ny, count_time, eat)
# print()






# import sys
# from collections import deque
# input = sys.stdin.readline

# dx = [-1, 0, 1, 0]
# dy = [0, -1 ,0, 1]

# def check_fish(stage, stage2, size):
#     shark_x = 0
#     shark_Y = 0
#     for i in range(len(stage)):
#         for j in range(len(stage)):
#             if stage[i][j] <= size and stage[i][j] > 0:
#                 stage2[i][j] = stage[i][j]
#             elif stage[i][j] > size and stage[i][j] <= 6:
#                 stage2[i][j] = -1
            
#             if stage[i][j] == 9:
#                 shark_x, shark_Y = i, j
#     return shark_x, shark_Y

# def bfs(stage, stage2, size, x ,y):
#     global count_time
#     cnt = 0
#     cnt2 = 0
#     check = [[0 for _ in range(n)] for _ in range(n)]
#     q = deque()
#     q.append((x, y))
#     check[x][y] = 1

#     while q:
#         x, y = q.poplef()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue

#             if check[nx][ny] == 0:
#                 if stage2[nx][ny] == 0 or stage2[nx][ny] == size:
#                     check[nx][ny] = check[x][y] + 1
#                     q.append((nx, ny))
#                 elif stage2[nx][ny] != 0 and stage2[nx][ny] < size:
#                     check[nx][ny] = check[x][y] + 1
#                     stage[nx][ny] == 0
#                     count_time += check[nx][ny]
#                     return nx, ny

    

        
# n = int(input())
# stage = [list(map(int,input().rstrip().split())) for _ in range(n)]

# stage2 = [[0 for _ in range(n)] for _ in range(n)]

# count_time = 0
# baby_shark_size = 2



# x, y = check_fish(stage, stage2, baby_shark_size)
# print(x, y)
# for i in stage2:
#     print(i)

# bfs(stage, stage2, baby_shark_size, x, y)