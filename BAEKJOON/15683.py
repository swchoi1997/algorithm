import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def where_cctv(stage):
    cctv = []
    for i in range(n):
        for j in range(m):
            if 1 <= stage[i][j] <= 5:
                cctv.append([i,j,stage[i][j]])
    cctv = sorted(cctv, key = lambda x : -x[2])
    return cctv

def view_cctv(x, y, cctvcase):
    if cctvcase == 1:
        case1(x, y)
    elif cctvcase == 2:
        case2(x, y)
    elif cctvcase == 3:
        case3(x, y)
    elif cctvcase == 4:
        case4(x, y)
    elif cctvcase == 5:
        case5(x, y)

def case1(x, y):
    # cnt = 1 # CCTV자리도 check해서 1
    maxview = []
    check[x][y] = 0
    for i in range(4):
        cnt = 1
        q = deque()
        q.append([x + dx[i], y + dy[i], i])
        while q:
            nx, ny, dirction = q.popleft()
            if nx< 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if stage[nx][ny] == 6:
                continue
            else:
                cnt += 1
                q.append([nx + dx[i], ny + dy[i], dirction])
        maxview.append([cnt, i])
    maxview = sorted(maxview, key=lambda x: (-x[0], x[1]))
    dirc = maxview[0][1]
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        nx, ny = x + dx[dirc], y + dy[dirc]
        if nx< 0 or nx >= n or ny < 0 or ny >= m:
                continue
        if stage[nx][ny] == 6:
            continue
        else:
            check[nx][ny] = 0
            q.append([nx, ny])
    
    
def case2(x, y):
    maxview = []
    check[x][y] = 0
    for i in range(2):
        cnt = 1
        q = deque()
        q.append()

            

def case3(x, y):
    return

def case4(x, y):
    return


def case5(x, y):
    check[x][y] = 0
    q = deque()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        q.append([nx, ny, i])
    
    while q:
        x, y, dirction = q.popleft()
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if stage[x][y] == 6:
            check[x][y] = 6
            continue
        else:
            check[x][y] = 0
            if dirction == 0:
                q.append([x, y + 1, dirction])
            elif dirction == 1:
                q.append([x + 1, y, dirction])
            elif dirction == 2:
                q.append([x, y - 1, dirction])
            elif dirction == 3:
                q.append([x - 1, y, dirction])


n, m = map(int,input().split())

stage = [list(map(int,input().split())) for _ in range(n)]
check = [[1 for _ in range(m)] for _ in range(n)]

cctv = where_cctv(stage)

for i in cctv:
    x, y, cctvcase = i[0], i[1], i[2]
    view_cctv(x, y, cctvcase)

print(cctv)

for i in check:
    print(i)



# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 5 0 6 0
# 0 0 0 0 0 0

# 6 6
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 5 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

