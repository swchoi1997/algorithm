import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    stic = [list(map(int,input().split())) for _ in range(2)]
    if n == 1:
        print(max(map(max, stic)))
        continue
    check = [[0 for _ in range(n)] for _ in range(2)]
    check[0][0], check[1][0] = stic[0][0], stic[1][0]
    check[0][1], check[1][1] = stic[0][1] + check[1][0], stic[1][1] + check[0][0]
    

    for i in range(2, n):
        for j in range(2):
            if j == 0:
                check[j][i] = max(check[j + 1][i - 1] + stic[j][i], check[j + 1][i - 2] + stic[j][i])
            else:
                check[j][i] = max(check[j - 1][i - 1] + stic[j][i], check[j - 1][i - 2] + stic[j][i])

    print(max(check[0][n-1], check[1][n -1]))
        









# def cur_max(stic):
#     curr = max(map(max, stic))
#     for i in range(2):
#         if curr in stic[i]:
#             x, y = i, stic[i].index(curr)
#     return curr, x, y

# def check_non_stic(stic, curr, x, y):
#     stic[x][y] = 0
#     dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx < 0 or ny < 0 or nx >= 2 or ny >= n:
#             continue
#         if stic[nx][ny] == 0:
#             continue
#         else:
#             stic[nx][ny] = 0
    

# t = int(input())
# for _ in range(t):
    
#     n = int(input())
#     stic = [list(map(int,input().split())) for _ in range(2)]
#     result = 0

#     while sum(map(sum, stic)) != 0:
#         curr, x, y = cur_max(stic)
#         result += curr
#         check_non_stic(stic, curr, x, y)
    
#     print(result)
