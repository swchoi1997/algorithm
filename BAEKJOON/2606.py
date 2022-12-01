from collections import deque

def bfs(graph, t , visited):
    queue = deque([t])
    visited[t] = True
    cnt = 0
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if not visited[i]:
                queue.append(i)
                cnt += 1
                visited[i] = True
    
    return cnt

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
print(bfs(graph, 1, visited))

