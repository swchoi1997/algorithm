from collections import deque

n, m, v = map(int, input().split())

def dfs(graph, v, visited1):
    visited1[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited1[i]:
            dfs(graph, i, visited1)

def bfs(graph, v, visited2):
    queue = deque([v])
    visited2[v] = True

    while queue:
        p = queue.popleft()
        print(p, end = ' ')

        for i in graph[p]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited1 = [False] * (n + 1)
dfs(graph, v, visited1)
print()

visited2 = [False] * (n + 1)
bfs(graph, v, visited2)




