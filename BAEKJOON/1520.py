from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx, dy = [0, 0, 1 ,-1], [1, -1 ,0 ,0]

def dfs(x, y):
    if x == (a - 1) and y == (b - 1):
        return 1

    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(4):
            nx ,ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue

            if stage[nx][ny] < stage[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

a, b = map(int,input().rstrip().split())
stage = [list(map(int,input().rstrip().split())) for _ in range(a)]
visited = [b * [-1] for _ in range(a)]



print(dfs(0, 0))
