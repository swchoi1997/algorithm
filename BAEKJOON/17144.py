from collections import deque

dx, dy = [0,-1,0,1], [1,0,-1,0]

r, c, t = map(int,input().split())

stage = [list(map(int,input().split())) for _ in range(r)]

air = []
# 다음방향 알려주기
def next_dir(x, y, check, dir):
    if check == 0:
        nx = x + dx[dir]
        ny = y + dy[dir]
    else:
        nx = x - dx[dir]
        ny = y + dy[dir]

    return nx, ny



#2. 공기청정기 
def aircon(air, mise):
    q = deque()
    q.append([air[0][0], air[0][1], 0, 0, 0]) #x좌료, y 좌표, 위/아래, 방향, val
    q.append([air[1][0], air[1][1], 1, 0, 0])

    while q:
        x, y, check, dir, val = q.popleft()

        nx, ny = next_dir(x, y, check, dir)
       
        if 0<= nx < r and 0<= ny < c:
            if mise[nx][ny] == -1:
                continue
            tmp1 = mise[nx][ny]
            mise[nx][ny] = val
            q.append([nx, ny, check, dir, tmp1])

        else:
            dir += 1
            if dir >= 4:
                dir = 0
            
            nx, ny = next_dir(x, y, check, dir)
            if 0<= nx < r and 0<= ny < c:
                if mise[nx][ny] == -1:
                    continue
                tmp1 = mise[nx][ny]
                mise[nx][ny] = val
                q.append([nx, ny, check, dir, tmp1])

#1. 미세먼지 확산
def spread(stage):
    global air
    mise = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if stage[i][j] == -1:
                mise[i][j] = -1
                air.append([i,j])
            if stage[i][j] > 0 :
                q = deque()
                tmp = stage[i][j] // 5
                
                for t in range(4):
                    nx, ny = i + dx[t], j + dy[t];
                    if 0<= nx < r and 0 <= ny < c and stage[nx][ny] != -1:
                        q.append([nx, ny])
                
                cnt = len(q)
                for a, b in q:
                    mise[a][b] += stage[i][j] // 5
                
                mise[i][j] += stage[i][j] - (stage[i][j] // 5) * cnt
    
    aircon(air, mise) # 공기청정기 돌리기

    return mise
for _ in range(t):
    stage = spread(stage)

print(sum(map(sum, stage)) + 2)
