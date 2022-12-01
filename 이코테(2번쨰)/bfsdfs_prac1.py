#--- 시간초과 --- 
# 특정 거리의 도시 찾기 bfs 이용해야 할 것 같음
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
visited = [-1] * (n + 1)

load = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    load[a].append(b)

visited[x] = 0

queue = deque()
queue.append(x, 0)

result = []
while queue:
    i, j = queue.popleft()
    if j == k:
        result.append(i)

def find_city(visited, x, load):
    queue = deque()
    for a in load: 
        if a[0] == x: #시작점에서 연결된 그걸 방향그래프를 하나 넣고
            queue.append(a)
    visited[x] = 0    
    
    while queue:
        i, j = queue.popleft()
        if visited[j] == -1:
            visited[j] = visited[i] + 1
        
        for a in load:
            if a[0] == j:
                queue.append(a)
    
    
find_city(visited, x, load)

new_visited = []
for i in range(1, len(visited)):
    new_visited.append(visited[i])

if k not in new_visited:
    print('-1')

for i in range(len(new_visited)):
    if new_visited[i] == k:
        print(i + 1)

    

