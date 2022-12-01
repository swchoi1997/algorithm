n, m = map(int, input().split()) # 맵 크기
x, y, direction = map(int, input().split()) # a b 현재위치, c 바라보는 방향
maps = []
for i in range(0, n):
    maps.append(list(map(int, input().split())))

dx = [0 ,1, 0, -1] # 북 서 남 동
dy = [-1, 0, 1, 0]

dir_count= 0
count = 0

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    direction -= 1
    if direction == -1:
        direction = 3
    
    if maps[nx][ny] == 1:
        maps[x][y] = 2
        x, y = nx, ny
        count += 1
    elif maps[nx][ny] == 0 or maps[nx][ny] == 2:
        dir_count += 1
        if dir_count == 4:
            nx = x - dx[direction]
            ny = y - dx[direction]
            if maps[nx][ny] != 0:
                x, y = nx, ny
            else:
                break

print(count)
