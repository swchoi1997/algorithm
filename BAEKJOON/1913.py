n = int(input())
find = int(input())

graph = [[0] * n for _ in range(n)]

dx, dy = [1, 0, -1, 0],[0, 1, 0, -1] # 하 우 상 좌
def where(graph, check, n, x ,y):
    global cnt
    for _ in range(n - 1):
        nx = x + dx[check]
        ny = y + dy[check]

        if graph[nx][ny] == 0:
            graph[nx][ny] = cnt
        else:
            nx = nx - dx[check]
            ny = ny - dy[check]
            return nx, ny
        x, y = nx, ny
        cnt -= 1
    return nx, ny
        
graph[0][0] = n * n
cnt = n * n - 1
check, x, y = 0, 0, 0

while graph[n //2][n //2] != 1:
    if check == 0:
        nx, ny = where(graph, check, n ,x, y)
    elif check == 1:
        nx, ny = where(graph, check, n ,x, y)
    elif check == 2:
        nx, ny = where(graph, check, n ,x, y)
    elif check == 3:
        nx, ny = where(graph, check, n ,x, y)

    x, y = nx, ny
    check += 1
    if check > 3:
        check = 0

for i in graph:
    for j in i:
        print(j, end = ' ')
    print()
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == find:
            print(i + 1, j + 1)
            exit()
        else:
            continue

# nx ,ny = left(graph, newn ,x, y)
# nx ,ny = down(graph, newn, x, y)
# nx ,ny = right(graph, newn, x, y)
# nx ,ny = up(graph, newn, x, y)

# def left(graph, n, x ,y):
#     global cnt
#     nx = 0
#     for i in range(1, n):
#         nx = x + i
#         if graph[nx][y] == 0:
#             graph[nx][y] = cnt
#         else:
#             return nx - 1, y
#         cnt -= 1
#     return nx, y
# def down(graph, n ,x ,y):
#     global cnt
#     ny = 0
#     for i in range(1, n):
#         ny = y + i
#         if graph[x][ny] == 0:
#             graph[x][ny] = cnt
#         else:
#             return x, ny -1
#         cnt -= 1
#     return x, ny
# def right(graph, n, x ,y):
#     global cnt
#     nx = 0
#     for i in range(1 ,n):
#         nx = x - i
#         if graph[nx][y] == 0:
#             graph[nx][y] = cnt
#         else:
#             return nx + 1, y
#         cnt -= 1
#     return nx, y
# def up(graph, n, x, y):
#     global cnt
#     ny = 0
#     for i in range(1 ,n):
#         ny = y - i
#         if graph[x][ny] == 0:
#             graph[x][ny] = cnt
#         else:
#             return x, ny + 1
#         cnt -= 1
#     return x, ny