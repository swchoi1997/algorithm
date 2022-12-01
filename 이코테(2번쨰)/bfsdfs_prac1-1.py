from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int,input().split())

city_map = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    city_map[a].append(b)

visited = [-1] * (n + 1)
visited[x] = 0

queue = deque([x])
while queue:    
    now = queue.popleft()
    for next_city in city_map[now]:
        if visited[now] == -1:
            visited[next_city] = visited[now] + 1
            queue.append(next_city)

check = False
for i in range(1, len(visited)):
    if visited[i] == k:
        print(i)
        check = True

if check == False:
    print('-1')
