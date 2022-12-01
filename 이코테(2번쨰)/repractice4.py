#상하좌우

n = int(input())
datas = input().split() #리스트로 저장이 됨

x, y = 1, 1

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]

type = ['U', 'D', 'L', 'R']

for data in datas:
    for i in range(len(type)):
        if data == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n :
        continue

    x, y = nx, ny
    
print(x, y)
    


