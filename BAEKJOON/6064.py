import sys
input = sys.stdin.readline



t = int(input())
for _ in range(t):
    m, n, x, y = map(int,input().split())

    result = -1
    while x <= m * n:
        if (x - y) % n == 0:
            result = x
            break
        x += m
    print(result)

# t = int(input())
# for _ in range(t):
#     m, n, x, y = map(int,input().split())
#     cnt = 1
#     curx, cury = 1, 1
#     # cal = [[1, 1, cnt]]
#     TF = False
#     i = 0
#     while True:
#         if curx == m and cury == n:
#             break
#         if curx == x and cury == y:
#             print(cnt)
#             TF = True
#             break
#         curx += 1
#         cury += 1
#         cnt += 1
#         if curx > m: curx = 1
#         if cury > n: cury = 1
#         i += 1
    
#     if not TF:
#         print(-1)