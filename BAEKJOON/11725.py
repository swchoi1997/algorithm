import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * (n + 1)
def dfs(num, v):
    visited[num] = v

    for i in graph[num]:
        if visited[i] == 0:
            dfs(i, num)

dfs(1, 1)

for i in range(2, len(visited)):
    print(visited[i])
