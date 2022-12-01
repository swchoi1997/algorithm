#음료수 어려 먹기
n, m = map(int, input().split())

frame = []
for i in range(n):
    frame.append(list(map(int, input())))

def a(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if frame[x][y] == 0:
        frame[x][y] = 1

        a(x - 1 , y)
        a(x, y - 1)
        a(x + 1, y)
        a(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if a(i, j) == True:
            result += 1

print(result)