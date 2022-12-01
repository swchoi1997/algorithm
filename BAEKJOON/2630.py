n  = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


# 1 파란색 0 빨간색
blue, red = 0, 0

def dq(n, x, y):
    global blue, red
    first = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if first != graph[i][j]:
                for a in range(2):
                    for b in range(2):
                        dq(n // 2 , x + n // 2 * a , y + n // 2 * b)
                return

    if first == 1:
        blue += 1
        
    elif first == 0:
        red += 1

    return        

dq(n, 0, 0)

print(red)
print(blue)
