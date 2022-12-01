#dfs 문제!!! 제대로 하고 넘어갈 것!!
import sys
sys.setrecursionlimit(10000)
def dfs(a, b):
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return False

    if maps[a][b] == 1:
        maps[a][b] = 0
        dfs(a - 1, b)
        dfs(a, b - 1)
        dfs(a + 1, b)
        dfs(a, b + 1)
        return True
    return False

test_case = int(input())

for _ in range(test_case):
    m, n, k = map(int, input().split())
    
    maps = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        maps[y][x] = 1

    if k == 1:
        print(k)
        continue

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)

