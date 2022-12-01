import sys
from collections import deque
sys.stdin.readline

def bfs(i, airplane, visited):
    q = deque()
    q.append([i])
    visited[i] == 0
    while q:
        now = q.popleft()
        for next in airplane[now]:
            if visited[now] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

tc = int(input().rstrip())

for _ in range(tc):
    n, m = map(int ,input().rstrip().split())
    airplane = [[0] for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int,input().rstrip().split())
        airplane[a].append(b)
        airplane[b].append(a)
    result= [0] * n
    for i in range(len(airplane)): # i국가에서 j국가로
        visited = [(-1) for a in range(n)]
        bfs(i, airplane, visited)

    print(min(result))