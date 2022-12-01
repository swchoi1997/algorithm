# n, m = map(int, input().split()) # map size
# r, c, d = map(int, input().split())

# stage = []
# for _ in range(n):
#     stage.append(list(map(int, input().split())))

# #북0 동1 남2 서3
# dx = [-1, 0 , 1, 0]
# dy = [0, 1, 0, -1]

# stage[r][c] = 2 # 현재위치 청소

# cnt = 0
# count = 1
# while True:
#     d = d - 1
#     if d < 0:
#         d = 3
#     nx = r + dx[d]
#     ny = c + dy[d]

#     if stage[nx][ny] != 0:
#         cnt += 1
#         if cnt == 4:
#             break
#         continue
#     else:
#         stage[nx][ny] = 2
#         r, c = nx, ny
#         count += 1

# print(count)
# for i in stage:
#     print(i)



n, m = map(int, input().split()) # map size
r, c, d = map(int, input().split())

stage = []
for _ in range(n):
    stage.append(list(map(int, input().split())))

#북0 동1 남2 서3
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

stage[r][c] = 2 # 현재위치 청소

cnt1, cnt2 = 0, 0
count = 1
while True:
    
    d = d - 1 # 방향을 왼쪽으로 바라보고
    if d < 0:
        d = 3
    nx = r + dx[d] # 왼쪽으로 한칸 갔을 때 방향
    ny = c + dy[d] # 2

    if stage[nx][ny] != 0:
        if stage[nx][ny] == 1:
            cnt1 += 1
        elif stage[nx][ny] == 2:
            cnt2 += 1
        if cnt1 + cnt2 == 4:
            
            if cnt1 == 4: # 4방향 전부 다 벽일때
                break                   
            else:
                backd = d - 2
                if backd < 0:
                    if backd == -1:
                        backd = 3
                    else:
                        backd = 2
                bx = r + dx[backd]
                by = c + dy[backd]
                
                if stage[bx][by] == 1:
                    break
                else:
                    r, c = bx, by
                    cnt1, cnt2 = 0, 0
                    continue
        continue
    else:
        stage[nx][ny] = 2
        r, c = nx, ny
        cnt1, cnt2 = 0, 0
        count += 1


print(count)
for i in stage:
    print(i)