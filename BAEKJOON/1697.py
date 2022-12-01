from collections import deque

def bfs(n ,k, visited):
    
    ck = deque([[n, 0]])
    
    while ck:
        value = ck.popleft()
        v1 = value[0]
        v2 = value[1]
        if not visited[v1]:
            visited[v1] = True

            if v1 == k:
                return v2
            
            if (v1 - 1) >= 0:
                ck.append([(v1 - 1), v2 + 1])
            if (v1 + 1) <= 100000:
                ck.append([(v1 + 1), v2 + 1])
            if (v1 * 2) <= 100000:
                ck.append([(v1 * 2), v2 + 1])

n, k = map(int ,input().split())
visited = [False] * (100001)

print(bfs(n, k, visited))

